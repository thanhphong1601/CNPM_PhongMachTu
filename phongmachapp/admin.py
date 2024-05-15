from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView
from phongmachapp.models import Thuoc, DonViThuoc, LoaiThuoc, VaiTroNguoiDung
from phongmachapp import app, db
from flask_login import logout_user, current_user
from flask import redirect

#
class AuthenticatedView(ModelView):
        def is_accessible(self):
                return current_user.is_authenticated and current_user.vaiTro_NguoiDung == VaiTroNguoiDung.ADMIN




class MyThuocView(AuthenticatedView):
        column_list = ['id', 'tenThuoc', 'congDung', 'donViThuoc_id', 'price', 'loaiThuocs']
        column_searchable_list = ['id', 'tenThuoc']
        column_filters = ['id', 'tenThuoc', 'price']
        column_editable_list = ['tenThuoc', 'congDung', 'price']
        column_labels = {
                'tenThuoc': 'Tên Thuốc',
                'congDung': 'Công Dụng',
                'donViThuoc_id': "Đơn vị thuốc",
                'price': 'Giá',
                'loaiThuocs': 'Loại Thuốc'
        }




class MyDonViThuocView(AuthenticatedView):
        column_list = ['id', 'tenDonVi', 'thuocs']
        column_editable_list = ['tenDonVi']
        column_labels = {
                'tenDonVi': 'Tên Đơn Vị',
                'thuocs': 'Các Thuốc'
        }


class MyLoaiThuocView(AuthenticatedView):
        column_list = ['id', 'tenLoai']
        column_editable_list = ['tenLoai']
        column_labels = {
                'tenLoai': 'Loại Thuốc'
        }


class StatsView(BaseView):
        @expose('/')
        def index(self):
                return self.render('admin/stats.html')

        def is_accessible(self):
                return current_user.is_authenticated and current_user.vaiTro_NguoiDung == VaiTroNguoiDung.ADMIN


class LogoutView(BaseView):
        @expose('/')
        def index(self):
                logout_user()
                return redirect('/admin')

        def is_accessible(self):
                return current_user.is_authenticated and current_user.vaiTro_NguoiDung == VaiTroNguoiDung.ADMIN



admin = Admin(app, name="Phong Mach Tu", template_mode="bootstrap4")
admin.add_view(MyDonViThuocView(DonViThuoc, db.session))
admin.add_view(MyThuocView(Thuoc, db.session))
admin.add_view(MyLoaiThuocView(LoaiThuoc, db.session))


admin.add_view(StatsView(name="Thống Kê"))
admin.add_view(LogoutView(name="Đăng Xuất"))
