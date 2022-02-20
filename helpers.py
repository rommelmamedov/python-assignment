# General Helper Functions.
def getValidIntegerValue(prompt, fieldName):
    inputValue = input(prompt).strip()
    if inputValue == 'no': return 'no'
    # Condition to checks if user entered numberic value.
    if inputValue.isnumeric():
        return int(inputValue)
    else:
        print(f"Please provide a valid interger value for {fieldName}.")
        return getValidIntegerValue(prompt, fieldName)


def confirm(message):
    choice = input(message).strip().lower()
    while True:
        if choice in ['yes', 'y']: return True
        elif choice in ['no', 'n']: return False
        else: print("Please respond with 'yes' or 'no'")


def goToMenu():
    return confirm('\nDo you want to go back into menu view? (Yes/No): ')

# Recursive function to get valid and unique value from user.

def getValidIdentifier(list, fieldIndex, fieldName):
    value = getValidIntegerValue(f'Please input {fieldName}: ', fieldName)
    if value == 'no': return 'no'
    for item in list:
        if value == item[fieldIndex]:
            return value
        else:
            continue
    print(f"{fieldName.capitalize()}: '{value}' does not exists in the list. Please correct value for {fieldName}.")
    return getValidIdentifier(list, fieldIndex, fieldName)

def getValidAndUniqueValue(list, fieldIndex, fieldName):
    value = getValidIntegerValue(f'Please input {fieldName}: ', fieldName)
    if value == 'no':
        return 'no'
    for item in list:
        if value == item[fieldIndex]:
            print(f"{fieldName.capitalize()}: '{value}' already exists in the list. Please provide unique value for {fieldName}.")
            getValidAndUniqueValue(list, fieldIndex, fieldName)
    return value

def getValidNameFieldValue(field):
    name = input(f'Please input {field.lower()} name: ').strip()
    if name and not name.isnumeric():
        return name.capitalize()
    else:
        print(f"{field} name can not be empty or numeric. You entered: '{name}'.")
        getValidNameFieldValue()


def getItemFromListByUniqueIdentifier(list, uniqueIdentifier, searchIndex):
    for item in list:
        if uniqueIdentifier == item[searchIndex]:
            return item
