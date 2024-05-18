-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: phongmachdb
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chi_tiet_danh_sach_kham`
--

DROP TABLE IF EXISTS `chi_tiet_danh_sach_kham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chi_tiet_danh_sach_kham` (
  `danhSachKham_id` int NOT NULL,
  `nguoiDung_id` int NOT NULL,
  `hoTen` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `gioiTinh` enum('Nam','Nu','KhongTraLoi') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `namSinh` date NOT NULL,
  `soDienThoai` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `diaChi` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `danhSachKham_id` (`danhSachKham_id`),
  KEY `nguoiDung_id` (`nguoiDung_id`),
  CONSTRAINT `chi_tiet_danh_sach_kham_ibfk_1` FOREIGN KEY (`danhSachKham_id`) REFERENCES `danh_sach_kham` (`id`),
  CONSTRAINT `chi_tiet_danh_sach_kham_ibfk_2` FOREIGN KEY (`nguoiDung_id`) REFERENCES `nguoi_dung` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chi_tiet_danh_sach_kham`
--

LOCK TABLES `chi_tiet_danh_sach_kham` WRITE;
/*!40000 ALTER TABLE `chi_tiet_danh_sach_kham` DISABLE KEYS */;
INSERT INTO `chi_tiet_danh_sach_kham` VALUES (1,1,'Nguyễn Trần Thanh Phong','Nam','2003-01-16','0903030303','Address1',3),(2,1,'Trương Văn Huy','Nam','2003-07-10','0702030848','Address2',4),(3,1,'Huỳnh Hữu Lộc','Nam','2003-09-18','0792030300','Address3',5),(3,1,'Nguyễn Văn A','Nam','1990-09-11','0903727858','Address4',6);
/*!40000 ALTER TABLE `chi_tiet_danh_sach_kham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chi_tiet_phieu_kham`
--

DROP TABLE IF EXISTS `chi_tiet_phieu_kham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chi_tiet_phieu_kham` (
  `soLuong` int DEFAULT NULL,
  `cachDung` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phieuKham_id` int NOT NULL,
  `thuoc_id` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `phieuKham_id` (`phieuKham_id`),
  KEY `thuoc_id` (`thuoc_id`),
  CONSTRAINT `chi_tiet_phieu_kham_ibfk_1` FOREIGN KEY (`phieuKham_id`) REFERENCES `phieu_kham` (`id`),
  CONSTRAINT `chi_tiet_phieu_kham_ibfk_2` FOREIGN KEY (`thuoc_id`) REFERENCES `thuoc` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chi_tiet_phieu_kham`
--

LOCK TABLES `chi_tiet_phieu_kham` WRITE;
/*!40000 ALTER TABLE `chi_tiet_phieu_kham` DISABLE KEYS */;
INSERT INTO `chi_tiet_phieu_kham` VALUES (10,'Uống',1,4,1),(2,'Uống',1,5,2),(10,'Uống',1,3,3),(10,'Uống',2,6,4),(10,'Uống',2,7,5),(4,'Uống',2,13,6),(20,'Uống',3,11,7),(24,'Uống',3,18,8),(12,'Uống',3,10,9),(10,'Uống',3,4,10),(20,'Uống',4,19,11),(20,'Uống',4,22,12),(10,'Uống',4,17,13),(5,'Uống',4,14,14),(10,'Uống',5,3,15),(10,'Uống',5,4,16),(5,'Uống',6,5,17),(5,'Uống',6,6,18);
/*!40000 ALTER TABLE `chi_tiet_phieu_kham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `danh_sach_kham`
--

DROP TABLE IF EXISTS `danh_sach_kham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `danh_sach_kham` (
  `lichNgayKham_id` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `lichNgayKham_id` (`lichNgayKham_id`),
  CONSTRAINT `danh_sach_kham_ibfk_1` FOREIGN KEY (`lichNgayKham_id`) REFERENCES `lich_kham` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `danh_sach_kham`
--

LOCK TABLES `danh_sach_kham` WRITE;
/*!40000 ALTER TABLE `danh_sach_kham` DISABLE KEYS */;
INSERT INTO `danh_sach_kham` VALUES (1,1),(3,2),(5,3);
/*!40000 ALTER TABLE `danh_sach_kham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `don_vi_thuoc`
--

DROP TABLE IF EXISTS `don_vi_thuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `don_vi_thuoc` (
  `tenDonVi` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `don_vi_thuoc`
--

LOCK TABLES `don_vi_thuoc` WRITE;
/*!40000 ALTER TABLE `don_vi_thuoc` DISABLE KEYS */;
INSERT INTO `don_vi_thuoc` VALUES ('Chai',1),('Vỹ',2),('Viên',3);
/*!40000 ALTER TABLE `don_vi_thuoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hoa_don`
--

DROP TABLE IF EXISTS `hoa_don`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hoa_don` (
  `ngayKham` date NOT NULL,
  `hoTenBenhNhan` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tienKham` float DEFAULT NULL,
  `tienThuoc` float DEFAULT NULL,
  `nguoiDung_id` int NOT NULL,
  `phieuKham_id` int NOT NULL,
  `da_thanh_toan` tinyint(1) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `nguoiDung_id` (`nguoiDung_id`),
  KEY `phieuKham_id` (`phieuKham_id`),
  CONSTRAINT `hoa_don_ibfk_1` FOREIGN KEY (`nguoiDung_id`) REFERENCES `nguoi_dung` (`id`),
  CONSTRAINT `hoa_don_ibfk_2` FOREIGN KEY (`phieuKham_id`) REFERENCES `phieu_kham` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoa_don`
--

LOCK TABLES `hoa_don` WRITE;
/*!40000 ALTER TABLE `hoa_don` DISABLE KEYS */;
INSERT INTO `hoa_don` VALUES ('2024-05-18','Nguyễn Trần Thanh Phong',100000,386000,1,1,1,1),('2024-05-19','Trương Văn Huy',100000,566000,1,2,1,2),('2024-05-20','Huỳnh Hữu Lộc',100000,2100000,1,3,1,3),('2024-05-20','Nguyễn Văn A',100000,1220000,1,4,1,4),('2024-06-01','Nguyễn Văn A',100000,350000,1,5,1,7),('2024-06-15','Nguyễn Trần Thanh Phong',100000,215000,1,6,0,8);
/*!40000 ALTER TABLE `hoa_don` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lich_kham`
--

DROP TABLE IF EXISTS `lich_kham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lich_kham` (
  `ngayKham` date NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lich_kham`
--

LOCK TABLES `lich_kham` WRITE;
/*!40000 ALTER TABLE `lich_kham` DISABLE KEYS */;
INSERT INTO `lich_kham` VALUES ('2024-05-18',1),('2024-05-19',3),('2024-05-20',5);
/*!40000 ALTER TABLE `lich_kham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loai_thuoc`
--

DROP TABLE IF EXISTS `loai_thuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loai_thuoc` (
  `tenLoai` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tenLoai` (`tenLoai`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loai_thuoc`
--

LOCK TABLES `loai_thuoc` WRITE;
/*!40000 ALTER TABLE `loai_thuoc` DISABLE KEYS */;
INSERT INTO `loai_thuoc` VALUES ('Thuốc Ngủ',1),('Thuốc Nhứt Đầu',2);
/*!40000 ALTER TABLE `loai_thuoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nguoi_dung`
--

DROP TABLE IF EXISTS `nguoi_dung`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nguoi_dung` (
  `hoTen` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `anhDaiDien` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `vaiTro_NguoiDung` enum('BenhNhan','YTa','BacSi','ThuNgan','ADMIN') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nguoi_dung`
--

LOCK TABLES `nguoi_dung` WRITE;
/*!40000 ALTER TABLE `nguoi_dung` DISABLE KEYS */;
INSERT INTO `nguoi_dung` VALUES ('Quản Trị Viên','https://res.cloudinary.com/dstjar2iy/image/upload/v1712391157/lwocwuc4opc6c9kl6fcw.jpg','admin','c4ca4238a0b923820dcc509a6f75849b','ADMIN',1);
/*!40000 ALTER TABLE `nguoi_dung` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieu_kham`
--

DROP TABLE IF EXISTS `phieu_kham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieu_kham` (
  `benhNhan_id` int NOT NULL,
  `tenBenhNhan` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `trieuChung` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `duDoanBenh` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ngayKham` date NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `benhNhan_id` (`benhNhan_id`),
  CONSTRAINT `phieu_kham_ibfk_1` FOREIGN KEY (`benhNhan_id`) REFERENCES `nguoi_dung` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu_kham`
--

LOCK TABLES `phieu_kham` WRITE;
/*!40000 ALTER TABLE `phieu_kham` DISABLE KEYS */;
INSERT INTO `phieu_kham` VALUES (1,'Nguyễn Trần Thanh Phong','Ho','Cảm','2024-05-18',1),(1,'Trương Văn Huy','Chóng Mặt','Sốt','2024-05-19',2),(1,'Huỳnh Hữu Lộc','Hắt Xì Nhiều','Cảm','2024-05-20',3),(1,'Nguyễn Văn A','Nhứt Đầu','Say nắng','2024-05-20',4),(1,'Nguyễn Văn A','Ho, Sốt','Cảm Nặng','2024-06-01',5),(1,'Nguyễn Trần Thanh Phong','Ho','Cảm','2024-06-15',6);
/*!40000 ALTER TABLE `phieu_kham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quy_dinh`
--

DROP TABLE IF EXISTS `quy_dinh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quy_dinh` (
  `soTienKham` float NOT NULL,
  `soLoaiThuoc` int NOT NULL,
  `soBenhNhan` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quy_dinh`
--

LOCK TABLES `quy_dinh` WRITE;
/*!40000 ALTER TABLE `quy_dinh` DISABLE KEYS */;
INSERT INTO `quy_dinh` VALUES (100000,30,40,1);
/*!40000 ALTER TABLE `quy_dinh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thuoc`
--

DROP TABLE IF EXISTS `thuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thuoc` (
  `tenThuoc` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `congDung` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` float NOT NULL,
  `donViThuoc_id` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tenThuoc` (`tenThuoc`),
  KEY `donViThuoc_id` (`donViThuoc_id`),
  CONSTRAINT `thuoc_ibfk_1` FOREIGN KEY (`donViThuoc_id`) REFERENCES `don_vi_thuoc` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thuoc`
--

LOCK TABLES `thuoc` WRITE;
/*!40000 ALTER TABLE `thuoc` DISABLE KEYS */;
INSERT INTO `thuoc` VALUES ('Paracetamol','Giảm đau, hạ sốt',15000,3,3),('Amoxicillin','Kháng sinh, điều trị nhiễm khuẩn',20000,1,4),('Ibuprofen','Giảm đau, kháng viêm',18000,2,5),('Ciprofloxacin','Kháng sinh, điều trị nhiễm khuẩn',25000,3,6),('Metformin','Điều trị tiểu đường',30000,3,7),('Atorvastatin','Điều trị mỡ máu',40000,2,8),('Amlodipine','Điều trị tăng huyết áp',22000,2,9),('Lisinopril','Điều trị tăng huyết áp',27000,1,10),('Omeprazole','Điều trị loét dạ dày',35000,1,11),('Prednisone','Điều trị viêm',32000,1,12),('Simvastatin','Điều trị mỡ máu',29000,3,13),('Furosemide','Điều trị phù, tăng huyết áp',24000,3,14),('Losartan','Điều trị tăng huyết áp',21000,2,15),('Clopidogrel','Chống đông máu',33000,1,16),('Levothyroxine','Điều trị suy giáp',28000,3,17),('Azithromycin','Kháng sinh, điều trị nhiễm khuẩn',50000,3,18),('Metronidazole','Kháng sinh, điều trị nhiễm khuẩn',26000,3,19),('Doxycycline','Kháng sinh, điều trị nhiễm khuẩn',34000,2,20),('Hydrochlorothiazide','Điều trị tăng huyết áp',23000,1,21),('Cetirizine','Điều trị dị ứng',15000,3,22);
/*!40000 ALTER TABLE `thuoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thuoc_loaithuoc`
--

DROP TABLE IF EXISTS `thuoc_loaithuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thuoc_loaithuoc` (
  `thuoc_id` int NOT NULL,
  `loaiThuoc_id` int NOT NULL,
  PRIMARY KEY (`thuoc_id`,`loaiThuoc_id`),
  KEY `loaiThuoc_id` (`loaiThuoc_id`),
  CONSTRAINT `thuoc_loaithuoc_ibfk_1` FOREIGN KEY (`thuoc_id`) REFERENCES `thuoc` (`id`),
  CONSTRAINT `thuoc_loaithuoc_ibfk_2` FOREIGN KEY (`loaiThuoc_id`) REFERENCES `loai_thuoc` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thuoc_loaithuoc`
--

LOCK TABLES `thuoc_loaithuoc` WRITE;
/*!40000 ALTER TABLE `thuoc_loaithuoc` DISABLE KEYS */;
/*!40000 ALTER TABLE `thuoc_loaithuoc` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-18  0:17:52
