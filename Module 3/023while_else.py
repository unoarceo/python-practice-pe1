# ELSE is always executed once even if the program does not go into the while loop.

print("""
First While...else loop""")
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


print("""
Second While...else loop""")
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)