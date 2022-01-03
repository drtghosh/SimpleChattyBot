# Save the input in this variable
ticket = input()

# Add up the digits for each half
ticket_digits = [int(i) for i in ticket]
half_1 = sum(ticket_digits[:3])
half_2 = sum(ticket_digits[3:])

# Thanks to you, this code will work
if half_1 == half_2:
    print("Lucky")
else:
    print("Ordinary")