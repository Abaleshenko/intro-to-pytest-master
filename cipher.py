def encryption(plaintext, shift):
    ciphertext = ''

    for i in range(len(plaintext)):
        special = plaintext[i].lower()

        if special == " ":
            ciphertext += ' '

        elif special.isalpha():
            ciphertext += chr((ord(special) + shift - 97) % 26 + 97)

    return ciphertext


def decryption(ciphertext, shift):
    plaintext = ''
    for i in range(len(ciphertext)):

        special = ciphertext[i].lower()
        if special == " ":
            plaintext += ' '
        elif special.isalpha():
            plaintext += chr((ord(special) - shift - 97) % 26 + 97)
    return plaintext


while True:
    print(
        'Добро пожаловать в алгоритм шифрования Цезаря!..\n \
        [*] Нажмите 1, что зашифровать пароль \n \
        [*] Нажмите 0, что расзашифровать пароль \n \
        [*] Нажмите 01, чтобы выйти ')

    way = input('Введите номер Encryption/Decryption: ')

    if way.isdigit():
        if way == '1':
            sen = input('Введите текст для шифрования: ')
            key = int(input('Введите сдвиг Цезаря: '))
            print(50 * '-')
            print(f'Результат кода Цезаря ---> {encryption(sen, key)}')
            print(50 * '-')
            print('Special symbols (!,# etc and numbers) are deleted..')
            con = input('Shall we continue ? [Any Key/no]')
            if con == 'no':
                print('Exiting..')
                break
            else:
                pass

        elif way == '0':
            csen = input('Insert the ciphertext : ')
            key = int(input('Insert shift value(Only integer values) : '))
            print(50 * '-')
            print(f'Your plaintext ---> {decryption(csen, key)}')
            print(50 * '-')
            print('Special symbols (!,# etc and numbers) are deleted..')
            con = input('Shall we continue ? [Any Key/no]')
            if con == 'no':
                print('Exiting..')
                break
            else:
                pass
        elif way == '01':
            print('Exiting..')
            break
        else:
            print('Exception error .. \n'
                  'Please insert 0 or 1 ')
