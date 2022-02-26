from helpers import printInfoMessage

def getAllEmployeesSummary(updatedEmployees):
    printInfoMessage('\n— — — — — — — — — — — — — — — — — — — — — — — — — Employees Summary — — — — — — — — — — — — — — — — — — — — — — — —')
    
    print('\nEmployee ID, Employee Name, Employee Type, Years Worked, Total Purchased, Total Discounts, Employee Discount Number\n')
    
    for employeeID, employeeName, employeeType, yearsWorked, totalPurchased, totalDiscounts, employeeDiscountNumber, in updatedEmployees:
        print(f'{employeeID}, {employeeName}, {employeeType}, {yearsWorked}, ${totalPurchased:.2f}, ${totalDiscounts:.2f}, {employeeDiscountNumber}\n')
    
    printInfoMessage('— — — — — — — — — — — — — — — — — — — — — — — — — Employees Summary — — — — — — — — — — — — — — — — — — — — — — — —')

