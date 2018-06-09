$(document).ready(function () {
    updateColors();
});

listOfIds = [];

function updateColors(booking) {
    let list = [];

    if (booking !== undefined) {
        let day = (getDayOfWeek(booking.start_date));
        let beginningHour = booking.start_time.substr(0, 2);
        let endingHour = booking.end_time.substr(0, 2) - 1;

        console.log(day + beginningHour + "-" + endingHour);
        listOfIds.push(day + beginningHour + "-" + endingHour);

    }

    listOfIds.forEach(id => {
        $("#"+id).addClass('booked');
    });
}

// Accepts a Date object or date string that is recognized by the Date.parse() method
function getDayOfWeek(date) {
  var dayOfWeek = new Date(date).getDay();
  return isNaN(dayOfWeek) ? null : ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][dayOfWeek];
}

function init(id) {
    $.getJSON({url: "/api/booking?room_id="+id, success: function (result) {
            result.forEach(booking =>{
                updateColors(booking)
            })
        }});

}