
import re

def cases(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

camel_case = input("Enter your string : ")
snake_case = cases(camel_case)
print(snake_case)
