def isFound(arr,ele):
    for i in arr:
        if i==ele:
            return 1
    return 0


n = int(input("Enter the length of the Array : "))
arr = []

print("Enter the elements one by one : ")
for i in range(n):
    arr.append(int(input()))

ele = int(input("Enter the element you wnat to search : "))

if(isFound(arr,ele)):
    print("Element Found")
else:
    print("Element Not Found")



