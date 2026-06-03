try:
    a = input("数字を入れてね:")
    b = input("もう１つ数字を入れてね:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")

