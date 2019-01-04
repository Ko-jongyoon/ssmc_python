'''
4. 함수
 - 기본 문법
 - 중요 내장 함수 몇개 확인
 - 용도 : 반복작업 처리, 재사용성을 높일 때, 개발 속도 향상
         -> 생산성이 증가된다.
'''
############################################################
'''
기본 syntax
def 함수이름( 인자(파라미터)들(개수는 자유롭게) ):
    수행문
    수행문 .. 
    return 리턴값들(개수는 자유롭게) <= [생략 가능]
'''    
# 더하기 함수 (2개의 정수값을 받아서 더한값을 리턴하는 함수 sum 구현)
def sum(x , y):
    return x + y
# 함수 호출 =>사용 => Call By Value : 호출하고 결과를 돌려받는다
# result = 3
result = sum(1,2)
############################################################
# 가변인자-> 몇개를 보낼지 모르겠으나 보낸 것 다 더해라
# 인자가 몇개 올지 알 수 없다, 보내는 족족 다 처리할 수 있게
#인자 표현법을 처리 ->가변인자 구성
def sum2 ( *args ):
    # args에서 하나씩 구성원을 뽑아서 전부 더한 값을 출력
    # 누적합을 담고 있을 변수, 초기값은 더한적이 없으니 0
    addSum = 0
    for arg in args:
        #하나씩 뽑기
        # print( arg )
        addSum +=arg
    return addSum

#누적합 함수 구현
print (sum2 (1,2))
print (sum2 (1,2,3))
print (sum2 (1,2,3,4))
print (sum2 (1,2,3,4,5))
print (sum2 (1,2,3,4,5,6))

#누적곱 함수를 구성하시오.
def mul ( *args ):
    # args에서 하나씩 구성원을 뽑아서 전부 더한 값을 출력
    # 누적합을 담고 있을 변수, 초기값은 더한적이 없으니 0
    addmul=1
    for arg in args:
        #하나씩 뽑기
        #print( arg )
        addmul *=arg
    return addmul

#누적합 함수 구현
print (mul (1,2))
print (mul (1,2,3))
print (mul (1,2,3,4))
print (mul (1,2,3,4,5))
print (mul (1,2,3,4,5,6))

# 여러값 리턴
# 가변인자로 누적합과, 누적곱을 리턴하는 mix 함수를 구현하시오.
def mix ( *args ):
    # args에서 하나씩 구성원을 뽑아서 전부 더한 값을 출력
    # 누적합을 담고 있을 변수, 초기값은 더한적이 없으니 0
    asum=0
    amul=1
    for arg in args:
        #하나씩 뽑기
        #print( arg )
        asum +=arg
        amul *=arg    
    #결과값 돌려주기    
    return amul, asum

result = mix (1,2,3,4,5,6)
print ( result, type(result) )
# 리턴값이 여러개면 tuple로 리턴된다
# mix(1,2,3,4,5,6) 호출해서 누적합은 a, 누적곱은 b라는변수에
# 담아서 각각출력하시오
a,b =mix (1,2,3,4,5,6)
print(a,b)
###########################################################
# 누적합은 'a'라는 키를 통해, 누적곱은 'b'라는 키를 통해 출력 
# 가능하게 mix()를 확장한mixEx()를 구성하시오
def mixEx ( *args ):
    asum=0
    amul=1
    for arg in args:
        asum +=arg
        amul *=arg    
    #결과값 돌려주기    
    #return {'a':asum, 'b':amul}
    dic = dict()
    dic['a']= asum
    dic['b']= amul
    #return dic
    return dic, {'a':asum, 'b':amul}

res= mixEx( 1,2,3,4,5,6 )
 # res의 타입은?
print( res )
 # res의 두번째 멤버에 데이터 중에 키가 b값을 출력하시오
 # res tuple를 의미
 # res[1]['b']=> 키를 넣어서 값을 획득
print( res[1]['b'])
#######################################################
dic =res[1]
print(dic['b'])
#######################################################
print('='*100)
# 문자열을 하나를 매개변수로 받아서 앞뒤 공백을 제거하고 앞뒤로
# [문자] 이렇게 출력해주는 함수 trimEx()를 만드시오
def trimEx( src ):
    print( '[%s]' % src.strip() )
trimEx('n      awr1       ')
#######################################################
# 콘솔출력 => print()
# 자주 사용하는 함수들은 재정의해서 사용할 수 있다.
# 일종의 어플리케이션 전체 기능을 통제할 수 있는 환경변수들을
# 정의하여서 세부 기능들도 조정이 가능하다
istest = True
# 로그함수, 상용화시에는 istest= False로 두어서
# 로그를 제거한다
def log( msg ):
    if istest:
      print( msg )
    
log('1')
log('2')
log('3')
######################################################
# 함수의 인자에 기본값 주기
# 기본값을 부여한 파라미터들은 순서가 없어진다.
def setPerson( name,age=30,weight=70 ):
    print('%s님의 나이는 %s, 몸무게는 %s이다' % (name,age,weight))

setPerson('multi1')
setPerson('multi2', age=10)
setPerson('multi3', age=20, weight=100)
setPerson('multi4', weight=100)
setPerson('multi5', weight=100, age=20 )
# 오류
#setPerson(weight=100, age=20 )
#####################################################
# 사용 타이밍
# 인터프린터 언어이기 때문에 먼저 정의된후에 사용 가능하다
#test()
def test():
    print('test')
#####################################################
a = 10 
def check():
    # 함수 안에서 정의된 변수
    # 지역변수, 함수가 호출될때만 존재
    a= 11
    # a가 글로벌 변수임을 지정하면 그때부터 
    # a를 로컬변수가 아닌 전역변수를 가르키게된다.
check()
print( a )
######################################################
# 함수도 수행문이 하나면 옆으로 쓸 수 있다
def text1( x ):return x+"<-"


