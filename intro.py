print("Hello World!")

# This is a comment!

#create variables
name = "Michel"
first_name = "Michel" #Python uses snake cases instead of camel cases
last_name = "Ngando"

print(name + " " + last_name)
#format strings
text = f'''
ksdhfllsjjnvvjfsn
jsdhsjfkhadfkjhda
dafdfdsfdf
fdfdfdf {name}
{last_name} {first_name}
'''
print(text)
print(f'''My name is {name} {last_name}''')
print(f"I'm {name}") #can use a double-quote if you know it will be only 1 sentence

print(1+1)
print(7+3)
print(5*3)
print(10/2)

#Identation
#for methods, functions, classes, for loops, if statement, need to be careful with the indentation
#conditions: <, >, ==, !=, !

age = 120
if(age<100):
    print(f"Don't worry you are very young")
elif(age == 100):
    print(f"What a long life!")
else:
    print(f"Sorry you're getting old")
print("I'm outside")

#Methods or functions
def sum_numbers():
    print(1+1)
    return 6

sum_numbers()
x = sum_numbers()
print(x)

def empty_function():
    print("This is an empty function")
    
def return_number():
    return 10

x = return_number()
print(x)

def sum_numbers(a,b):
    return a + b

result = sum_numbers(3,5)
print(result)

def sum_numbers(a,b):
    return a + b
result = sum_numbers(10,30)
print(result)

def sub_numbers(a,b):
    return a - b
result = sub_numbers(30,50)
print(result)

def mul_numbers(a,b):
    return a * b
result = mul_numbers(8,9)
print(result)


def div_numbers(a,b):
    return a / b
result = div_numbers(9,4)
print(result)

#Input- allows to use the prompt to send data (it only contains a string, but can be converted using a data type)

first_name = input("Enter your first name: ")
print(first_name)

x = int(input("Enter a number: "))
print(f"The result is {sum_numbers(x,4)}")

#Collections
#Lists: they use [] (square brackets) . Properties: ordered, changeable and allow duplicate values
students_list = ["Brad", "Chris","Michel","Wilbert","Ryan"]
                # 0        1       2        3         4
print(f"Printing the whole list: {students_list}")
print(f"Printing only Wilbert: {students_list[3]}")

students_list[4] = "Luis"
print(f"Replacinng Ryan: {students_list}")

students_list.append("Ryan")
students_list.append("Luis")
print(f"Adding a value to the list: {students_list}")

students_list.remove("Luis")
print(f"Removeng the 1st occurence of a value from the list: {students_list}")

print(f"Printing the lenght of the list: {len(students_list)}")

#Tuples
# ---> Properties: ordered, unchangeable and allow duplicate values
students_list("Brad", "Chris","Michel","Wilbert","Ryan")
print(f"Printing the whole list: {students_list}")
print(f"Printing only Wilbert: {students_list[2]}")

students_list[1] = "Luis"
print(f"Printing the whole list: {students_list}") #Creates an error

#Set
# ---> Properties: unordered, unchangeable, unindexed, no duplicate values

#Dictionary
# ---> ordered, changeable, no duplicate values




