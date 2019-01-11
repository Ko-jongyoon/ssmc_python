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
import os
app = Flask(__name__)
app.secret_key= 'qweasdzxc'

# 세션 생성, 해제, 체크
config= {
    'site_title':'점심 메뉴 단가 분석',
    'menu1':'Today`s 코스닥 150',
    'login':'로그인',
    'menu2':'파일업로드'
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
# 파일 업로드
@app.route('/uploadPhoto', methods=['GET','POST'])
def uploadPhoto():
    if request.method =='GET':
        rows =selectFildeData()
        return render_template('sub/uploadPhoto.html', config=config ,
                                                    items= rows)
    else:
        # 딕셔너리 구조로
        # 디비에 들어갈 데이터를 준비
        dic = dict()      
        
        # 전달된 데이터를 콘솔에 출력한다( 작성자 아이디 포함 )
        print( request.form['title'] )
        print( request.form['content'] )
        print( session['user_id'] )
        # 파일 저장 처리
        # 파일 1개 보냈을때
        # f = request.files['fileData']
        # print (type(f), f)
        # 파일을 n개 multiple일 경우
        tmp = list()
        for f in request.files.getlist('fileData'):
            # 2.파일 저장 처리
            print ( type(f), f.filename)
            # 윈도우던, 리눅스던 경로가 알아서 적용되게 구현해야 한다
            # 어디다가 저장할것인가? => 정적 url을 제공하는 위치
            # ~/static/upload
            # 사용자별로 구분 -> 아이디를 폴더로 or 파일명에 아이디를붙이기
            # 동일 파일 구분 -> 사건을 추가 
            # 궁극적인 해결방안 => 중복되지않는 해시값(32바이트)으로 이름변경
            path = os.path.join(os.getcwd(), 'static','upload', f.filename)
            # 디스크상 저장 위치
            #'C:\Users\rhwhd\Desktop\github\ssmc_python\flask_advance\static\upload\coffea.jpg
            # 웹경로상
            # http://127.0.0.1:5000/static/upload/coffea.jpg
            # 저장 위치는 무조건 ~/static/upload/ 고정이다
            # 그렇다면 저장은 파일명만
            # a.jpg[b.jpg]c.jpg.....
            print ( path )
            f.save(path);
            # 파일명 추가
            tmp.append(f.filename)
            # 디비에 입력된 파일 정보를 출력하시오
            # 어떤 정보만 디비에 들어가면 되는지 고민해서 출력
        dic['title'] =request.form['title']
        dic['content'] =request.form['content']
        dic['author'] =session['user_id']
        dic['files']  = '|'.join(tmp)
        print(dic)
        '''
        {'title:'1',
         'content':'2',
         'author': 'm',
         'files:'coffea.jpg|summer.jpg|summer2.jpg|summer3.jpg
        }
        '''
        # 3.디비 입력 처리
        result = insertFileData( dic )
        if result:
            # 3-1. 성공이면 저장되었습니다. -> 리스트로 이동
            return render_template('error.html', msg='등록성공',url=url_for('uploadPhoto') )
        else:
            # 3-2. 실패면 실패했습니다 -> 돌아가기
            return render_template('error.html', msg='등록실패')


if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    