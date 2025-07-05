
def print_header():
    print("-----------------")
    print("Header")
    print("-----------------")


def can_i_drink(age):
    if age < 21:
        print("No, you can't")
    else:
        print("You can")


def about_me():
    #dictionary
    info = {
        "name": "Michel Ngando",
        "email": "mn24@lukeenservices.com",
        "age": 43
    }

    print(info)

    #reading data from a dictionary
    print(info["name"])
    #print(info["address"])


def colors():
    #list
    basic_colors = ["Red", "Green", "Blue"]
    print(basic_colors)

    #read
    print(basic_colors[0]) #prints the first element


# call the fns
print_header()
can_i_drink(19)
can_i_drink(21)

print_header()
about_me()

print_header()
colors()