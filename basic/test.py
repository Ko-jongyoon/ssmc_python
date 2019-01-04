import random
#난수 발생
print( random.randint(0,1) )





# 특정 문자열이 숫자 임을 체크
txt = ['1','A','a','1','가','1.1']
for item in txt:
    print(item, item.isalpha(),
                item.isdigit(),
                item.isdecimal(),
                item.isnumeric() )




# a가 값이 있으면1, 없으면 2를 출력하시오
#######################################
# 참인 케이스를 잡고 아닌것 나머지 처리
a=''
if a:
    print('1')
else:
    print('2')
#######################################
#부정인 케이스를 잡고 아닌것 나머지 처리
a=''
if not a:
    print('2')
else:
    print('1')

