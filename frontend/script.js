const API_URL = 'http://localhost:8000';

document.addEventListener('DOMContentLoaded', async () => {
    // Load Options
    try {
        const res = await fetch(`${API_URL}/options`);
        const data = await res.json();

        if (data.error) {
            alert('Backend not ready: ' + data.error);
            return;
        }

        populateSelect('state', data.states);
        populateSelect('district', data.districts);
        populateSelect('type', data.types);
        populateSelect('cause', data.causes);

    } catch (e) {
        console.error("Could not load options. Ensure backend is running.", e);
    }
});

function populateSelect(id, items) {
    const el = document.getElementById(id);
    el.innerHTML = '';
    items.forEach(item => {
        const option = document.createElement('option');
        option.value = item;
        option.textContent = item;
        el.appendChild(option);
    });
}

document.getElementById('predict-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const payload = {
        state: document.getElementById('state').value,
        district: document.getElementById('district').value,
        death_type: document.getElementById('type').value,
        cause: document.getElementById('cause').value,
        year: parseInt(document.getElementById('year').value)
    };

    try {
        const res = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await res.json();

        // Update UI
        document.getElementById('results').style.display = 'block';

        const riskVal = document.getElementById('risk-val');
        riskVal.textContent = result.risk_level;
        riskVal.className = `value ${result.risk_level}`;

        document.getElementById('deaths-val').textContent = result.predicted_deaths;

        // Mock Chart Data update (Visual effect only since we only predicted one point)
        updateChart(result.predicted_deaths);

    } catch (e) {
        alert('Prediction failed. See console.');
        console.error(e);
    }
});

let trendChart = null;

function updateChart(prediction) {
    const ctx = document.getElementById('trendChart').getContext('2d');

    // Generate some mock history for the chart context
    const history = [
        prediction * 0.8,
        prediction * 0.85,
        prediction * 0.9,
        prediction * 0.95,
        prediction
    ];

    const labels = ['2022', '2023', '2024', '2025', '2026 (Pred)'];

    if (trendChart) {
        trendChart.destroy();
    }

    trendChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Death Toll Trend',
                data: history,
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: 'white' } }
            },
            scales: {
                y: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(255,255,255,0.05)' } },
                x: { ticks: { color: '#94a3b8' }, grid: { display: false } }
            }
        }
    });
}
