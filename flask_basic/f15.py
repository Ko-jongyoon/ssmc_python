# 홈페이지를 요청하면 주식 종목 리스트 종목코드 오름차순정렬하여 상위 10개 뿌린다
# 뿌려지는 내용은 코드, 이름, 현재가, 상한가, 최저가 이다
# step1 디비에서 위에 언급된 데이터를 가져오는 selectTradeData 함수 d7에 구현
# step2 selectTradeData은 모듈 가져오기로 처리
# step3 trade.html 파일을 생성해서 해당 데이터를 출력할수 있는 html 구성
#       컬러명 : 코드 : 이름 : 현재가 : 상한가 : 최저가
# step4 ~/ 요청하면 해당내용이 작동하여 브라우저에 주식 목록이 나타난다
# step5 검색창을 상단에 붙이고(HTML), 
#       ajax 통신을 이용(JS사용)하여 검색어에 해당되는
#       종목 리스트를 구해서(SQL) -> 브라우저로 전송하면(JSON 방식전송)
#       동적으로 화면(DOM)에 뿌린다
#       ajax : 화면이 껌벅이지 않고 뒷단(백그라운드)에서 통신을 진행하는 기술
from flask import Flask, render_template, request, jsonify, url_for, redirect
#from d7 import selectTradeData, selectStockByKeyword as ssbk
# 모듈 밑에 모든 함수, 변수, 클레스등등 가져올려면 *를 표시한다
from d7 import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('trade.html', trades=selectTradeData() )

# 검색
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

# 코드별 상세페이지
@app.route('/info/<code>')
def info( code ):
    
    # 코드값이 없으면 백 -> 동적 파라미터 특성상 값이 없으면 404에러
    #if not code:
    #    return render_template('error.html', msg='정보누락')
    ###########################################################
    # 코드값이 존재하면 -> 코드를 기준으로 종목정보 전체 획득
    # 종목 정보를 화면에 표시 (표 형태로 )
    #----------------------------
    #    컬럼      : 값
    #----------------------------
    # 왼쪽에 컬럼명 : 오른쪽에 값
    #----------------------------
    print( "업데이트 여부", request.args.get('update'))
    return render_template('info.html', trade=selectOneStockInfo(code),
                                        update=request.args.get('update') )


# 종목 정보 수정하기
# 수정이 성공하면 -> /info/code 화면으로
# 수정이 실패하면 -> 경고창 -> 되돌아가기
@app.route('/updateStock',methods=['POST'])
def updateStock():
    # 1. 파라미터 획득
    # ImmutableMultiDict([('cur', '3123'), ('rate', '123')])
    # print( request.form )
    # 2. 쿼리수행
    # 3. 수행 결과 판단
    if updateStockInfo(request.form):
       # 수정이 성공하면 ->/info/code 화면으로
       return render_template('error.html', msg="수정완료",
                                url=url_for('info', code=request.form['code']) )
                                #url="/info/"+request.form['code'])
    else:   
       # 수정이 실패하면 -> 경고창 -> 되돌아가기
       return render_template('error.html', msg='수정실패')
    #return "%s" % updateStockInfo( request.form )

#종목 삭제하기
@app.route('/deleteStock')
def deleteStock():
    # 파라미터 획득
    code =request.args.get('code')
    # 삭제 처리
    if deleteStockInfo( code ):
        # 홈페이지로 이동
        return render_template('error.html', msg="삭제완료",
                                url=url_for('home'))
        #return redirect( url_for('home'))
    else:
        return render_template('error.html', msg="삭제실패")


if __name__=='__main__':# 이코드를 메인으로 구동시 서버가동
    app.run(debug=True)
