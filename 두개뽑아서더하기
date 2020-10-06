def solution (numbers):
    sum_list=[]
    new_list=[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            sum_list.append(numbers[i]+numbers[j])
    for i in sum_list:
        if i not in new_list:
            new_list.append(i)
    new_list.sort()
    print(new_list)
    return new_list

input_num=[2,1,3,4,1]
sum(input_num)
