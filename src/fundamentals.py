# variables and data types
    # string concatenation: "string1" + "string2"
    # f-string interpolation: f"{string1}{string2}"

name = "Keyla"
last_name = "Leiva"

favorite_number = 4
# print(name + "'s favorite number is " + str(favorite_number))
# print(f"{name}'s favorite number is {favorite_number}")

# conditional statements
if name == "Keyla":
    print("Hello Key")

if name == "Tyler" and last_name == "Taylor":
    print("Hello Tyler")
else: 
    print("you're not tyler")


if favorite_number < 0:
    print("the number is negative")
elif favorite_number == 0:
    print("the num is 0")
else: 
    print("the num is positive")

print("the number is BIG") if favorite_number > 5 else print("the number is small")

# loops and sequences
    # for loops
    # while loops
# for i in range(10):
#     print(i)
# for i in range(5,10):
#     print(i)
# for i in range(5, 10, 2):
#     print(i)

counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1 
# functions

def prints_hello_world():
    print("hello world")
prints_hello_world()

def adds_two_numbers(num1, num2):
    sum = num1 + num2 
    return sum 

sum = adds_two_numbers(3, 4)
print(sum)