# n = int(input())
# nums = list(map(int, input().split()))
# min_num, max_num = nums[0], nums[0]
# for num in nums:
#     if min_num > num:
#         min_num = num
#     if max_num < num:
#         max_num = num
# print(f"{min_num} {max_num}")

n = int(input())
num_list = list(map(int, input().split()))
print(min(num_list), max(num_list))