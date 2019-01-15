# 환경 변수를 class로 정의한다
# 방법은 맴버변수로 지정하면된다
# 여기서는 디비 접속 주소만 다르게 하고 나머지는 모두 동일하게 
# 테스트(개발), 상용의 정보를 동일하게 가겠다(설정)
class DBConfig:
    '''
    맴버변수
    '''
    DB_TEST_URL =  '127.0.0.1' # 디비 IP 
    DB_REAL_URL =  'pythondb.ch7clkfgazvf.ap-northeast-2.rds.amazonaws.com'          # 디비 IP 
    DB_PORT     =  3306        # 디비 포트
    DB_USER     =  'root'      # 사용자 계정 (원래 root 사용 않함)
    DB_PASSWORD =  '12341234'  # 사용자 비번
    DB_DATABASE =  'python_db' # 데이터베이스명
    DB_CHARSET  =  'utf8'      # 문자셋
    MAX_POOL    =  100         # 디비 커넥션 최대수(만약 풀링기법을 사용하면)
