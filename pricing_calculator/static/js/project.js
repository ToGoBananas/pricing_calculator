//$('.datacenter').on('click', function () {
//    $(this).find('.packages_description').toggle(700);
//});
//

$('.packages_name').on('click', function () {
    $('.packages_name').removeClass('active');
    $(this).addClass('active');
    $.ajax({
      url: "packages/",
      data: {package_name: $(this).html()}
    }).done(function(html) {
      $('#packages').replaceWith(html);
    });
});

$('.packages').on('change', '.checkbox', function () {
    var parent = $(this).parent();
    var pack = parent.attr('class');
    var datacenter = parent.find('h5').data('datacenter');
    var price = parent.find('.package_price').html();
    var text = pack + ' ' + datacenter + ' ' + price;
    var new_html = $('<div></div>');
    var total_price = $('#total_price');
    var new_price;
    if (!$(this).hasClass('checked')) {
        $(this).addClass('checked');
        new_html.html(text);
        new_html.attr('package', pack);
        new_html.attr('datacenter', datacenter);
        $('#select').append(new_html);
        new_price = parseFloat(total_price.html()) + parseFloat(price);
        total_price.html(new_price+'$')
    } else {
        $(this).removeClass('checked');
        $('#select').find("div:contains("+text+")").remove();
        new_price = parseFloat(total_price.html()) - parseFloat(price);
        total_price.html(new_price+'$')
    }
});