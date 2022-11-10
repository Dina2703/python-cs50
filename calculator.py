from cs50 import get_int
# when you import like below, put cs50.get_int to show where you're referring to.
# import cs50

#EXAMPLE WITH NUMBERS input
# x = get_int("x: ")
# y = get_int("y: ")
# print(x + y)

#EXAMPLE WITH STRINGS input
# example with input() from Python. input() treates numbers as strings, and returns a string, joining two strings into one.
# when dealing with numbers input use int()

# x = int(input("x: "))
# y = int(input("y: "))
# print(x + y)


#EXAMPLE WITH HANDLING ERRORS misinput type
#to catch unexpected inputs(like a string, when expecting a number), we can use  'try, except'
# try:
#     x= int(input("x: "))
# except:
#     print("That is not an int!")
#     exit()
# try:
#     y = int(input("y: "))
# except:
#     print("That is not an int!")
#     exit()
# print(x + y)

#EXAMPLE WITH NUMBERS DIVISION

# x = get_int("x: ")
# y = get_int("y: ")
# print(x / y)

#EXAMPLE WITH FLOATS NUMBERS
x = get_int("x: ")
y = get_int("y: ")
z = x / y
print(f"{z:.25f}") #to get numbers after decimal points