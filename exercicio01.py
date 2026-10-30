print("Escola Senac\n")
nome = input("Nome: ").title()
prova01 = float(input("Prova 01: ").replace(",","."))
prova02 = float(input("Prova 02: ").replace(",","."))
prova03 = float(input("Prova 03: ").replace(",","."))
media = (prova01 + prova02 + prova03)/3
if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperação"
else:
    situacao = "reprovado"
print("\nResultado:\n")
print(f"Nome: {nome}")
print(f"Prova 01: {prova01:.1f}".replace(".",","))
print(f"Prova 02: {prova02:.1f}".replace(".",","))
print(f"Prova 03: {prova03:.1f}".replace(".",","))
print(f"Média: {media:.1f}".replace(".",","))
print(f"Situação: {situacao.upper()}")