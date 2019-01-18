#!/usr/bin/env python
# coding: utf-8

# In[17]:


from urllib.request import urlopen, Request


# In[18]:


import urllib


# In[19]:


# kakao REST API 키
KAKAO_REST_API_KEY = 'd99f329dfcdb238f998f101230a64885'
URL_BASE = 'https://dapi.kakao.com/v2/search/web'
# 한글을 웹으로 전송시 인코딩 처리한다
# '문자열'.encode("utf-8")
PARAMS = 'query=%s&page=1&size=50' % urllib.parse.quote('서가대')
HEADER = 'KakaoAK %s' % KAKAO_REST_API_KEY
PARAMS


# In[20]:


# 헤더 설정
url = '%s?%s' % (URL_BASE, PARAMS)
url


# In[21]:


request = Request(url)


# In[22]:


request.add_header("Authorization", HEADER)


# ### http 요청
# - 테스트

# In[38]:


response = urlopen( request )


# In[39]:


# 응답 결과를 json으로 파싱
import json


# In[40]:


tmp = json.load( response )
tmp


# ### 데이터 추출

# In[41]:


tmp['documents'][0]['title']


# In[42]:


tmp['documents'][0].keys()


# In[43]:


for i in range( len(tmp['documents']) ):
    # 데이터 전처리 : <b>, </b> 제거
    print( tmp['documents'][i]['title'].replace('<b>','').replace('</b>','') )


# ### 수집한 데이터를 DataFrame으로 변환
# 
# * 파이썬의 자료구조(핵심데이터)를 pandas의 DaraFrame으로 변환
# * DataFrame을 db으로 전송해야 마무리 

# ### 데이터 적제
# - 데이터 베이스에 데이터를 넣는다
# * pandas를 이용하면 데이터를 덩어리채로 넣을 수있다
# - 일단 여기서는 pymysql을 이용하여 데이터를 적제하겟다
# > 콘다 프럼프트 오프  
# > **pip install pymysql**  
# > 콘다 미설치자분들  
# > **pip install sqlalchemy**   
# > **pip install pandas**   

# In[51]:


import pymysql
from sqlalchemy import create_engine
import pandas as pd
import pandas.io.sql as pSql


# In[53]:


# tmp['documents']:dict -> DataFrame 변환
df_dict = pd.DataFrame.from_dict( tmp['documents'] )
df_dict.head(2)


# In[48]:


# 연결
db_url = 'mysql+pymysql://root:12341234@127.0.0.1/python_db'
engine = create_engine( db_url, encoding='utf8')


# In[49]:


# 실연결
conn = engine.connect()


# In[50]:


# 수집한 내용을 디비에 삽입
# 테이블명, 연결세션, 중복되면추가, 인덱스열은 미삽입
df_dict.to_sql(name='seoul', con=conn, 
               if_exists='append', index=False)


# In[45]:


# 데이터 가져오기
df = pSql.read_sql('select * from tbl_trade', conn)
df


# In[32]:


# 해제
conn.close()


# In[ ]:




