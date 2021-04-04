rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
       'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
print('Здравствуйте! Давайте зашифруем (или дешифруем) ваш текст.')
print('Вы знакомы с шифрованием методом Цезаря? (введите да или нет)')

proverka = ['да', 'нет']
z = input().lower()
cycle = 0
while cycle != 1:
    try:
        proverka.index(z)
        cycle = 1
    except ValueError:
        print('Введите -да- или -нет-')
        z = input().lower()

if z == 'да':
    print('\nОтлично!')
elif z == 'нет':
    print(
        'Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,\nнаходящимся на некотором постоянном числе позиций правее него в алфавите.\nНапример, в шифре со сдвигом на 3, А была бы заменена на Г, Б станет Д, и так далее.')

print('\nВведите язык текста:\nРусский - 1\nАнглийский - 2')
yazik = ['1', '2']
vvod = input()
cycle = 0
while cycle != 1:
    try:
        yazik.index(vvod)
        cycle = 1
    except ValueError:
        print('Введите -1- или -2-')
        vvod = input().lower()

if vvod == '1':
    lang = rus
else:
    lang = eng


def shifrovka(txt, lang):
    print('Какой шаг шифрования хотите задать? (Для дешифрования введите отрицательное значение)')

    r = 0
    while r != 1:
        ste = input()
        try:
            step = int(ste)
            r = 1
        except ValueError:
            print('Пожалуйста введите целое число')
            r = 0
        dlina = len(lang)
        if step < 0:
            otric = True
        else:
            otric = False
        modstep = abs(step)
        while modstep > dlina:
            modstep -= dlina
        if otric == True:
               step = (-1)*modstep
        else:
               step = modstep
        neizm = " ,.!?:;'1234567890{}[]@#$%^&*"
        out = ''
        for char in txt:
            if neizm.find(char) == -1:
                y = lang.index(char) + step
                while y >= dlina:
                    y -= dlina
                out += lang[y]
            else:
                out += char
        return out


txt = input('Введите ваш текст: ').lower()
proverim_txt = 0
while proverim_txt == 0:
    neizm = " ,.!?:;'1234567890{}[]@#$%^&*"
    txt_prov = ''
    for char in txt:
        if char not in neizm:
            txt_prov += char
    try:
        for char in txt_prov:
            d = lang.index(char)
        proverim_txt = 1
    except ValueError:
        print('В вашем тексте есть буквы другого языка. Попробуйте снова.')
        txt = input('Введите ваш текст: ').lower()
print('Результат шифрования:', shifrovka(txt, lang))
