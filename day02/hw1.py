# 01 첫 숫자와 끝 숫자를 입력받고 첫숫자, 끝숫자 합을 구하기.
num1 = int(input("첫 숫자를 입력하세요."))
num2 = int(input("끝 숫자를 입력하세요."))
sum = num1 + num2
print("01. 첫숫자와 끝숫자의 합은 : ", sum)
# 위 아래 같은 표현법임. 
print("숫자의 합은 {}입니다.".format(sum))
