var barChartData = {
    labels: [
        "USA",
        "Inida",
        "Brazil",
        "France",
        "Turkey"
    ],
    datasets: [
      {
        label: "Active cases",
        backgroundColor: "pink",
        borderColor: "red",
        borderWidth: 1,
        data: [31862094, 15941658, 14139674, 5524207,5271498]
      },
      {
        label: "Vaccinated",
        backgroundColor: "lightgreen",
        borderColor: "green",
        borderWidth: 1,
        data: [134162782, 111694798, 26403481, 13018381, 12590582]
      },
      {
        label: "Dead",
        backgroundColor: "grey",
        borderColor: "black",
        borderWidth: 1,
        data: [569402,184954,382581,105955,37337]
      }
    ]
  };
  
  var chartOptions = {
    responsive: true,
    legend: {
      position: "top"
    },
    title: {
      display: true,
      text: "Chart.js Bar Chart"
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
  
  window.onload = function() {
    var ctx = document.getElementById("canvas").getContext("2d");
    window.myBar = new Chart(ctx, {
      type: "bar",
      data: barChartData,
      options: chartOptions
    });
  };
  