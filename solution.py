def isIsomorphic(s, t): # 55%
    return map(s.find, s) == map(t.find, t)

def isIsomorphic2(s, t): # 86%
    print((set(zip(s, t)))) # think of this as stacking 2 sets/tuples on top of each other
    print((set(s))) # set returns all unique elements as a tuple
    print((set(t)))
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) # first len takes the number of tuples in the set

def isIsomorphic1(s, t): # 8%
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
        

print(isIsomorphic2("egg", "add"))
print(isIsomorphic2("foo", "bar"))
print(isIsomorphic2("paper", "title"))
print(isIsomorphic2("bbbaaaba","aaabbbba"))
print(isIsomorphic2("aa", "b")) # takes advantage of the fact that t.len = s.len so this is equivalent to aa == bb