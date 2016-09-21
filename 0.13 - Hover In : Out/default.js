$(document).ready(function() {
      $("img").hover(function () {
            var imgSrc = $(this).attr("src"); 
            var imgAltSrc = $(this).attr("alt-image"); 
            $(this).attr("src", imgAltSrc);
            $(this).attr("alt-image", imgSrc); 
      }); 
}); 