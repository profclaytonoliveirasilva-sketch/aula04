nota = input("Escolha uma Letra: A - B - C - D - F: ").upper()
match nota:
    case "A":
        print("Excelente")
    case "B":
        print("Bom")
    case "C":
        print("Regular")
    case "D":
        print("Ruim")
    case "F":
        print("Reprovado")
    case _:
        print("Opção Inválida")