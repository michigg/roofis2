$.document.ready(function () {
    updateColors();
});

function updateColors(listOfBookings) {
    let list = [];

    listOfBookings.forEach(booking =>{
        list.add(getDayOfWeek(booking.startDate)+)

    });


    list.forEach(id => {
        $("#"+id).addClass("booked");
    });
}

// Accepts a Date object or date string that is recognized by the Date.parse() method
function getDayOfWeek(date) {
  var dayOfWeek = new Date(date).getDay();
  return isNaN(dayOfWeek) ? null : ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][dayOfWeek];
}