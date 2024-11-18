nhiet_do = int(input("Nhập nhiệt độ: "))
def kiemtra_nuocsoi(nhiet_do):
    if nhiet_do<100:
        return "Nước chưa sôi !"
    else:
        return "Nước đã sôi !"
print(kiemtra_nuocsoi(nhiet_do))

nhiet_do = int(input("Nhập nhiệt độ: "))
def kiemtra_nuocsoi(nhiet_do):
    return "Nước "+("đã sôi !" if nhiet_do ==100 else "chưa sôi !")
print (kiemtra_nuocsoi(nhiet_do))