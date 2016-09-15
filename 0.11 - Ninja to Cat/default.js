$(document).ready(function() {
      var imgSrc; 
      var temp; 
      $(".puzzle").click(function() {
            imgSrc = $(this).css("background-image"); 
                  if (imgSrc !== $(".dummy-1").css("background-image")) {
                        temp = $(".dummy-1").css("background-image"); 
                        $(this).css("background-image", temp); 
                  }
                  if (imgSrc !== $(".dummy-2").css("background-image")) {
                        temp = $(".dummy-2").css("background-image"); 
                        $(this).css("background-image", temp); 
                  }
            }
      ); 
});