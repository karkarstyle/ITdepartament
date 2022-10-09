lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

eng_rus = {
    "cat" :"кот",
    "car": "машина"
}

for item in lst:
    print(item)

print(range(10))
print(list(range(1,11)))

for i in range(10):
    if i==1:
        #continue
        break
    print(i)

cats=['Барсик', 'Мурзик', 'Васька']
print(list(enumerate(cats)))
for i, cat in enumerate(cats):
     print(f"{i}.{cat}")

print(list(reversed(cats)))
print(list(sorted(cats)))

for key, value in eng_rus.items():
    print('ключ', key, "значение", value)

i=0
while i!=5:
    i+=1
print(i)

#вывод алфавита
print('а', ord('а'))
symbol_number=ord("а")
while symbol_number<=ord('я'):
    print(symbol_number, chr(symbol_number))
    symbol_number+=1