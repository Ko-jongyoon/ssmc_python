console.log('자바스크립트 연습');
// 변수 : 변수의 타입은 값이 할당될 때 결정된다. 타입추론(파이썬, js, 스칼라...)
var name  = "hi";
var name2 = "hi";
// 상수
const PI = 3.14;
console.log(name, PI, name2);
//###########################################
//조건문, 반복문, 제어문 등등 다 대동소이하다
if(name =='hi'){
    console.log('일치')
}
//###########################################
// 기본 함수
function sum( x,y )
{
    return x+y;
}
// 익명 함수 => 이름이 없다(함수 이름)=> 1화요으 콜백용으로만 단 한번 사용
var sum2 = function ( x,y )
{
    return x+y; 
}
//$(document.read( function(){

//} ));
console.log(sum(1,2));
console.log(sum(1,2));
//###########################################

