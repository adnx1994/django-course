document.addEventListener("DOMContentLoaded", function () {
    const rawDataElement = document.getElementById('jsonData');
    const rawData = rawDataElement.textContent || rawDataElement.innerText;
    console.log(rawData); // Print raw JSON data to console for debugging
    const parsedData = JSON.parse(rawData);
    console.log(parsedData); // Print parsed JSON data to console for debugging

    const dates = parsedData.index.map(date => new Date(date));
    const closePrices = parsedData.data.map(row => row[3]); // Assuming 'Close' price is at index 3

    const ctx = document.getElementById('talaChart').getContext('2d');
    const talaChart = new Chart(ctx, {
        type: 'line', // or 'candlestick' if using a candlestick chart library
        data: {
            labels: dates,
            datasets: [{
                label: 'tala Close Price',
                data: closePrices,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day'
                    }
                },
                y: {
                    beginAtZero: false
                }
            }
        }
    });
});