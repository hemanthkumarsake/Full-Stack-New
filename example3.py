def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Oops sorry! Division by zero is not possible"
n,m = map(int,input("Enter the numbers: ").split())
print(divide(n,m))