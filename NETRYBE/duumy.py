arrival_time  = float(input(" enter arrival time "))
depart = float(input(" enter departure  time "))
normal_arrival  =  8.00
clsoing = 16.00
if arrival_time >= normal_arrival and arrival_time <= clsoing:
    print(" PRESENT ")
    if depart < clsoing:
        print("wrong time to leave office PENALTY")
    else:
        print("your in time, enjoy yourself")
else:
    print("ABSENT")