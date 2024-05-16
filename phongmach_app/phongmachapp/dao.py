import json, hashlib

from sqlalchemy import func

from phongmachapp.models import (Thuoc, LoaiThuoc, DonViThuoc, NguoiDung, PhieuKham,
                                 ChiTietPhieuKham, GioiTinh, ChiTietDanhSachKham, LichKham, DanhSachKham, QuyDinh)
from phongmachapp import app, db


def load_categories():
    with open('data/categories.json', encoding='utf-8') as f:
        return json.load(f)


def load_gender():
    return [(gender.name, gender.value) for gender in GioiTinh]


def get_user_by_id(id):
    return NguoiDung.query.get(id)


def sreach_medicines(q=None, medi_id=None):
    query = Thuoc.query

    if q:
        query = query.filter(Thuoc.tenThuoc.contains(q))

    # if medi_id:
    #     query = query.filter(Thuoc.category_id.__eq__(medi_id))

    return query.all()


def load_medicines():
    return Thuoc.query.all()


def load_examination_details():
    return ChiTietPhieuKham.query.all()


def load_examination():
    return PhieuKham.query.all()


def load_medicines_unit():
    return DonViThuoc.query.all()


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


def count_soBenhNhan(id):
    return db.session.query(func.count(ChiTietDanhSachKham.id))\
        .filter(ChiTietDanhSachKham.danhSachKham_id == id)\
        .scalar()


def get_max_benhNhan():
    qd = QuyDinh.query.get(1)
    soBenhNhan = qd.soBenhNhan
    return soBenhNhan


def get_lichKham_by_date(date):
    return LichKham.query.filter_by(ngayKham=date).first()


def get_danhSachKham_by_lichKhamID(id):
    return DanhSachKham.query.filter_by(lichNgayKham_id=id).first()



if __name__ == '__main__':
    print(load_categories())
