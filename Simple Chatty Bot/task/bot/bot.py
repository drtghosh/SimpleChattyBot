def greet(bot_name, birth_year):
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    question = """
    When do we use break in loop?
    1. To stop the loop immediately in any iteration.
    2. To continue to next iteration.
    3. To break out of a loop when a condition is met in that iteration.
    4. None of the above.
    """
    print(question)
    while True:
        answer = int(input())
        if answer == 3:
            break
        else:
            print("Please, try again.")
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('ProgTut', '2022')  # change it as you need
remind_name()
guess_age()
count()
test()
end()