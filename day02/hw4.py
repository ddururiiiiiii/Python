#05 첫숫자~끝숫자 홀수의 합은?
num1 = int(input("첫 숫자를 입력하세요."))
num2 = int(input("끝 숫자를 입력하세요."))

sum5 = 0
for i in range(num1, num2+1) : 
    if(i % 2) != 0 :
        sum5 += i
print("첫숫자~끝숫자 홀수의 합은 ? ", sum5)