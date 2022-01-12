
$(document).ready(function(){
  $("#demo").on("hide.bs.collapse", function(){
    $(".btn1").html('<label class="glyphicon glyphicon-collapse-down">ETKİNLİK</label>');
    demo.style.display = "none";
    if (demo2.style.display == "none") {
      document.getElementById("buton1").style.marginLeft = "0px";
      document.getElementById("buton2").style.marginLeft = "0px";
    }   
  });

  $("#demo").on("show.bs.collapse", function(){
    $(".btn1").html('<label class="glyphicon glyphicon-collapse-up">ETKİNLİK</label>');
    $(".btn2").html('<label class="glyphicon glyphicon-collapse-down">HABER</label>');
    demo.style.display = "block";
      demo2.style.display = "none";
      document.getElementById("buton1").style.marginLeft = "250px";
      document.getElementById("buton2").style.marginLeft = "250px";
      
  });

  $("#demo2").on("hide.bs.collapse", function(){
    $(".btn2").html('<label class="glyphicon glyphicon-collapse-down">HABER</label>');
    demo2.style.display = "none";
    if (demo.style.display == "none") {
      document.getElementById("buton1").style.marginLeft = "0px";
      document.getElementById("buton2").style.marginLeft = "0px";
    }   
  });
  $("#demo2").on("show.bs.collapse", function(){
    $(".btn2").html('<label class="glyphicon glyphicon-collapse-up">HABER</label>');
    $(".btn1").html('<label class="glyphicon glyphicon-collapse-down">ETKİNLİK</label>');
    demo.style.display = "none";
    demo2.style.display = "block";
    document.getElementById("buton1").style.marginLeft = "250px";
    document.getElementById("buton2").style.marginLeft = "250px";
    
  });
    
});