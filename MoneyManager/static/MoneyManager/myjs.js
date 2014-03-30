window.onload = init; // set onload callback function. no ()

// Load the Visualization API and the piechart package.
google.load('visualization', '1', {'packages':['corechart']});

var dt = new Date();
var curr_year  = dt.getFullYear();
var curr_month = dt.getMonth() + 1;

// initial calendar options
function init() {
    var year_options  = getYearList(2014, curr_year);
    var month_options = getMonthList(curr_month);
    var year_obj  = document.getElementById('yoptions');
    var month_obj = document.getElementById('moptions');

    fillSelect(year_obj, year_options, curr_year.toString());
    fillSelect(month_obj, month_options, formatMonth(curr_month));
}

// set google chart callbacks to run when the Google Visualization API is loaded.
function drawCharts() {
    google.setOnLoadCallback(function() {drawMonthlyChart(formatMonth(curr_month), curr_year.toString())});
    google.setOnLoadCallback(function() {drawYearlyChart(curr_year.toString())});
    google.setOnLoadCallback(function() {drawMChartByMonth(formatMonth(curr_month), curr_year.toString())});
    google.setOnLoadCallback(function() {drawYChartByYear(curr_year.toString())});
}

// call back for Year select
// update monthly and yearly charts
function updateYCharts(sel) {
    var year = sel.options[sel.selectedIndex].value;
    drawYearlyChart(year);
    drawYChartByYear(year);

    var mObj = document.getElementById('moptions');
    var month = mObj.options[mObj.selectedIndex].value;
    drawMonthlyChart(month, year);
    drawMChartByMonth(month, year);
}

// call back for Month select
// update monthly charts
function updateMCharts(sel) {
    var yObj = document.getElementById('yoptions');
    var year  = yObj.options[yObj.selectedIndex].value;
    var month = sel.options[sel.selectedIndex].value;
    drawMonthlyChart(month, year);
}

// TODO move to server side
// sample data
var sample = [
   ['Category', 'Spense'],
   ['Food',     80],
   ['Gas',     150],
   ['Social',  200],
];

function drawMonthlyChart(monthVal, yearVal) {
    var jsonData = $.ajax({
        url: 'getMDataByCategory/',
        dataType:"json",
        async: false,
	data: {month: monthVal, year: yearVal}
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable(jsonData);
    var formatter = new google.visualization.NumberFormat({negativeColor: 'red', negativeParens: true, pattern: '$###,###'});
    formatter.format(data, 1);
    var options = {
        title: 'Spending by Category',
	is3D:  true,
	pieSliceText: 'value',
    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('month-chart'));

    // select handler
    function selectHandler() {
        var selectedItem = chart.getSelection()[0];
	if (selectedItem) {
            //var value = data.getValue(selectedItem.row, selectedItem.column);
            strBlackout();
	}
    }
    google.visualization.events.addListener(chart, 'select', selectHandler);

    chart.draw(data, options);
}

function drawYearlyChart(yearVal) {
    var jsonData = $.ajax({
        url: "getYDataByCategory/",
        dataType:"json",
        async: false,
	data: {year: yearVal}
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

function drawMChartByMonth(monthVal, yearVal) {
    var jsonData = $.ajax({
        url: 'getDataByMonth/',
        dataType:"json",
        async: false,
	data: {month: monthVal, year: yearVal}
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable(jsonData);
    //var formatter = new google.visualization.NumberFormat({negativeColor: 'red', negativeParens: true, pattern: '$###,###'});
    //formatter.format(data, 1);
    var options = {
        title: 'Spending by Month',
	legend: {position: "none"},
    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.ColumnChart(document.getElementById('month-table'));
    chart.draw(data, options);
}

function drawYChartByYear(yearVal) {
    var jsonData = $.ajax({
        url: 'getDataByYear/',
        dataType:"json",
        async: false,
	data: {year: yearVal}
    }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable(jsonData);
    //var formatter = new google.visualization.NumberFormat({negativeColor: 'red', negativeParens: true, pattern: '$###,###'});
    //formatter.format(data, 1);
    var options = {
        title: 'Spending by Year',
	legend: {position: "none"},
    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.ColumnChart(document.getElementById('year-table'));
    chart.draw(data, options);
}

// ------------------------------------------------------
// utility functions
// ------------------------------------------------------

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

// detail table box
function endBlackout() {
    $(".blackout").css("display", "none");
    $(".msgbox").css("display", "none");
}

function strBlackout() {
    $(".blackout").css("display", "block");
    $(".msgbox").css("display", "block");
}

// set buttons to trigger blackout on click
$(document).ready(function() {
    $("#demo").click(strBlackout);
    $(".blackout").click(endBlackout);
    $(".closeBox").click(endBlackout);
});

