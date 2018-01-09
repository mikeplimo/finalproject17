# Using one or two quotation marks
print("My name is Bob")
print('Bob is strong')
print('Bob said "I\'m strong"')


# You can put the letter f in front of a string, and putting your variables in curly brackets inside the string
dog_1 = "Lucky"
dog_2 = "Teddy"
dog_1_age = 5
dog_2_age = 12
print(f"{dog_2} is a tiny dog.")
print(f'{dog_1} is {dog_1_age} years old')

# Variable is defined as a string
description = f"{dog_1} and {dog_2} are both white dogs, but {dog_1} is bigger than {dog_2}."
print(description)



# You can also use empty brackets in your string and append .format() with a comma-separated list of the variables you want to insert

print("I go on a lot of walks with {} and {}".format(dog_1, dog_2))
print("{} and {} are {} and {} years old".format(dog_1, dog_2, dog_1_age, dog_2_age))

# When you do this, you can number the brackets to control which bracket displays each argument
# The first argument is number 0, not number 1
print("The brackets can be used to control the position in which {} and {}'s names are shown".format(dog_1, dog_2))
print("The brackets can be used to control the position in which {1} and {0}'s names are shown".format(dog_1, dog_2))


# You can even save a string that has the brackets and use that repeatedly

f_string = "{} {} {}"

print(f_string.format('z', 'x', 'c', 'v'))
print(f_string.format('bronze', 'silver', 'gold', 'platinum'))
print(f_string.format(44, "three", 90.0, "4.9"))

math_string = "{} / {} = {}"

print(math_string.format(4, 6, 24))
print(math_string.format(9, 0, 0))


# You can also concatenate (join) strings. This doesn't work with anything that isn't a string

a = "Bronze"
b = "Silver"
c = "Gold"
d = "Platinum"
e = "Diamond"

print(a + b + c + d + e)

# Or you can use the join() function
# put all the strings you want to join in a set of parentheses (which creates something called a tuple)
# that tuple belongs inside the parentheses for join()
# Use .join() on a string you want to put in between each string you're joining
print(" ".join((a,c,b,e,d)))
print("*".join(("b", "c", "a")))

# You can create a new line using \n
print("Hi my name is \nbob")

# You can also create a multi-line string using three sets of double quotes
Robinhood = """Robinhood was really tall.
Robinhood was fast.
Robinhood could jump high.
Robinhood could fly.
"""

print(Robinhood)