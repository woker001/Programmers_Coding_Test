#
def solution(board, moves):
    answer = 0
    count = 0
    stk=[]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0 :
                stk.append(board[j][i-1])
                board[j][i-1]=0
                if count>0 and stk[count-1]==stk[count] :
                    stk.pop()
                    stk.pop()
                    count-=2
                    answer+=2
                count+=1
                break
    return answer
