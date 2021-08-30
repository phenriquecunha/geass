$( document ).ready(function() {
    var baseUrl   = 'http://192.168.88.123:8000/';
    var filter     = $('#filter')

    $(filter).change(function() {
        var filter = $(this).val();

        window.location.href = baseUrl + '?filter=' + filter;
    });

});