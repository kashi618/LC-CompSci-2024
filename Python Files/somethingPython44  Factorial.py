def factorial(n):
    answer = 1
    for i in range(n,1,-1):
        answer = answer * i
    return answer

print(factorial(2))