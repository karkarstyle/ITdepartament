#списки
lst=[1, 2, 3, 4, 4]
lst.append(4)
lst.remove(3)
print(lst)
print(lst[0])
print(lst[-1])

if 2 in lst:
    print('2 есть в списке')
else:
    print('2 нет в списке')

# lst_con=input('Введите список чисел через пробел: ')
# numbers=lst_con.split(' ')
# print(numbers)

tup=(4, 8, 1) #кортеж
print(tup)
print(tup[0])
print(tup[-1])
#нелья добавлять или убирать из кортежей

f, s, t=tup
print(f)
print(s)
print(t)

print(1 in tup) #true or false

#словари

eng_rus = {
    "cat" :"кот",
    "car": "машина"
}
print(eng_rus)
print(eng_rus['cat'])
eng_rus['cat'] = 'кошка'
print(eng_rus['cat'])

print('car' in eng_rus)  #true or false
print(eng_rus.values()) #вывод списока
print('кот' in eng_rus.values())

print(eng_rus.keys()) #список ключей
print(eng_rus.items()) #ывод пары-ключ значений

print(eng_rus.get("brother", "(нет перевода)"))
print(eng_rus.get("cat", "(нет перевода)"))

# множества

set_from_lst=set(lst)
set_example={1, 2, 3}

print(set_from_lst)
print(set_example)
set_example.add(5)
set_example.remove(2)
print(set_example)
print(set_example-{3, 5})
print(set_example.union({6, 7}))
print(set_example=={1, 3, 5}) #true or false

print(len(lst))
print(len('cat'))
print(len(eng_rus))
print(len(set_example))
print(len(tup))