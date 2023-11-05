#Bản quyền của NguyenCaoMinh_22410082
import math

class ShapeInputError(Exception):
    pass

# Hàm tính tổng các số
def tinh_tong(*args):
    return sum(args)

# Hàm tính tích các số
def tinh_tich(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Hàm tính chu vi hình vuông, chữ nhật, tròn
def tinh_chu_vi(**kwargs):
    shape = kwargs.get('hinh', None)
    if shape == 1:
        if 'canh' in kwargs and all(key not in kwargs for key in ['chieu_rong', 'chieu_dai', 'ban_kinh']):
            side_length = kwargs.get('canh', 0)
            return 4 * side_length, side_length * side_length
        else:
            raise ShapeInputError("Hình vuông chỉ có cạnh")
    elif shape == 2:
        if 'chieu_rong' in kwargs and 'chieu_dai' in kwargs and all(key not in kwargs for key in ['canh', 'ban_kinh']):
            width = kwargs.get('chieu_rong', 0)
            length = kwargs.get('chieu_dai', 0)
            return 2 * (width + length), width * length
        else:
            raise ShapeInputError("Hình chữ nhật chỉ có chiều dài và chiều rộng")
    elif shape == 3:
        if 'ban_kinh' in kwargs and all(key not in kwargs for key in ['canh', 'chieu_rong', 'chieu_dai']):
            radius = kwargs.get('ban_kinh', 0)
            return 2 * math.pi * radius, math.pi * radius * radius
        else:
            raise ShapeInputError("Hình tròn chỉ có bán kính")
    else:
        raise ShapeInputError("Hình không hợp lệ")

# Hàm main
def main():
    try:
        # Nhập số từ người dùng
        nums = list(map(float, input("Nhập các số cách nhau bằng dấu cách: ").split()))

        # Tính tổng và tích các số
        print("Tổng các số là:", tinh_tong(*nums))
        print("Tích các số là:", tinh_tich(*nums))

        print("Chọn loại hình cần tính:")
        print("1. Hình vuông")
        print("2. Hình chữ nhật")
        print("3. Hình tròn")

        choice = int(input("Nhập số tương ứng với loại hình: "))

        if choice in [1, 2, 3]:
            if choice == 1:
                canh = float(input("Nhập độ dài cạnh: "))
                chu_vi, dien_tich = tinh_chu_vi(hinh=choice, canh=canh)
                print(f"Chu vi hình vuông: {chu_vi}, Diện tích hình vuông: {dien_tich}")
            elif choice == 2:
                chieu_rong = float(input("Nhập chiều rộng: "))
                chieu_dai = float(input("Nhập chiều dài: "))
                chu_vi, dien_tich = tinh_chu_vi(hinh=choice, chieu_rong=chieu_rong, chieu_dai=chieu_dai)
                print(f"Chu vi hình chữ nhật: {chu_vi}, Diện tích hình chữ nhật: {dien_tich}")
            else:
                ban_kinh = float(input("Nhập bán kính: "))
                chu_vi, dien_tich = tinh_chu_vi(hinh=choice, ban_kinh=ban_kinh)
                print(f"Chu vi hình tròn: {chu_vi}, Diện tích hình tròn: {dien_tich}")
        else:
            print("Lựa chọn không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số.")
    except ShapeInputError as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
