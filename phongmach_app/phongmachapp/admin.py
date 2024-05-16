from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView
from phongmachapp.models import Thuoc, DonViThuoc, LoaiThuoc, VaiTroNguoiDung, NguoiDung, LichKham, DanhSachKham, ChiTietDanhSachKham, PhieuKham, ChiTietPhieuKham, HoaDon
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


class MyUserView(ModelView):
        column_list = ['id', 'hoTen', 'username', 'password', 'vaiTro_NguoiDung', 'phieuKhams', 'chiTietDanhSachKhams', 'hoaDons']


class MyLichView(ModelView):
        column_list = ['id', 'ngayKham']


class MyDanhSachKham(ModelView):
        column_list = ['id', 'lichNgayKham_id']


class MyChiTietDanhSachKham(ModelView):
        column_list = ['id', 'danhSach_id', 'nguoiDung_id', 'hoTen', 'namSinh']


class MyPhieuKhamView(AuthenticatedView):
        column_list = ['id', 'benhNhan_id', 'tenBenhNhan', 'trieuChung', 'duDoanBenh', 'ngayKham', 'chiTietPhieuKhams', 'hoaDon']
        column_searchable_list = ['tenBenhNhan']
        column_editable_list = [ 'tenBenhNhan', 'trieuChung', 'duDoanBenh']
        column_labels = {
                'tenBenhNhan': 'Tên bệnh nhân',
                'trieuChung': 'Triệu Chứng',
                'duDoanBenh': 'Dự Đoán',
                'ngayKham': 'Ngày Khám',
                'chiTietPhieuKhams': 'Các phiếu khám',
                'hoaDon': 'Hóa Đơn'
        }


class MyChiTietPhieuKhamView(AuthenticatedView):
        column_list = ['id', 'soLuong', 'cachDung', 'phieuKham_id', 'thuoc_id']
        column_searchable_list = ['id']
        column_editable_list = ['soLuong', 'cachDung']
        column_labels = {
                'id': 'Mã',
                'soLuong': 'Số lượng',
                'phieuKham_id': 'Mã phiếu khám',
                'thuoc_id': 'Mã Thuốc'
        }


class MyHoaDonView(AuthenticatedView):
        column_list = ['id', 'ngayKham', 'tienKham', 'tienThuoc', 'nguoiDung_id', 'phieuKham_id']
        column_searchable_list = ['ngayKham', 'id', 'nguoiDung_id']
        column_editable_list = ['tienKham', 'tienThuoc']
        column_labels = {
                'id': 'Mã Hóa Đơn',
                'ngayKham': 'Ngày Khám',
                'tienKham': 'Tiền Khám',
                'tienThuoc': 'Tiền thuốc',
                'nguoiDung_id': 'Mã bệnh nhân',
                'phieuKham_id': 'Mã Phiếu Khám'
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
admin.add_view(MyUserView(NguoiDung, db.session))
admin.add_view(MyLichView(LichKham, db.session))
admin.add_view(MyDanhSachKham(DanhSachKham, db.session))
admin.add_view(MyChiTietDanhSachKham(ChiTietDanhSachKham, db.session))
admin.add_view(MyPhieuKhamView(PhieuKham, db.session))
admin.add_view(MyChiTietPhieuKhamView(ChiTietPhieuKham, db.session))
admin.add_view(MyHoaDonView(HoaDon, db.session))

admin.add_view(StatsView(name="Thống Kê"))
admin.add_view(LogoutView(name="Đăng Xuất"))
