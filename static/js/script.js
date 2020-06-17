var angry = false;
var disgust = false;
var scared = false;
var happy = false;
var sad = false;
var surprised = false;
var neutral= false;

$(document).ready(function(){
  setInterval(function () {
    $.ajax({
        type : "GET", //전송방식을 지정한다 (POST,GET)
        url : "http://localhost:7777/result",//호출 URL을 설정한다. GET방식일경우 뒤에 파라티터를 붙여서 사용해도된다.
        dataType : "html",//호출한 페이지의 형식이다. xml,json,html,text등의 여러 방식을 사용할 수 있다.
        error : function(){
            
        },
        success : function(Parse_data){
           
          var result = Parse_data.split(',');
          
          if(result[0] == 'angry') {
            $(".big_emotion").text("화가 난다!!");
            if(angry == false) {
              $(".angry-img").trigger("click");
              angry = true;
              disgust = false;
              scared = false;
              happy = false;
              sad = false;
              surprised = false;
              neutral= false;
            }
            
          }
          else if(result[0] == 'disgust') {
            $(".big_emotion").text("역겨워!!");
            if(disgust == false) {
              $(".disgust-img").trigger("click");
              angry = false;
              disgust = true;
              scared = false;
              happy = false;
              sad = false;
              surprised = false;
              neutral = false;
            }
            
          }
          else if(result[0] == 'scared') {
            $(".big_emotion").text("무서워...");
            if(scared == false) {
              $(".scared-img").trigger("click");
              angry = false;
              disgust = false;
              scared = true;
              happy = false;
              sad = false;
              surprised = false;
              neutral = false;
            }
          } 
          else if(result[0] == 'happy') {
            $(".big_emotion").text("행복해~");
            if(happy == false) {
              $(".happy-img").trigger("click");
              angry = false;
              disgust = false;
              scared = false;
              happy = true;
              sad = false;
              surprised = false;
              neutral = false;
            }
          }
          else if(result[0] == 'sad') {
            $(".big_emotion").text("슬퍼 ㅜㅜㅜ");
            if(sad == false) {
              $(".sad-img").trigger("click");
              angry = false;
              disgust = false;
              scared = false;
              happy = false;
              sad = true;
              surprised = false;
              neutral = false;
            }
          }
          else if(result[0] == 'surprised') {
            $(".surprised_emotion").text("깜짝이야~");
            if(disgust == false) {
              $(".surprised-img").trigger("click");
              angry = false;
              disgust = false;
              scared = false;
              happy = false;
              sad = false;
              surprised = true;
              neutral = false;
            }
          } 
          else if(result[0] == 'neutral') {
            $(".big_emotion").text("내 평상시 표정이야~");
            if(neutral == false) {
              $(".neutral-img").trigger("click");
              angry = false;
              disgust = false;
              scared = false;
              happy = false;
              sad = false;
              surprised = false;
              neutral = true;
            }
          }

          $(".angry-rate").text(result[1] + '%');
          $(".disgust-rate").text(result[2] + '%');
          $(".scared-rate").text(result[3] + '%');
          $(".happy-rate").text(result[4] + '%');
          $(".sad-rate").text(result[5] + '%');
          $(".surprised-rate").text(result[6] + '%');
          $(".neutral-rate").text(result[7] + '%');
        }
    });
}, 1000);

  $('.angry-img').on('click', function(){
    $('.emotion__img').animate({width:"50px", height:"50px"},500);
    $('.angry-img').animate({width:"100px", height:"100px"},1000);
  })

  $('.disgust-img').on('click', function(){
    $('.emotion__img').animate({width:"50px", height:"50px"},500);
    $('.disgust-img').animate({width:"100px", height:"100px"},1000);
  })

  $('.angry-img').on('click', function(){
    $('.emotion__img').animate({width:"50px", height:"50px"},500);
    $('.angry-img').animate({width:"100px", height:"100px"},1000);
  })

  $('.scared-img').on('click', function(){
    $('.emotion__img').animate({width:"50px", height:"50px"},500);
    $('.scared-img').animate({width:"100px", height:"100px"},1000);
  })

  $('.happy-img').on('click', function(){
    $('.emotion__img').animate({width:"50px", height:"50px"},500);
    $('.happy-img').animate({width:"100px", height:"100px"},1000);
  })

  $('.sad-img').on('click', function(){
    $('.emotion__img').animate({width:"50px", height:"50px"},500);
    $('.sad-img').animate({width:"100px", height:"100px"},1000);
  })

  $('.surprised-img').on('click', function(){
    $('.emotion__img').animate({width:"50px", height:"50px"},500);
    $('.surprised-img').animate({width:"100px", height:"100px"},1000);
  })

  $('.neutral-img').on('click', function(){
    $('.emotion__img').animate({width:"50px", height:"50px"},500);
    $('.neutral-img').animate({width:"100px", height:"100px"},1000);
  })
});