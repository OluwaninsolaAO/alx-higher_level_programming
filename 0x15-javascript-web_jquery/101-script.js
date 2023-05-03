$('document').ready(function () {
  const add = $('div#add_item');
  const remove = $('div#remove_item');
  const clear = $('div#clear_list');
  const list = $('ul.my_list');
  const item = '<li>Item</li>';

  add.on('click', function () {
    list.append(item);
  });

  remove.on('click', function () {
    $('ul.my_list :last-child').remove();
  });

  clear.on('click', function () {
    list.children().remove();
  });
});
