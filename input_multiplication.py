"""
Fix the error:
input ("Enter a number: ")
print (num * 8)
"""

# Fixed 'num' not declared and changed 'num' to an integer from string.
num = input("Enter a number: ")
print(int(num) * 8)