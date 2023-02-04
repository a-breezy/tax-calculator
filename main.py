# Calculate federal and state taxes of someone living in new york city

'''
ideas for control flow:
    functions:
        tax_amount_eq - calculates the tax to be paid based on bracket (this is the same equation between state and federal)
        filing_jointly - calculates whether users are joint filing or solo
        federal_bracket - if statements for each bracket that the user belongs to based on joint or not
        state_bracket - if statements determining user rate based on which bracket they belong in & joint or not

    How to hold the data?
        {'0 - 21600': [0, income, 0, 0.03078]} - objects with bracket as the key (but how will that be read?)

'''

single_federal_brackets = {
    # bracket: [intial amount, 'income', bracket to be subtracted, tax rate to multiply]
        # possible refactor to make each object easier to access
        # 10275: [{'initial amount': 0}, "income", {'bracket': 0},{'tax rate': 0.1}],
    10275: [0, "income", 0, 0.1],
    41775: [1027.5, "income", 10275, 0.12],
    89075: [4807.5, "income", 41775, 0.22],
    170050: [15213.5, "income", 89075, 0.24],
    215950: [34647.5, "income", 170050, 0.32],
    539900: [49335.5, "income", 215950, 0.35],
    539901: [162718, "income", 539900, 0.37]
}


joint_federal_brackets = {
    20550: [0, 'income', 0, 0.1],
    83550: [2055, 'income', 20550, 0.12],
    178150: [9615, 'income', 83550, 0.22],
    340100: [30427, 'income', 178150, 0.24],
    431900: [69295, 'income', 340100, 0.32],
    647850: [98671, 'income', 431900, 0.35],
    647851: [174253.5, 'income', 647850, 0.37],
}

# add single and joint NY State brackets here

tax_amount = 1

def tax_amount_eq(bracket_rate, income, initial_bracket, tax_rate):
    tax_equation = bracket_rate + (income - initial_bracket) * tax_rate

    print('your bracket is %s. your income is %s. your initial bracket is %s. your rate is %s' % (
    bracket_rate, income, initial_bracket, round(tax_rate * 10, 2)))
    return tax_amount


def filing_joint():
    filing_joint = input("Are you filing jointly or single? (Y/N) ")

    if filing_joint.lower() == "y":
        return income = int(input("What is your joint annual income? "))
        # state_income_joint(income)

    elif filing_joint.lower() == "n":
        income = int(input("What is your annual income? "))
         # state_income_single(income)
    else:
        print("You didn't input an accurate filing status")
        tax_amount = 0

def check_tax(income, brackets):
    incomes = list(brackets.keys())

    for key in range(len(brackets)):
        # if income is less than 20550 (first bracket
        if income <= incomes[0]:
            print('if', income[0])
            break
        # if income is in other brackets
        elif income >= incomes[key] and not income > incomes[key+1]:
            print('elif', incomes[key], incomes[key+1])
            break
        # if income is greater than largest bracket
        elif income >= 647851:
            print('income greater than brackets', incomes[key])
            break
        else:
            # print('else', initial_bracket)
            pass

def calculate_user_tax():
    print('Welcome to this New York State and Federal tax calculator')

    filing_joint()

print(tax_amount)

'''
joint_state brackets = {
    '0 - 21600': [0, income, 0, 0.03078],
    '21601 - 45000': [655, income, 21600, 0.03762],
    '45001 - 90000': [1545, income, 45000, 0.03819],
    '90001 < ': [3264, income, 90000, 0.03876],
}



single_federal_brackets = {
    '0 - 10275' = [0, income, 0, 0.1]
    '10276 - 41775' = [1027.5, income, 10275, 0.12],
    '41776 - 89075' = [4807.5, income, 41775, 0.22],
    '89076 - 170050' = [15213.5, income, 89075, 0.24],
    '170051 - 215950' = [34647.5, income, 170050, 0.32],
    '215951 - 539900' = [49335.5, income, 215950, 0.35],
    '539901 < ' = [162718, income , 539900, 0.37]
}

joint_federal_brackets = {
    '0 - 20550' = [0, income, 0, 0.1],
    '20551 - 83550' = [2055, income, 20550, 0.12],
    '83551 - 178150' = [9615, income, 83550 0.22]
    '178151 - 340100' = [30427, income, 178150, 0.24],
    '340101 - 431900' = [69295, income, 340100, 0.32],
    '431901 - 647850' = [98671, income, 431900, 0.35],
    '647850 < ' = [174253.5, income, 647850, 0.37],
}



# idea for how to hold data
joint_federal_brackets = {
    'bracket 1' = [20550, 0, income, 0, 0.1],
    '20551 - 83550' = [2055, income, 20550, 0.12],
    '83551 - 178150' = [9615, income, 83550 0.22]
    '178151 - 340100' = [30427, income, 178150, 0.24],
    '340101 - 431900' = [69295, income, 340100, 0.32],
    '431901 - 647850' = [98671, income, 431900, 0.35],
    '647850 < ' = [174253.5, income, 647850, 0.37],
}
'''

'''
federal tax brackets:
Single:
    0 - 10275 = 10%
    10276 - 41775 = 12%
    41776 - 89075 = 22%
    89076 - 170050 = 24%
    170051 - 215950 = 32%
    215951 - 539900 = 35%
    539901 > = 37%

Joint:
    0 - 20550 = 10%
    20551 - 83550 = 12%
    83551 - 178150 = 22%
    178151 - 340100 = 24%
    340101 - 431900 = 32%
    431901 - 647850 = 35%
    647850 > = 37%
'''
