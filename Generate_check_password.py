import random

# TASK 1
s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2 = "0123456789"
s3 = "~!@#$%^&*()_+{}[\]:/"

s = s1.upper() + s1.lower() + s2 + s3
password = ""

for i in range(15):
    p = random.choice(s)
    password = password + p

print(f"New password: {password}")


# TASK 2
print("\nПРОВЕРКА БУКВ В ПАРОЛЕ: ")
for symbol in password:
    alpha = symbol.isalpha()
    print(f"{symbol} - {alpha}")
    if (not alpha) and (symbol == "@"):
        print(f"It is {symbol}")


