# PersonEx 클래스를 구성하시오
# 속성으로 name, age가 존재한다
# 액션(함수)로 getName, getAge 가 존재한다
# name과 age는 생성자에서 초기화 된다
########################################
# 파이썬의 모든 클래스의 슈퍼 클래스(근본 클래스)는
# Object 존재함
class PersonEx:
    # 멤버변수
    name = None
    age  = None
    # 생성자
    def __init__( self, name, age ):
        self.name = name
        self.age  = age
    # 멤버함수
    def getName( self ):
        return self.name  
    def getAge( self ):
        return self.age
    

# F반 멤버
f1 = PersonEx("홍길동",30)
f2 = PersonEx("홍길동2",20)
# F반 멤버 리스트
print( [ f1, f2 ] )
#########################################
# 요구사항 PersonEx는 그대로 두고, PersonEx2를 만들어서
# eat() 함수를 추가해달라 요구사항
# PersonEx2 = PersonEx + eat()
# 위의 요구사항은 상속이라는 방법으로 해결
# PersonEx는 부모, PersonEx2는 자식이 되서
# 자식은 부모의 모든 기능을 승계하고, 자식은 별도로 기능 추가
#########################################
# class 자식클래스명(부모클래스명): =>상속
class PersonEx2(PersonEx):
    def eat(self):print('eat call')

pe = PersonEx2('역삼', 20)
print( pe.getAge(), pe.getName(), pe.eat() )      
#########################################
# 상속후 재정의(부모로 부터 받은 함수를 재정의) 예
class PersonEx3(PersonEx2):
    def eat(self):print('eat call 1234')
pe2 = PersonEx3('역삼', 20)
pe2.eat()
