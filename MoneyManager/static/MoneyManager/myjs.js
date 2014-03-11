function drawCharts() {
    // Load the Visualization API and the piechart package.
    google.load('visualization', '1', {'packages':['corechart']});

    // Set a callback to run when the Google Visualization API is loaded.
    google.setOnLoadCallback(drawMonthlyChart);
    google.setOnLoadCallback(drawYearlyChart);
}

// sample data
var sample = [
   ['Category', 'Spense'],
   ['Food',     80],
   ['Gas',     150],
   ['Social',  200],
];

function drawMonthlyChart() {
    var jsonData = $.ajax({
        url: 'getMonthlyData/',
        dataType:"json",
        async: false
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable(jsonData);
    var formatter = new google.visualization.NumberFormat({negativeColor: 'red', negativeParens: true, pattern: '$###,###'});
    formatter.format(data, 1);
    var options = {
        title: 'Monthly Spending',
	is3D:  true,
	pieSliceText: 'value',
    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('month-chart'));
    chart.draw(data, options);
}

function drawYearlyChart() {
    var jsonData = $.ajax({
        url: "getYearlyData/",
        dataType:"json",
        async: false
    }).responseText;

    var data;
    var options = {is3D: true, pieSliceText: 'value'};

    if (jsonData == "{}") {
        data = google.visualization.arrayToDataTable(sample);
	options['title'] = 'Sample Data';
    } else {
        // Create our data table out of JSON data loaded from server.
        data = new google.visualization.DataTable(jsonData);
	options['title'] = 'Yearly Spending';
    }

    var formatter = new google.visualization.NumberFormat({prefix: '$'});
    formatter.format(data, 1);
    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('year-chart'));
    chart.draw(data, options);
}
