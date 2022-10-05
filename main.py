filename = input('Введите имя файла:')
f = open(f'{filename}.txt', encoding='utf-8')
file = f.read().split('\n')
data = []
f.close()

class Contact:
    def __init__(self, name, num, mail):
        self.name, self.num, self.mail = name, num, mail

    def changename(self, newname):
        self.name = newname

    def changenum(self, newnum):
        self.num = newnum

    def changemail(self, newmail):
        self.mail = newmail

for i in file:
    something = i.split(',')
    some = [i if i.rstrip() != '' else 'no' for i in something]
    contact = Contact(some[0], some[1], some[2])
    data.append(contact)

while True:
    what_to_do = int(input('Выберите действие: 1-поиск, 2-вывести на экран что-либо, 3-редактировать:'))
    if what_to_do == 1:
        search = input('Введите информацию для поиска:')
        if '@' in search:
            cnt = 0
            n = 0
            while cnt < len(data):
                if search in data[cnt].mail or search == data[cnt].mail or search.capitalize() in data[cnt].mail or search.capitalize() == data[cnt].mail:
                    print(f'результат: {data[cnt].name}, {data[cnt].num}, {data[cnt].mail}')
                    n += 1
                cnt += 1
            else:
                if n == 0:
                    print('Ничего не найдено.')
        elif '+' in search:
            cnt = 0
            n = 0
            while cnt < len(data):
                if search in data[cnt].num or search == data[cnt].num:
                    print(f'результат: {data[cnt].name}, {data[cnt].num}, {data[cnt].mail}')
                    n += 1
                cnt += 1
            else:
                if n == 0:
                    print('Ничего не найдено.')
        else:
            cnt = 0
            n = 0
            while cnt < len(data):
                if search in data[cnt].name or search == data[cnt].name or search.capitalize() in data[cnt].name or search.capitalize() == data[cnt].name:
                    print(f'результат: {data[cnt].name}, {data[cnt].num}, {data[cnt].mail}')
                    n += 1
                cnt += 1
            else:
                if n == 0:
                    print('Ничего не найдено.')
    if what_to_do == 2:
        names = []
        nums = []
        mails = []
        vivod = input('Людей с 1-не заполненным имэйлом, 2-с незаполненным номером, 3-вместе')
        if '1' == vivod:
            for i in data:
                if i.mail == 'no':
                    print(i.name, i.num, i.mail)
        if '2' == vivod:
            for i in data:
                if i.num == 'no':
                    print((i.name, i.num, i.mail))
        if '3' == vivod:
            for i in data:
                if i.mail == 'no' and i.num == 'no':
                    print(i.name, i.num, i.mail)
    if what_to_do == 3:
        for i in range(len(data)):
            print(i, data[i].name, data[i].num, data[i].mail)
        change = int(input('Выберите номер:'))
        what_to_change = int(input('Что хотите поменять:1-ФИО, 2-номер 3-mail:'))
        what_to_write = input('Введите новую информацию:')
        if what_to_change == 1:
            data[change].changename(what_to_write)
        elif what_to_change == 2:
            data[change].changenum(what_to_write)
        elif what_to_change == 3:
            data[change].changemail(what_to_write)
        print('Измененные данные:')
        for i in data:
            print(i.name, i.num, i.mail)