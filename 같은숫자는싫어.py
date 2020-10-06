def solution(arr):
    answer = []
    arr.append('end')
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
    return answer
