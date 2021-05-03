# 02 첫숫자와 끝 숫자를 입력받고 첫숫자~끝숫자의 합을 구하기
num1 = int(input("첫 숫자를 입력하세요."))
num2 = int(input("끝 숫자를 입력하세요."))

result = 0
for i in range(num1, num2+1):
        result += i
print(result)