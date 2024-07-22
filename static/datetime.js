window.onload = function () {
    DisplayCurrentTime();

    setInterval(() => {
        DisplayCurrentTime();
    }, 1000);
};

function DisplayCurrentTime() {
    var date = new Date();

    var day = date.getDate();
    var month = date.toLocaleString('default', { month: 'short' });
    var year = date.getFullYear();

    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    var am_pm = hours >= 12 ? 'PM' : 'AM';

    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    var current_date = `${day}/${month}/${year}`;
    var current_time = `${hours}:${minutes}:${seconds} ${am_pm}`;
    var date_time = `${current_date} ${current_time}`;

    document.getElementById("demo1").innerHTML = date_time;
}
