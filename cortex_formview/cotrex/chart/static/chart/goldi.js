// static/market/btc.js

document.addEventListener("DOMContentLoaded", function() {
    var fig = JSON.parse(document.getElementById('fig-data').textContent);
    Plotly.newPlot('chart', fig.data, fig.layout);
});
