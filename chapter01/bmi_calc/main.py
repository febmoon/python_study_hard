'''
bmi_calc를 만들기 위한 사전 준비
'''
# age = input("당신의 나이는 몇 살입니까>>>")
# print(type(age))
# print(f"당신은 내년에 {age+1}살이 됩니다.") -> 오류 발생
'''
input()함수의 결과값은 언제나 str입니다. -> 즉, 수학 연산을 하기 위해서는
별도의 과정이 필요합니다.

이때 필요한 함수가 '형변환 함수'입니다.(Conversion)
'''
# age1 = input("당신의 나이는 몇 살입니까>>>")
# print(type(age1))   # 결과값 : str
# age1_int = int(age1) # str인 age1을 int 로 자료형을 변환시켜서
#                      # age1_int라는 새로운 변수에 대입
# print(type(age1_int))
# print(f"당신은 내년에 {age1_int+1}살이 됩니다.")    #여기서는 오류 발생 X
'''
자주 쓰이는 형변환 함수
1. int() -> str 또는 float을  int 로 변경 -> 소수의 경우 버림
2. float() -> str 또는 int 를  float으로 변경 -> 정수의 경우 .0 붙여줌
3. round() -> 반올림
'''
temp = int(3.8)
print(temp)
temp2 = float(4)
print(temp2)

temp3 = round(3.8)
print(temp3)

temp4 = round(5.3491285,2) #괄호 첫번재 수를 소수점 2쩨자리까지 표기
print(temp4)
'''
BMI 계산기를 작성합니다.

1. 키(cm) 를 입력받아 (input()를 쓰라는 의미) 변수 height에 저장합니다.
2. 몸무게(kg)을 입력받아 변수 weight에 저장합니다.
3. 몸무게 / (키(m)의 제곱)을 계산하면 bmi 지수가 나옵니다.
4. bmi 지수를 int 로 출력하세요. -> int() 함수 사용하라는 의미
5. bmi 지수를 소수점 셋째자리에서 반올림하여 둘째자리까지 출력하세요. -> round()함수 사용

실행 예

로고 출력하세요(구글에서 text to ascii art 검색하면 나옵니다
당신의 키는 몇 cm 입니까>>> 173.2
당신의 몸무게는 몇 kg입니까? >>> 70
당신의 bmi 지수는 23입니다.
당신의 bmi 지수는 23.xx 입니다.
'''

# 로고 출력

# 키 / 몸무게 입력받고 변수에 저장


# height = input("당신의 키는 몇 cm입니까 >>>")
# weight = input("당신의 몸무게는 몇 kg입니까? >>>")
# height_float = float(height)
# # 1. height = float(height) 이렇게 가능하다!! 파이썬에서는~ a=a+1되는 것 거처럼!!
# # height = height / 100
# # weight = float(weight)
# # bmi = weight / (height**2)
# # bmi_int = int(bmi) 정수로 표현
# # bmi_round = round(bmi,2) 결과값을 소수점 셋째 자리에서 반올림한 결과

height = float(input("당신의 키는 몇 cm입니까?>>>"))/100
weight = float(input("당신의 몸무게는 몇kg입니까?>>>"))
print(f"당신의 bmi지수는 {int(weight/(height**2))}입니다.")
print(f"당신의 bmi지수는 {round(weight/(height**2),2)}입니다")




# weight_float = float(weight)
# height_m = height_float / 100
# BMI = weight_float / (height_float**2)
# 
# print(int(BMI))
# print(round(BMI,2))