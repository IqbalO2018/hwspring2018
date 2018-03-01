#CurrentNumber = int(raw_input("enter a number"))
input_num = int(input('Enter any number: '))
if input_num % 2 == 0:
    print(input_num * 3 + 1)
else:
    print(input_num / 2.0)
