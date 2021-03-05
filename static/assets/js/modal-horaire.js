$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-horaire .modal-content").html("");
          $("#modal-horaire").modal("show");
        
        },
        success: function (data){
          $("#modal-horaire .modal-content").html(data.html_form);
        }
      });
    };
  
    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
              //location.reload()
              //$('#comment_articles').html(response['form'])
             
             $("#comment_articles").html(data.html_comment);
             $("#id_comment").val(null);
             //location.reload()
              //$("#modal-horaire .modal-content").modal("hide");
          }
          else {
            $("#modal-horaire").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create book
    $(".js-create-book").click(loadForm);
    $("#modal-horaire").on("submit", ".js-horaire-create-form", saveForm);
  
    // Update book
    $("#book-table").on("click", ".js-update-horaire", loadForm);
    $("#modal-horaire").on("submit", ".js-horaire-update-form", saveForm);

    // modal-delete
    $("#book-table").on("click", ".js-delete-book", loadForm);
    $("#modal-horaire").on("submit", ".js-book-delete-form", saveForm);
  
  });

  