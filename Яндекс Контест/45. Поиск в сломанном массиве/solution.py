def broken_search(nums: list, target: int):
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        return -1
    head_index = get_head(nums, 0, len(nums)-1)
    if nums[head_index] == target:
        return head_index
    elif nums[head_index] < target <= nums[-1]:
        return binary_search(nums, target, head_index, len(nums)-1)
    else:
        return binary_search(nums, target, 0, head_index-1)


def binary_search(nums: list, target: int, left: int, right: int):
    while left <= right:
        mid = (right+left)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def get_head(nums: list, left: int, right: int):
    if right-left == 1:
        return right
    mid = (left + right) // 2
    if nums[mid] < nums[left]:
        return get_head(nums, left, mid)
    else:
        return get_head(nums, mid, right)
