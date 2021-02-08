$.ajax({
  method: "GET",
  url: "/data/",
  success: function (data) {
    new Chart(document.getElementById("Ping Chart"), {
      type: "line",
      data: {
        labels: data.timestamps,
        datasets: [
          {
            label: "secondes",
            backgroundColor: "rgba(34, 211, 90, 0.8)",
            borderColor: "rgba(34, 211, 90, 0.9)",
            pointRadius: false,
            pointColor: "#3b8bba",
            pointStrokeColor: "rgba(60,141,188,1)",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(60,141,188,1)",
            fill: true,
            data: data.responsetime,
          },
        ],
      },
      options: {
        responsive: true,
        title: {
          display: false,
        },
        legend: {
          display: false,
        },
        tooltips: {
          mode: "index",
          intersect: false,
        },
        hover: {
          mode: "nearest",
          intersect: true,
        },
        scales: {
          xAxes: [
            {
              display: true,
              scaleLabel: {
                display: true,
                labelString: "Ping time",
              },
            },
          ],
          yAxes: [
            {
              display: true,
              scaleLabel: {
                display: true,
                labelString: "Response time (s)",
              },
              ticks: {
                beginAtZero: true, // minimum value will be 0.
              },
            },
          ],
        },
      },
    });
  },
  error: function (data) {
    console.log("Error");
  },
});
