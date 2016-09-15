$(document).ready(function () {
      $("div.thumbnail").click(function () {
            $(this).fadeOut("slow"); 
      });
      $("a.btn").click(function () {
            $("div.thumbnail").fadeIn("slow");
      }); 
}); 