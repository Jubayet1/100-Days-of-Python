# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remainingYears = 90 - int(age)
remainingMonths = int(remainingYears * 12)
remainingWeeks = int(remainingYears * 52)
remainingDays = int(remainingYears * 365)

print(f"You have {remainingDays} days, {remainingWeeks} weeks, and {remainingMonths} months left.")