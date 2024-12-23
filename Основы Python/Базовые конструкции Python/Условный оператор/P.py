petya_speed = int(input())
vanya_speed = int(input())
tolya_speed = int(input())

participants = [
    ("Петя", petya_speed),
    ("Вася", vanya_speed),
    ("Толя", tolya_speed)
]

sorted_participants = sorted(participants, key=lambda x: x[1], reverse=True)

pedestal = ["" for _ in range(3)]

pedestal[0] = f"          {sorted_participants[0][0]}        "  
pedestal[1] = f"  {sorted_participants[1][0]}  "              
pedestal[2] = f"                  {sorted_participants[2][0]}  "  

positions = "   II      I      III   "

for line in pedestal:
    print(line)
print(positions)
