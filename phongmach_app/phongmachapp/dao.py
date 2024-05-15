import json, hashlib
from phongmachapp.models import Thuoc, LoaiThuoc, DonViThuoc, NguoiDung, GioiTinh, ChiTietDanhSachKham, LichKham, DanhSachKham
from phongmachapp import app, db


def load_categories():
    with open('data/categories.json', encoding='utf-8') as f:
        return json.load(f)


def load_gender():
    return [(gender.name, gender.value) for gender in GioiTinh]


def get_user_by_id(id):
    return NguoiDung.query.get(id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    # print(password)
    # print(username)
    return NguoiDung.query.filter(NguoiDung.username.__eq__(username.strip()),
                                  NguoiDung.password.__eq__(password)).first()


def add_user(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = NguoiDung(hoTen=name, username=username, password=password, anhDaiDien=avatar)
    db.session.add(u)
    db.session.commit()


def add_detail_benhNhan(danhSach_id, nguoiDangKy_id, hoTen, gioiTinh, namSinh, soDienThoai, diaChi):
    detail = ChiTietDanhSachKham(danhSachKham_id=danhSach_id,
                                 nguoiDung_id=nguoiDangKy_id,
                                 hoTen=hoTen,
                                 gioiTinh=gioiTinh,
                                 namSinh=namSinh,
                                 soDienThoai=soDienThoai,
                                 diaChi=diaChi)
    db.session.add(detail)
    db.session.commit()


def add_lichKham(ngayKham):
    lichKham = LichKham(ngayKham=ngayKham)
    db.session.add(lichKham)
    db.session.commit()


def add_danhSachKham(lichKham_id):
    danhSachKham = DanhSachKham(lichNgayKham_id=lichKham_id)
    db.session.add(danhSachKham)
    db.session.commit()



if __name__ == '__main__':
    print(load_categories())
