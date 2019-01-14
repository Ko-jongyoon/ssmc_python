# member 테이블과 연계되는 클레스
from service.model import Base
from sqlalchemy import Column, Integer, String
from enum import unique

class Member(Base):
    # 테이블 생성
    # 테이블 명
    __tablename__ = 'member'
    # 컬럼명
    id  = Column(Integer,    primary_key=True )
    uid = Column(String(50), unique=True)
    upw = Column(String(50), unique=False)
    # 생성자
    def __init__(self, uid, upw):
        self.uid = uid
        self.upw = upw
    # 클레스(객체)를 설명하는 함수
    def __repr__(self):
        return "<Member %s %s>" % (self.uid, self.upw)



