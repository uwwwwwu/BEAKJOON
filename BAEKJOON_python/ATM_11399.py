num=int(input())
n_list = list(map(int, input().split()))

n_list.sort()

for i in range(num-1):
    n_list[i+1]=n_list[i]+n_list[i+1]

print(sum(n_list))