import random

print("Gunting-Batu-Kertas")
print("-------------------")

print("1.Gunting")
print("2.Batu")
print("3.Kertas")
print("-------------------")

tipe = input("Silikan Pilih:")

if tipe in ("Gunting", "Batu", "Kertas"):
    choice = ("Gunting", "Batu", "Kertas")
    komputer_random = random.choice(choice)
    print(tipe, "Lawan", komputer_random)
    print("-------------------")

    #logic
    if tipe == komputer_random:
        print("Seri")
    else:
        if tipe == 'Batu':
            if komputer_random == 'Gunting':
                print("Menang")
            if komputer_random == 'Kertas':
                print("Kalah")

        if tipe == 'Kertas':
            if komputer_random == 'Gunting':
                print("Kalah")
            if komputer_random == 'Batu':
                print("Menang")
        
        if tipe == 'Gunting':
            if komputer_random == 'Batu':
                print("Kalah")
            if komputer_random == 'Kertas':
                print("Menang")
                
