# Programa que converte as temperaturas Fahrenheit, Celsius e Kelvin

while True:
    print("""Qual temperatura irá ser convertida?
    Opções:
    Fahrenheit -> F
    Celsius -> C
    Kelvin -> K""")
    temp = str(input("-> ")).strip()
    match temp.upper():
        case "F" | "C" | "K":
            break
        case _:
            print("Opção invalida\n")
            continue

while True:
    print("Digite o valor a ser convertido!")
    try:
        valor = float(input("-> "))
        break
    except Exception:
        print("Algo deu errado!")
        print("Digite apenas números!\n")
        continue

match temp.upper():
    case "F":
        celsius = float((valor - 32) * 5 / 9)
        kelvin = float(celsius + 273.15)
        print("""{:.2f}º Fahrenheit é o mesmo que:
        {:.2f}º Celsius
        {:.2f} Kelvin""".format(valor, celsius, kelvin))
    case "C":
        kelvin = float(valor + 273.15)
        fahrenheit = float((valor * 9 / 5) + 32)
        print("""{:.2f}º Celsius é o mesmo que:
        {:.2f}º Fahrenheit
        {:.2f} Kelvin""".format(valor, fahrenheit, kelvin))
    case "K":
        celsius = float(valor - 273.15)
        fahrenheit = float((celsius * 9 / 5) + 32)
        print("""{:.2f} Kelvin é o mesmo que:
        {:.2f}º Celsius
        {:.2f}º Fahrenheit""".format(valor, celsius, fahrenheit))

print("*" * 30)
