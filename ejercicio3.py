def imprime_pares_inverso(n):
    if n % 2 == 1:
        n -= 1

    for i in range(n, 1, -2):
        print(i, end=" ")


if __name__ == '__main__':
    print("Imprimiendo números pares menores o iguales a 5:")
    imprime_pares_inverso(5)

    print("\nImprimiendo números pares menores o iguales a 6:")
    imprime_pares_inverso(6)
