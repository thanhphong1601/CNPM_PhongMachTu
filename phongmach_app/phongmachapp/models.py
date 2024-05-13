from sqlalchemy import Column, String, Float, Integer, ForeignKey, Enum, Boolean, DateTime
from sqlalchemy.orm import relationship
from phongmachapp import db, app
from flask_login import UserMixin
from enum import Enum as RoleEnum
from datetime import datetime


class VaiTroNguoiDung(RoleEnum):
    BenhNhan = 1
    YTa = 2
    BacSi = 3
    ThuNgan = 4
    ADMIN = 5


class DonViThuoc(RoleEnum):
    Chai = 1
    Vy = 2
    Vien = 3


class GioiTinh(RoleEnum):
    Nam = 1
    Nu = 2
    KhongTraLoi = 3


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, autoincrement=True, primary_key=True)


class NguoiDung(Base, UserMixin):
    hoTen = Column(String(100), nullable=False)
    anhDaiDien = Column(String(100), nullable=False)
    tenNguoiDung = Column(String(50), unique=True)
    matKhauNguoiDung = Column(String(50), nullable=False)
    gioiTinh = Column(Enum(GioiTinh), default=GioiTinh.Nam)
    namSinh = Column(DateTime, nullable=False)
    soDienThoai = Column(String(10), nullable=False)
    diaChi = Column(String(100), nullable=False)
    vaiTro_NguoiDung = Column(Enum(VaiTroNguoiDung), default=VaiTroNguoiDung.BenhNhan)
    phieuKham = relationship('PhieuKham', backref='nguoidung', lazy=True)
    phieuDangKyKham = relationship('PhieuDangKyKham', backref='nguoidung', lazy=True)
    hoaDon = relationship('HoaDon', backref='nguoidung', lazy=True)
    # backref dùng để truy vấn ngược lại dễ hơn,
    # lazy được sử dụng để xác định cách truy xuất dữ liệu từ cơ sở dữ liệu khi cần thiết
    # active = models.BooleanField(default=True)

    def __str__(self):
        return self.hoTen

    def nam_sinh(self):
        if self.namSinh:
            return self.namSinh.year
        else:
            None


class PhieuKham(Base):
    benhNhan_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
    hoTen = Column(String(100), nullable=False)
    trieuChung = Column(String(50), nullable=False)
    duDoanBenh = Column(String(50), nullable=False)
    ngayKham = Column(DateTime, default=datetime.now())
    chiTietPhieuKham = relationship('ChiTietPhieuKham', backref='phieukham', lazy=True)
    hoaDon = relationship('HoaDon', backref='phieukham', lazy=True)

    def __str__(self):
        return self.hoTen


class Thuoc(Base):
    tenThuoc = Column(String(50), unique=True, nullable=False)
    congDung = Column(String(50), nullable=False)
    donViThuoc = Column(Enum(DonViThuoc), default=DonViThuoc.Vien)
    chiTietPhieuKham = relationship('ChiTietPhieuKham', backref='thuoc', lazy=True)

    def __str__(self):
        return self.tenThuoc


class ChiTietPhieuKham(Base):
    soLuong = Column(Integer, default=0)
    cachDung = Column(Float, default=0)
    phieuKham_id = Column(Integer, ForeignKey(PhieuKham.id), nullable=False)
    thuoc_id = Column(Integer, ForeignKey(Thuoc.id), nullable=False)


class HoaDon(Base):
    ngayKham = Column(DateTime, default=datetime.now(), nullable=False)
    tienKham = Column(Float, default=0)
    tienThuoc = Column(Float, default=0)
    nguoiDung_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
    phieuKham_id = Column(Integer, ForeignKey(PhieuKham.id), nullable=False)


class LichKham(Base):
    ngayKham = Column(DateTime, default=datetime.now(), nullable=False)
    danhSachKham = relationship('DanhSachKham', backref='lichkham', lazy=True)


class DanhSachKham(Base):
    benhNhan_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
    lichNgayKham_id = Column(Integer, ForeignKey(LichKham.id), nullable=False)


class PhieuDangKyKham(Base):
    benhNhan_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
    yTa_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

