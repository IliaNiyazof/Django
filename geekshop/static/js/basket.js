var config = {
    selector: {
        add: '.basket-item-add',
        delete: '.basket-item-delete',
        quantity: '.basket-item-quantity',
    },
    urls: {
        add: '/basket/add/',
        delete: '/basket/remove/',
        update: '/basket/update/'
    }
};


$(document).ready(function () {
    $(config.selector.add).on('click', function () {
        var items_id = $(this).data('id');
        var item_url = config.urls.add + items_id + "/";

        var parent_item = $(this).parents()[0]; //<li>
        var counter = $(parent_item).find(config.selector.quantity)

        $.ajax({
            url: item_url,

            success: function (data) {
                counter.text(data.quantity)
            }
        });
    })
});


$(document).ready(function () {
    $(config.selector.delete).on('click', function () {
        var items_id = $(this).data('id');
        var item_url = config.urls.delete + items_id + "/";

        var parent_item = $(this).parents()[0]; //<li>
        var counter = $(parent_item).find(config.selector.quantity)

        $.ajax({
            url: item_url,

            success: function (data) {
                $(parent_item).hide();
            }
        });
    })
});