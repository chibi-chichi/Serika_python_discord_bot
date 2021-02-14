import random

#possible_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
total_number = 0
possible_number = []
picked_list = [0, 0, 0, 0, 0, 0, 0]
bonus = 0
def lotto_number():
    while total_number < 45:
        total_number = total_number + 1
        possible_number.append(total_number)

    for i in range(len(picked_list)):
        randomNumber = random.choice(possible_number)
        picked_list[i] = randomNumber

    bonus = picked_list[6]
    del picked_list[5:]
    other_number = sorted(picked_list)
    six_number =' '.join(other_number)
    return six_number

def bonus_number():
    return bonus