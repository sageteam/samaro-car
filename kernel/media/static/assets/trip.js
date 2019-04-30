$(document).ready(function () {
    $('#id_destination_region').empty();
    $('#id_origin_region').empty();
    $('#id_origin').empty();
    $('#id_destination').empty();

    $('#id_origin_region').append('<option value="' + 0 + '">' + 'ابتدا شهر انتخاب کنید' + '</option>');
    $('#id_destination_region').append('<option value="' + 0 + '">' + 'ابتدا شهر انتخاب کنید' + '</option>');

    $('#id_origin').append('<option value="' + 0 + '">' + 'انتخاب شهر' + '</option>');
    $('#id_destination').append('<option value="' + 0 + '">' + 'انتخاب شهر' + '</option>');

    $.ajax({
        url: '/api/v1/city/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            $.each(data, function (index, city) {
                $('#id_origin').append('<option value="' + city.pk + '">' + city
                    .name + '</option>');
            });
            $.each(data, function (index, city) {
                $('#id_destination').append('<option value="' + city.pk + '">' + city
                    .name + '</option>');
            });
        }
    });


    // ORIGIN REGION
    $('#id_origin').change(function () {
        $('#id_origin_region').empty();
        // console.log('drop down changed')
        city = $('#id_origin option:selected').text();
        // console.log('api/v1/city/' + city)
        $.ajax({
            url: '/api/v1/city/' + city,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // console.log('data is ' + data.regions)
                $.each(data.regions, function (index, region) {
                    // console.log(region)
                    $('#id_origin_region').append('<option value="' + region.id +
                        '">' + region.name + '</option>');
                })
            }
        })

    });
    // DESTINATION REGION
    $('#id_destination').change(function () {
        $('#id_destination_region').empty();
        // console.log('drop down changed')
        city = $('#id_destination option:selected').text();
        // console.log('api/v1/city/' + city)
        $.ajax({
            url: '/api/v1/city/' + city,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // console.log('data is ' + data.regions)
                $.each(data.regions, function (index, region) {
                    // console.log(region)
                    $('#id_destination_region').append('<option value="' +
                        region.id + '">' + region.name + '</option>');
                })
            }
        });

    });
});


$(document).ready(function () {
    console.log('html is read.')
    $('#price-recommender-btn').click(function () {
        origin = $('#id_origin option:selected').text();
        destination = $('#id_destination option:selected').text();
        if (origin == 'انتخاب شهر' || destination == 'انتخاب شهر') {
            console.log('error');
            $('#id_suggested_price').val('مبدا و مقصد باید انتخاب شوند');
        } else if (origin == destination) {
            $('#id_suggested_price').val('مبدا و مقصد برابر هستند');
        } else {
            origin = $('#id_origin option:selected').val();
            destination = $('#id_destination option:selected').val();
            console.log(origin)
            console.log(destination)
            $('#id_suggested_price').val('');
            $.ajax({
                url: '/api/v1/distance/?city1=' + origin + '&city2=' + destination,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    console.log('data is ' + data)
                    if (data[0]) {
                        $('#id_suggested_price').val(data[0].price);
                    } else {
                        $.ajax({
                            url: '/api/v1/distance/?city1=' + destination + '&city2=' + origin,
                            type: 'GET',
                            dataType: 'json',
                            success: function (data) {
                                console.log('data is ' + data)
                                $('#id_suggested_price').val(data[0].price);
                            },  
                        });
                    }
                }, 
            });
        }


    });
});