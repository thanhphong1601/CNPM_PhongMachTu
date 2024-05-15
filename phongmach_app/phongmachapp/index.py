from flask import render_template, request, redirect
import dao
from phongmachapp import app, admin, login
from flask_login import login_user, current_user, logout_user
from phongmachapp.models import NguoiDung
import cloudinary.uploader


@app.route('/')
def index():
    categories = dao.load_categories()
    return render_template('index.html', categories=categories)


@app.route('/benhnhan')
def user():
    return render_template('trangBenhNhan.html')


@app.route('/dangkykham', methods=['get', 'post'])
def dangKyLich():
    if request.method.__eq__('POST'):
        print(request.form)
    return render_template('dangKyKham.html')


@app.route('/login', methods=['get', 'post'])
def login_my_user():
    if current_user.is_authenticated:
        return redirect('/')
    err_msg = ''
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user)
            return redirect('/')
        else:
            err_msg = 'Tài khoản hoặc mật khẩu không đúng'
    return render_template('login.html', err_msg=err_msg)


@app.route('/logout', methods=['get'])
def logout_my_user():
    logout_user()
    return redirect('/login')


@app.route('/register', methods=['get', 'post'])
def register_user():
    err_msg = ''
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
