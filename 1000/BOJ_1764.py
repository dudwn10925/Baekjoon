# n, m = map(int, input().split())
# name_dict = {}
# for i in range(n):
#     name = input()
#     name_dict[name] = name
    
# cnt = 0
# lst = []
# for i in range(m):
#     name = input()
#     if name in name_dict:
#         cnt += 1
#         lst.append(name)

# print(cnt)
# for name in sorted(lst):
#     print(name)

# 집합으로 풀어보기
n, m = map(int, input().split())
listen_no = set(input() for _ in range(n))
see_no = set(input() for _ in range(m))
name_list = list(listen_no.intersection(see_no))

print(len(name_list))
for name in sorted(name_list):
    print(name)