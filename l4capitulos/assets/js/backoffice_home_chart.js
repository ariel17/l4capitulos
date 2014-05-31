$(function () {
    $('#container').highcharts({
        title: {
            text: 'Purchases vs Sells for last 7 days'
        },
        xAxis: {
            categories: [
                '2014-05-04', '2014-05-05', '2014-05-06', '2014-05-07',
                '2014-05-08', '2014-05-09', '2014-05-10',
            ]
        },
        labels: {
            items: [{
                html: 'Total fruit consumption',
                style: {
                    left: '50px',
                    top: '18px',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
                }
            }]
        },
        series: [{
            type: 'column',
            name: 'Sell',
            data: [3, 2, 1, 3, 4, 6, 7]
        }, {
            type: 'column',
            name: 'Purchase',
            data: [2, 3, 5, 7, 6, 5, 4]
        }, {
            type: 'spline',
            name: 'Average',
            data: [3, 2.67, 3, 6.33, 3.33, 5, 4],
            marker: {
            	lineWidth: 2,
            	lineColor: Highcharts.getOptions().colors[3],
            	fillColor: 'white'
            }
        }, {
            type: 'pie',
            name: 'Total money',
            data: [{
                name: 'Sell',
                y: 13,
                color: Highcharts.getOptions().colors[0] // Jane's color
            }, {
                name: 'Purchase',
                y: 19,
                color: Highcharts.getOptions().colors[1] // Joe's color
            }],
            center: [100, 80],
            size: 100,
            showInLegend: false,
            dataLabels: {
                enabled: false
            }
        }]
    });
});
