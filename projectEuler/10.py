#10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

#이백만(2,000,000) 이하 소수의 합은 얼마입니까?

#200만 이하의 소수 구하기

n = 2000000

a = []
for i in range(2, n + 1) :
    cnt = 0

    for j in range(2, i) :
        if i % j == 0 :
           cnt = 1

    if cnt == 0 :
        #print(i)
        a.append(i)




print(sum(a))
    




    
        

    

    


