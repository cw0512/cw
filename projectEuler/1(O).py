#10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고,
#이것을 모두 더하면 23입니다.

#1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

#a = range(1,1000)
#sum = 0

##if int(a) % 3 == 0:
##    sum = sum+a
#for N in a:
    ##print(N)
    #if N % 3 == 0 or N % 5 == 0:
        #sum += N
        ##print(N)
#print(sum)

x=[]
for i in range(1,1000):
  if i%3 == 0 or i%5 == 0: #5아니면 3의 배수일때
    x.append(i) #x에 넣기
print(x)

