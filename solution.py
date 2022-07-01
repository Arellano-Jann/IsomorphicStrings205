def isIsomorphic(s, t): # 8%
    num1 = []
    num2 = []
    value1 = []
    value2 = []
    for index, value in enumerate(s):
        if value not in value1:
            num1.append(index)
            value1.append(value)
        else:
            num1.append(value1.index(value))
            value1.append(value)
        if t[index] not in value2:
            num2.append(index)
            value2.append(t[index])
        else:
            num2.append(value2.index(t[index]))
            value2.append(t[index])
    return num1 == num2
        
    

# def isIsomorphic(s, t): # 12%
#     final = [x for x in range(len(nums)) if sum(nums[:x]) == sum(nums[x+1:])]
#     return -1 if len(final) == 0 else final[0]

# def isIsomorphic(s, t): # 77%
#     left, right = 0, sum(nums)
#     for index, num in enumerate(nums):
#         right -= num
#         if left == right:
#             return index
#         left += num
#     return -1


print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))