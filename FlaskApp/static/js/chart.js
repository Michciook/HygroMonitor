let myChart;

async function fetchData() {
    try {
        const response = await fetch('/api/data/'); 
        return await response.json(); 
    } catch (error) {
        console.error("Błąd pobierania danych:", error);
        return { labels: [], values: [] }; 
    }
}

async function createChart() {
    const dataset = await fetchData();

    const ctx = document.getElementById('myChart').getContext('2d');
    myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dataset.labels,
            datasets: [{
                label: 'Wilgotność (%)',
                data: dataset.values,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 2,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {beginAtZero: true, max: 100}
            },
            plugins: {
                legend: {
                    display: true
                }
            }
        }
    });
}

async function updateChart() {
    const dataset = await fetchData();
    if (dataset.labels.length > 0) { 
        myChart.data.labels = dataset.labels;
        myChart.data.datasets[0].data = dataset.values;
        myChart.update();
    }
}

window.onload = function() {
    createChart();
    setInterval(updateChart, 5000); 
};
