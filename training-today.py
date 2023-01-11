name = input(" what is your name? ")

if len(name) >= 6:
    print("You name is long")
elif len(name) == 5:
    print("Your name is normal")
else:
    print("Your name is short")


my_list = [1, 4, 3]
print(4 in my_list)
print(2 in my_list)
print(sorted(my_list))

my_sting = "ThIs lEtTer"
print(my_sting.capitalize())
print(my_sting.upper())

lines = ['First line', 'Second line', 'Third line']
print(lines)
print(", ".join(lines))
print("".join(lines))
print(" ".join(lines))
print('\n'.join(lines))



