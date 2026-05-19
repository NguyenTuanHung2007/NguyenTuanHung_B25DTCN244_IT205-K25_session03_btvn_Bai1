print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

# 1. Khởi tạo biến tổng ở NGOÀI vòng lặp
total_budget = 0

# Vòng lặp chạy 3 lần để nhập lương cho 3 nhân viên
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    
    # Nhập mức lương
    salary = int(input("  Nhập mức lương (VNĐ): "))
    
    # Cộng dồn vào tổng
    total_budget = total_budget + salary

# Sau khi vòng lặp kết thúc, in kết quả cuối cùng
print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")