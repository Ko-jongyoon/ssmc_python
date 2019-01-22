###################################################################
# 쿼리 + 풀링
from flask_ex.service.model.dbMgr import DBHelper

db_session = None
# 오직 1회만 호출되고, 디비 커넥션도 총 100개의 세션을 단 한번 세트로 구성
def initDBHelper( app ):
    global db_session
    db_session = DBHelper( app )    

###################################################################
# ORM 방식
# pip install sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# 테이블 한개당 class 한개와 연결하는 
# row데이터 한개와 class 객체 한개를 연결하는 과정
# 이런 방식이 ORM 방식이다 => sql을 몰라도 디비 처리 가능 
# 내가 작성한 패턴이나 함수가 => sql로 변환되서 처리된다
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# Base를 상속받은 클레스가 테이블 하나와 매칭된다

# 디비 세션 (향후 디비 사용시 dao만 가져오면 된다)
dao = None
# 디비 관리자
class DBManager:
    # 맴버변수
    __engine  = None
    __session = None
    # 정적함수 (static function)
    # app => Flask 객체
    @staticmethod
    def init( app ):
        # 디비에 접속 URL 구성
        db_url = 'mysql+pymysql://%s:%s@%s/%s?charset=%s' % (
            app.config.get('DB_USER'),
            app.config.get('DB_PASSWORD'),
            app.config.get('DB_REAL_URL')  
            if app.config.get('SERVER_RUN_MODE_IS_REAL') else
            app.config.get('DB_TEST_URL'),
            app.config.get('DB_DATABASE'),
            app.config.get('DB_CHARSET')
        )
        # 엔진생성 가져와서 그냥 쓰면된다
        DBManager.__engine  = create_engine( db_url, echo=True)
        # 세션생성
        DBManager.__session = scoped_session( sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=DBManager.__engine
        ) ) 
        # 글로벌 적용을 통한 다른곳에서 사용가능하게 처리
        global dao
        dao = DBManager.__session

    @staticmethod
    def init_db():
        from flask_ex.service.model import member
        # 테이블이 없으면 만들어서 처리
        Base.metadata.create_all( bind=DBManager.__engine )



 