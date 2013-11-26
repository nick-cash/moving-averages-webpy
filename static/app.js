$(document).ready(function(){
    // Quite a bit of this comes from the jqPlot example here:
    // http://www.jqplot.com/tests/data-renderers.php
    var ajaxDataRenderer = function(url, plot, options) {
        var ret = null;
        $.ajax({
          // have to use synchronous here, else the function
          // will return before the data is fetched
          async: false,
          url: url,
          dataType:"json",
          success: function(data) {
            ret = data;
          }
        });
        return ret;
    };

    var jsonurl = '/moving-averages/json'

    $.jqplot('chartdiv',  jsonurl, {
        title: 'Moving Averages',
        animate: true,
        dataRenderer: ajaxDataRenderer,
        dataRendererOptions: {unusedOptionalUrl: jsonurl},
        legend:{
            renderer: $.jqplot.EnhancedLegendRenderer,
            show: true
        },
        series:[
            {label:'Data'},
            {label:'Simple'},
            {label:'Cumulative'},
            {label:'Weighted'},
            {label:'Exponential'}
        ],
        axes: {
            xaxis: {label: 'Time'},
            yaxis: {
                label: 'Values',
                tickOptions:{
                    formatString: '%.2f'
                }
            }
        },
        cursor:{
            show: true,
            zoom: true,
            showTooltip: false
        },
        highlighter: {
            show: true,
            sizeAdjust: 7.5
        }
    });
});