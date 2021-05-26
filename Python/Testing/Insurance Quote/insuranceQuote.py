'''
Author: Brogan Avery
Date: 2020/08/30
Project Title: Auto Insurance Quote
Desc: Program that calculates a drives auto insurance rate based on info that they enter
'''

# determines the base rate they pay for coverage type and age
def get_base_rate(first,last,age,coverageSelection):
    stateMinimumRates = {"ageBracket_1": 2593, "ageBracket_2": 608, "ageBracket_3": 552, "ageBracket_4": 525, "ageBracket_5": 495, "ageBracket_6": 515}
    liabilityCoverageRates = {"ageBracket_1": 2957, "ageBracket_2": 691, "ageBracket_3": 627, "ageBracket_4": 596, "ageBracket_5": 560, "ageBracket_6": 585}
    fullCoverageRates = {"ageBracket_1": 6930, "ageBracket_2": 1745, "ageBracket_3": 1564, "ageBracket_4": 1469, "ageBracket_5": 1363, "ageBracket_6": 1402}

    if (age < 25):
        ageBracket = "ageBracket_1"
    elif (age < 35):
        ageBracket = "ageBracket_2"
    elif (age < 45):
        ageBracket = "ageBracket_3"
    elif (age < 55):
        ageBracket = "ageBracket_4"
    elif (age < 65):
        ageBracket = "ageBracket_5"
    else:
         ageBracket = "ageBracket_6"

    if (coverageSelection.upper() == 'S'):
        rate = stateMinimumRates.get(ageBracket)
        coverageSelection = 'State Minimum'
    if (coverageSelection.upper() == 'L'):
        rate = liabilityCoverageRates.get(ageBracket)
        coverageSelection = 'Liability Coverage'
    if (coverageSelection.upper() == 'F'):
        rate = fullCoverageRates.get(ageBracket)
        coverageSelection = 'Full Coverage'

    driverInfo = {"First Name": first.capitalize(), "Last Name": last.capitalize(), "Age": age, "Coverage Type": coverageSelection,
              "Coverage Rate": "{:.2f}".format(rate)}
    return driverInfo

# adds the accident fee
def add_accident_fee(driverInfo):
    accidentPenalty = 0.41

    rate = (float(driverInfo.get("Coverage Rate"))* accidentPenalty) + float(driverInfo.get("Coverage Rate"))
    driverInfo.update({"Coverage Rate": "{:.2f}".format(rate)})
    return driverInfo

# subtracts the discount
def add_discount(driverInfo):
    discount = 0.1

    rate = float(driverInfo.get("Coverage Rate")) - (float(driverInfo.get("Coverage Rate")) * discount)
    driverInfo.update({"Coverage Rate": "{:.2f}".format(rate)})
    return driverInfo

# prints a display of the users info from dictionary and the final payment owed
def display_final_price(driverInfo):
    driverInfo.update({"Coverage Rate": "$" + driverInfo.get("Coverage Rate")})
    print('__Driver Info__')
    for key, value in driverInfo.items():
        print(key, ': ', value)

#######################################################################################
if __name__ == '__main__':
# declaring/ initializing vars
    age = 0
    minDrivingAge = 16
    coverageSelection = ''
    coverageOptions = ['S','L','F']
    ageBracket = ''
    yes_no = ['yes', 'no']
    accidents = ''
    applyDiscount = ''

# get the users info
    print('Enter information for the following questions regarding yourself and your selected auto coverage to determine the rate you will pay.')

    first = input('Enter your first name: ')
    last = input('Enter you last name: ')

    while True:
        try:
            while (age < minDrivingAge):
                age = int(input('Enter your age: '))
                if (age < minDrivingAge):
                    print('You must be 14 or older to drive.')
            break
        except (TypeError, ValueError):
            print('You must enter a valid age in the form of a number.')

    while(coverageSelection.upper() not in coverageOptions):
        coverageSelection = input('Enter your choice for the level of coverage. Type "S" to select state minimum, "L" to select liability coverage, or "F" to select full coverage: ')
        if (coverageSelection.upper() not in coverageOptions):
            print('That is not a valid option.')

    driverInfo = get_base_rate(first,last,age,coverageSelection)
    print(driverInfo)
    print('The base rate price for you according to the information you entered is $' + str(driverInfo.get("Coverage Rate")))

    print('Please answer the reaming questions to determine your final payment.')

    while (accidents.lower() not in yes_no):
        accidents = input('Have you ever been in any accidents? Type "yes" or "no": ')
        if (accidents.lower() not in yes_no):
            print('You must enter "yes" or "no".')

    if (accidents.lower() == 'yes'):
        driverInfo = add_accident_fee(driverInfo)
        print('After incurring the penalty charge for having accident(s) on your record, your new rate has gone up to $' + str(driverInfo.get("Coverage Rate")))

    while (applyDiscount.lower() not in yes_no):
        applyDiscount = input('Would you like to pay upfront today to receive a 10% discount? Type "yes" or "no": ')
        if (applyDiscount.lower() not in yes_no):
            print('You must enter "yes" or "no".')

    if(applyDiscount.lower() == 'yes'):
        driverInfo = add_discount(driverInfo)
        print('With the discount, applied your final payment due has dropped to $' + str(driverInfo.get("Coverage Rate")))

    print('Please review the information you entered and ensure you are aware of the rate you will need to pay.')
    display_final_price(driverInfo)


