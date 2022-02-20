
from getAllEmployeesSummary import getAllEmployeesSummary
from helpers import confirm, getItemFromListByUniqueIdentifier, getValidIdentifier


def updateEmployeeList(employeeDiscountNumber, currentEmployees, totalPurchased, totalDiscounts):
    updatedEmployees = []

    for employee in currentEmployees:
        if employeeDiscountNumber == employee[6]:
            employee[4] = totalPurchased
            employee[5] = totalDiscounts
    
    updatedEmployees = currentEmployees

    return updatedEmployees


def calculateCost(employee, item):
    maxTotalDiscount = 200
    maxYearlyPercentage = 10
    employeeType = employee[2]
    yearsWorked = employee[3]
    totalPurchased = employee[4]
    totalDiscounts = employee[5] + 120

    totalYearBasedPercentage = yearsWorked * 2
    totalPercentage = 0
    if totalYearBasedPercentage > maxYearlyPercentage:
        totalPercentage = totalYearBasedPercentage - (totalYearBasedPercentage - maxYearlyPercentage)
    else:
        totalPercentage = totalYearBasedPercentage

    if employeeType == 'manager': totalPercentage += 10
    elif employeeType == 'hourly': totalPercentage += 2

    itemCost = item[2]
    totalPurchased += itemCost - (itemCost * totalPercentage / 100)
    totalDiscounts += itemCost * totalPercentage / 100
    print(totalPurchased, 'totalPurchased')
    print(totalDiscounts, 'totalDiscounts')
    print(totalPercentage, 'totalPercentage')
    return totalPurchased, totalDiscounts, maxTotalDiscount


def makePurchase(currentItems, currentEmployees):
    updatedEmployees = currentEmployees
    
    print('\n— — — — — — Items Summary — — — — — —')
    print('\nItem Number, Item Name, Item Cost\n')
    for itemNumber, itemName, itemCost in currentItems:
        print(f'{itemNumber}, {itemName}, ${itemCost:.2f}\n')
    print('— — — — — — Items Summary — — — — — —\n')
    
    employeeDiscountNumber = getValidIdentifier(currentEmployees, 6, 'employee discount number')
    if employeeDiscountNumber == 'no': return
    
    itemNumber = getValidIdentifier(currentItems, 0, 'item number')
    if itemNumber == 'no': return
    
    if confirm('\nDo you want to confirm purchase? (Yes/No): '):
        employee = getItemFromListByUniqueIdentifier(currentEmployees, employeeDiscountNumber, 6)
        item = getItemFromListByUniqueIdentifier(currentItems, itemNumber, 0)
        totalPurchased, totalDiscounts, maxTotalDiscount = calculateCost(employee, item)
        
        if totalDiscounts > maxTotalDiscount:
            print(f"\nSorry employee with discount number: '{employeeDiscountNumber}' is not allowed to make this purchase. No discount allowed once you have received $200 discount. Current calculated discount amount is: '{totalDiscounts}'.")
        else:
            updatedEmployees = updateEmployeeList(employeeDiscountNumber, currentEmployees, totalPurchased, totalDiscounts)
    
    if confirm('\nDo you want to make new purchase? (Yes/No): '):
        makePurchase(currentItems, currentEmployees)
    else: 
        getAllEmployeesSummary(updatedEmployees)
    
    return updatedEmployees
