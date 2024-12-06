def mdc(x, y):
    if y == 0:
        return x
    else:
        return mdc(y, x % y)

def main():
    x = int(input("Digite o primeiro número (x): "))
    y = int(input("Digite o segundo número (y): "))
    resultado = mdc(x, y)
    print(f"O MDC de {x} e {y} é: {resultado}")
if __name__ == "__main__":
    main()
