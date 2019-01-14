# 주소 : ~/users/..
# ~/users/login, ~/users/logout, ~/users/signup
# app라는 실체가 바뀌면(블루프린트로) 주소의 시작방식이 변경이된다
from service.controller import bp_users as app
from service.model import db_session
from service.model import dao
from service.model.member import Member

# 세션 없이 갈수 있는 유일한 페이지(가정)
# ~/users/login
@app.route('/login')
def login():
    print( '로그인;', db_session.loginSql('m', '1') )
    return "users 홈"

# ~/users/logout
@app.route('/logout')
def logout():
    return "users logout"

# ~/users/signup
@app.route('/signup')
def signup():
    # 회원가입
    newUser = Member('multi','1234')
    dao.add( newUser )
    dao.commit()
    return "users signup"