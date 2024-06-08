
exp = input("Enter an arithmetic expression : ")

exp_format = exp.split()

x = int(exp_format[0])
y = exp_format[1]
z = int(exp_format[2])

if y == "+":
   print(float(x+z))
elif y == "-":
    print(float(x-z))
elif y == "*":
    print(float(x*z))
elif y == "/":
    print(float(x/z))


