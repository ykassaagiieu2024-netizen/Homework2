try:
    gross = float(input("Hello. Introduce your gross salary:"))
    kids = int(input("Enter the number of kids:"))
except ValueError:
    print("Invalid input, please try again.")

if gross < 1000:
    taxrate = 0.1
elif gross < 2000:
    taxrate = 0.12
elif gross < 4000:
    taxrate = 0.14
else:
    taxrate = 0.18

# Apply children tax cut
if gross < 2000:
    taxrate = kids * 0.01
else:
    taxrate = kids * 0.05

#Calculate Final Output
tax = gross * taxrate
net = gross - tax
print("Your net salary is:", net)