def solution(n, lost, reserve):
    answer = 0
    for i in lost:
        if len(lost)==0:
            break
        elif i in reserve:
            answer+=1
            reserve.remove(i)   
        elif i-1 in reserve and i-1 not in lost:
            answer+=1
            reserve.remove(i-1)         
        elif i+1 in reserve and i+1 not in lost:
            answer+=1
            reserve.remove(i+1)
    answer = n+answer-len(lost)
    return answer
