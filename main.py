# In this code, I'll just try to learn the if and else statement.

print("Weclome to the rollercoster!")

height = int(input("What is your height in cm: "))


# if I input my height as 120 without >= 120: in my conditions,
# 120cm will fall under too short to ride which is not normal. Try to change the code if you're not sure.
if height >= 120:
    print("Tall enough to ride!")
else:
    print("Too short to ride, come back when you're taller!")
