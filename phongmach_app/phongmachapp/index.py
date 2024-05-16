from datetime import datetime

from flask import render_template, request, redirect, session
from sqlalchemy import func

import dao
from phongmachapp import app, admin, login, db
from flask_login import login_user, current_user, logout_user
from phongmachapp.models import NguoiDung, LichKham, DanhSachKham, ChiTietDanhSachKham, QuyDinh
import cloudinary.uploader
from decorators import loggedin, not_loggedin


@app.route('/')
def index():
    categories = dao.load_categories()
    return render_template('index.html', categories=categories)


@app.route('/benhnhan')
def user():
    return render_template('trangBenhNhan.html')


@app.route('/dangkykham', methods=['get', 'post'])
@not_loggedin
def dangKyLich():
    genders = dao.load_gender()
    # print(genders)
    if request.method.__eq__('POST'):
        # print(request.form)
        name = request.form.get('name')
        birthday = request.form.get('birthday')
        gender = request.form.get('gender')
        address = request.form.get('address')
        date = request.form.get('date')
        phone = request.form.get('phone')
        ngay_kham = datetime.strptime(date, '%d/%m/%Y').date()
        nam_sinh = datetime.strptime(birthday, '%d/%m/%Y').date()

        # print(ngay_kham)
        # print(date)

        lichKham_check = dao.get_lichKham_by_date(ngay_kham)
        if lichKham_check:
            # danhSachKham_check = DanhSachKham.query.filter_by(lichNgayKham_id=lichKham_check.id).first()
            danhSachKham_check = dao.get_danhSachKham_by_lichKhamID(lichKham_check.id)
            # print(danhSachKham_check)
            # lịch và danh sách đều đã có
            if danhSachKham_check:
                # thêm chi tiết bệnh nhân
                max = dao.get_max_benhNhan()
                # print(danhSachKham_check.id)
                result = dao.count_soBenhNhan(danhSachKham_check.id)

                # print(result)

                # check số bệnh nhân cùng danh sách
                if (result <= max):
                    dao.add_detail_benhNhan(danhSachKham_check.id,
                                            current_user.id,
                                            hoTen=name,
                                            gioiTinh=gender,
                                            namSinh=nam_sinh,
                                            soDienThoai=phone,
                                            diaChi=address)

                    return redirect('/')
                else:
                    # thông báo cho người dùng...
                    return redirect('/')
            else:
                # tạo danh sách mới
                dao.add_danhSachKham(lichKham_check.id)
                dao.add_detail_benhNhan(danhSachKham_check.id,
                                        current_user.id,
                                        hoTen=name,
                                        gioiTinh=gender,
                                        namSinh=nam_sinh,
                                        soDienThoai=phone,
                                        diaChi=address)

                return redirect('/')

        else:
            dao.add_lichKham(ngay_kham)
            lichKham_new = dao.add_lichKham(ngay_kham)
            dao.add_danhSachKham(lichKham_new.id)
            # danhSachKham_new = DanhSachKham.query.filter_by(lichNgayKham_id=lichKham_new.id).first()
            danhSachKham_new = dao.add_danhSachKham(lichKham_new.id)
            dao.add_detail_benhNhan(danhSachKham_new.id,
                                    current_user.id,
                                    hoTen=name,
                                    gioiTinh=gender,
                                    namSinh=nam_sinh,
                                    soDienThoai=phone,
                                    diaChi=address)

            return redirect('/')

    return render_template('dangKyKham.html', genders=genders)


@app.route('/yta')
def trang_yTa():
    return render_template('trangYTa.html')


# @app.route('/danhsachkham')
# def danhSachKham():
#     return render_template('danhSachKham.html')


@app.route('/danhsachkham', methods=['get', 'post'])
def get_patient_list():
    patients = []
    if request.method.__eq__('POST'):
        date = request.form.get('date')
        ngayChon = datetime.strptime(date, '%d/%m/%Y')# Chuyển đổi sang định dạng date

        # Xử lí dữ liệu
        lichKham_check = LichKham.query.filter_by(ngayKham=ngayChon).first()
        if lichKham_check:
            danh_sach_kham = DanhSachKham.query.filter_by(lichNgayKham_id=lichKham_check.id).all()
            # print(danh_sach_kham)
            for p in danh_sach_kham:
                patient_info = ChiTietDanhSachKham.query.filter_by(danhSachKham_id=p.id).all()
                patients.extend(patient_info)

    return render_template('danhsachkham.html', patients=patients)


@app.route('/thungan')
def trang_ThuNgan():
    return render_template('trangThuNgan.html')


@app.route('/tracuuhoadon')
def traCuuHoaDon():
    return render_template('hoaDon.html')


@app.route('/login', methods=['get', 'post'])
def login_my_user():
    if current_user.is_authenticated:
        return redirect('/')
    err_msg = ''
    done_msg = request.args.get('done_msg')
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user)
            return redirect('/')
        else:
            err_msg = 'Tài khoản hoặc mật khẩu không đúng'
    return render_template('login.html', err_msg=err_msg, done_msg=done_msg)


@app.route('/logout', methods=['get'])
def logout_my_user():
    logout_user()
    return redirect('/login')


@app.route('/register', methods=['get', 'post'])
@loggedin
def register_user():
    done_msg = 'Đã tạo tại khoản thành công'
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        if NguoiDung.query.filter(NguoiDung.username.__eq__(username)).first():
            err_msg = 'Tài khoản đã tồn tại'
        else:
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            if password.__eq__(confirm_password):
                avatar_path = ''
                avatar = request.files.get('avatar')
                if avatar:
                    res = cloudinary.uploader.upload(avatar)
                    avatar_path = res['secure_url']

                dao.add_user(name=request.form.get('name'),
                             username=username,
                             password=password,
                             avatar=avatar_path)
                return redirect('/login')
            else:
                err_msg = 'Mật khẩu xác nhận không đúng'

    return render_template('/register.html', err_msg=err_msg)


@app.route('/admin-login', methods=['post'])
def process_admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    # print(username)
    # print(password)
    u = dao.auth_user(username=username, password=password)
    if u:
        login_user(user=u)

    return redirect('/admin')


@app.route('/api/test', methods=['post'])
def test_add():
    print(request.json)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
