array = [1, 5, 2, 6, 3, 7, 4]
tmp=[]
answer=[]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
for i,j,k in commands :
    print(i,j,k)
    tmp=array[i-1:j]
    tmp.sort()
    answer.append(tmp[k-1])
print(answer)
