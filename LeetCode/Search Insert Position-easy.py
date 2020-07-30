def binary_search(elementList, searchElement):
    n = len(elementList)
    left = 0
    right = n - 1

    while left <= right:
        mid = int ((left+right)/2)
        if elementList[mid] == searchElement:
            return mid
        elif searchElement > elementList[mid]:
            left = mid + 1
        elif searchElement < elementList[mid]:
            right = mid - 1
    return left

result = binary_search([1,3,5,6],7)
print("Element found at index: ",result)
