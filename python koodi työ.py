import random
while True:
    try:
        print("""
╔══════════════════════╗
║   🎰 SLOT PELI 🎰    ║
╚══════════════════════╝
""")
        money = int(input("Tervetuloa slot peliin! Paljonko laitat rahaa koneeseen? "))
        if money > 0:
            break
        else:
            print("Anna positiivinen luku!")
    except:
        print("Anna numero!")

rounds = 0
wins = 0


symbols = ["🍒", "🍒", "🍒", "🍋", "🍋", "🔔", "⭐", "💎"]

print("\n🎰 Slot-peli alkaa!")
print("Rahat:", money)

while money > 0:
  
    while True:
        try:
            bet = int(input("Paljonko panostat (1-5)? "))
            if 1 <= bet <= 5:
                break
            else:
                print("Anna panos väliltä 1-5!")
        except:
            print("Anna numero!")

    input("\n✨Paina Enter pyöräyttääksesi✨")

    if bet > money:
        print("Ei tarpeeksi rahaa!")
        continue

    money -= bet
    rounds += 1

    r1 = random.choice(symbols)
    r2 = random.choice(symbols)
    r3 = random.choice(symbols)

    print(r1, r2, r3)

    if r1 == r2 == r3:
        if r1 == "💎":
            print("💎💎💎 🎉Jackpot!🎉 +10")
            money += bet * 10
            wins += bet * 10
        elif r1 == "⭐":
            print("⭐⭐⭐ 🎉Iso voitto!🎉 +5")
            money += bet * 5
            wins += bet * 5
        elif r1 == "🍒":
            print("🍒🍒🍒 Pieni voitto! +3")
            money += bet * 3
            wins += bet * 3
        else:
            print("Kolme samaa! +2")
            money += bet * 2
            wins += bet * 2

    elif r1 == r2 == "🍒" or r2 == r3 == "🍒" or r1 == r3 == "🍒":
        print("🍒🍒 Pieni voitto! +1")
        money += bet * 1
        wins += bet * 1

    elif r1 == r2 == "⭐" or r2 == r3 == "⭐" or r1 == r3 == "⭐":
        print("🌟 BONUS-KIERROS! 🌟")
        bonus = random.randint(1, 5)
        print(f"Sait {bonus} euroa!")
        money += bonus * bet
        wins += bonus * bet

    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("😏 Lähellä! Kaksi samaa...")

    else:
        print("😢 Ei voittoa")

    print("Rahat:", money)
    choice = input("Jatkatko vai nostat rahat? (j = jatka, n = nosta): ").lower()

    if choice == "n":
        print(f"Nostit {money} euroa. Peli loppui.")
        break

if rounds > 0:
    print(f"Voittoprosentti: {wins/rounds:.2f} per kierros")   

file = open("save.txt", "w")
file.write("Rahat: " + str(money) + "\n")
file.write("Kierrokset: " + str(rounds) + "\n")
file.write("Voitot: " + str(wins) + "\n")
file.close()

print("\n💾 Tulokset tallennettu tiedostoon save.txt")  