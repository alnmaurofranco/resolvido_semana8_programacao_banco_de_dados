import math
import random

def friends_age_covariance():
    ages = [22, 6, 18]
    num_friends = [4, 10, 9]
    print(f'Covariância: {covariance(ages, num_friends)}')


def friends_age_correlation():
    ages = [22, 6, 18]
    num_friends = [4, 10, 9]
    print(f'Correlação: {correlation(ages, num_friends)}')


def friends_amount_minutes_one(n):
    list_friends = []
    minutes_list = []

    for i in range(n):
        list_friends.append(random.randint(0, 1000))
    
    for item in list_friends:
        minutes_list.append(item * 2)

    return (list_friends, minutes_list)

def friends_amount_minutes_two(n):
    random_number = 0
    list_friends = []
    minutes_list = []    

    for i in range(n):
        list_friends.append(random.randint(0, 1000))
    
    for item in list_friends:
        random_number = random.randint(1, 9)
        minutes_list.append(item * -1)

    return (list_friends, minutes_list)

def friends_amount_minutes_three(n):
    random_number = 0
    list_friends = []
    minutes_list = []

    for i in range(n):
        list_friends.append(random.randint(0, 1000))
    
    for item in list_friends:
        random_number = random.randint(0, 1)
        if random_number >= 1:
            minutes_list.append(item / 2)
        else:
            list_friends.append(item * 2)

    return (list_friends, minutes_list)

def correlation_tests(n):
    test1 = friends_amount_minutes_one (n)
    print(f'Correlação: {correlation(test1[0], test1[1])}')

    test2 = friends_amount_minutes_two (n)
    print(f'Correlação: {correlation(test2[0], test2[1])}')

    test3 = friends_amount_minutes_three (n)
    print(f'Correlação: {correlation(test3[0], test3[1])}')

def main():
    correlation_tests(22)
    pass
    
main()