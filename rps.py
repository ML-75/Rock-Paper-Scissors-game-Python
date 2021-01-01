
from random import randint

t = ["Rock", "Paper", "Scissors"]

player = False
values = {
        "rp":0, "pr":1, "rs":1, "sr":0, 
        "ps":0, "sp":1
        }

cpu_pts = 0
play_pts = 0

while not player:
    computer = t[randint(0, 2)]
    player = input("Rock, Paper, Scissors ? ").lower()
    comp = computer[0].lower() == player[0]  
    if comp: 
        print("Tie!")
    else:
        try:
            won = values[computer[0].lower() + player[0].lower()]
            winner = "computer" if won else "you"

            print(f"computer choice: {computer}")
            print(f"{winner} Won!")

            cpu_pts += won
            play_pts += 1 if not won else 0

            print(f"Cpu: {cpu_pts} ---- Player: {play_pts} ")
        except:
            print("values not acepted")

    conti = 0
    while conti != "y" and conti != "n":
        conti = input("Play again (Y/N) ? ").lower()
        
        try:
            player = {"y": False, "n": True}[conti]
        except:
            print("introduce correct answer")












