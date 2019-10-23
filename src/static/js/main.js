function initForm() {
    let today = new Date();
    let date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
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

    startDateInput.value = date;
    startTimeInput.value = time;
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
    console.log("Data Table")
});

initForm();