def bad_13(nums):
    """Does not add up 13 and its immediate elemnet to the total and returns the total"""
    index = []
    for i,j in enumerate(nums):
        if j ==13:
            index.append(i)
    index = list(set(index + list(map(lambda i: i+1,index))))
    sums = 0
    for i in range(len(nums)):
        if i in index:
            continue
        else:
            sums = sums + nums[i]
    return sums
print(bad_13([13,13,5,5,13,13,13,5,3]))
    
        

