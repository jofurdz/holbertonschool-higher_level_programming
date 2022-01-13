const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.getJSON(URL, (data) => {
  const hello = data.hello;
  $('DIV#hello').text(hello);
});
