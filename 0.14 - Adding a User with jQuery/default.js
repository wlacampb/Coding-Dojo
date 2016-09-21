$(document).ready(function() {
      $("form").submit(function() {
            $("tbody").append("<tr>" +
                  "<td>" + $("input[name=firstName]").val() + "</td>" + 
                  "<td>" + $("input[name=lastName]").val() + "</td>" + 
                  "<td>" + $("input[name=emailAddress]").val() + "</td>" + 
                  "<td>" + $("input[name=contactNumber]").val() + "</td>" +  
                  "</tr>"); 
            $(".input").val("");
            return false; 
      }); 
}); 