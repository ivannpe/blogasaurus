function greeting(){
  var userName = $('#username').val();
  var Email = $('#email').val();
  alert("Thank You " + userName + " I will contact you in the future at " + Email);

}

function setup() {
  $("#ok_button").click(greeting);
}

$(document).ready(setup);
