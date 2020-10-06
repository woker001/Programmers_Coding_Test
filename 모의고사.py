def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]  # 5
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    len_answers=len(answers)
    s1 = (s1 * (len_answers // 5)) + s1[0:len_answers%5]
    s2 = (s2 * (len_answers // 8)) + s2[0:len_answers%8]
    s3 = (s3 * (len_answers // 10)) + s3[0:len_answers%10]
    d=[0,0,0]
    for i in range(len_answers):
        if s1[i] == answers[i] :
            d[0]+=1
        if s2[i] == answers[i] :
            d[1]+=1
        if s3[i] == answers[i] :
            d[2]+=1
    for i in range(3) :
        if d[i]==max(d):
            answer.append(i+1)

    return answer
