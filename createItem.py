from helpers import confirm, getValidNameFieldValue, getValidIntegerValue, getValidAndUniqueValue

def createItem(currentItems):
    itemNumber = getValidAndUniqueValue(currentItems, 0, 'item number')
    if itemNumber == 'no': return
  
    itemName = getValidNameFieldValue('Item')
    if itemName == 'no': return
  
    itemCost = getValidIntegerValue('Please input item cost: ', 'item cost')
    if itemCost == 'no': return
  
    currentItems.append([itemNumber, itemName, itemCost])
  
    if confirm('\nDo you want to add another item into list? (Yes/No): '):
        createItem()

    return currentItems