# Tip Calculator

# Create a greeting
print('Welcome to the Tip Calculator!')
print('In only 3 easy steps I will get the calculations done for you!')

# We turn the users input into float to get the most accurate results
total_bill = float(input('First, please enter the total bill amount: €'))
tip_percentage = int(input('Second, please enter the tip percentage that you want to give (e.g., 5, 7, 10): '))
num_people = int(input('Lastly, please enter the number of people to split the bill: '))

tip_amount = total_bill * (tip_percentage / 100)

total_amount = total_bill + tip_amount

final_bill = total_amount / num_people

# Display the results
print('\n--- Calculation Summary ---')
print(f'Total Bill: €{total_bill:.2f}')
print(f'Tip Percentage: {tip_percentage}%')
print(f'Tip Amount: €{tip_amount:.2f}')
print(f'Total Amount (Bill + Tip): €{total_amount:.2f}')
print(f'Number of People: {num_people}')

# we use the f string {variable: .2f} to get the 2 decimal numbers
print(f'Each person should pay: €{final_bill:.2f}')
# or we can use the variable = format(variable , '2.f')

print('Thank you for using the Tip Calculator, we hope to see you again!')

