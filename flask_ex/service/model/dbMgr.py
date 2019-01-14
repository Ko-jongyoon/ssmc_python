'''
- 파이썬에서 디비 접속, 해제
- 쿼리수행 -> Row 쿼리 수행 -> 매번접속,해제를 하기때문에 
  => 풀링(Pooling) 사용으로 속도나 포퍼먼스를 해결
     pip install DBUtils, pip3 install DBUtils
  => 풀링은 특정 수만큼 디비와 연결을 맺어서 보관하고 있고
  => 요청이 들어오면 빌려주고 사용이 끝나면 반납받고 ..
- 쿼리수행 -> ORM 방식 지원
'''
import pymysql as my
from DBUtils.PooledDB import PooledDB

class DBHelper:
    # 디비 연결정보
    app = None
    # 풀링 객체(디비와 커넥션 정보를 가지고 잇는 객체)
    connectionPool = None
    # 생성자
    def __init__(self, app):
        self.app = app
        self.initPool()
    # 소멸자
    def __del__(self):
        self.freePool()
    #########################
    # 커넥션 풀 생성
    def initPool( self ):
        # 아래 코드 수행후 connectionPool 객체는 총 100개(maxconnections수)
        # 디비와 연결 세션을 가지고 있게 된다
        self.connectionPool = PooledDB(
            creator = my,
            # 값1 if 조건문 else 값2
            host = self.app.config.get('DB_REAL_URL')  
                   if self.app.config.get('SERVER_RUN_MODE_IS_REAL') else
                   self.app.config.get('DB_TEST_URL'),
            user = self.app.config.get('DB_USER'),
            password = self.app.config.get('DB_PASSWORD'),
            database = self.app.config.get('DB_DATABASE'),

            charset = self.app.config.get('DB_CHARSET'),
            maxconnections= self.app.config.get('MAX_POOL'),

            autocommit = False,
            blocking=False,
            cursorclass=my.cursors.DictCursor
        )

    # 커넥션 풀 해제
    def freePool(self):
        # 잡아두고 있던 100개의 디비세션을 모두 반납한다
        if self.connectionPool:
            self.connectionPool.close()
    
    # 로그인
    def loginSql( self, uid, upw ):        
        row = None # 로그인 결과를 담는 변수
        connection = None
        try:     
            # 디비 연결 세션 하나 빌림
            connection = self.connectionPool.connection()
            with connection.cursor() as cursor:                
                sql    = "select * from users where uid=%s and upw=%s;"
                cursor.execute( sql, (uid, upw) )
                row    = cursor.fetchone()
        except Exception as e:
            print('->', e)
            row = None
        finally:
            # 연결 세션 반납
            connection.close()
        return row