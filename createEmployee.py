from helpers import confirm, getValidNameFieldValue, getValidIntegerValue, getValidAndUniqueValue

def getValidEmployeeType():
    employeeType = input('Please input employee type ("hourly" or "manager"): ').strip()
    if employeeType == 'no': return 'no'
    if employeeType == 'hourly' or employeeType == 'manager': return employeeType
    else:
        print(f"Employee type must be either 'hourly' or 'manager'. You entered: '{employeeType}'.")
        getValidEmployeeType()

def createEmployee(currentEmployees):
    totalPurchased = 0
    totalDiscounts = 0
    employeeID = getValidAndUniqueValue(currentEmployees, 0, 'employee ID')
    if employeeID == 'no': return
    employeeName = getValidNameFieldValue('Employee')
    if employeeName == 'no': return
    employeeType = getValidEmployeeType()
    if employeeType == 'no': return
    yearsWorked = getValidIntegerValue('Please input years of work: ', 'year of work')
    if yearsWorked == 'no': return
    employeeDiscountNumber = getValidAndUniqueValue(currentEmployees, 6, 'employee discount number')
    if employeeDiscountNumber == 'no': return
    currentEmployees.append([employeeID, employeeName, employeeType, yearsWorked, totalPurchased, totalDiscounts, employeeDiscountNumber])
    shouldAddAnotherEmployee = confirm('\nDo you want to add another employee into list? (Yes/No): ')
    if shouldAddAnotherEmployee:
        createEmployee()
    return currentEmployees