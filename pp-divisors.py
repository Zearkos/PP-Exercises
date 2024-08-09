## I did this before but I also appreantly don't understand how to use git, and deleted all my work.

num = int(input("I am a math MACHINE!  Give me any number, i'll tell you wthat it's divisible by. "))
for val in range(2,10):
    if num % val == 0:
        print(f"You can divide {num} by {val}!")
    else:
        print(f"No, not by {val}.")