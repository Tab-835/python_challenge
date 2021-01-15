# import modules
import os
import csv

# set variables
num_months = 0
profit_loss_total = 0
average_change = 0
greatest_increase_date = ''
greatest_increase_value = 0
greatest_decrease_date = ''
greatest_decrease_value = 0

# open the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # store the csv header
    csv_header = next(csvreader)

    for row in csvreader:
        my_date = row[0]
        # if there is a date add 1
        if (my_date):
            num_months = num_months + 1

        profit_loss = int(row[1])
        # if there is an int as to total
        if (profit_loss):
            profit_loss_total = profit_loss_total + profit_loss

            # check if the current row contains the greatest increase/decrease
            if (profit_loss > greatest_increase_value):
                greatest_increase_date = my_date
                greatest_increase_value = profit_loss
            elif (profit_loss < greatest_decrease_value):
                greatest_decrease_date = my_date
                greatest_decrease_value = profit_loss

    # calculate average change if num_months is > 0
    if (num_months > 0):
        average_change = round(profit_loss_total / num_months, 2)

# print the results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {num_months}')
print(f'Total: ${profit_loss_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})')

# print to output file
output_file = 'output.txt'

with open(output_file, 'w') as text:
    text.write('Financial Analysis\n')
    text.write('----------------------------\n')
    text.write(f'Total Months: {num_months}\n')
    text.write(f'Total: ${profit_loss_total}\n')
    text.write(f'Average Change: ${average_change}\n')
    text.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})\n')
    text.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})')