"""
Priority	
1	**	
2	+, - (note: unary operators located next to the right of the power operator bind more strongly)	unary
3	*, /, //, %	
4	+, -	binary
"""

print(2 * 3 % 5)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print(-2**3)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))