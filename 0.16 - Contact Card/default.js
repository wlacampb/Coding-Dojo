$(document).ready(function () {
      
      $("form").submit(function () {
            
            $("h1").css("margin-top", "0px");
            
            $("#contactList").append("<div class='cardDefault'>" +
                  "<h3>" + $("input[name=firstName]").val() + " " + $("input[name=lastName]").val() + "</h3>" +
                  "<p>" + "Click for a description!" + "</p>" +
                  "</div>");
            
            $("#contactList").on("click", ".cardDefault", function () {
                  $(this).html("<h3>" + $("input[name=description]").val() + "</h3>" +
                        "<p>" + "Click again for names!" + "</p>");
                  $(this).attr("class", "cardAlternative");
            });
            
            $("#contactList").on("click", ".cardAlternative", function () {
                  $(this).html("<h3>" + $("input[name=firstName]").val() + " " + $("input[name=lastName]").val() + "</h3>" +
                        "<p>" + "Click for a description!" + "</p>");
                  $(this).attr("class", "cardDefault");
            });
            
            return false;
            
      });
      
});