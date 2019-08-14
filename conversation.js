var loadingMsgIndex,
    botui = new BotUI('convo-bot'),
    API = 'http://127.0.0.1:5000/';

function sendXHR(repo, cb) {
  var response =  $.get('http://127.0.0.1:5000/'+value_response, function(response)
  {
    botui.message.add({
        content: response
        });
  });
}

function init() {
  botui.message
  .bot({
    delay: 1000,
    content: 'Hello. Add a file for Photographs!'
  })
  .then(function () {
    return botui.action.text({
      delay: 1000,
      action: {
        value: 'Enter File to Stage',
        placeholder: 'Enter File to Stage'
      }
    })
  }).then(function (res) {
    loadingMsgIndex = botui.message.bot({
      delay: 200,
      loading: true
    }).then(function (index) {
      loadingMsgIndex = index;
      sendXHR(res.value, showStars)
    });
  });
}

function showStars(stars) {
  botui.message
  .update(loadingMsgIndex, {
    content: 'it has !(star) ' + (stars || "0") + ' stars.'
  })
  .then(init); // ask again for repo. Keep in loop.
}

init();