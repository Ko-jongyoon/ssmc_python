# 파이썬의 3항 연산자는 없어서 비슷하게 만드는게 3항식
# 파이썬의 3항 연산자는 조건문 ? 값: 값;
# cur나 rate면 ""아니면 disabled

key = 'cur'
result='' if key == 'cur' or key =='rate' else "disabled"
print(result)
