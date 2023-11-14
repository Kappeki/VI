
# 15. zadatak
def promeni(lista, x):
    print(list((broj - x if broj > x else broj + x for broj in lista)))


if __name__ == '__main__':
    promeni([7, 1, 3, 5, 6, 2], 3)
