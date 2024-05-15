import json, hashlib
from phongmachapp.models import Thuoc, LoaiThuoc, DonViThuoc, NguoiDung


def load_categories():
    with open('data/categories.json', encoding='utf-8') as f:
        return json.load(f)


def get_user_by_id(id):
    return NguoiDung.query.get(id)


def load_medicines():
    return Thuoc.query.all()

def load_medicines_unit():
    return DonViThuoc.query.all()


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    print(password)
    print(username)
    return NguoiDung.query.filter(NguoiDung.username.__eq__(username.strip()),
                                  NguoiDung.password.__eq__(password)).first()


if __name__ == '__main__':
    print(load_categories())
