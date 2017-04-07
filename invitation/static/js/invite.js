$(document).ready(function(){
  $(".invite").click(function(event){
    event.preventDefault()
    var button = $(this)
    var studentID = button.attr("student-id")
    $.ajax({
        url : "/request/" + studentID + "/invite",
        type: "POST",
        success: function(data, textStatus, jqXHR)
        {
          alert("The paragraph was clicked.");
        },
        error: function (jqXHR, textStatus, errorThrown)
        {
     
        }
    });
  });
});
