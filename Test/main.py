import random

print("Загадайте число от 1 до 100")
print('"Используйте  "Больше", "Меньше", "Да" или "Нет"')

max_number = 100
guess = random.randint(1, 100)

computer_question = ('Ваше число: ')
print(computer_question, guess, '?')

while True:

    answer = input()

    if answer == "Да" :
        print("Ты угадал!")
        break
    elif answer == "Нет":
        check = input("Больше или Меньше? ")
        if check == "Больше" :
            print ('Ваше число: ', random.randint(guess, max_number), '?')
        elif check == "Меньше" :
            print ('Ваше число: ', random.randint(0, guess), '?')

