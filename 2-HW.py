
a = 19
b = "slovo"
d = (1,2,3)
c = 2 + 3j
e=True 
print(type(a))
print(type(e))
print(type(d))
print(type(c))
print(type(b))

print("Второе задание")
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
     ele = int(input())
     lst.append(ele)
print(lst)
h=0
newlist=[]
if(n%2==0):
    for i in range(0,n,2):
        for f in range(1,n,2):
            h=lst[i]+lst[f]
            i+=2
            print(i,f,h)
            newlist.append(h)
        break
else:
    for y in range(0,n,2):
        for x in range(1,n,2):
            h=lst[y]+lst[x]
            y+=2
            print(y,x,h)
            newlist.append(h)
        break
    newlist.append(ele)
print(newlist)
    
print("Третье задание")
seasons = {'Winter': (12, 1, 2),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}
 
month = int(input('Choose month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)



print('Четвертое задание')
my_str = input("введите строку ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1
print("Пятое задание")
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (стоп число -- 666)"))
while digit != 666:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
        

    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))
print('Шестое задание')
tovar = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'Ед. измерения': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед. измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Чтобы выйти из программы нажмите 'Q', Чтобы внести товар в базу введите 'J', Чтобы просмотреть список введите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    if control == 'J':       
        for f in features.keys():
            feature_ = input(f'Input feature "{f}"')
            features[f] = int(feature_) if (f == 'Цена' or f == 'Количество') else feature_
            analytics[f].append(features[f])
    tovar.append((num, features))

