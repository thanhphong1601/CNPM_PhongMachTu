from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from phongmachapp.models import Thuoc, LoaiThuoc, DonViThuoc
from phongmachapp import app, db


class MyThuocView(ModelView):
        column_list = ['id', 'tenThuoc', 'congDung', 'donViThuoc_id']


class MyDonViThuocView(ModelView):
        column_list = ['id', 'tenDonVi', 'thuocs']


class MyLoaiThuocView(ModelView):
        column_list = ['id', 'tenLoai']


admin = Admin(app, name="Phong Mach Tu", template_mode="bootstrap4")
admin.add_view(MyThuocView(Thuoc, db.session))
admin.add_view(MyLoaiThuocView(LoaiThuoc, db.session))
admin.add_view(MyDonViThuocView(DonViThuoc, db.session))