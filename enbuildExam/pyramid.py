# 1. Render the Triangle for the given character and number of rows. That means if input character is D and number of rows are 4 then pyramid will be:
# D
# D E
# D E F
# D E F G

# code for Triangle for the given character

n = 4
for i in range(n):
    for j in range(i+1):
        print(chr(j + 68), end="")
    print()