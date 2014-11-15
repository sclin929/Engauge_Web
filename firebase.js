var firebaseDataRef = new Firebase('https://engauge.firebaseio.com/');

firebaseDataRef.onAuth(function(authData){
	if (authData) {
		console.log("User ID: " + authData.uid + ", Provider: " + authData.provider);
	} else {
		console.log("Logged out");
	}
});


var usernameText = $('#txtEmail').val();
var passwordText = $('#txtPass').val();

$('#loginPressed').keypress(function (e) {
	if (e.keyCode == 13) {
		firebaseDataRef.authWithPassword({
			email : usernameText,
			password: passwordText
		}, function(err, authData) {
			console.log("Fail");
		});
	}
});