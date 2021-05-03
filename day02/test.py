#04 첫숫자~끝숫자 짝수의 합은?
num1 = int(input("첫 숫자를 입력하세요."))
num2 = int(input("끝 숫자를 입력하세요."))

sum4 = 0
for i in range(num1, num2+1) : 
    if(i % 2) == 0 :
        sum4 += i
print("첫숫자~끝숫자 짝수의 합은 ? ", sum4)