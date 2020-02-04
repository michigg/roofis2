const SELECT_BOX_ID = "location-select";
const SELECT_BOX = document.getElementById(SELECT_BOX_ID);

function initForm() {
    let today = new Date();
    let month = (today.getMonth() + 1).toString();
    if (month.length == 1) {
        month = "0" + month
    }
    let day = today.getDate().toString();
    if (day.length == 1) {
        day = "0" + day
    }

    let date = today.getFullYear() + '-' + month + '-' + day;
    let minutes = today.getMinutes();
    let hours = today.getHours();
    if (minutes >= 30) {
        hours += 1;
        if (hours > 24) {
            hours = 0;
        }
    }
    minutes = 0;
    let time = ("0" + hours).slice(-2) + ":" + ("0" + minutes).slice(-2);

    let startDateInput = document.getElementById('startdate');
    let startTimeInput = document.getElementById('starttime');

    console.log("INIT");
    console.log(startDateInput.value);
    console.log(startTimeInput.value);
    console.log(date);

    if (!startDateInput.value) {
        startDateInput.value = date;
    }

    if (!startTimeInput.value) {
        startTimeInput.value = time;
    }

    const locationButton = document.querySelector('#position-btn');
    let url = locationButton.dataset.lectorBuildingApi;
    fetch(url + "building/")
        .then((resp) => resp.json())
        .then(function (data) {
            // Handle data
            resetSelectBox(data)
        }).catch(error => {
        // Handle error
        // alert("Orte konnten nicht geladen werden.")
    });

}


document.addEventListener("DOMContentLoaded", function () {
    $('#results').DataTable({
        responsive: true,
        columnDefs: [
            {responsivePriority: 1000, targets: 0},
            {responsivePriority: 1, targets: 1},
            {responsivePriority: 1, targets: 3},
            {responsivePriority: 1, targets: -1}
        ],
        "dom": '{ <t> }',
        paging: false
    });
    $('.dataTables_length').addClass('bs-select');
    initForm();
});

function loadPositionRankedBuildings() {
    console.log("START");
    const locationButton = document.querySelector('#position-btn');
    let url = locationButton.dataset.lectorBuildingApi;

    if ("geolocation" in navigator) {
        /* geolocation funktioniert */
        navigator.geolocation.getCurrentPosition(function (position) {
            let positionFilteredUrl = url + "building/?coord=" + position.coords.longitude + "," + position.coords.latitude;
            fetch(positionFilteredUrl)
                .then((resp) => resp.json())
                .then(data => {
                    // Handle data
                    console.log(data);
                    changeLocationDropdownContent(data)
                }).catch(error => {
                // Handle error
                // alert("Orte konnten nicht geladen werden.")
            });
        });
    } else {
        /* geolocation funktioniert NICHT */
        alert("Geolocation Modul konnte nicht gefunden werden.")
    }
}

function clearSelectBox(selectBox) {
    for (const elem in selectBox.options) {
        selectBox.remove(0);
    }

}

function fillSelectBox(data, selectBox) {
    var option = document.createElement("option");
    option.value = "";
    option.text = "Ort auswählen";
    selectBox.add(option);

    for (const elem of data) {
        var option = document.createElement("option");
        option.value = elem;
        option.text = elem;
        selectBox.add(option);
    }
}

function resetSelectBox(data) {
    clearSelectBox(SELECT_BOX);
    fillSelectBox(data, SELECT_BOX);
}

function changeLocationDropdownContent(data) {
    resetSelectBox(data);

    if (SELECT_BOX.options.length > 2) {
        SELECT_BOX.options[1].selected = true;
    }
}
