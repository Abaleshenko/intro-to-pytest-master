symbols = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
}

ask = input("Phrase: ")

length = len(ask)
output = ""

for i in range(length):
    if ask[i] in symbols.keys():
        output = output + " " + symbols.get(ask[i])

print(output)


