console.log("hi");

var firebaseDataRef = new Firebase('https://jqo8s40aj38.firebaseio-demo.com/');

$('#messageInput').keypress(function (e) {
        if (e.keyCode == 13) {
          var name = $('#nameInput').val();
          var text = $('#messageInput').val();
          firebaseDataRef.set('User ' + name + ' says ' + text);
          $('#messageInput').val('');
        }
      });