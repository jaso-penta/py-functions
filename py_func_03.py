import typing

def podijeli(a : int, b : int) -> None:
    print(a / b)


x = 4
y = 5


podijeli(5, 15)
podijeli(b=15, a=5)
podijeli(15, 5)
podijeli(x, y)
podijeli(y, x)
podijeli(b=y, a=x)