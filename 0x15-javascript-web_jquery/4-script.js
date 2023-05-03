const toggler = $('div#toggle_header');
const header = $('body header');

toggler.on('click', function () {
  if (header.hasClass('green')) {
    header.removeClass('green');
    header.addClass('red');
  } else {
    header.removeClass('red');
    header.addClass('green');
  }
});
