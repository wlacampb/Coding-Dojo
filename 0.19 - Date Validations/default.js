$(document).ready(function () {
      
      $(function () {
            $(".date").datepicker();
      });
      
      $("form").submit(function () {
            
            if ($("input[name=from]").val() === "") {
                  $("#submit").css("background-color", "red");
                  alert("You have to start sometime!")
            }
            
            if ($("input[name=to]").val() === "") {
                  $("#submit").css("background-color", "red");
                  alert("The fun has to end sometime!")
            }
            
            if ($("input[name=name]").val() === "") {
                  $("#submit").css("background-color", "red");
                  alert("Your name can't be blank!")
            }
            
            else {
                  alert("Thanks " + $("input[name=name]").val() + "! Your cruise leaves on " + $("input[name=from]").val() + " and returns on " + $("input[name=to]").val() + "!");
            }
            
            return false;
      });
      
});