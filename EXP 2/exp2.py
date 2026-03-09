runs=int(input("Enter Runs:"))
balls=int(input("Enter Balls:"))
wickets=int(input("Enter wickets:"))
Economy=int(input("Enter economy:"))
Overs=int(input("Enter overs:"))
runscovered=int(input("Enter runs covered"))
catches=int(input("Enter catches"))

SR=((runs/balls)*100)

print(SR)

if runs>=50 and SR>=120:
    batter=print("Exellent Batsman")
elif runs>=30 and SR >=100:
    batter=print("Good Batsman")
elif runs>=20:
    batter=print("Average Batsman")
else:
    batter=print("Poor Batsman")

ER = runscovered/Overs
print(ER)

if wickets >=3 and ER <=6:
    bowler = print("Excellent Bowler")
elif wickets >=2 and ER <=8:
    bowler = print("Good Bowler")
elif wickets >=2:
    bowler = print("Average Bowler")
else:
    bowler = print("Poor Bowler")

if catches>=2:
    print("Outstanding Fielder")
elif catches == 1:
    print("Active Fielder")
else:
    print("Needs Work")

if batter == "Excellent Batsman" and bowler == "Excellent Bowler":
    print("All Star")
elif batter == "Good Batsman" and bowler == "Good Bowler":
    print("Strong")
else:
    print("Needs improvement")
