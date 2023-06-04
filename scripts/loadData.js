function displayJSONData() {
  $.getJSON('../json/data_set.json', function(data) {
    // Extract the date and sold_price values from the JSON
    var dates = data.map(function(obj) {
      return obj[0];
    });

    var soldPrices = data.map(function(obj) {
      return parseFloat(obj[1]);
    });
    console.log(soldPrices)
    // Create the chart
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: dates,
        datasets: [{
          label: 'Sold Prices',
          data: soldPrices,
          borderColor: '#ffcc03',
          backgroundColor: '#286bbd',
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true
          }
        },
        plugins: {
          legend: {
            position: 'bottom' // Move the legend to the bottom
          }
        }
      },
    });
  });
}

$(document).ready(function() {
  displayJSONData();
});
