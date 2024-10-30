def classifica(xp):
    if int(xp) <= 1000:
        level = "Ferro"
    elif int(xp) <= 2000:
        level = "Bronze"
    elif int(xp) <= 5000:
        level = "Prata"
    elif int(xp) <= 7000:
        level = "Ouro"
    elif int(xp) <= 8000:
        level = "Platina"
    elif int(xp) <= 9000:
        level = "Ascendente"
    elif int(xp) <= 10000:
        level = "Imortal"
    else:
        level = "Radiante"
    return level


hero_name = input("Digite o nome do Herói: ").capitalize()
while True:
    hero_xp = input("Digite a quantidade de experiência do Herói: ")
    if hero_xp.isdigit():
        break
    else:
        print("A experiência precisa ser um valor inteiro!")
        
lvl = classifica(hero_xp)

print(f"O Herói de nome {hero_name} está no nível de {lvl}")