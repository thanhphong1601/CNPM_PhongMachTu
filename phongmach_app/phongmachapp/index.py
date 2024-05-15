from flask import render_template, request, redirect
import dao
from phongmachapp import app, admin, login
from flask_login import login_user, current_user, logout_user


@app.route('/')
def index():
    categories = dao.load_categories()
    return render_template('index.html', categories=categories)


@app.route('/lapphieukham', methods=['get', 'post'])
def lapPhieuKham():
    thuocs = dao.load_medicines()
    medicines_unit = dao.load_medicines_unit()

    if request.method.__eq__('POST'):
        print(request.form)
    return render_template('lapPhieuKham.html', thuocs=thuocs, medicines_unit=medicines_unit)


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


@app.route('/register')
def register_user():
    return render_template('/register.html')


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


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
