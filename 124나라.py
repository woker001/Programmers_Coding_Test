##124나라

def solution(n):
    answer = ''
    num_124 = [1, 2, 4]
    while 1:
        if n-1<3 :
            answer += str(num_124[(n - 1) % 3])
            break
        answer += str(num_124[(n - 1)%3])
        n=(n-1)//3
        
    answer = ''.join(reversed(answer))
    return answer
    
    
    
    #재귀
def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))
