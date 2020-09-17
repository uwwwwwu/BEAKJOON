# 가장 빨리 끝나는 거
num=int(input())
n_list = [0]*num

for i in range(num):
    a,b = input().split()
    n_list[i]=[int(b),int(a)] # 끝나는 시간이 앞으로

n_list.sort()

list_dic =[]
val=[]

key = n_list[0][0]
val.append(n_list[0][1])

for j in range(1,num):
    if key == n_list[j][0]:
        val.append(n_list[j][1])
    else :
        val.sort()
        list_dic.append([key,val])
        val =[]

        key = n_list[j][0]
        val.append(n_list[j][1])
list_dic.append([key,val])


last_class = list_dic[0][0]
classCnt = 1
for k in range(1,len(list_dic)):
    for l in range(len(list_dic[k])):
        if last_class <= list_dic[k][l]:
            classCnt += 1
            last_class = list_dic[k][0]
        


print(n_list)