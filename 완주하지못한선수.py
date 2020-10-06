def solution(participant,completion):
    participant.sort()
    completion.sort()
    answer=''
    for i in range(len(participant)-1):
        if participant[i]!=completion[i]:
            answer=participant[i]
            break
    if answer=='':
        answer=participant[len(participant)-1]
    return answer
