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


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, autoincrement=True, primary_key=True)


class NguoiDung(Base, UserMixin):
    hoTen = Column(String(100))
    anhDaiDien = Column(String(100))
    tenNguoiDung = Column(String(50), unique=True)
    matKhauNguoiDung = Column(String(50))
    gioiTinh = Column(String(10))
    namSinh = Column(DateTime, default=datetime.now())
    soDienThoai = Column(String(10))
    diaChi = Column(String(100))
    vaiTro_NguoiDung = Column(Enum(VaiTroNguoiDung), default=VaiTroNguoiDung.BenhNhan)
    # active = models.BooleanField(default=True)

    def __str__(self):
        return self.hoTen

    def nam_sinh(self):
        return self.namSinh.year if self.namSinh else None


class PhieuKham(Base):
    nguoiDung_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
    trieuChung = Column(String(50), nullable=False)
    duDoanBenh = Column(String(50), nullable=False)
    ngayKham = Column(DateTime, default=datetime.now())
    hoTenNguoiDung = relationship('NguoiDung', backref='phieukham', lazy=True)
    # backref dùng để truy vấn ngược lại dễ hơn,
    # lazy được sử dụng để xác định cách truy xuất dữ liệu từ cơ sở dữ liệu khi cần thiết.

    def benhnhan_name(self):
        if self.hoTenNguoiDung.vaiTro_NguoiDung == VaiTroNguoiDung.BenhNhan:
            return self.hoTenNguoiDung.hoTen
        else:
            return None


class Thuoc(Base):
    tenThuoc = Column(String(50), unique=True, nullable=False)
    congDung = Column(String(50), nullable=False)
    donViThuoc = Column(Enum(DonViThuoc), default=DonViThuoc.Vien)

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


class PhieuDangKyKham(Base):
    benhNhan_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
    yTa_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
    NguoiDung = relationship('NguoiDung', backref='phieudangkykham', lazy=True)

    def benhnhan_id(self):
        if (self.NguoiDung.vaiTro_NguoiDung == VaiTroNguoiDung.BenhNhan
                and self.NguoiDung.vaiTro_NguoiDung == VaiTroNguoiDung.YTa):
            return self.benhNhan_id, self.yTa_id
        else:
            return None

