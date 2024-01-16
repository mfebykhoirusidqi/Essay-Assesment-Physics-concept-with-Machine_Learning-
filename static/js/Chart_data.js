document.addEventListener('DOMContentLoaded', function() {
    fetch('/data').then(function(response) {
        return response.json();
    }).then(function(data) {
        var labels = [];
        var scores = [];

        data.forEach(function(result) {
            labels.push(result.nama); // Ganti dengan kolom yang berisi nama siswa
            scores.push(result.nilai); // Ganti dengan kolom yang berisi nilai ujian siswa
        });

        var ctx = document.getElementById('hasilChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Nilai Ujian',
                    data: scores,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });
});
