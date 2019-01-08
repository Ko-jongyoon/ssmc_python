# 홈페이지를 요청하면 주식 종목 리스트 종목코드 오름차순 정렬하여 상위10개 뿌린다
# 뿌려지는 내용은 코드, 이름, 현재가, 상한가, 최저가 이다
# step1 디비에서 위에 언급된 데이터를 가져오는 selectTradeData 함수 d7에구현
# step2 selectTradeData은 모듈 가져오기로 처리
# step3 trade.html 파일을 생성해서 해당 데이터를 출력할 수 있는 html 구성  
#          컬러명: 코드 : 이름 : 현재가 : 상한가 : 최저가
# step4 ~/ 요청하면 해당내용이 작동하여 브라우저에 주식 목록이 나타난다
# step5 검색창을 상단에 붙이고, 
#       ajax 통신을 이용(JS사용)하여 검색어에 해당되는
#       종목 리스트를 구해서(SQL)-> 브라우저로 전송하면(JSON 방식전송)
#       동적으로 화면(DOM) 뿌린다
#       ajax : 화면이 껌뻑이지 않고 뒷단(백그라운드)에서 통신을 진행하는 기술
from flask import Flask, render_template
from d7 import selectTradeData
                             
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('trade.html', trades=selectTradeData())

if __name__ == '__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
    