#OPTION 1 FINANCIAL DECISIONS

#Determining sales bonuses
sales = int(input('Please enter your sales:'))
bonus = 500.0
if sales > 5000:
    print(f'Your bonus:{bonus}')
else:
    print(f'Your sales:{sales}')
    
#Checking Payment Status
balance = int(input('Please enter your balance:'))
payment_amnt = int(input('Please enter you payment amount:'))

if balance < payment_amnt:
    print('Insufficient Funds')
    print('You did not pay enough')
else:
    print('You have enough funds')

#Salary Comparison
salary = int(input('Please enter your salary:'))
if salary <= 20000:
    print('Small Salary:')
else:
    print("Big Salary")
    
#Loan Qualification Assessment
salary = int(input("Please enter your Salary:"))
years = int(input('Please enter your years on the Job:'))
if salary >= 30000 and years >= 2:
    print('You qualify for a loan')
elif salary >= 30000 and years < 2:
    print("You must have been on your current job for 2 years")
elif salary < 30000 and years >=2:
    print('You must earn at least 30k to qualify')
    
#Special Offer Eligibility
age = int(input('Enter your age:'))
student = input("Are you a student? (yes/no):")

if age > 60 and student == 'no':
    print('You got the special')
elif age < 60 and student == 'yes':
    print('You get the special')
else:
    print('You did not get the student special')

#OPTION 2 GENERAL CONDITION CHECKING

#WEATHER TEMPERATURE EVALUATION
temperature = int(input('Please enter the temperature:'))
if temperature < 40:
    print("A little cold,isn't it?")
else:
    print("Nice weather we're having")

#LEGO AGE RESTRICTION
age = int(input('Please enter your age:'))
if age > 4 and age < 94:
    print("You can play Lego")
else:
    print("You cannot play Lego")
#EVEN NUMBER CHECKER
number = int(input('Please enter a number:'))
if number % 2 ==0:
             print("Even Number!")
else:
    print("Uneven Number!")
    
    
