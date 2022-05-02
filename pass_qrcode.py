from random import sample
from qrcode import make


def call_password(n):
    alpha = "abcdefhijklmnopqrstuvxyz"
    digits = '1234567890'
    symbols = '!@#$%^&*()_+~-[]{};/'
    all_n = alpha.lower() + alpha.upper() + digits + symbols
    password = ''.join(sample(all_n, n))
    return password


def qr_code(password):
    file = input('Введите имя для файла ')
    picture = make(password)
    picture.save(f"{file}.png")


def follow():
    chars = int(input("Сколько символов будет содержать новый пароль? "))
    password = call_password(chars)
    print(f"Сгенерированній пароль: {password}")
    qr_code(password)
    print("QRCODE WAS SAVED!")


if __name__ == "__main__" :
    follow()