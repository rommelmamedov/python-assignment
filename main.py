"""
Ramil Mamedov - 101343299
COMP 2152 - Open Source Development - Assignment 1
Lab Professor: Mr. Hesham Akbari
"""

from helpers import goToMenu, printInfoMessage, printErrorMessage
from initials import getInitialItems, getInitialEmployees
from createItem import createItem
from makePurchase import makePurchase
from createEmployee import createEmployee
from getAllEmployeesSummary import getAllEmployeesSummary

def menu():
    print('— — — — — — — — — — — — — — —')
    printInfoMessage('| 1 - Create Employee.      |')
    printInfoMessage('| 2 - Create Item.          |')
    printInfoMessage('| 3 - Make Purchase.        |')
    printInfoMessage('| 4 - All Employee Summary. |')
    printInfoMessage('| 5 - Exit.                 |')
    print('— — — — — — — — — — — — — — —')
    return input('Choose one of the following options (1, 2, 3, 4, 5): ')


def main():
    print("\nWelcome to the 'Employee Discount Calculator' program!")

    currentItems = getInitialItems()
    currentEmployees = getInitialEmployees()
    
    while True:
        choice = menu()
        if choice == '1':
            currentEmployees = createEmployee(currentEmployees)
            if not goToMenu(): break
        elif choice == '2':
            currentItems = createItem(currentItems)
            if not goToMenu(): break
        elif choice == '3':
            makePurchase(currentItems, currentEmployees)
            if not goToMenu(): break
        elif choice == '4':
            getAllEmployeesSummary(currentEmployees)
            if not goToMenu(): break
        elif choice == '5':
            printInfoMessage('Thanks for using our program!')
            break
        else:
            printErrorMessage('Invalid option! Please select again.')

main()
