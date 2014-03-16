window.onload = init; // set onload callback function. no ()

function init() {
    var dt = new Date();
    var curr_year  = dt.getFullYear();
    var curr_month = dt.getMonth() + 1;
    var year_options = getYearList(2014, curr_year);
    var month_options = getMonthList(curr_month);
    var year_obj  = document.getElementById('yoptions');
    var month_obj = document.getElementById('moptions');

    fillSelect(year_obj, year_options, curr_year.toString());
    fillSelect(month_obj, month_options, formatMonth(curr_month));
}

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

// fill select options
// input  - obj: select DOM object
//          values: values for options
//          selected: value as selected
// output - none
function fillSelect(obj, values, selected) {
     obj.options.length = 0;
     for (var i=0; i<values.length; i++) {
         obj.options[i] = new Option(values[i]);
	 if (values[i] == selected) {
             obj.options[i].selected = true;
	 }
     }
}

// return a year list
// input  - max year
// output - a list of string from init year to max year
function getYearList(init_year, max_year) {
    var list = new Array();
    for(var i=max_year; i>=init_year; i--) {
        list.push(i.toString());
    }
    return list;
}

// return a month list
// input  - max month
// output - a list of string from 01 to max month
function getMonthList(max_month) {
    var init_month = 1;
    var list = new Array();
    for(var i=max_month; i>=init_month; i--) {
	list.push(formatMonth(i));
    }
    return list;
}

// convert month number to 2 digit string
// input:  number 1..12
// output: string 01..12
function formatMonth(month) {
    var prefix = "0";
    if (month < 10) {
        return prefix.concat(month.toString());
    } else {
	return month.toString();
    }
}
