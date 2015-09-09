$(document).ready(function () {
    $('#calendar').fullCalendar({
        eventClick: function (calEvent, jsEvent, view) {
            window.location.href ='/events/' +calEvent.url + '/edit/';
        },
        timeFormat: '(H:mm)',
        eventLimit: true,
        events: '/events/list-json/'
    });
});



