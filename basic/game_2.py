'''
game_1.py는 절차적 프로그램이다
좀 더 효율성과 확장성, 재사용성을 높이기 위해
함수 지향적 프로그램으로 마이그레이션(이주) 진행
-> 시작점 존재(시작함수가 존재)
'''
#환경변수
TITLE_MAX_LEN = 100
ai_value  = None
try_count = 0

def main():
    # 게임시작
    game_title = gamestep1_inputGameTitle( TITLE_MAX_LEN )
    print('game_title', game_title)
    gameStep2_displayGameTitle(game_title,50)
    gamerName = gameStep3_InputGamerName()
    #게임
    game_on = True
    while game_on:
        # G1. 게임 변수 초기화
        gameStep4_initGameVariable()
        # G2. 게임중
        gameStep4_playGame()
        # G3. 게임 엔딩 처리
        game_on = gameStep4_Ending(gamerName)

# G1. 게임 변수 초기화
def gameStep4_initGameVariable():
    # global 변수명 -> 전역변수(글로벌 변수) 라는 의미
    # 해당변수가 전역 변수임을 선언
    global ai_value, try_count
    # 사용
    ai_value = None
    try_count = 0
    
# G2. 게임중
def gameStep4_playGame():
    global try_count,ai_value

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
            temp = random.randint(0,99)
            ai_value =temp

        if gamer_input < ai_value:
            print('입력값이 작습니다.')
        elif gamer_input > ai_value:
            print('입력값이 큽니다.')
        else:
            print('정답입니다.')
            break
# G3. 게임 엔딩 처리
def gameStep4_Ending(gamer_name):
    global try_count
    prompt = '''

    총 시도 횟수 : %s
    점수 : %s
    다시 게임을 하시겠습니까?(YES/NO)

    ''' % ( try_count, (10-try_count)*10 )
    game_on = True
    while True:
        result = input( prompt ).strip().upper()
        
        if  result == 'NO':            
            print(gamer_name + 'Bye Bye!') 
            game_on = False
            break            
        elif result == 'YES':  
            print('YES') 
            #game_on = True
            
        else:
            print('YES or NO 중에 하나를 입력하세요') 

# gamer 이름을 입력받는 함수
def gameStep3_InputGamerName():
    flag = True
    while flag:
        gamer_name = input('게이머의 이름을 입력하세요?\n')
        if not gamer_name:
            print('이름을 정확하게 넣으세요')
            continue
        flag = False
    return gamer_name
#게임 제목을 출력하는 함수
def gameStep2_displayGameTitle(game_title, title_len):
    TITLE_LEN = title_len
    print( '='*TITLE_LEN )
    txt  = '={0:^%s}=' % (TITLE_LEN-2)
    data = [game_title, 'v 1.0.0', 'thanks K,K,S'] 
    for t in data:
        print( txt.format(t) )

    print( '='*TITLE_LEN )

# 게임 제목의 길이 제한을 인자로 받아서 확장성을 높였다.
def gamestep1_inputGameTitle( titleLen ):
    while True:# 무한루프 -> break를 사용해야함
        game_title = input("게임의 제목을 %s자이내로 입력하세요\n" % titleLen)
        if not game_title: # 입력하지 않으면
        # if len(game_title) == 0:
            print('게임 제목이 입력되지 않았습니다. 다시 입력하세요')
        elif len(game_title)>titleLen:# 28자를 초과
            print('게임 제목이 %s자를 초과합니다 다시 입력하세요' % titleLen)
        else:# 1글자 이상 28자 이내면 ok
            break
    return game_title

# 이코드(모듈)를 중심으로 구동될때만 main을 호출하고 싶다.
if __name__ == '__main__' :
    main()
