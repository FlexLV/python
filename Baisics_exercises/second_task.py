
number = input("Enter a 2 digit integer: ")

if len(number) == 2 and number.isdigit():
    number_list = list(number)
    number_list[0], number_list[1] = number_list[1], number_list[0]
    reversed_num = "".join(number_list)
    print("Reversed number:", reversed_num)
else:
    print("Enter a 2 digit integer: ")
