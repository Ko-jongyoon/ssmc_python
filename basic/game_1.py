game_jump = False
if game_jump:
    '''
    step 1 : 3분
    "게임의 제목을 입력하세오" 프럼프트 출력 
    "적당한 제목(영문)" 입력하면 다음 단계 진행
    '''
    # # "게임의 제목을 입력하세오" 프럼프트 출력 
    # print( "게임의 제목을 입력하세오" )
    # # "적당한 제목(영문)" 입력하면 다음 단계 진행
    # game_title = input()
    # print( game_title )
    # \n : 줄바꿈
    #game_title = input("게임의 제목을 28자이내로 입력하세요\n")

    ''' 
    step 1-1 : 게임 제목은 28자이내로 입력 받는다 (10분)
    입력하지 않으면 "게임 제목이 입력되지 않았습니다. 다시 입력하세요"
    넘으면 "게임 제목이 28자를 초과합니다 다시 입력하세요"
    28자 이내면 ok
    '''
    while True:# 무한루프 -> break를 사용해야함
        game_title = input("게임의 제목을 28자이내로 입력하세요\n")
        if not game_title: # 입력하지 않으면
        # if len(game_title) == 0:
            print('게임 제목이 입력되지 않았습니다. 다시 입력하세요')
        elif len(game_title)>28:# 28자를 초과
            print('게임 제목이 28자를 초과합니다 다시 입력하세요')
        else:# 1글자 이상 28자 이내면 ok
            break

    ''' 
    step 1-1 : 게임 제목은 28자이내로 입력 받는다 (10분)
    입력하지 않거나(or) 28자가 넘으면 "게임 입력이 부정확합니다."
    28자 이내면 ok
    '''
    # while True:
    #     game_title = input("게임의 제목을 28자이내로 입력하세요\n")
    #     if not game_title or len(game_title)>28:
    #         print('게임 입력이 부정확합니다.')
    #     else:
    #         break


    '''
    step 2 : 10분, =는 한줄에 30개, 글자는 총 몇개 가능? 28자가능
    ==============================
    =     게임제목(중앙정렬)      =
    =        v 1.0.0             =
    ==============================
    이렇게 출력
    '''
    # TITLE_LEN = 50
    # print( '='*TITLE_LEN )
    # txt = '={0:^%s}=' % (TITLE_LEN-2)
    # print( txt.format(game_title) )
    # print( txt.format('v 1.0.0') )
    # print( '='*TITLE_LEN )

    TITLE_LEN = 50
    print( '='*TITLE_LEN )

    txt  = '={0:^%s}=' % (TITLE_LEN-2)
    data = [game_title, 'v 1.0.0', 'thanks K,K,S'] 
    for t in data:
        print( txt.format(t) )

    print( '='*TITLE_LEN )

    '''
    step 3 (3분)
    게이머의 이름을 입력하세요?
    -> 이름을 넣지 않으면 "모라 하고" 다시 입력
    '''
    # flag = True
    # while flag:
    #     gamer_name = input('게이머의 이름을 입력하세요?\n')
    #     if not gamer_name:
    #         print('이름을 정확하게 넣으세요')
    #     else:
    #         flag = False


    flag = True
    while flag:
        gamer_name = input('게이머의 이름을 입력하세요?\n')
        if not gamer_name:
            print('이름을 정확하게 넣으세요')
            continue
        flag = False
    #################################################
    game_info = '''
    게임 제목 : %s
    플레이어 이름 : %s
    ''' % (  game_title, gamer_name )
    print( game_info )

# 개발 시간 단축을 위해 해당 변수값을 미리 세팅하여 여기서부터
# 시작 
game_title = 'number match game'
gamer_name = 'multi'
#########################################################
'''
step 4
AI의 숫자를 입력하세요?
-> 숫자를 않넣으면 "경고 메세지" 다시 입력
-> 숫자가 아닌 값을 넣으면 "경고 메세지" 다시 입력
   isnumeric()으로 체크
-> 0보다 작거나(or), 100 이상을 입력하면 "경고 메세지" 다시 입력
-> 정상 범위에 정수값을 입력하면 다음 단계 진행
'''
# 게임 시도 횟수를 저장하는 변수
game_on = True
while game_on:#온전한 게임 1회를 반복하는 구간
    # G1. 게임 변수 초기화
    ai_value  = None
    try_count = 0
    while True: # 사용자가 ai값을 맞출때까지 반복
        # 사용자가 숫자를 입력하는 반복
        
        # G2.게임중
        while True:
            # 공백제거를 해서 오동작을 미연에 방지
            # '1 ', ' 1'
            gamer_input = input('AI의 숫자(0~99)를 입력하세요?\n').strip()
            if not gamer_input:# 숫자를 않넣으면
                print('입력을 정확하게 하세요')
            elif not gamer_input.isnumeric():# 숫자가 아닌 값을 넣으면
                print('0~99사이의 정수값만 입력하세요')
            else: 
                tmp = int( gamer_input )
                #if tmp>=0 and 100<tmp:
                #if 0<=tmp and tmp<100:
                if tmp>=0 and tmp<100:
                    gamer_input = tmp
                    break
                print( '정상 범위에 정수값을 입력하세요' )
        print('한번 시도 했다')
        #try_count = try_count + 1
        try_count += 1
        # break는 가장 가까운 반복문을 빠져나간다
        
        '''
        step 5
        AI는 숫자를 하나 생성한다(랜덤) -> 1회만 생성되야함
        즉 게임 한번이 종료될때까지 유지되어야 한다
        '''
        # 모듈 가져오기 (다름 사람이 만든 라이브러리 이해)
        # 파이썬은 모듈, 패키지 밖에 없다
        import random
        if not ai_value:# ai값이 세팅되어 있지 않았다면
            # 세팅해라
            ai_value = random.randint(0,99)

        '''
        step 6
        판단
        1) 입력값이 정답보다 작으면 => 작다고 코멘트 => 사용자 재입력
        2) 입력값이 정답보다 크면   => 크다고 코멘트 => 사용자 재입력
        3) 입력값이 정답과 동일하면 => 축하메시지를 뿌려준다 => step7
        '''

        if gamer_input < ai_value:
            print('입력값이 작습니다.')
        elif gamer_input > ai_value:
            print('입력값이 큽니다.')
        else:
            print('정답입니다.')
            break
    # G3. 게임 엔딩 처리
    '''
        step 7 : 정답이후 처리 내용
        결과 표시
        총 시도 횟수 표시
        점수=(10-총시도회수)*10 를 표시
        다시 게임을 하시겠습니까?
        YES(대소문자구분않함) => 다시 게임 시작(step4부터 진행)
        NO(대소문자구분않함)  => 게임 종료 => 프로그램 종료
        아무것도 않넣고 엔터 => 경고 메시지 
        입력값이 틀려도 경고 
    '''
    prompt = '''

    총 시도 횟수 : %s
    점수 : %s
    다시 게임을 하시겠습니까?(YES/NO)

    ''' % ( try_count, (10-try_count)*10 )
    while True:
        result = input( prompt ).strip().upper()
        
        if  result == 'NO':            
            print('gamer_name' + 'Bye Bye!') 
            game_on = False
            break            
        elif result == 'YES':  
            print('YES') 
            break
        else:
            print('YES or NO 중에 하나를 입력하세요') 
