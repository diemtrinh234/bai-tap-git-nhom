def tinh_diem_gpa(diem_so): 
  # TODO: Cần cập nhật logic quy đổi sang hệ 4 
  # return 0.0
  if tinh_diem_gpa(diem_so):
    if diem_so >= 8.5: return 4.0
    elif diem_so >= 7.0: return 3.0
    else: return 2.0
print("Điểm GPA hệ 4 là:", tinh_diem_gpa(8.5))
