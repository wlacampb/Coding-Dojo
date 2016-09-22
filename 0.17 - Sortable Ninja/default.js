$(document).ready(function () {
      $(function () {
            $("#accordion")
                  .accordion({
                        header: ""
                  })
                  .sortable({
                        axis: "y",
                        handle: "img",
                        stop: function (event, ui) {
                              $(this).accordion("refresh");
                        }
                  });
      });
});