const loadChartData = (countryNames, countryCases, countryActive, countryRecovered, countryDeaths, countryCritical) => {
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: countryNames,
            datasets: [{
                label: 'Total Cases',
                data: countryCases,
                backgroundColor:'rgba(255, 197, 1, 1)',
                borderColor: 'rgba(255, 197, 1, 1)',
                borderWidth: 1
            }, {
                label: 'Active Cases',
                data: countryActive,
                backgroundColor:'rgba(0, 123, 255, 1)',
                borderColor: 'rgba(0, 123, 255, 1)',
                borderWidth: 1
            },
            {
                label: 'Recovered Cases',
                data: countryRecovered,
                backgroundColor:'rgba(40, 167, 69, 1)',
                borderColor: 'rgba(40, 167, 69, 1)',
                borderWidth: 1
            },
            {
                label: 'Total Deaths',
                data: countryDeaths,
                backgroundColor:'rgba(220, 53, 69, 1)',
                borderColor: 'rgba(220, 53, 69, 1)',
                borderWidth: 1
            },
            {
                label: 'Critical Cases',
                data: countryCritical,
                backgroundColor:'rgba(220, 53, 69, 0.6)',
                borderColor: 'rgba(220, 53, 69, 0.6)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            maintainAspectRatio: false,
            responsive: true
        }
    });
 }

const loadCountryPieData = (countryActive, countryRecovered, countryDeaths, countryCritical) => {
    var config = {
        type: 'pie',
        data: {
            datasets: [{
                data: [
                    countryActive,
                    countryRecovered,
                    countryDeaths,
                    countryCritical
                ],
                backgroundColor: [
                    'rgba(0, 123, 255, 1)',
                    'rgba(40, 167, 69, 1)',
                    'rgba(220, 53, 69, 1)',
                    'rgba(220, 53, 69, 0.6)',
                ],
                label: 'Covid Case Overview'
            }],
            labels: [
                'Active Cases',
                'Recovered Cases',
                'Total Deaths',
                'Critical Cases'
            ]
        },
        options: {
            responsive: true
        }
	};
     new Chart(ctx, config);
}
