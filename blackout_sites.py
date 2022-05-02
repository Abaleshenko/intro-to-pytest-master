"""
Выполняем блокиратор сайтов

Скрипт отыщет по адресу C:\Windows\System32\drivers\etc\hosts
файл и будет записывать там строку для блокирования
сайта из списка, если ещё не наступило время разблокировки

"""

from datetime import datetime

end_time = datetime(2022, 1, 4, 14, 58)  # y, month, d, h, min - До когда заблокировать сайты
out_sites = ['www.facebook.com', 'facebook.com']  # из этого списка

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"


def blackout_sites():
    if datetime.now() < end_time:
        print("BLACKOUT")
        with open(hosts_path, 'r+') as host:
            host_description = host.read()
            for site in out_sites:
                if site not in host_description:
                    host.write(redirect + " " + site + "\n")

    else:
        print("AVAILABLE")
        with open(hosts_path, 'r+') as host:
            lines = host.readlines()
            host.seek(0)
            for line in lines:
                if not any(site in line for site in out_sites):
                    host.write(line)
            host.truncate()


if __name__ == "__main__":
    blackout_sites()


"""
Одна из причин делать именно так – тот факт, что иногда вы пишете модуль (файл с расширением .py), предназначенный для 
непосредственного исполнения. Кроме того, он также может быть импортирован и использован из другого модуля. Производя 
подобную проверку, вы можете сделать так, что код будет исполняться только при условии, что данный модуль запущен как 
программа, и запретить исполнять его, если его хотят импортировать и использовать функции модуля отдельно.
"""