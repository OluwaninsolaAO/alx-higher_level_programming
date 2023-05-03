const header = $('body header');
const toggler = $('div#update_header');

toggler.on('click', function () {
  header.text('New Header!!!');
});
