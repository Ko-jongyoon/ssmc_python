# ./templates : html 파일들이 위치하는 곳
# ./static    : 리소스파일들이 위치하는 곳 (js, css ,img, ...)
# static 밑에 있는 모든 리소스는
# http://localhost/static/리소스명 이렇게 직접 적근 가능
# 즉, 라우팅 할 필요가 없다 무조건 웹경로로 인식한다
'''
1. 이미 작성된 템플릿을 입히기
2. 템플릿 쪽개서 조합하기 
3. 파일 업로드
4. 세션, 쿠키 처리 (로그인 업그레이드)
'''
# 세션: 클라이언트 정보를 서버가 유지하거나 보관하고 있다
# 단 서버가 들고 있으면 리소스 부족해지거나 성능 저하를 가져올 수 있다
# 실습할때는 서버 메모리에 들고 있을것이고, 서비스 할때는
# 디비나, 서드파트 솔류션을 이용하여 처리한다.
from flask import Flask, render_template ,url_for, request, redirect, session, jsonify
from db.sql import *
app = Flask(__name__)
app.secret_key= 'qweasdzxc'

# 세션 생성, 해제, 체크
config= {
    'site_title':'점심 메뉴 단가 분석',
    'menu1':'Today`s 코스닥 150',
    'login':'로그인'
}
@app.route('/')
def home():
    # 세션이 없으면 로그인으로
    if not 'user_id' in session:
        return redirect( url_for( 'login' ) )
    return render_template('index.html', config =config)

@app.route('/search', methods=['POST'])
def search():
    # 검색어 획득
    keyword = request.form['keyword']
    # 검색 쿼리 수행
    rows    = selectStockByKeyword( keyword )    
    if rows:
        # 성공:검색 결과를 json 형식으로 응답
        return jsonify( rows )
    else:
        # 실패:검색 결과가 없으면 json의 다른 형태로 ㅍ응답
        return jsonify( [] )
        
@app.route('/logout')
def logout():
    # 세션 제거
    if 'user_id' in session:
        session.pop('user_id',None)
    if 'user_nm' in session:   
        session.pop('user_nm',None)
    # 홈페이지 이동
    return redirect(url_for('logout'))

# get방식과 post방식을 모두 허용하는 라우트 정의
@app.route('/login',methods=['GET','POST'])
def login():
    if  request.method == 'GET':
        # GET
        return render_template('login.html', config =config)
    else:  
         uid = request.form['uid']
         upw = request.form['upw']
         row = loginSql(uid,upw)
         if row:
             # 세션생성
             session['user_id']= uid
             session['user_nm']= row['name']
             # 홈페이지로 이동    
             return redirect(url_for('home') )
         else:
            return render_template('error.html', msg='아이디 비번확인 요청')

@app.route('/tradeList')
def tradeList():
    return render_template('sub/tradeList.html', config=config, 
                                                trades=selectTradeData())
if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    