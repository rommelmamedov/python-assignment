def printErrorMessage(message):
    print('\033[91m' + message + '\033[0m')

def printSuccessMessage(message):
    print('\033[92m' + message + '\033[0m')

def printWarningMessage(message):
    print('\033[93m' + message + '\033[0m')

def printInfoMessage(message):
    print('\033[94m' + message + '\033[0m')

# General Helper Functions.
def getItemFromListByUniqueIdentifier(list, uniqueIdentifier, searchIndex):
    for item in list:
        if uniqueIdentifier == item[searchIndex]:
            return item

def getValidIntegerValue(prompt, fieldName):
    inputValue = input(prompt).strip()
    if inputValue == 'no': return 'no'
    # Condition to checks if user entered numberic value.
    if inputValue.isnumeric():
        return int(inputValue)
    else:
        printErrorMessage(f"Please provide a valid interger value for {fieldName}.")
        return getValidIntegerValue(prompt, fieldName)

# Reusable confirmation function
def confirm(message):
    choice = input(message).strip().lower()
    while True:
        if choice in ['yes', 'y']: return True
        elif choice in ['no', 'n']: return False
        else: printWarningMessage("Please respond with 'Yes/Y' or 'No/N'")


def goToMenu():
    return confirm('\nDo you want to go back into menu view? [Yes/No or Y/N]: ')

# Recursive function to get valid and unique value from user.
def getValidIdentifier(list, fieldIndex, fieldName):
    value = getValidIntegerValue(f'Please input {fieldName}: ', fieldName)
    if value == 'no': return 'no'
    
    for item in list:
        if value == item[fieldIndex]:
            return value
        else:
            continue

    printWarningMessage(f"{fieldName.capitalize()}: '{value}' does not exists in the list. Please correct value for {fieldName}.")
    return getValidIdentifier(list, fieldIndex, fieldName)

def getValidAndUniqueValue(list, fieldIndex, fieldName):
    value = getValidIntegerValue(f'Please input {fieldName}: ', fieldName)
    if value == 'no': return 'no'

    for item in list:
        if value == item[fieldIndex]:
            printWarningMessage(f"{fieldName.capitalize()}: '{value}' already exists in the list. Please provide unique value for {fieldName}.")
            return getValidAndUniqueValue(list, fieldIndex, fieldName)

    return value

def getValidNameFieldValue(field):
    name = input(f'Please input {field.lower()} name: ').strip()
    
    if name and not name.isnumeric():
        return name.title()
    else:
        printErrorMessage(f"{field} name can not be empty or numeric. You entered: '{name}'.")
        return getValidNameFieldValue(field)


