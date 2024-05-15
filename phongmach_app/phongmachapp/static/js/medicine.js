function addMedicine() {
        // Lấy dòng cuối cùng trong bảng
        let lastRow = $('.medicineTable tbody tr:last');

        // Sao chép dòng cuối cùng và thêm vào cuối bảng
        let newRow = lastRow.clone();

        // Tăng biến đếm số thứ tự lên 1
//        sttCount++;

        // Cập nhật số thứ tự của dòng mới
//        newRow.find('td:first').text(sttCount);

        // Đặt lại giá trị của các ô input trong dòng mới thành rỗng
        newRow.find('input').val('');

        // Thêm dòng mới vào bảng
        $('.medicineTable tbody').append(newRow);
}