'''
step 1
"게임의 제목을 입력하세요" 프럼프트 출력
"적당한 제목(영문)" 입력하면 다음 단계 진행
step 1-1

게임 제목은 28자 이내로 입력 받는다
입력하지 않으면 "게임 제목이 입력되지 않았습니다. 다시 입력하세오"
넘으면 " 게임 제목이 28자를 초과합니다 다시 입력하세요 "
28자 이내면 ok

step 2
=====================================
=       게임 제목(중앙정렬)           =
=       v 1.0.0 (중앙정렬)           =
=====================================
이렇게 출력

step 3 
게이머의 이름을 입력하세요
->이름을 넣지 않으면 "뭐라하고" 다시 입력

step 4
AI의 숫자를 입력하세요

->숫자를안넣으면 "경고 메시지" 다시 입력
->숫자가 아닌 값을 넣으면 "경고 메시지" 다시 입력
   isnumeric()으로 체크
->0보다 작거나 (or), 100이상을 입력하면 "경고 메세지" 다시 입력
->정상 범위에 정수값을 입력하면 다음 단계 진행

step 5
AI는 숫자를 하나 생성한다.(랜덤) ->1회만 생성되야함
즉 게임 한번이 종료될때까지 유지되어야 한다.

step 6
판단
1)입력값이 정답보다 작으면 -> 작다고 코멘트
2)입력값이 정답보다   크면 -> 크다고 코멘트
3)입력값이 정답과 동일하면 -> 축하메시지를 뿌려준다

step 7
결과 표시
총 시도 횟수 표시
점수=(10- 총시도횟수)*10
다시 게임을 하시겠습니까?
yes(대소문자 구분 않함) -> 다시 게임 시작(step4부터 진행)
no(대소문자 구분 않함) -> 게임종료 -> 프로그램 종료
아무것도 않넣고 엔터 -> 경고
입력값이 틀려도 -> 경고 

'''
import random
while True:
    gname = input("게임의 영문이름을 28자 이내로 입력해 주세요.\n")

 

    if not gname:
        print("게임 제목이 입력되지 않았습니다. 다시입력하세요")  
        continue  
    elif len(gname)>28:
        print("게임 제목이 28자를 초과합니다. 다시입력하세요") 
        continue
    else:
        print("="*30)
        a = '={0:^28}='.format(gname)
        b = '={0:^28}='.format("v 1.0.0")
        print(a)
        print(b)
        print("="*30)
        break
while True:
   
    gamer = input("게임머의 이름을 입력해주세요.\n")
    if gamer =='':
        print('이름을 입력하지 않았습니다.')
        continue
    else:
        print(gamer)
        break
AI_num = random.randint(0,99)
i='0'
while True:
    num = input("숫자를 하나 입력하세요 (0~99까지).\n")
    if not num:
        print("숫자를 입력하지 않으셨습니다. 다시 입력하세요")
        continue
    elif num.isnumeric()==False :
        print("숫자가 아닙니다.다시 입력하세요.")
        continue
    elif int(num)<0 or int(num)>99:
        print("숫자의 범위는0~99입니다. 다시 입력하세요")
        continue
    else:
        if AI_num == int(num):    
            i=(10-int(i))*10
            print("축하합니다.\n 점수: "+str(i))
            while True:
                y=input("계속 하시겠습니까?(yes,no 입력)\n")

                if y=='yes' or y=='YES':
                    AI_num=random.randint(0,99)
                    i=0
                    break
                elif y=='no' or y=='NO':
                    break;
                elif not y:
                    print("'yes'나'no'의 값을 입력하세요.")
                else:
                    print("입려값이 틀렸습니다.'yes'나'no'의 값을 입력하세요.")
            continue
        elif AI_num <int(num):   
            print("정답보다 큽니다")
            i=int(i)+1
            continue
        else:
            print("정답보다 작습니다")
            i=int(i)+1
            continue

