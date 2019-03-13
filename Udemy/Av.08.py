def ran_check(num,low,high):
    if num in list(range(low, high+1)):
        print(num)
        print(low)
        print(high)
        return True
    else:
        return False
print(ran_check(3,1,10))