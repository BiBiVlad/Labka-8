def kbig(nums, k):
    counter = 1
    for i in range(1, len(nums)):
        if counter == k:
            break
        nums.remove(max(nums))
        counter += 1
    return max(nums)

print(kbig(nums, k))