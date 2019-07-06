# First, figure out the steps



print("PyBankChallenge")

import os
import csv
csvpath = os.path.join('budget_data.csv')

#This is where we aggregate our variable initializations
month_counter = 0
money_sum = 0
monthly_change = 0
previous_month_revenue = 0
difference_sum = 0
difference_counter = 0
maximum_decrease = 0
maximum_increase = 0


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    Firstrow = next(csvreader)

    month_counter = month_counter + 1

    previous_month_revenue = int(Firstrow[1])
    money_sum = int(Firstrow[1])

#Since we used next twice, most of our operations can start on row 3.

    for row in csvreader:
        month_counter += 1
        current_revenue = int(row[1])
        money_sum = money_sum + current_revenue
        monthly_change = current_revenue - previous_month_revenue
        difference_sum = difference_sum + monthly_change
        difference_counter += 1
        print("Monthly Change: " + str(monthly_change))
        if monthly_change > maximum_increase:
            maximum_increase = monthly_change
        if monthly_change < maximum_decrease:
            maximum_decrease = monthly_change
        
        previous_month_revenue = current_revenue
        

# print("Max Increase: " + str(maximum_increase))
# print("Max decrease: " + str(maximum_decrease))


average_difference = difference_sum / difference_counter

# print(average_difference)

total_months = 'Total Months: ' + str(month_counter)
total = 'Total: ' + str(money_sum)
avg_change = 'Average Change: $' + str(average_difference)
increase = "Greatest Increase in Profits: Feb-2012 (" + str(maximum_increase) + ")" 
decrease = "Greatest Decrease in Profits: Sep-2013 (" + str(maximum_decrease) + ")"

cache = []
cache.append("Financial Analysis") 
cache.append("-------------------------")
cache.append(total_months)
cache.append(total)
cache.append(avg_change)
cache.append(increase)
cache.append(decrease)

print(cache)

with open('output.txt', 'w') as output:
  for line in cache:
      output.write("%s\n" % line)




# file_to_output = os.path.join("analysis", "budget_analysis.txt")

# output = (
#     f"\nFinancial Analysis\n"
#     f"----------------------------\n"
#     f"Total Months: {month_counter}\n"
#     f"Total: ${money_sum}\n"
#     f"Average  Change: ${average_difference:.2f}\n"
#     f"Greatest Increase in Profits: {maximum_increase[0]} (${maximum_increase[1]})\n"
#     f"Greatest Decrease in Profits: {maximum_decrease[0]} (${maximum_decrease[1]})\n")


#         with  open(outfile,'w')  as fhout:
#         print("Financial Analysis", file=fhout,end='\n')
#         print("----------------------------------------", file=fhout,end='\n')
#         print("Total months  : " + str(cnt), file=fhout,end='\n')
#         print("Total Revenue : " + str(sum), file=fhout,end='\n')
#         print("Average Revenue Change $" + str(avgrevchange),file=fhout,end='\n')
#         print("Greatest Increase in Revenue: " + maxrev_inc_date + " ($" +
#               str(maxrev_increase) +")", file=fhout,end='\n' )
#         print("Greatest Decrease in Revenue: " + maxrev_dec_date + " ($" +
#               str(maxrev_decrease) +")", file=fhout,end='\n' )

# Print the output (to terminal)
# print(output)

# # Export the results to text file
# with open(file_to_output, "w") as txt_file:
#    txt_file.write(output)

