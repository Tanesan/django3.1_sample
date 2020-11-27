
$(function() {

    $('#logout').click(function (){
        $.ajax({
            url: '/logout/',
            method: "GET",
            data : "logout",
            success: function () {
            if (confirm('ログアウトしますか？')) {
                window.location.href = '/accounts/';
                }
            // console.log("logged out");
            return true
            },
            error: function() {
            console.log("nope, it didn't work");
            return false
            }
      });
    
  });
});