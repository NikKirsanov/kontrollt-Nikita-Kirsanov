from ipaddress import summarize_address_range
from math import *
from random import *



#5
print("sisesta number")
n = int(input())
sum = 0
korrutis = 1
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
    print("summa:", sum)
    print("korrutis:",korrutis)



#3
print("Arvuti mõistab numbrit 1-100 ja sina üritad seda ära arvata")
n = randint(0, 100)
i = 0
while True:
    a =int(input())
    if a == n:
        print("Sina võisid")
        break
    if a < n:
        print("peidutud arv on suurem")
    else:
        print("peidetud arv on väiksem")
    i += 1
    if i ==10:
        print(f"sa kaotasid. Varjatud number{n}")
        break


#2 
#Посчитать сумму числового ряда от 0 до L (например, 14) включительно. Например, 0+1+2+3+…+14;

L=int(input("Sisestage number L: "))
sum = 0  #сумма равна 0
for i in range(L+1):
   sum += i
print("Numbrite summa 0 kuni L on: ", sum)

print()
#1Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n зайцев. Mежду двумя соседними зайцами также имеется пустой
#(из пробелов) столбец. Разрешается вывести пустой столбец после последнего зайца. Для упрощения рисования скопируйте зайца  в среду разработки.

#2 v
n= int(input("Enter a number (1-9): "))
pin=["  (\_/)",
      "  (o o)",
     "  / | \*"]
for i in pin:
   print(i*a)

#1 v
n = int(input("Enter a number (1-9): "))

for i in range(n):
    print("   (\_/) ")
    print("   (o o) ")
    print("   / | \ ")




