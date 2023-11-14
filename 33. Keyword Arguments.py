# keyword arguments = arguments prefixed with
#                       the names of parameters

#                       order of the arguments 
#                       doesn’t matter

#                       helps with readability

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", last="Abdullah", first="Rakib", title="Mr.")
# With keyword arguments, the order in which 
# we assign arguments does not matter

# Need to make sure that positional arguments 
# come first, and then keyword arguments

for x in range(1,11):
    print(x, end=" ")
# this "end" statement is a built-in
# keyword argument in print function
print()
# Another built-in argument is the 
# separate ("sep") argument
print("1", "2", "3", "4", "5", sep="-")

#------------------------X-----------------------
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=880, area=19, first=3312, last=2933)

print(phone_num)

