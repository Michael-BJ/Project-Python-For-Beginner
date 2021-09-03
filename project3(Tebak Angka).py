import random

print("Tebak Angka Python")
print("------------------")

komputer_random = random.randint(1,10)

lives = 3

while True:
    guess = int(input("Masukan angkanya : "))

    # logic
    if guess != komputer_random:
        lives -=1
        if guess < komputer_random:
            print("Wah angkanya terlalu kecil nih")
        if guess > komputer_random:
            print("Wah angkanya terlalu besar nih")
    else:
        print("Selamat tebakan anda benar")
        break

    if lives == 0:
        break 

print("------------------")
print("Sisa kesempatan", lives )