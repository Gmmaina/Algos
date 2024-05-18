def linear_search(list, target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

# def verify(index):
#     if index != None:
#         print("The target is at index:",index)
#     else:
#         print("Target not in the list!")
        
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# result = linear_search(numbers, 5)
# print(result)

print(linear_search(numbers,6))

# result = linear_search(numbers, 16)
# verify(result)

# result = linear_search(numbers, 14)
# verify(result)