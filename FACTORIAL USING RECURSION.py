# USN 1RUA25BCA0038 NAME HARIKUMAR R
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

n = int(input("Enter number: "))
print(fact(n))
