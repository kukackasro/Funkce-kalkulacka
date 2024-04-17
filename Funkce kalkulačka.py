def plus(a, b):
    print(a + b)
def minus(a, b):
    print(a - b)
def deleno(a, b):
    print(a / b)
def krat(a, b):
    print(a * b)
def mocnina(a, b):
    print(a ** b)
def odmocnina(a, b):
    print(a // b)









print("Vítejte v kalkulačce, jestli chcete program ukončit napište konec do operace.")
while True:
    a = float(input("Zadej první číslo:"))
    b = float(input("Zadej druhé číslo:"))
    operace = input("Zadej operaci +, -, *, /, **,//")
    if operace == "+":
        plus(a, b)
    elif operace == "-":
        minus(a, b)
    elif operace == "*":
        krat(a* b)
    elif (a == 0 or b == 0) and operace == "/":
        print("Nulou nelze delit")
    elif operace == "/":
        deleno(a / b)
    elif operace == "**":
        mocnina(a ** b)
    elif operace == '//':
        odmocnina(a // b) 
    elif operace == "konec":
        print("Díky za použití kalkulačky")
        break
    else:
        print("Proč tam něco píšeš")