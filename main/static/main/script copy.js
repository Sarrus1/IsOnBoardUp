$.ajax({
  method: "GET",
  url: "/data/1/",
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
        aspectRatio: 3,
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
                fontColor: "#e3e3e3",
              },
              ticks: {
                fontColor: "#e3e3e3",
              },
            },
          ],
          yAxes: [
            {
              display: true,
              scaleLabel: {
                display: true,
                labelString: "Response time (s)",
                fontColor: "#e3e3e3",
              },
              ticks: {
                beginAtZero: true, // minimum value will be 0.
                fontColor: "#e3e3e3",
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

function donutChart() {
  $.ajax({
    method: "GET",
    url: "/data/2/",
    success: function (data) {
			new Morris.Donut({
				element: "ratio",
				data: [
					{ label: "Failed ping", value: data.total_failed },
					{ label: "Successful pings", value: data.total - data.total_failed },
				],
				resize: true,
				redraw: true,
				colors: ["#3A89C9", "#22d25a"],
			});
		},
    error: function (data) {
      console.log("Error");
    },
  });
}



$(document).ready(function () {
  donutChart();

  $(window).resize(function () {
    window.donutChart.redraw();
  });
});
