# Консольная версия игры "Быки и Коровы"
import random

number_length =  int(input("Введите длину числа:"))
start_diapozon = int(input("Введите число начало дипозона:"))
end_diapozon = int(input("Введите число завершения дипозона:"))

random_number = [random.randint(start_diapozon, end_diapozon) for t in range(number_length)]

bull = None

while bull != number_length: 
    my_list = list(input("Введите "+ str(number_length) +" числа:"))
    
    cow = 0
    bull = 0
    
    num = None
    norm_list = []
    
    for j in range(len(my_list)):
        num = int(my_list[j])
        norm_list.append(num)
    print(norm_list)
    
    for i in range(len(random_number)):
        if random_number[i] == norm_list[i]:
            bull += 1
        elif random_number[i] in norm_list:
            cow += 1
            
    print("bull" + " " + str(bull))
    print("cow" + " " + str(cow))
else:
    print("YOU WINN!!!")