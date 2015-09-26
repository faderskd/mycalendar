$(function() {
    $('.search-engine').keyup(function(){

        $.ajax({
            //dataType: "json",
            type: "GET",
            url: "/friends/search-list-json/",
            data: {
                'username':$('.search-engine').val()
            },
            success: appendSearchResults
        });

    });
});

function appendSearchResults(data, textStatus, jqXHR) {
    var $searchResults = $('.search-results');
    $searchResults.html('');
    $.each(data, function(key, value){
       $searchResults.append(
           '<div class="search-result"><img class="profile-photo" src='+value.image_url+'><span>'+value.username+'</span></div>'
       );
    });
}