$('document').ready(function () {
  const view = $('div#hello');
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (data) {
      view.text(data.hello);
    }
  });
});
