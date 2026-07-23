principle=0
rate=0
time=0

while True:
    principle=float(input("Enter the amount:"))
    if principle<0:
        print("Principle cannot be less than zero.")
    else:
        break

while True:
    rate=float(input("Enter the amount:"))
    if rate<0:
        print("Rate cannot be less than zero.")
    else:
        break

while True:
    time=float(input("Enter the year:"))
    if time<0:
        print("Time cannot be less than zero.")
    else:
        break    


print(principle)
print(rate)
print(time)

total=principle*pow((1+rate/100),time)
print(f"Balance after{time} year/s:${total:.2f}")