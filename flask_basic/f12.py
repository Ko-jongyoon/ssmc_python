# @app ~> 데코레이터라고 한다
# 하나의 함수에 여러개의 데코레이터를 연결할 수 있다
from flask import Flask

app = Flask(__name__)

@app.route('/test')
@app.route('/test/<uid>')
def home(uid=None):
    if uid:
        return 'uid %s' %uid
    else:
        return 'test 요청'

if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    