def imprime_pares(n):
    for i in range(2, n+1, 2):
        print(i, end=" ")


if __name__ == '__main__':
    print("Imprimiendo números pares menores o iguales a 5:")
    imprime_pares(5)

    print("\nImprimiendo números pares menores o iguales a 6:")
    imprime_pares(6)
