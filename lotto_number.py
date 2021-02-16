import random

possible_number = []
picked_list = [0, 0, 0, 0, 0, 0, 0]
bonus_num = 0
lotto_list = []

def lotto_number():
    total_number = 0
    bonus = 0
    
    while total_number < 45:
        total_number = total_number + 1
        possible_number.append(total_number)

    for i in range(len(picked_list)):
        randomNumber = random.choice(possible_number)
        picked_list[i] = randomNumber

    bonus = picked_list[6]
    del picked_list[6]
    other_number = sorted(picked_list)
    #six_number =' '.join(other_number)
    return other_number, bonus

lotto_list, bonus_num = lotto_number()

def bonus_number():
    return bonus_num

def lotto_number():
    return lotto_list
