from math import sqrt


R = 6371

for i in range(1, 11):
    distance = sqrt((R + i)**2 - R**2)  # 1.06 * sqrt((R + i)**2 - R**2)
    # 1.06 -в реальной жизни атмосферная рефракция расширяет горизонт примерно на 6%

    print(f"Расстояние до горизонта при такой высоте {i} км: {round(distance)} км")