High_score = 95
test1 = int(input("Enter your results for test 1:"))
test2 = int(input("Enter your results for test 2:"))
test3 = int(input("Enter your results for test 2:"))
average = (test1 + test2 +test3)/ 3
print(f"The average score is {average}.")
if average >= High_score:
    print('Congrats')
    print('That is a great average')
