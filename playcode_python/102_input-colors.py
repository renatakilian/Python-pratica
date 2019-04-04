'''
Bite 102. Infinite loop, input, continue and break
In this Bite we'll get you to take user input using the input builtin and see if it matches items within a list.

Ask the user to enter a color and capture that input.

Check to see whether they've entered 'quit'. If so, print bye and exit (break) the loop, effectively ending the function.

If not, check to see whether the color (input) is in the VALID_COLORS color list. If it is, then print the color in lower case. If not, print Not a valid color and continue the loop.

As you want to ask the user over and over again till they quit, you can use an infinite while loop. We already provided that in the template code, just code inside that loop.
'''

'''
VALID_COLORS = ['blue', 'yellow', 'red']

def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""

    while True:
        color = input("Please enter a color: ").lower()
        if color == "quit":
            print('Bye bye')
            break
        elif color == VALID_COLORS[0]:
            print(color)
            continue
        elif color == VALID_COLORS[1]:
            print(color)
            continue
        elif color == VALID_COLORS[2]:
            print(color)
            continue
        else:
            print('Not a valid color')
        pass

print_colors()
'''