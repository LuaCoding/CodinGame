# opponent: opponent's draw
# me: my draw
opponent, me = input().split()

if opponent == "ROCK" and me != "SCISSORS":
    oppnext = "SCISSORS"
    mynext = opponent
elif opponent == "ROCK":
    oppnext = opponent
    mynext = "PAPER"

elif opponent == "PAPER" and me != "ROCK":
    oppnext = "ROCK"
    mynext = opponent
elif opponent == "PAPER":
    oppnext = opponent
    mynext = "SCISSORS"


elif opponent == "SCISSORS" and me != "PAPER":
    oppnext = "PAPER"
    mynext = opponent
elif opponent == "SCISSORS":
    oppnext = opponent
    mynext = "ROCK"

else:
    print("CHEATER")

# your opponent next draw followed by the draw to beat him, or "CHEATER"
print(oppnext, mynext)