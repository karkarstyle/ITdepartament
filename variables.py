name=input("Введите имя:")
age=float(input("Введите возраст: "))
is_working_now=input("Работает сейчас? (1 или 0)") == "1"
workplace = None

if is_working_now:
    workplace = input("Место работы: ")
if is_working_now and not workplace:
# if is_working_now and  (workplace == "" or workplace is None):
    print("не заполнено место работы")

#print("Имя: " +name)
print(f"Имя: {name}")
print(f"Возраст: {age}")
print("Работает сейчас: " +str(is_working_now))
if is_working_now:
    print("Место работы: " +str(workplace))

if age>=20:
    print("Пользователю больше 20 лет")
elif age>=18:
    print("совершеннолетний")
else:
    print("несовершеннолетний")

str_template="Информация о пользователе: {}-{}"
print(str_template.format(name, age))
# print(name.upper())
# print(name.lower())
# print(name.find("а"))
# print(name.replace("я","ян"))
# print(name)
#
# a=2
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(5//a) #деление без остатка
#
# num=input("Введите число:")
# num=int(num)
# print(2*num)

