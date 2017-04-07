$(document).ready(function(){
  $(".invite").click(function(event){
    event.preventDefault()
    var button = $(this)
    var studentID = button.attr("student-id")
    $.ajax({
        url : "/request/" + studentID + "/invite",
        type: "POST",
        data: JSON.stringify({"student-id":studentID}),
        contentType: 'application/json; charset=utf-8',
        dataType:"json",
        success: function(data, textStatus, jqXHR)
        {
          location.reload();
        },
        error: function (jqXHR, textStatus, errorThrown)
        {
          alert("Bir sorun var. Konsola bak")
          console.log(jqXHR)
          console.log(textStatus)
          console.log(errorThrown)
        }
    });
  });
});
