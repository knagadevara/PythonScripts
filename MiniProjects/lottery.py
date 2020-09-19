read_input = input("Please enter the numbers with seperated by comma ',':")

def user_numbers(string):
    """ User should be able to choode only 6 numbers """
    num = []
    for x in string.split(','):
        try:
            num.append(int(x))
        except ValueError as err:
            num.append(0)
    return set(num)

def generate_lottery_numbers():
    from random import randint, random , randrange
    randrange()




print(user_numbers(read_input))
read_input() 