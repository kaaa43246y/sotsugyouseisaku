$(function(){

  // 使用例をclick時にポップアップ画像表示
  $("#popup1").click(function(){
    $("#popup1_modal").fadeIn();
  });

  $("#popup2").click(function(){
    $("#popup2_modal").fadeIn();
  });

  $("#popup3").click(function(){
    $("#popup3_modal").fadeIn();
  });

  $("#popup4").click(function(){
    $("#popup4_modal").fadeIn();
  });

  $("#popup5").click(function(){
    $("#popup5_modal").fadeIn();
  });

  $("#popup101").click(function(){
    $("#popup101_modal").fadeIn();
  });

  $("#popup102").click(function(){
    $("#popup102_modal").fadeIn();
  });

  $("#popup103").click(function(){
    $("#popup103_modal").fadeIn();
  });

  $("#popup104").click(function(){
    $("#popup104_modal").fadeIn();
  });

  $("#popup105").click(function(){
    $("#popup105_modal").fadeIn();
  });

  $("#popup201").click(function(){
    $("#popup201_modal").fadeIn();
  });

  $("#popup202").click(function(){
    $("#popup202_modal").fadeIn();
  });

  $("#popup203").click(function(){
    $("#popup203_modal").fadeIn();
  });

  $("#popup204").click(function(){
    $("#popup204_modal").fadeIn();
  });

  $("#popup205").click(function(){
    $("#popup205_modal").fadeIn();
  });

  $("#popup301").click(function(){
    $("#popup301_modal").fadeIn();
  });

  $("#popup302").click(function(){
    $("#popup302_modal").fadeIn();
  });

  $("#popup303").click(function(){
    $("#popup303_modal").fadeIn();
  });

  $("#popup304").click(function(){
    $("#popup304_modal").fadeIn();
  });

  $("#popup305").click(function(){
    $("#popup305_modal").fadeIn();
  });



  // 画像を閉じる
  $(".close-btn").click(function(){
    $("#popup1_modal").fadeOut();
    $("#popup2_modal").fadeOut();
    $("#popup3_modal").fadeOut();
    $("#popup4_modal").fadeOut();
    $("#popup5_modal").fadeOut();
    $("#popup101_modal").fadeOut();
    $("#popup102_modal").fadeOut();
    $("#popup103_modal").fadeOut();
    $("#popup104_modal").fadeOut();
    $("#popup105_modal").fadeOut();
    $("#popup201_modal").fadeOut();
    $("#popup202_modal").fadeOut();
    $("#popup203_modal").fadeOut();
    $("#popup204_modal").fadeOut();
    $("#popup205_modal").fadeOut();
    $("#popup301_modal").fadeOut();
    $("#popup302_modal").fadeOut();
    $("#popup303_modal").fadeOut();
    $("#popup304_modal").fadeOut();
    $("#popup305_modal").fadeOut();

  });
  
  $(".black-background").click(function(){
    $("#popup1_modal").fadeOut();
    $("#popup2_modal").fadeOut();
    $("#popup3_modal").fadeOut();
    $("#popup4_modal").fadeOut();
    $("#popup5_modal").fadeOut();
    $("#popup101_modal").fadeOut();
    $("#popup102_modal").fadeOut();
    $("#popup103_modal").fadeOut();
    $("#popup104_modal").fadeOut();
    $("#popup105_modal").fadeOut();
    $("#popup201_modal").fadeOut();
    $("#popup202_modal").fadeOut();
    $("#popup203_modal").fadeOut();
    $("#popup204_modal").fadeOut();
    $("#popup205_modal").fadeOut();
    $("#popup301_modal").fadeOut();
    $("#popup302_modal").fadeOut();
    $("#popup303_modal").fadeOut();
    $("#popup304_modal").fadeOut();
    $("#popup305_modal").fadeOut();
  });

  
  //入力されたキーを保存する
  var inputKey = [];

  //入力されたキーと比較する隠しコマンド
  //38 = 上
  //40 = 下
  //37 = 左
  //39 = 右
  //66 = B
  //65 = A
  var konamiCommand = [38,38,40,40,37,39,37,39,66,65];

 //画面上のキー入力イベントリスナ
 $(window).keyup(function(e) {
   //キー入力を配列に追加
   inputKey.push(e.keyCode);

   //キー入力が保存された配列と隠しコマンドを比較
   if (inputKey.toString().indexOf(konamiCommand) >= 0) {

      //隠しコマンド成功時の何らかの処理
      window.open('/edit', '_blank')
      //キー入力を初期化
      inputKey = [];
   }
 });

});