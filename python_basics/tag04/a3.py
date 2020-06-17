def leadingZero(number):
    if number < 10:
        return "0"+str(number)
    return number


for h in range(24):
    for m in range(60):
        print(f"{h:02d}:{m:02d}")
