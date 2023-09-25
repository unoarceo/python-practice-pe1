"""
Expected output
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
Ready or not, here I come!
"""

import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

for x in range(5):
    print(str(x+1) + " Mississippi")
    time.sleep(1)
    
print("Ready or not, here I come!")
