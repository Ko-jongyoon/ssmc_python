import os
# 현재 디렉토리
print( os.getcwd() )
#print( os.path.curdir )
#print( os.path.realpath() )
# 해당 파일이 존재하는지 체크
#print( os.path.exists() )

print( '|'.join(['a.png','b.png','c.png']) )

dic = {'title': '1', 
         'content': '2', 
         'author': 'm',}
print( tuple( dic.values() ) )

tmp = 'Lighthouse.jpg|Penguins.jpg'.split('|')
print( tmp, type(tmp) )

for t in 'Lighthouse.jpg|Penguins.jpg'.split('|'):
    print( "<img src='/static/upload/%s' height='50'/>" % t )

'''
{% for t in item['files'].split('|'): %}
    <img src='/static/upload/{{t}}' height='50'/>
{% endfor %}
'''
# 파일이 이미지가 아닌 경우
# 이미지 => png jpg, jpeg, bmp, gif (미리보기) => 확장자 검사해서 
# 일반파일 => 링크제공(누르면 다운로드)
#           <a href='/static/upload/파일명'><img src='아이콘'/></a>
fName = 'Desrt.jpg'
# .없는 파일은 일단 무시 (테스트상에는 . 포함해서 처리하고 없는경우는 차후 적용)
# 파일의 MIME 타입을 조사하여 image/xxx 로 되는것은 원래 다 이미지이다
# 이것으로 체크하는 것이 본질적인 처리 방식이다.
print (fName.split('.')[-1] )
ext =fName.split('.')[-1]
if ext in 'png, jpg, jpeg, bmp, gif'.split(','):
    print("<img src='/static/upload/%s' height='50'/>" % fName)
else:
    print("<a href='/static/upload/%s'> %s </a>" % (fName,fName) )
'''
jpg
<img src='/static/upload/tea.jpg' height='50'/>
jpg1
<a href='/static/upload/summer.jpg1'> summer.jpg1 </a>

