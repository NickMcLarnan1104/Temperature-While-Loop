# PROGRAMMER: Nick McLarnan
# PROGRAM NAME: Assignment 11 - Creating Arrays/Lists
# DATE CREATED: 04/19/2022
# PURPOSE: A program to create a list of outdoor Temperature data.

# Import myCustomFunctions file
from myCustomFunctions import *

def main():

    # Assign variables
    count = 1
    total = 0

    # open file to write our display/results in
    file = open('mclarnan_nick_A11_wTemp_WHILE_LOOP_output.txt', 'w')

    # Ask user to enter state they will be measuring
    print("Enter the name of the state you are recording the temperature for [i.e. Florida, Georgia, New York]")
    state = input()

    # Ask how many days they will record. Sets count for while loop
    print(f"How many days will you record the outdoor Temperature for the state of {state}?")
    days = checkIntegerDataType()
    wTemp = [0] * (days + 1)

    # While count <= days: ask user temperature for each day
    while count <= days:
        print(f"What's the outdoor temperature in {state} on day #{count}?")
        wTemp[count] = checkFloatDataType()

        # Adding wTemp element value to total
        total = total + wTemp[count]
        # Add 1 to count [day value]
        count = count + 1

    # ===============================================================================================
    file.write("--------------------------------------------------------------------------------\n")

    # Print out title for table
    file.write(f"Unsorted Temperature List for the state of {state}".center(80) + "\n")
    file.write("--------------------------------------------------------------------------------\n")

    # set count or index back to 0
    count = 1

    # While count less than days+1, print out the temperature for each day
    while count < days + 1: 
        file.write(f"wTemp[{count}] = {wTemp[count]}°".center(80) + "\n")
        count = count + 1
    file.write("--------------------------------------------------------------------------------\n")
    file.write("--------------------------------------------------------------------------------\n")
    file.write(f"THE AVERAGE DAILY TEMPERATURE IN {state} {'':5s} = {(total / days):,.2f}°".center(80) + "\n")
    del wTemp[0]
    print(wTemp)
    file.write(f"The Minimum Temperature {'':21s} =  {min(wTemp)}°".center(80) + "\n")
    file.write(f"The maximum Temperature {'':21s} =  {max(wTemp)}°".center(80) + "\n")
    file.write("--------------------------------------------------------------------------------\n")

    # ===============================================================================================

    file.write("--------------------------------------------------------------------------------\n")
    # Print out title for table
    file.write(f"Sorted Temperature List for the state of {state}".center(80) + "\n")
    file.write("--------------------------------------------------------------------------------\n")
    # had to delete the 0 in the list and add it on or else I got an error. Did not know how to fix!
    wTemp.insert(0, 0)
    print(wTemp)

    # set count or index back to 1
    count = 1
    wTemp.sort()
    while count < days + 1:             
        file.write(f"wTemp[{count}] = {wTemp[count]}°".center(80) + "\n")
        count = count + 1

    file.write("--------------------------------------------------------------------------------\n")

    # Print average daily temperature
    file.write(f"THE AVERAGE DAILY TEMPERATURE IN {state} {'':5s} = {(total / days):,.2f}°".center(80) + "\n")
    print(wTemp)
    del wTemp[0]
    print(wTemp)

    # Had to declare these variables here or else I had another error for index count.
    minValue = min(wTemp)
    maxValue = max(wTemp)

    # Print min and max temperature values with min and max function
    file.write(f"The Minimum Temperature {'':21s} =  {minValue}°".center(80) + "\n")
    file.write(f"The maximum Temperature {'':21s} =  {maxValue}°".center(80) + "\n")
    file.write("--------------------------------------------------------------------------------\n")

    # ===============================================================================================

    # Close file and print message
    file.close()
    print("File closes successfully.")

# Call main function
if __name__ == '__main__':
    main()


# END PROGRAM
