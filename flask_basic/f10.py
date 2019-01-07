# f8을 개선
# 로그인시 아이디와 비번이 주소창에 노출되는 부분 개선 
# ->get, post 방식으로 변경
# /login, /logonproc를 는 이어진 작업이으모로 하나의 주소 /login으로 통합처리
# -> restful(이런 처리방식에 대한 용어) 방식 처리
# render_template :jinja2 라는 템플릿 엔진을 연동
# jinja2는 html에 변수나 연산등을 넣어서 동적으로 페이지를 구성할 수 있는 엔진
'''
request: get,post 등의 메소드 방식으로 데이터가 전달시 데이터가 들어오는 객체
render_template: html을 읽어서 랜더링하여 브라우저로 전송하는 텍스트 구성
redirect: 요청을 다른쪽으로 던져주는 역할
url_for: 함수명을 통해서 라우트된 주소를 반환 하는 함수
'''

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world3'

# get방식과 post방식을 모두 허용하는 라우트 정의
@app.route('/login',methods=['GET','POST'])
def login():
    if  request.method == 'GET':
        # GET
        return render_template('login2.html')
    else:
        # POST
        # 1. 아이디 비번 획득
        uid = request.form.get('uid')
        upw = request.form['upw']
        # 1-1. 값이 누락이 있으면 경고후 되돌린다
        # 아이디나 비번이 없는 경우 -> not or
        if not uid or not upw:
            return render_template('error.html', msg='비정상접근')
        print(uid, upw)
        # 2. 우리 회원인지 조회 (차후 디비 조회)
        if uid =='m' and upw=='1':
            # 3. 회원이면 서비스로 이동
            # 3-1 세션생성
            # 3-2 페이지 이동(요청을 포워딩)
            return redirect(url_for('main') )
        else:
            # 4. 회원아니면 경고수 페이지를 되돌린다
            return render_template('error.html',msg='아이디 비번확인 요청')
@app.route('/main')
def main(): 
    return "서비스2"
if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    