document.addEventListener('DOMContentLoaded', function() {
    // Atur urutan hari dalam seminggu dimulai dari Minggu
    moment.updateLocale('en', {
        weekdaysShort: 'Sat_Sun_Mon_Tue_Wed_Thu_Fri_'.split('_')
    });

    // Fungsi untuk mengupdate waktu nyata setiap detik
    function updateWaktuNyata() {
        var tanggalWaktu = moment().format('LLLL');
        document.getElementById('tanggal-waktu').innerText = tanggalWaktu;
    }

    // Fungsi untuk menampilkan kalender dengan menggunakan Moment.js
    function tampilkanKalender() {
        var kalender = document.getElementById('kalender');

        // Ambil tanggal saat ini
        var tanggalSekarang = moment();

        // Tampilkan kalender bulan ini
        

        // Tambahkan hari-hari dalam seminggu
        
        // Hitung jumlah hari pada bulan ini
        var daysInMonth = tanggalSekarang.daysInMonth();

        // Hitung hari pertama dari bulan ini
        var firstDay = moment(tanggalSekarang).startOf('month').format('d');

        // Tampilkan tanggal dari bulan ini
        var row = '';
        for (var i = 1; i <= daysInMonth; i++) {
            if (i === moment().date() && tanggalSekarang.isSame(moment(), 'month')) {
                row += '<div class="today">' + i + '</div>';
            } else {
                row += '<div>' + i + '</div>';
            }
        }
        kalender.innerHTML += row;
    }

    // Panggil fungsi untuk menampilkan kalender dan waktu nyata
    tampilkanKalender();
    updateWaktuNyata();

    // Fungsi untuk memperbarui waktu nyata setiap detik
    setInterval(function() {
        updateWaktuNyata();
    }, 1000);
});