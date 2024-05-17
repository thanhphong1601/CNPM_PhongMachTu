from datetime import datetime

from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, AdminIndexView
from phongmachapp.models import (Thuoc, DonViThuoc, LoaiThuoc, VaiTroNguoiDung, NguoiDung, LichKham, DanhSachKham,
                                 ChiTietDanhSachKham, PhieuKham, ChiTietPhieuKham, HoaDon, QuyDinh)
from phongmachapp import app, db, dao
from flask_login import logout_user, current_user
from flask import redirect, request


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
        column_list = ['id','hoTenBenhNhan' , 'ngayKham', 'tienKham', 'tienThuoc', 'nguoiDung_id', 'phieuKham_id']
        column_searchable_list = ['ngayKham', 'id', 'nguoiDung_id', 'hoTenBenhNhan']
        column_editable_list = ['tienKham', 'tienThuoc', 'hoTenBenhNhan']
        column_labels = {
                'id': 'Mã Hóa Đơn',
                'hoTenBenhNhan': 'Họ Tên Bệnh Nhân',
                'ngayKham': 'Ngày Khám',
                'tienKham': 'Tiền Khám',
                'tienThuoc': 'Tiền thuốc',
                'nguoiDung_id': 'Mã bệnh nhân',
                'phieuKham_id': 'Mã Phiếu Khám'
        }


class MyQuyDinhView(AuthenticatedView):
        column_list = ['id', 'soTienKham', 'soLoaiThuoc', 'soBenhNhan']
        column_editable_list = ['soTienKham', 'soLoaiThuoc', 'soBenhNhan']
        column_labels = {
                'id': 'Mã Quy Định',
                'soTienKham': 'Số Tiền Khám',
                'soLoaiThuoc': 'Số Loại Thuốc',
                'soBenhNhan': 'Số Bệnh Nhân'
        }


class StatsView(BaseView):
        @expose('/')
        def index(self):
                stats = dao.stats_revenue_by_month(year=request.args.get('year', datetime.now().year),
                                                   month=request.args.get('month', datetime.now().month))
                return self.render('admin/stats.html', stats=stats, current_month=datetime.now().month)

        def is_accessible(self):
                return current_user.is_authenticated and current_user.vaiTro_NguoiDung == VaiTroNguoiDung.ADMIN

class StatsView2(BaseView):
        @expose('/')
        def index(self):
                stats = dao.frequency_revenue_by_period(year=request.args.get('year', datetime.now().year),
                                                        month=request.args.get('month', datetime.now().month),
                                                        name=request.args.get('name'))

                return self.render('admin/stats2.html', stats=stats, current_month=datetime.now().month)

        def is_accessible(self):
                return current_user.is_authenticated and current_user.vaiTro_NguoiDung == VaiTroNguoiDung.ADMIN


class LogoutView(BaseView):
        @expose('/')
        def index(self):
                logout_user()
                return redirect('/admin')

        def is_accessible(self):
                return current_user.is_authenticated and current_user.vaiTro_NguoiDung == VaiTroNguoiDung.ADMIN


class MyAdminIndexView(AdminIndexView):
        @expose('/')
        def index(self):
                stats = dao.stats_revenue_by_month()
                return self.render('admin/index.html', stats=stats)




admin = Admin(app, name="Phong Mach Tu", template_mode="bootstrap4", index_view=MyAdminIndexView())
admin.add_view(MyDonViThuocView(DonViThuoc, db.session, name="Đơn Vị Thuốc"))
admin.add_view(MyThuocView(Thuoc, db.session, name="Thuốc"))
admin.add_view(MyLoaiThuocView(LoaiThuoc, db.session, name="Loại Thuốc"))
admin.add_view(MyUserView(NguoiDung, db.session))
admin.add_view(MyLichView(LichKham, db.session))
admin.add_view(MyDanhSachKham(DanhSachKham, db.session))
admin.add_view(MyChiTietDanhSachKham(ChiTietDanhSachKham, db.session))
admin.add_view(MyPhieuKhamView(PhieuKham, db.session))
admin.add_view(MyChiTietPhieuKhamView(ChiTietPhieuKham, db.session))
admin.add_view(MyHoaDonView(HoaDon, db.session))
admin.add_view(MyQuyDinhView(QuyDinh, db.session, name='Quy Định'))

admin.add_view(StatsView(name="Thống Kê"))
admin.add_view(StatsView2(name="Thống Kê 2"))
admin.add_view(LogoutView(name="Đăng Xuất"))
