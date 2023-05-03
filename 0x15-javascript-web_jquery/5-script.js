const toggler = $('div#add_item');
const ul = $('ul.my_list');

toggler.on('click', function () {
  ul.append('<li>Item</li>');
});
