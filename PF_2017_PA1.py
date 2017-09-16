# Data input from the user


dayOfWeek = input("Enter the day of the week ")
stepsTaken = int(input
                 ("Enter the number of steps reported on the pedometer "))

# Calculation of variables


milesWalked = (stepsTaken/2000)
caloriesLost = (milesWalked*65)

# Display of data calculated for the day entered


print ("The following is for ", dayOfWeek)
print ("Walking ", milesWalked, " miles results in ", caloriesLost,
        "calories lost.")
