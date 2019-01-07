# Flask 내에서 구성하는 모든 페이지내에 주소를 참조하거나
# 사용시 직접적으로 주소를(URL)을 기입하지않는다
# redirect('/main') => x
# => url_for('기술하고자 하는 주소와 라우팅된 함수명')함수를 사용
# 일반 주소, 동적파라미터 스타일, 
# 리소스(css, js, 이미지등등 참조하는 주소)단 주소등의 형태가 존재
# 나머지 스타일은 뒤에서 확인!!
from flask import Flask, url_for, redirect

app = Flask(__name__)

# 홈페이지
@app.route('/')
def home():
    # 홈페이지를 진입하면 바로 메인페이지로 이동한다
    # return redirect('/main')
    # 함수명을 통해 연결된 주소를 획득한다-> 함수명은 고유할테니까
      return redirect( url_for('main') )

# 메인페이지
# 주소가 변경이 되도 함수명으로 참조되었기 때문에 유지보수 측면에서는
# 최소의 수정만 발생되고, 전체적으로 운영에는 관계 없다
@app.route('/main')
def main(): 
    return "서비스2"

if __name__ == '__main__':
    app.run(debug=True)
    