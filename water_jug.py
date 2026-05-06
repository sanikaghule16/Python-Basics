def water_jug():
    x, y = 0, 0 # jugs
    while True:
        print(x, y)
        if y == 4: # goal: 4 gallons in 2nd jug
            break
        if x == 0:
            x = 5
        elif y == 7:
            y = 0
        else:
            pour = min(x, 7 - y)
            x -= pour
            y += pour
water_jug()
