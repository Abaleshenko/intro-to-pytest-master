from time import sleep

OFFSET = 13.12
WC_FACTOR1 = .6215
WC_FACTOR2 = -11.37
WC_FACTOR3 = .3965
WC_EXPONENT = .16

temperature = float(input("Fill the gap of temperature in C "))
speed_of_wind = float(input("Fill the gap of velocity of wind in km/hour "))

if temperature <= 10 and speed_of_wind > 4.8:

    wind_chill_index = OFFSET + \
                       WC_FACTOR1 * temperature + \
                       WC_FACTOR2 * speed_of_wind ** WC_EXPONENT + \
                       WC_FACTOR3 * temperature * speed_of_wind ** WC_EXPONENT

    # LOADER
    for idx in range(10):
        print("\r{0}%".format((idx + 1) * 10), end='\t')
        sleep(.4)

    print(f"WIND CHILL INDEX --> {round(wind_chill_index, 1)} Celsius")

else:
    print("Некорректные данные")
