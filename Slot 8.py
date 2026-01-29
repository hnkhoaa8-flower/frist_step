#- cho phep nguoi dung nhap 10 so ngyuyen sau do in ra so Nguyen co gia tri lon thu 2 trong danh sach
lst = []
nums=0
while nums<10:
    nums=nums+1
    inter=int(input('Enter int'))
    if inter not in lst:
        lst.append(inter)
print(lst)

lst.sort()

print(lst)
print(lst[-2])

#ctr cho phep nhap ho ten sv, sau do in ten sv len man hinh
#ctr in ra so luong trong chuoi nguoi dung nhap
#ctr in ra so luong chu A xuat hien trong chuoi nguoi dung nhap
#ctr cho phep nhap mot chuoi bat ky, ctr in ra cac tu trong chuoi duoc viet hoa moi tu, sau khi da loai bo cac khoang trang du thua
