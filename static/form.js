$(document).ready(function() {
    $("button").click(function(){
        $.ajax({
            url:'/data/'.concat(document.getElementById('number').value),
            type: 'POST',
            success: function(result){
                document.getElementById('number').value = 'Success';
            }
        });
    });
});