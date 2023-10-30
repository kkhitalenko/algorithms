# С использованием рекурсии
#
# def get_qty_of_blocks(nums, comparable=None, qty=0):
#     if len(nums) == 1:
#         return qty + 1

#     last_smaller_value_ind, larger_values_indices = 0, []
#     if comparable is None:
#         comparable = nums[0]
#     for i, v in enumerate(nums[::-1]):
#         if v < comparable:
#             last_smaller_value_ind = len(nums) - 1 - i
#             break
#     for i, v in enumerate(nums[:last_smaller_value_ind]):
#         if v > comparable:
#             larger_values_indices.append(i)

#     if last_smaller_value_ind == len(nums) - 1:
#         return qty + 1

#     if not larger_values_indices:
#         qty += 1
#         return get_qty_of_blocks(nums[last_smaller_value_ind+1:], qty=qty)

#     for i in larger_values_indices:
#         if nums[i] > comparable:
#             comparable = nums[i]
#     return get_qty_of_blocks(nums, comparable=comparable)

def get_qty_of_blocks(nums):
    start, end, res = 0, 1, 0
    while end < len(nums):
        if min(nums[end:]) > max(nums[start:end]):
            start = end
            end += 1
            res += 1
        else:
            end += 1
    res += 1
    return res


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print((get_qty_of_blocks(nums)))
