from helpers import confirm, getValidNameFieldValue, getValidIntegerValue, getValidAndUniqueValue, printSuccessMessage, printWarningMessage, printInfoMessage

def getValidEmployeeType():
    employeeType = input('Please input employee type [Hourly/Manager]: ').strip()
    if employeeType == 'no': return 'no'
    acceptedEmployeeTypes = ['hourly', 'manager']
    if not employeeType.lower() in acceptedEmployeeTypes: 
        printWarningMessage(f"Employee type must be either 'hourly' or 'manager'. You entered: '{employeeType}'.")
        return getValidEmployeeType()
    return employeeType

def createEmployee(currentEmployees):
    totalPurchased = 0
    totalDiscounts = 0
    printInfoMessage('\nEmployee creation page:\n')
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
    
    printSuccessMessage(f"\nNew employee with id: '{employeeID}' and name: '{employeeName}' successfully added into list.")
   
    if confirm('\nDo you want to add another employee into list? [Yes/No or Y/N]: '):
        createEmployee(currentEmployees)
   
    return currentEmployees