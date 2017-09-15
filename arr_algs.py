def minarr(arr):
    a = arr[0]
    for i in arr:
        if i<a:
            a=i
    return a

def avgarr(arr):
    summ=0
    for i in arr:
        summ+=i
    return summ/len(arr)

arr1 = [7,3,4,5,11,12,13]

print(minarr(arr1))
print(avgarr(arr1))
