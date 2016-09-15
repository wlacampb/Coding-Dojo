alert("JS CONNECTED! WOOP WOOP")

$(document).ready(function () {
      $("button").click(function () {
            $("#myParagraph").text("see how I .text() works as a setter!");
      });
      $("#focusOnMe").focus(function () {
            console.log("Handler for .focus() called.");
      });
      $("#addClass").addClass("aqua");
      $("#val").keyup(function () { // I listen for keyups in #val
                  var value = $(this).val(); // I set value of #val, which is in the html, equal to $(this), which stores the value of the keyup, using .val(), which gets the string from #val
                  $("#inputHere").text(value); // I target #inputHere and write a new value into #val
            })
            .keyup(); // I ensure the value of <p> = "some text" because I trigger a keyup event and thus write the initial #val, which is preset, to #inputHere
      var title = $("em").attr("title"); // I get the title attr of em
      $("#iAmDiv").text(title); // I add take the title attr of em and add it between the <div> tags
      $("div.iAmNotDiv").html("<b>Wow!</b> Such excitement..."); // I add new html into .iAmNotDiv
      $("div.iAmNotDiv b") // I target the new html's <b>
            .append("!!!") // I add three exclamation marks
            .css("color", "red"); // I add new CSS to div.iAmNotDiv b
      $("button.blah").click(function () { // I listen for click @button.blah
            var value; // I store a value
            switch ($("button.blah").index(this)) { // I use .index to search for the value of this, which is owned by button.blah's, and then evaluate the cases to determine what line of code I need to run
            case 0:
                  value = $("div.nah").data("blah"); // I make value equal to "blah" if the button.blah the user clicks has an index of 0
                  break;
            case 1:
                  $("div.nah").data("blah", "hello"); // '' I make"blah" = "hello"  if the button.blah the user clicks has an index of 1
                  value = "Stored!";
                  break;
            case 2:
                  $("div.nah").data("blah", 86); // I make"blah" = 86  if the button.blah the user clicks has an index of 2
                  value = "Stored!";
                  break;
            case 3:
                  $("div.nah").removeData("blah"); // I remove "blah," which causes value = undefined
                  value = "Removed!";
                  break;
            }
            $("span").text("" + value);
      });
      $('.target')
            .append('<div class="child">1. Append</div>') // adds data to existing structure after existing data
            .prepend('<div class="child">2. Prepend</div>') // adds data to existing structure before existing data
            .before('<div class="sibling">3. Before</div>') // adds new data structure before existing structure
            .after('<div class="sibling">4. After</div>'); // adds new data structure after existing structure
      $("button.show-me").click(function () {
            $("p.yellow").show("slow");
      });
      $("button.hide-me").click(function () {
            $("p.yellow").hide("slow");
      });
      $("button.toggle-me").click(function () {
            $("p.yellow").toggle("slow");
      });
      $(".click-me").click(function () {
            $(".censored-1").fadeIn(3000, function () {
                  $(".censored-2").fadeIn(100);
            });
      });
});