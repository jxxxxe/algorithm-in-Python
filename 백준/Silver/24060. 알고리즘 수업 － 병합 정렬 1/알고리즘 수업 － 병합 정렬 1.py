N, K = map(int,input().split())
nums = list(map(int, input().split()))
count = 0

def is_count(current):
    if count == K:
        print(current)
        exit()

def merge_sort(start, end):
    if start<end:
        merge_sort(start,(start+end)//2)
        merge_sort((start+end)//2+1, end)
        merge(start, end)

def merge(start, end):
    middle = (start+end)//2
    left, right = start, middle+1
    tmp=[]
    global count
    while left<=middle and right<=end:
        if nums[left] <= nums[right]:
            tmp.append(nums[left])
            left+=1
        else:
            tmp.append(nums[right])
            right+=1
        count+=1
        is_count(tmp[-1])
    while left<=middle:
        tmp.append(nums[left])
        left+=1
        count+=1
        is_count(tmp[-1])
    while right<=end:
        tmp.append(nums[right])
        right+=1
        count+=1
        is_count(tmp[-1])
    nums[start:end+1] = tmp
    
merge_sort(0, len(nums)-1)
print(-1)