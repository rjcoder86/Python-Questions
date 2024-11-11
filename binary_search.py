arr = [2,1,3,5,6,4,8,7,9,0]
arr.sort()
print(arr)
target = 10
l,r=0,len(arr)-1
for i in range(len(arr)):
    mid = (l+r)//2
    if arr[mid] == target:
        print('found')
        break
    elif arr[mid] > target:
        r = mid -1
    else :
        l = mid+1
print('no found')
