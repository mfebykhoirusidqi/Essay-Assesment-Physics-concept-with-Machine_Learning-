-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 16 Jan 2024 pada 15.55
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sidqi_db`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin_db`
--

CREATE TABLE `admin_db` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `db_soal`
--

CREATE TABLE `db_soal` (
  `id` int(11) NOT NULL,
  `jawaban` text NOT NULL,
  `labels` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `db_soal`
--

INSERT INTO `db_soal` (`id`, `jawaban`, `labels`) VALUES
(31, 'Penunjukkan skala pada timbangan saat lift bergerak dipercepat ke atas\nGaya yang bekerja pada ikan adalah gaya berat ke bawah w=mg dan tegangan tali T ke atas yang diberikan oleh timbangan. Jika lift bergerak dipercepat ke atas, aplikasi hukum II Newton pada ikan menghasilkan gaya total berikut.\nsigma (f=m.a)  T-mg=ma_y\n T=ma_y+ mg\nTegangan tali  T,\nT=m(a_y+ g)\nT=m(a+ g)\nJika lift bergerak dipercepat ke atas, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya.  Jadi, penunjukkan skala pada timbangan adalah menunjuk lebih dari 5 N', 4),
(32, 'Gaya yang bekerja pada ikan adalah gaya berat ke bawah  dan tegangan tali T ke atas yang diberikan oleh timbangan. Jika lift bergerak dipercepat ke atas, aplikasi hukum II Newton pada ikan menghasilkan gaya total berikut.\nTegangan tali  T,\nJika lift bergerak dipercepat ke atas, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya.  Jadi, penunjukkan skala pada timbangan adalah menunjuk lebih dari 5 N', 4),
(33, 'Timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya karena lift bergerak dipercepat ke atas.hukum II Newton pada ikan menghasilkan gaya total berikut\nT = ma_y + mg\nT = m(a + g)', 3),
(34, 'Tegangan tali T sama dengan gaya berat ikan.', 2),
(35, 'Resultan gaya yang bekerja pada ikan adalah nol.', 1),
(36, 'Seseorang menimbang ikan bermassa dengan timbangan yang digantungkan pada atap lift, seperti terlihat pada Gambar dibawah ini. Saat lift diam, skala pada timbangan menunjukkan angka 5 N', 1),
(37, '', 1),
(38, 'Tegangan tali T sama dengan gaya berat ikan.', 2),
(39, 'Tegangan tali T sama dengan gaya berat ikan.', 2),
(40, '&nbsp; &nbsp; Penunjukkan skala pada timbangan saat lift bergerak dipercepat ke atasGaya yang bekerja pada ikan adalah gaya berat ke bawah w=mg dan tegangan tali T ke atas yang diberikan oleh timbangan. Jika lift bergerak dipercepat ke atas, aplikasi hukum II Newton pada ikan menghasilkan gaya total berikut.sigma (f=m.a) &nbsp;T-mg=ma_y&nbsp;T=ma_y+ mgTegangan tali &nbsp;T,T=m(a_y+ g)T=m(a+ g)Jika lift bergerak dipercepat ke atas, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya. &nbsp;Jadi, penunjukkan skala pada timbangan adalah menunjuk lebih dari 5 N', 4),
(41, 'Seseorang menimbang ikan bermassa dengan timbangan yang digantungkan pada atap lift, seperti terlihat pada Gambar dibawah ini. Saat lift diam, skala pada timbangan menunjukkan angka 5 N', 1),
(42, 'Seseorang menimbang ikan bermassa dengan timbangan yang digantungkan pada atap lift, seperti terlihat pada Gambar dibawah ini. Saat lift diam, skala pada timbangan menunjukkan angka 5 N', 1),
(43, 'seharusnya jika lift di percepat maka skalanya menjadi kebih berat', 1),
(44, 'skala nya sama dengan gaya berat ikan yaitu\r\nT = m g', 2),
(45, 'jawab:\r\nT = ma_y + mg\r\nT = m(a + g)', 1),
(48, 'Timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya karena lift bergerak dipercepat ke atas.', 3),
(49, 'Timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya karena lift bergerak dipercepat ke atas', 3),
(50, 'skala nya mnejjadi lebih besar', 1),
(51, 'ikan akan menjadi lebih berat', 1),
(52, 'tentunya timbangan akan jadi lebih berat', 1),
(53, 'Timbangannya akan menunjukkan nilai yang lebih besar daripada berat ikan karena lift bergerak dipercepat ke atas..', 3),
(54, 'Seseorang menimbang ikan bermassa dengan timbangan yang digantungkan pada atap lift, seperti terlihat pada Gambar dibawah ini. Saat lift diam, skala pada timbangan menunjukkan angka 5 N', 1),
(55, 'Timbangan lebih besar berat ikan lebiih kecil lift bergerak dipercepat ke atas.', 1),
(57, 'Gaya yang bekerja pada ikan adalah gaya berat ke bawah dan tegangan tali T ke atas yang diberikan oleh timbangan. Jika lift bergerak dipercepat ke atas, aplikasi hukum II Newton pada ikan menghasilkan gaya total berikut.Tegangan tali T,Jika lift bergerak dipercepat ke atas, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya. Jadi, penunjukkan skala pada timbangan adalah menunjuk lebih dari 5 N', 4),
(58, 'Timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya karena lift bergerak dipercepat ke atas.hukum II Newton pada ikan menghasilkan gaya total berikutT = ma_y + mgT = m(a + g)', 3),
(59, 'eknaap denbga dj dad po', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `hasil_siswa`
--

CREATE TABLE `hasil_siswa` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `nama` text NOT NULL,
  `kode` text NOT NULL,
  `Chapter` text NOT NULL,
  `jawaban` text NOT NULL,
  `jawabandb` text NOT NULL,
  `skor` text NOT NULL,
  `nilai` text NOT NULL,
  `keterangan` text NOT NULL,
  `guru` text NOT NULL,
  `selesai` int(11) NOT NULL,
  `time` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `hasil_siswa`
--

INSERT INTO `hasil_siswa` (`id`, `username`, `nama`, `kode`, `Chapter`, `jawaban`, `jawabandb`, `skor`, `nilai`, `keterangan`, `guru`, `selesai`, `time`) VALUES
(142, 'andika tri prasetyo', 'andika tri prasetyo', '3A8yh', 'Newton 1', 'seharusnya jika lift di percepat maka skalanya menjadi kebih berat', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 18:26:18'),
(143, 'andika tri prasetyo', 'andika tri prasetyo', '3A8yh', 'Newton 2', 'Bola A, B dan C bergerak pada garis lurus dari kiri ke kanan. Saat t=0, bola A, B dan C melewati x=0, posisi bola pada setiap detik berikutnya ditunjukkan pada Gambar dibawah', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 18:27:12'),
(144, 'andika tri prasetyo', 'andika tri prasetyo', '3A8yh', 'Newton 3', 'F(2&rarr1) dan F(1&rarr2) adalah gaya yang sama besar, tetapi berlawanan arah.', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 18:29:04'),
(145, 'andika tri prasetyo', 'andika tri prasetyo', '3A8yh', 'Newton 4', 'Menggunakan hukum Newton II, diperoleh\r\n F=M a\r\nmg=(3m) a\r\n a=mg/3m\r\n a=g', '', '4', 'Pemahaman keseluruhan', '', 'm feby khoiru sidqi', 100, '2023-09-10 18:29:45'),
(146, 'andika tri prasetyo', 'andika tri prasetyo', '3A8yh', 'Newton 5', 'Tegangan tali T dapat dihitung dengan menggunakan hukum Newton II untuk balok m_2, yaitu:\r\nT - m_2 g = m_2 a\r\nT = m_2 g - m_2 a\r\nJika balok m_2 diam, maka percepatan a = 0.', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 18:31:32'),
(147, 'icha mulya', 'icha mulya', '3A8yh', 'Newton 1', 'skala nya sama dengan gaya berat ikan yaitu\r\nT = m g', '', '2', 'Miskonsepsi spesifik', '', 'm feby khoiru sidqi', 100, '2023-09-10 18:54:21'),
(148, 'icha mulya', 'icha mulya', '3A8yh', 'Newton 2', 'perbandingannya :untuk bola A tidak mengalami perubahan arah, artinya total gaya yang bekerja pada bola A adalah nol. Sementara itu, bola B dan C mengalami perpindahan atau perubahan arah yang sama, artinya total gaya yang bekerja pada bola B dan C adalah sama besar', '', '2', 'Miskonsepsi spesifik', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:02:17'),
(149, 'icha mulya', 'icha mulya', '3A8yh', 'Newton 3', 'Besar dua balok itu :\r\nBesarnya gaya F(1&rarr2 ) berbanding lurus dengan massa dari balok m2 karena gaya F(1&rarr2 ) adalah gaya tarik-menarik antara balok m1 dan balok m_2', '', '3', 'Pemahaman sebagian', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:05:18'),
(150, 'icha mulya', 'icha mulya', '3A8yh', 'Newton 4', 'Perhatikan Gambar dibawah ini, jika meja licin dan gesekan dengan katrol diabaikan, massa tali juga dianggap nol, percepatan gerakan sistem (a)', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:05:46'),
(151, 'icha mulya', 'icha mulya', '3A8yh', 'Newton 5', 'Balok berada di sepanjang bidang miring licin dihubungkan dengan balok , gesekan tali dengan katrol diabaikan dan massa tali juga dianggap nol, seperti terlihat pada Gambar dibawah ini. Ketika ditahan sehingga balok diam, tegangan tali sebesar . Jika balok dilepas, sehingga balok bergerak ke bawah dengan percepatan , berapa tegangan talinya?', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:06:41'),
(152, 'enggar fajri', 'enggar fajri', '3A8yh', 'Newton 1', 'jawab:\r\nT = ma_y + mg\r\nT = m(a + g)', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:08:58'),
(153, 'enggar fajri', 'enggar fajri', '3A8yh', 'Newton 2', '', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:11:21'),
(154, 'enggar fajri', 'enggar fajri', '3A8yh', 'Newton 3', 'Percepatan sistem dari dua balok ini adalah sama dengan percepatan balok m1.', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:12:56'),
(155, 'enggar fajri', 'enggar fajri', '3A8yh', 'Newton 4', 'Perhatikan Gambar dibawah ini, jika meja licin dan gesekan dengan katrol diabaikan, massa tali juga dianggap nol, percepatan gerakan sistem (a)', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:13:19'),
(156, 'enggar fajri', 'enggar fajri', '3A8yh', 'Newton 5', 'tidak tahu', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:14:10'),
(157, 'kayla aura zakia', 'kayla aura zakia', '3A8yh', 'Newton 1', 'skala yang tejadi adalah skala timbangan lebih besar daripada berat ikan karena lift bergerak ke atas', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:17:55'),
(158, 'kayla aura zakia', 'kayla aura zakia', '3A8yh', 'Newton 2', 'bola a tidak mengalami perubahan kecepatan, sedangkan bola b mengalami di percepat, dan bola c lebih cepat lagi', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:21:14'),
(159, 'kayla aura zakia', 'kayla aura zakia', '3A8yh', 'Newton 3', 'Besarnya gaya F1-2 sama dengan gaya F yang bekerja pada balok m1', '', '2', 'Miskonsepsi spesifik', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:23:03'),
(160, 'kayla aura zakia', 'kayla aura zakia', '3A8yh', 'Newton 4', 'Percepatan gerakan sistem ke bawah adalah g', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:25:26'),
(161, 'kayla aura zakia', 'kayla aura zakia', '3A8yh', 'Newton 5', 'Tegangan tali T pada balok dapat dihitung dengan menggunakan hukum Newton II untuk balok m2,:\r\nT - m2 g = m2 a\r\nT = m2 g - m2 a', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:27:44'),
(162, 'm agus hardiansyah', 'm agus hardiansyah', '3A8yh', 'Newton 1', 'Timbangannya akan mnjadi nilai yang lebih besar daripada berat ikan yang sesungguhnya karena lift bergerak dipercepat ke atas.', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:34:43'),
(163, 'm agus hardiansyah', 'm agus hardiansyah', '3A8yh', 'Newton 2', 'gaya yang bekerja pada bola A adalah nol, sedangkan resultan gaya yang bekerja pada bola B lebih besar dari nol, tetapi lebih kecil dari resultan gaya yang bekerja pada bola C.', '', '3', 'Pemahaman sebagian', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:38:26'),
(164, 'm agus hardiansyah', 'm agus hardiansyah', '3A8yh', 'Newton 3', 'Gaya yang terjadi antara kedua balok sama dengan gaya dorong yang diberikan pada balok ke 1.', '', '2', 'Miskonsepsi spesifik', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:39:41'),
(165, 'm agus hardiansyah', 'm agus hardiansyah', '3A8yh', 'Newton 4', 'percepatan sistem adalah g', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:50:10'),
(166, 'm agus hardiansyah', 'm agus hardiansyah', '3A8yh', 'Newton 5', 'tidak tau', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:50:37'),
(167, 'nabila putri yanti', 'nabila putri yanti', '3A8yh', 'Newton 1', 'Timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya karena lift bergerak dipercepat ke atas', '', '3', 'Pemahaman sebagian', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:56:14'),
(168, 'nabila putri yanti', 'nabila putri yanti', '3A8yh', 'Newton 2', 'gaya yang bekerja pada bola A adalah nol, sedangkan resultan gaya yang bekerja pada bola B dan C adalah sama besar.', '', '2', 'Miskonsepsi spesifik', '', 'm feby khoiru sidqi', 100, '2023-09-10 19:57:10'),
(169, 'nabila putri yanti', 'nabila putri yanti', '3A8yh', 'Newton 3', 'Gaya antara kedua balok adalah gaya yang bekerja pada balok 1 ke arah kiri. Gaya ini besarnya sama dengan gaya dorong yang diberikan pada balok 2, tetapi arahnya berlawanan. Gaya interaksi antara kedua balok ini dapat dihitung menggunakan hukum III Newton', '', '3', 'Pemahaman sebagian', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:01:34'),
(170, 'nabila putri yanti', 'nabila putri yanti', '3A8yh', 'Newton 4', 'Menggunakan hukum Newton II, diperoleh\r\n F=M a\r\nmg=(3m) a\r\n a=mg/3m\r\n a=g', '', '4', 'Pemahaman keseluruhan', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:02:24'),
(171, 'nabila putri yanti', 'nabila putri yanti', '3A8yh', 'Newton 5', 'Balok berada di sepanjang bidang miring licin dihubungkan dengan balok , gesekan tali dengan katrol diabaikan dan massa tali juga dianggap nol', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:02:47'),
(172, 'siti maimunah', 'siti maimunah', '3A8yh', 'Newton 1', 'skala nya mnejjadi lebih besar', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:06:42'),
(173, 'siti maimunah', 'siti maimunah', '12345', 'Newton 2', 'bola a akan mengalami gerak yang tetap, dan bola b akan cepat dan bola c', '', '1', 'Tidak paham', '', 'prof sidqi', 100, '2023-09-10 20:08:08'),
(174, 'siti maimunah', 'siti maimunah', '3A8yh', 'Newton 3', 'balok m1 lebih besar dari m2', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:09:37'),
(175, 'siti maimunah', 'siti maimunah', '3A8yh', 'Newton 4', 'Menggunakan hukum Newton II, diperoleh  F=M amg=(3m) a  a=mg/3m  a=g', '', '4', 'Pemahaman keseluruhan', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:11:23'),
(176, 'siti maimunah', 'siti maimunah', '3A8yh', 'Newton 5', 'Balok berada di sepanjang bidang miring licin dihubungkan dengan balok , gesekan tali dengan katrol diabaikan dan massa tali juga dianggap nol, seperti terlihat pada Gambar dibawah ini. Ketika ditahan sehingga balok diam, tegangan tali sebesar . Jika balok dilepas, sehingga balok bergerak ke bawah dengan percepatan', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:12:27'),
(177, 'rahma sari', 'rahma sari', '3A8yh', 'Newton 1', 'ikan akan menjadi lebih berat', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:13:58'),
(178, 'rahma sari', 'rahma sari', '3A8yh', 'Newton 2', 'bola a dan bola b bergerak sama sedangkan', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:14:32'),
(179, 'rahma sari', 'rahma sari', '3A8yh', 'Newton 3', 'balok m1 akan mengalami\r\nF - Gayag gesekan = m1 * a', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:16:53'),
(180, 'rahma sari', 'rahma sari', '3A8yh', 'Newton 4', 'Perhatikan Gambar dibawah ini, jika meja licin dan gesekan dengan katrol diabaikan, massa tali juga dianggap nol, percepatan gerakan sistem (a)', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:17:38'),
(181, 'rahma sari', 'rahma sari', '3A8yh', 'Newton 5', 'tegangan talinya adalah 0', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:18:21'),
(182, 'novia putri', 'novia putri', '3A8yh', 'Newton 1', 'tentunya timbangan akan jadi lebih berat', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:20:43'),
(183, 'novia putri', 'novia putri', '3A8yh', 'Newton 2', 'bola a dan bola b bergerak bersama bola c', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:22:01'),
(184, 'novia putri', 'novia putri', '3A8yh', 'Newton 3', 'Menggunakan hukum Newton II:\r\n F=M a\r\nmg=(3m) a\r\n a=mg/3m\r\n a=1/3 g', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:23:15'),
(185, 'novia putri', 'novia putri', '3A8yh', 'Newton 4', 'Menggunakan hukum Newton II, diperoleh\r\n F=M a\r\nmg=(3m) a\r\n a=mg/3m\r\n a=1/3 g', '', '4', 'Pemahaman keseluruhan', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:24:53'),
(186, 'novia putri', 'novia putri', '3A8yh', 'Newton 3', 'Hukum III Newton menyatakan bahwa gaya aksi sama dengan gaya reaksi', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:25:38'),
(187, 'novia putri', 'novia putri', '3A8yh', 'Newton 5', 'Tegangan tali lebih kecil dari gaya berat balok m2', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:27:41'),
(188, 'reza dwi putra', 'reza dwi putra', '3A8yh', 'Newton 1', 'Timbangannya akan menunjukkan nilai yang lebih besar daripada berat ikan karena lift bergerak dipercepat ke atas..', '', '3', 'Pemahaman sebagian', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:31:30'),
(189, 'reza dwi putra', 'reza dwi putra', '3A8yh', 'Newton 2', 'Bola B dan C bergerak dipercepat, perpindahan bola B diantara setiap posisi bertambah setiap waktu lebih kecil dari pada bola C, sehingga kecepatan bola B lebih kecil dari bola C. Perubahan kecepatan bola B setiap waktu lebih kecil dari pada bola C, sehingga percepatan bola B lebih kecil dari bola C.', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:33:17'),
(190, 'reza dwi putra', 'reza dwi putra', '3A8yh', 'Newton 3', 'gaya yang bekerja pada bola A adalah nol, sedangkan resultan gaya yang bekerja pada bola B dan C adalah sama besar.', '', '2', 'Miskonsepsi spesifik', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:34:06'),
(191, 'reza dwi putra', 'reza dwi putra', '3A8yh', 'Newton 3', 'Gaya yang terjadi antara kedua balok sama dengan gaya dorong yang diberikan pada balok ke 1.', '', '2', 'Miskonsepsi spesifik', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:37:34'),
(192, 'reza dwi putra', 'reza dwi putra', '3A8yh', 'Newton 4', 'Tegangan tali T sama dengan gaya normal benda 2m yaitusigma (F_y) N-mg=0', '', '2', 'Miskonsepsi spesifik', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:42:24'),
(193, 'reza dwi putra', 'reza dwi putra', '3A8yh', 'Newton 5', '', '', '1', 'Tidak paham', '', 'm feby khoiru sidqi', 100, '2023-09-10 20:42:48'),
(194, 'm feby khoiru sidqi', 'm feby khoiru sidqi', '12345', 'Newton 1', 'Seseorang menimbang ikan bermassa dengan timbangan yang digantungkan pada atap lift, seperti terlihat pada Gambar dibawah ini. Saat lift diam, skala pada timbangan menunjukkan angka 5 N', '', '1', 'Tidak paham', '', 'prof sidqi', 100, '2023-09-12 10:56:00'),
(195, 'm feby khoiru sidqi', 'm feby khoiru sidqi', '12345', 'Newton 1', 'Timbangan lebih besar berat ikan lebiih kecil lift bergerak dipercepat ke atas.', '', '1', 'Tidak paham', '', 'prof sidqi', 100, '2023-09-12 11:00:06'),
(197, 'sidqi', 'sidqi', '12345', 'Newton 1', 'Gaya yang bekerja pada ikan adalah gaya berat ke bawah dan tegangan tali T ke atas yang diberikan oleh timbangan. Jika lift bergerak dipercepat ke atas, aplikasi hukum II Newton pada ikan menghasilkan gaya total berikut.Tegangan tali T,Jika lift bergerak dipercepat ke atas, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya. Jadi, penunjukkan skala pada timbangan adalah menunjuk lebih dari 5 N', '', '4', 'Pemahaman keseluruhan', 'Jawaban mencakup semua komponen atau sebagian besar dari Jawaban dapat diterima secara ilmiah', 'prof sidqi', 100, '2023-10-21 13:41:42'),
(198, 'sidqi', 'sidqi', '12345', 'Newton 1', 'Gaya yang bekerja pada ikan adalah gaya berat ke bawah dan tegangan tali T ke atas yang diberikan oleh timbangan. Jika lift bergerak dipercepat ke atas, aplikasi hukum II Newton pada ikan menghasilkan gaya total berikut.Tegangan tali T,Jika lift bergerak dipercepat ke atas, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya. Jadi, penunjukkan skala pada timbangan adalah menunjuk lebih dari 5 N', '', '4', 'Pemahaman keseluruhan', 'Jawaban mencakup semua komponen atau sebagian besar dari Jawaban dapat diterima secara ilmiah', 'prof sidqi', 100, '2023-10-21 13:42:21'),
(199, 'sidqi', 'sidqi', '12345', 'Newton 1', 'Timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya karena lift bergerak dipercepat ke atas.hukum II Newton pada ikan menghasilkan gaya total berikutT = ma_y + mgT = m(a + g)', 'Penunjukkan skala pada timbangan saat lift bergerak dipercepat ke atas\nGaya yang bekerja pada ikan adalah gaya berat ke bawah w=mg dan tegangan tali T ke atas yang diberikan oleh timbangan. Jika lift bergerak dipercepat ke atas, aplikasi hukum II Newton pada ikan menghasilkan gaya total berikut.\nsigma (f=m.a)  T-mg=ma_y\n T=ma_y+ mg\nTegangan tali  T,\nT=m(a_y+ g)\nT=m(a+ g)\nJika lift bergerak dipercepat ke atas, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya.  Jadi, penunjukkan skala pada timbangan adalah menunjuk lebih dari 5 N', '3', 'Pemahaman sebagian', 'Jawaban mencakup setidaknya sebagian besar dari ide-ide yang dapat diterima dan menunjukkan pemahaman konsep, akan tetapi juga mengandung beberapa kesalahpahaman.', 'prof sidqi', 100, '2023-10-21 13:52:00'),
(200, 'sidqi', 'sidqi', '12345', 'Newton 1', 'eknaap denbga dj dad po', 'Penunjukkan skala pada timbangan saat lift bergerak dipercepat ke atas\nGaya yang bekerja pada ikan adalah gaya berat ke bawah w=mg dan tegangan tali T ke atas yang diberikan oleh timbangan. Jika lift bergerak dipercepat ke atas, aplikasi hukum II Newton pada ikan menghasilkan gaya total berikut.\nsigma (f=m.a)  T-mg=ma_y\n T=ma_y+ mg\nTegangan tali  T,\nT=m(a_y+ g)\nT=m(a+ g)\nJika lift bergerak dipercepat ke atas, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya.  Jadi, penunjukkan skala pada timbangan adalah menunjuk lebih dari 5 N', '1', 'Tidak paham', 'Mengulangi sebagian dari, atau seluruh pertanyaan atau tanggapan yang tidak relevan', 'prof sidqi', 100, '2023-10-21 18:32:41'),
(201, 'sidqi', 'Listrik Arus Searah 3', '12345', 'Newton 3', 'wqf iufw msa fifewi iw fuw iwf uw ifbw', '', '1', 'Tidak paham', '', 'prof sidqi', 100, '2024-01-16 21:31:03');

-- --------------------------------------------------------

--
-- Struktur dari tabel `kode`
--

CREATE TABLE `kode` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `dosen` text NOT NULL,
  `kelas` text NOT NULL,
  `tanggal` text NOT NULL,
  `kode` text NOT NULL,
  `time` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `kode`
--

INSERT INTO `kode` (`id`, `username`, `dosen`, `kelas`, `tanggal`, `kode`, `time`) VALUES
(1, 'prof sidqi', 'prof sidqi', 'dasd', 'dasd', '12345', '2023-07-23 23:53:08'),
(6, 'prof sidqi', 'prof sidqi', 'reguler A 2019', '2023-08-29', 'ffIrF', '2023-08-26 06:48:34'),
(7, 'prof sidqi', 'prof sidqi', '10 mia 2', '2023-08-26', 'S4HsI', '2023-08-26 10:07:01'),
(8, 'prof sidqi', 'prof sidqi', 'X MIPA 1', '2023-09-05', '9UesW', '2023-08-31 10:01:24'),
(9, 'prof sidqi', 'prof sidqi', 'X MIPA 1', '2023-09-05', '9UesW', '2023-08-31 10:02:16'),
(10, 'prof sidqi', 'prof sidqi', 'REGULAR B', '2023-09-03', 'TbLcg', '2023-09-02 20:43:21'),
(11, 'guru', 'guru', 'SMA ', '2023-09-06', 'NTGeJ', '2023-09-06 19:39:52'),
(12, 'm feby khoiru sidqi', 'm feby khoiru sidqi', 'KELAS 10', '2023-09-04', '3A8yh', '2023-09-10 18:05:23');

-- --------------------------------------------------------

--
-- Struktur dari tabel `login_guru`
--

CREATE TABLE `login_guru` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `login_guru`
--

INSERT INTO `login_guru` (`id`, `username`, `email`, `password`) VALUES
(12, 'prof sidqi', 'eki@gmail.com', '123'),
(13, 'guru', 'm2234@gmail.com', '123'),
(14, 'wawan', 'w@g.com', '123'),
(15, 'm feby khoiru sidqi', 'ekimansatubatanghari@gmail.com', '123');

-- --------------------------------------------------------

--
-- Struktur dari tabel `login_siswa`
--

CREATE TABLE `login_siswa` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `login_siswa`
--

INSERT INTO `login_siswa` (`id`, `username`, `email`, `password`) VALUES
(13, 'm feby khoiru sidqi', 'eki@gmail.com', '123'),
(15, 'sidqi', 'sidqi@gmail.com', 'sidqi'),
(16, 'siswa 1', 'siswa1@gmail.com', 'siswa1'),
(17, 'student 1', 'student@gmail.com', '123'),
(18, 'siswa 2', 'siswa@gmail.com', '123'),
(19, 'Nina Amelia Putri', 'ninaameliaputri2@gmail.com', 'ninaunja2023'),
(20, 'A1C323020', 'ta2467586@gmail.com', 'Yunita29'),
(21, 'Yunita', 'ta2467586@gmail.com', '291204'),
(22, 'A1C323008', 'melakhoirunnisa233@gmail.com', 'khoirunnisa030506'),
(23, 'siswa 5', 'mfebykhoirus@gmail.com', '123'),
(24, 'azmi aufa ', 'azmiaufaa22@gmail.com', 'Azmi aufa1612'),
(25, 'Cindy Aulia Phadila', 'cindyvee73@gmail.com', 'khalisutndy816032'),
(26, 'Challilullah ', 'challilullahtungkal@gmail.com', '270305'),
(27, 'Clara Arimbi Dwi Putri', 'claudiaarindia212@gmail.com', '@clara_arimbi2006'),
(28, 'tamara nissa saputri', 'maraputri44@gmail.com', 'mada putri1212'),
(29, 'Nafisa Maharani', 'nafisa.maharani06@gmail.com', 'Maharani_16'),
(30, 'A1C323026', 'nasranijuntak@gmail.com', 'fisika123'),
(31, 'Iqbal kurniady', 'Iqbalkurniady2018@gmail.com', 'sandi123'),
(32, 'Esti kurnia wati/reguler b', 'estkurnia10@gmail.com', '12345678'),
(33, 'Tuti supriyanti ', 'tsupriyanti060@gmail.com', 'siswa23'),
(34, 'A1C323044', 'liasihombing664@gmail.com', 'Katasandi123.'),
(35, 'guru', 'm2234@gmail.com', '123'),
(36, 'andika tri prasetyo', 'andika1234567@gmail.com', '123'),
(37, 'icha mulya', 'ichacantik@gmail.com', '123'),
(38, 'enggar fajri', 'fajriganteng123@gmail.com', '123'),
(39, 'kayla aura zakia', 'kaylaaz@gmail.com', '123'),
(40, 'm agus hardiansyah', 'agusmuhammad@gmail.com', '123'),
(41, 'nabila putri yanti', 'nabila@gmail.com', '123'),
(42, 'siti maimunah', 'maimunahsiti@gmail.com', '123'),
(43, 'rahma sari', 'rahmas06@gmail.com', 'rahma123'),
(44, 'novia putri', 'nvputri@gmail.com', 'novia'),
(45, 'reza dwi putra', 'rezadptra@gmail.com', 'reza');

-- --------------------------------------------------------

--
-- Struktur dari tabel `profil_guru`
--

CREATE TABLE `profil_guru` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `nama` text NOT NULL,
  `nip` text NOT NULL,
  `user` text NOT NULL,
  `email` text NOT NULL,
  `universitas` text NOT NULL,
  `prodi` text NOT NULL,
  `alamat` text NOT NULL,
  `nohp` text NOT NULL,
  `time` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `profil_guru`
--

INSERT INTO `profil_guru` (`id`, `username`, `nama`, `nip`, `user`, `email`, `universitas`, `prodi`, `alamat`, `nohp`, `time`) VALUES
(8, 'prof sidqi', 'M Feby Khoiru Sidqi ', '051001', 'prof sidqi', 'eki@gmail.com', 'MIT ', 'AI MACHINE LEQARNIG', 'sanghai', '08xxxx', '2023-08-26 06:49:04');

-- --------------------------------------------------------

--
-- Struktur dari tabel `profil_siswa`
--

CREATE TABLE `profil_siswa` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `nama` text NOT NULL,
  `nim` text NOT NULL,
  `user` text NOT NULL,
  `email` text NOT NULL,
  `universitas` text NOT NULL,
  `prodi` text NOT NULL,
  `alamat` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `profil_siswa`
--

INSERT INTO `profil_siswa` (`id`, `username`, `nama`, `nim`, `user`, `email`, `universitas`, `prodi`, `alamat`) VALUES
(6, 'm feby khoiru sidqi', 'm feby khoiru sidqi', 'a1c319011', 'sidqi', 'mfebykhoirus@gmail.com', 'MAN 1 Batanghari', 'MIPA', 'Bulian'),
(8, 'm feby khoiru sidqi', 'm feby khoiru sidqi', 'a1c319011', 'sidqi', 'mfebykhoirus@gmail.com', 'MAN 1 Batanghari', 'MIPA', 'Bulian'),
(9, 'm feby khoiru sidqi', 'm feby khoiru sidqi', 'a1c319011', 'sidqi', 'mfebykhoirus@gmail.com', 'MAN 1 Batanghari', 'MIPA', 'Bulian'),
(10, 'Nina Amelia Putri', 'NINA AMELIA PUTRI', 'putri', 'Nina Amelia Putri ', 'ninaameliaputri2@gmail.com', 'Unja', 'Pendidikan Fisika ', 'jalan Petaling Blok a'),
(11, 'azmi aufa ', 'Azmi Aufa Ibti Samah', 'A1C323022', 'azmi aufa', 'azmiaufaa22@gmail.com', 'Universitas Jambi', 'Pendidikan Fisika', 'Jln. Prabu Siliwangi'),
(12, 'sidqi', 'm feby khoiru sidqi', 'a1c329011', 'sidqi', 'mfebykhoirus@gmail.com', 'MAN 1 Batanghari', 'MIPA', 'Kanada');

-- --------------------------------------------------------

--
-- Struktur dari tabel `soal_2`
--

CREATE TABLE `soal_2` (
  `id` int(11) NOT NULL,
  `jawaban` text NOT NULL,
  `labels` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `soal_2`
--

INSERT INTO `soal_2` (`id`, `jawaban`, `labels`) VALUES
(5, 'Bola A bergerak dengan kecepatan konstan, percepatan bola A adalah nol, sehingga resultan gaya yang bekerja pada bola A adalah nol (Bola B dan C bergerak dipercepat, perpindahan bola B diantara setiap posisi bertambah setiap waktu lebih kecil dari pada bola C, sehingga kecepatan bola B lebih kecil dari bola C. Perubahan kecepatan bola B setiap waktu lebih kecil dari pada bola C, sehingga percepatan bola B lebih kecil dari bola C. Jadi, resultan gaya bola C lebih besar dari pada resultan gaya B ()\nPerbandingan resultan gaya yang bekerja pada bola A, B dan C adalah ', 4),
(6, 'Resultan gaya yang bekerja pada bola A adalah nol, sedangkan resultan gaya yang bekerja pada bola B lebih besar dari nol, tetapi lebih kecil dari resultan gaya yang bekerja pada bola C.', 3),
(7, 'Resultan gaya yang bekerja pada bola A adalah nol, sedangkan resultan gaya yang bekerja pada bola B dan C adalah sama besar.', 2),
(8, 'Resultan gaya yang bekerja pada bola A, B, dan C adalah sama besar.', 1),
(9, 'Bola A, B dan C bergerak pada garis lurus dari kiri ke kanan. Saat t=0, bola A, B dan C melewati x=0,posisi bola pada setiap detik berikutnya ditunjukkan pada Gambar dibawah ini. .....', 1),
(10, '', 1),
(11, 'Resultan gaya yang bekerja pada bola A, B, dan C adalah sama besar.', 1),
(12, 'Bola A, B dan C bergerak pada garis lurus dari kiri ke kanan. Saat t=0, bola A, B dan C melewati x=0, posisi bola pada setiap detik berikutnya ditunjukkan pada Gambar dibawah', 1),
(13, 'perbandingannya :untuk bola A tidak mengalami perubahan arah, artinya total gaya yang bekerja pada bola A adalah nol. Sementara itu, bola B dan C mengalami perpindahan atau perubahan arah yang sama, artinya total gaya yang bekerja pada bola B dan C adalah sama besar', 2),
(14, '', 1),
(15, 'bola a tidak mengalami perubahan kecepatan, sedangkan bola b mengalami di percepat, dan bola c lebih cepat lagi', 1),
(16, 'gaya yang bekerja pada bola A adalah nol, sedangkan resultan gaya yang bekerja pada bola B lebih besar dari nol, tetapi lebih kecil dari resultan gaya yang bekerja pada bola C.', 3),
(17, 'gaya yang bekerja pada bola A adalah nol, sedangkan resultan gaya yang bekerja pada bola B dan C adalah sama besar.', 2),
(18, 'bola a akan mengalami gerak yang tetap, dan bola b akan cepat dan bola c', 1),
(19, 'bola a dan bola b bergerak sama sedangkan', 1),
(20, 'bola a dan bola b bergerak bersama bola c', 1),
(21, 'Bola B dan C bergerak dipercepat, perpindahan bola B diantara setiap posisi bertambah setiap waktu lebih kecil dari pada bola C, sehingga kecepatan bola B lebih kecil dari bola C. Perubahan kecepatan bola B setiap waktu lebih kecil dari pada bola C, sehingga percepatan bola B lebih kecil dari bola C.', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `soal_3`
--

CREATE TABLE `soal_3` (
  `id` int(11) NOT NULL,
  `jawaban` text NOT NULL,
  `labels` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `soal_3`
--

INSERT INTO `soal_3` (`id`, `jawaban`, `labels`) VALUES
(4, 'Menganggap gabungan dua balok sebagai \r\nsatu sistem sigma(F_x (sistem)=)  F=(m_1+m_2 ) ( a)_x a_x=F/(m_1+m_2 )  \r\nGaya dorong yang bekerja pada m_1 adalah gaya F ⃗ ke kanan dan  F(2→1 ) ke kiri (gaya yang dikerjakan oleh m_2 pada m_1). Dari hukum III Newton,  F(2→1 )adalah gaya reaksi terhadap  F(1→2 )sehingga  F(2→1 )= F(1→2). Menggunakan Hukum II Newton pada m_1 menghasilkan, sigma(Fx=a)  F- F_(2→1 )=(F-F_(1→2 )=m)1 (a)x\r\n(F-F_(1→2 )=m)_1 ( a)_x\r\n〖F_(1→2 )=F-m〗_1 〖 a〗_x\r\n〖F_(1→2 )=F-m〗_1 (F/(m_1+m_2 ))\r\nF_(1→2 )=(m_2/(m_1+m_2 ))F\r\n', 4),
(5, 'Gaya horizontal yang bekerja pada m_2 adalah gaya F(1→2 ) (gaya yang dikerjakan oleh m_1  pada m_2), yang arahnya ke kanan. Menggunakan hukum II Newton, diperoleh\r\n∑(F_x=)  F_(1→2 )=m_2 〖 a〗_x\r\nF_(1→2 )=m_2 (F/(m_1+m_2 ))\r\nF_(1→2 )=(m_2/(m_1+m_2 ))F\r\n', 4),
(7, 'F ⃗> F ⃗_(2→1)\r\nHukum  III Newton: F ⃗_(2→1 )adalah gaya reaksi terhadap  F ⃗_(1→2 ), sehingga F ⃗\\_(1→2 )< F\r\n', 4),
(8, 'Gaya interaksi antara kedua balok adalah gaya yang bekerja pada balok 1 ke arah kiri. Gaya ini besarnya sama dengan gaya dorong yang diberikan pada balok 2, tetapi arahnya berlawanan. Gaya interaksi antara kedua balok ini dapat dihitung menggunakan hukum III Newton,gaya interaksi antara kedua balok dapat dihitung sebagai berikut:\r\nF(1 → 2) = -F(2 → 1)\r\n', 3),
(9, 'Gaya interaksi antara kedua balok sama dengan gaya dorong yang diberikan pada balok 1.', 2),
(10, 'Percepatan sistem dua balok adalah sama dengan percepatan balok 1.', 1),
(11, '', 1),
(12, 'Dua balok diletakkan pada meja yang licin didorong dengan gaya F ⃗ seperti pada Gambar dibawah ini. Jika F ⃗_(1→2 ) merupakan gaya yang dikerjakan oleh m_1 pada m_2, besarnya F ⃗_(1→2 ) adalah . ', 1),
(13, 'Besarnya gaya F(1→2 ) berbanding lurus dengan massa m_2 karena gaya F(1→2 ) adalah gaya tarik-menarik antara m_1 dan m_2. Semakin besar massa m_2, maka gaya tarik-menarik antara m_1 dan m_2 juga semakin besar.', 3),
(14, 'Besarnya gaya F(1→2 ) sama dengan gaya F yang bekerja pada m_1.', 2),
(15, 'Gaya F(1→2 ) sama dengan gaya gravitasi yang bekerja pada m_2', 1),
(16, '', 1),
(17, 'Hukum III Newton menyatakan bahwa gaya aksi sama dengan gaya reaksi, tetapi arahnya berlawanan. Oleh karena itu, F_(1→2) adalah gaya aksi yang bekerja pada benda 1 oleh benda 2. Besarnya F_(1→2) sama dengan besar F_(2→1).', 3),
(18, 'F_(2→1) adalah gaya yang bekerja pada benda 2 oleh benda 1. Oleh karena itu, F_(1→2) harus lebih besar daripada F_(2→1', 2),
(19, 'Hukum III Newton menyatakan bahwa gaya aksi sama dengan gaya reaksi. Oleh karena itu, F_(1→2) = F_(2→1).', 1),
(20, '', 1),
(22, 'Besar dua balok itu :\r\nBesarnya gaya F(1&rarr2 ) berbanding lurus dengan massa dari balok m2 karena gaya F(1&rarr2 ) adalah gaya tarik-menarik antara balok m1 dan balok m_2', 3),
(23, 'Percepatan sistem dari dua balok ini adalah sama dengan percepatan balok m1.', 1),
(24, 'Besarnya gaya F1-2 sama dengan gaya F yang bekerja pada balok m1', 2),
(25, 'Gaya yang terjadi antara kedua balok sama dengan gaya dorong yang diberikan pada balok ke 1.', 2),
(26, 'Gaya antara kedua balok adalah gaya yang bekerja pada balok 1 ke arah kiri. Gaya ini besarnya sama dengan gaya dorong yang diberikan pada balok 2, tetapi arahnya berlawanan. Gaya interaksi antara kedua balok ini dapat dihitung menggunakan hukum III Newton', 3),
(27, 'balok m1 lebih besar dari m2', 1),
(28, 'balok m1 akan mengalami\r\nF - Gayag gesekan = m1 * a', 1),
(29, 'Menggunakan hukum Newton II:\r\n F=M a\r\nmg=(3m) a\r\n a=mg/3m\r\n a=1/3 g', 1),
(30, 'Hukum III Newton menyatakan bahwa gaya aksi sama dengan gaya reaksi', 1),
(32, 'Gaya yang terjadi antara kedua balok sama dengan gaya dorong yang diberikan pada balok ke 1.', 2),
(33, 'wqf iufw msa fifewi iw fuw iwf uw ifbw', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `soal_4`
--

CREATE TABLE `soal_4` (
  `id` int(11) NOT NULL,
  `jawaban` text NOT NULL,
  `labels` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `soal_4`
--

INSERT INTO `soal_4` (`id`, `jawaban`, `labels`) VALUES
(4, 'Diagram benda bebas 1 sistem: \r\nM = m + m + m\r\nMenggunakan hukum Newton II, diperoleh\r\n    F=M a\r\n mg=(3m) a\r\n     a=mg/3m;\r\n     a=1/3  g\r\n\r\n', 4),
(5, 'Benda 2m bergerak ke kanan, gaya horisontal yang bekerja pada 2m adalah tegangan tali T ke kanan. Gaya vertikal yang bekerja pada 2m adalah gaya normal N ke atas dan gaya berat 2mg ke bawah. Menggunakan hukum Newton II, diperoleh\r\n(1)     ∑▒〖F_x=〗  T=2m a\r\n(2)     ∑▒〖F_y=〗  N-mg=0\r\n\r\nDiagram benda bebas:\r\nBenda m bergerak ke bawah, arah ke bawah sebagai arah positif. Gaya vertikal yang bekerja pada m adalah tegangan tali T ke atas dan gaya berat mg ke bawah. Menggunakan hukum Newton II, diperoleh,\r\n(3)   ∑〖F_y=〗  mg-T=m a\r\nPercepatan gerakan sistem ke bawah. Ketika (1) ditambah dengan (3), T saling meniadakan, sehingga diperoleh\r\nT+mg-T=2m a+m a\r\nmg=3 m a;\r\n a=1/3 g\r\n', 4),
(6, 'Diagram benda bebas 1 sistem:\nMenggunakan hukum Newton II, diperoleh\n    F=M a\n mg=(3m) a\n     a=mg/3m;\n     a=1/3  g\nJadi, percepatan sistem adalah 1/3 g.\n', 3),
(7, 'Diagram benda bebas 1 sistem:\nMenggunakan hukum Newton II, diperoleh\n    F=M a\n mg=(3m) a\n     a=mg/3m;\n     a=g\n', 2),
(8, 'Tiga benda dengan massa m digantungkan pada tali yang sama. Jika tali tidak meregang, maka percepatan sistem adalah g.', 1),
(9, 'Perhatikan Gambar dibawah ini, jika meja licin dan gesekan dengan katrol diabaikan, massa tali juga dianggap nol, percepatan gerakan sistem (a) adalah ', 1),
(10, '', 1),
(11, 'Percepatan gerakan sistem ke bawah adalah 1/3 g.\r\ndengan rumus\r\nmg=3 m a;\r\n a=1/3 g\r\n', 3),
(12, 'Tegangan tali T sama dengan gaya normal benda 2m\nsigma (F_y)  N-mg=0', 2),
(13, 'Benda 2m bergerak ke kanan dan benda m bergerak ke bawah\r\nT=2m a\r\nmg-T=m a\r\n', 1),
(14, '', 1),
(15, 'Bodo amat', 1),
(16, 'Menggunakan hukum Newton II, diperoleh\r\n F=M a\r\nmg=(3m) a\r\n a=mg/3m\r\n a=g', 4),
(17, 'Perhatikan Gambar dibawah ini, jika meja licin dan gesekan dengan katrol diabaikan, massa tali juga dianggap nol, percepatan gerakan sistem (a)', 1),
(18, 'Perhatikan Gambar dibawah ini, jika meja licin dan gesekan dengan katrol diabaikan, massa tali juga dianggap nol, percepatan gerakan sistem (a)', 1),
(19, 'Percepatan gerakan sistem ke bawah adalah g', 1),
(20, 'percepatan sistem adalah g', 1),
(21, 'Menggunakan hukum Newton II, diperoleh\r\n F=M a\r\nmg=(3m) a\r\n a=mg/3m\r\n a=g', 4),
(22, 'Menggunakan hukum Newton II, diperoleh  F=M amg=(3m) a  a=mg/3m  a=g', 4),
(23, 'Perhatikan Gambar dibawah ini, jika meja licin dan gesekan dengan katrol diabaikan, massa tali juga dianggap nol, percepatan gerakan sistem (a)', 1),
(24, 'Menggunakan hukum Newton II, diperoleh\r\n F=M a\r\nmg=(3m) a\r\n a=mg/3m\r\n a=1/3 g', 4),
(25, 'Tegangan tali T sama dengan gaya normal benda 2m yaitusigma (F_y) N-mg=0', 2);

-- --------------------------------------------------------

--
-- Struktur dari tabel `soal_5`
--

CREATE TABLE `soal_5` (
  `id` int(11) NOT NULL,
  `jawaban` text NOT NULL,
  `labels` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `soal_5`
--

INSERT INTO `soal_5` (`id`, `jawaban`, `labels`) VALUES
(4, 'Diagram benda bebas m_1:\nKetika balok m_1  dilepas, sehingga balok m_2 bergerak ke bawah dengan percepatan a ⃗.\nMenggunakan hukum Newton II pada diperoleh:\n(1)     sigma〖F_x=〗  T-m_1 g sin⁡θ=m_1 a\n(2)     sigma〖F_y=〗  N-m_1 g cos⁡θ=0\n\nDiagram benda bebas m_2:\n\nMenggunakan hukum Newton II diperoleh,\n(1)     sigma〖F_x=〗 0\n(2)     sigma〖F_y=〗  m_2 g-T=m_2 a\nT=m_2 g-m_2 a\n                        T=m_2 (g-a)\nJadi, ketika balok m_1  dilepas, sehingga balok m_2 bergerak ke bawah dengan percepatan a ⃗, tegangan tali lebih kecil dari m_2 g.\n', 4),
(5, 'Tegangan tali T lebih kecil dari gaya berat balok m_2 karena balok m_2 bergerak ke bawah dengan percepatan a.\r\n  sigma〖F_x=〗  T-m_1 g sin⁡θ=m_1 a\r\nsigma〖F_y=〗  N-m_1 g cos⁡θ=\r\n', 3),
(6, 'Tegangan tali T lebih kecil dari gaya berat balok m_2 karena balok m_2 bergerak ke bawah dengan percepatan a', 1),
(7, 'Tegangan tali T ini disebabkan oleh gaya tarik yang diberikan oleh balok m_1 pada balok m_2.', 1),
(8, 'Balok m_1 berada di sepanjang bidang miring licin dihubungkan dengan balok m_2, gesekan tali dengan katrol diabaikan dan massa tali juga dianggap nol, seperti terlihat pada Gambar dibawah ini. Ketika m_1 ditahan sehingga balok diam, tegangan tali sebesar T=m_2 g. Jika balok m_1  dilepas, sehingga balok m_2 bergerak ke bawah dengan percepatan a ', 1),
(9, '', 1),
(10, 'Tegangan tali T sama dengan gaya berat balok m_2\r\nTegangan tali T dapat dihitung dengan menggunakan hukum Newton II untuk balok m_2, yaitu:\r\nT - m_2 g = m_2 a\r\nT = m_2 g - m_2 a', 2),
(11, 'saya tisdak tahu', 1),
(12, 'm feby khoriu sidqi A2 MENJADI C3\r\ndiketahui :\r\ntekanan = &rho.g.h', 1),
(13, 'Tegangan tali T dapat dihitung dengan menggunakan hukum Newton II untuk balok m_2, yaitu:\r\nT - m_2 g = m_2 a\r\nT = m_2 g - m_2 a\r\nJika balok m_2 diam, maka percepatan a = 0.', 1),
(14, 'Balok berada di sepanjang bidang miring licin dihubungkan dengan balok , gesekan tali dengan katrol diabaikan dan massa tali juga dianggap nol, seperti terlihat pada Gambar dibawah ini. Ketika ditahan sehingga balok diam, tegangan tali sebesar . Jika balok dilepas, sehingga balok bergerak ke bawah dengan percepatan , berapa tegangan talinya?', 1),
(15, 'tidak tahu', 1),
(16, 'Tegangan tali T pada balok dapat dihitung dengan menggunakan hukum Newton II untuk balok m2,:\r\nT - m2 g = m2 a\r\nT = m2 g - m2 a', 1),
(17, 'tidak tau', 1),
(18, 'Balok berada di sepanjang bidang miring licin dihubungkan dengan balok , gesekan tali dengan katrol diabaikan dan massa tali juga dianggap nol', 1),
(19, 'Balok berada di sepanjang bidang miring licin dihubungkan dengan balok , gesekan tali dengan katrol diabaikan dan massa tali juga dianggap nol, seperti terlihat pada Gambar dibawah ini. Ketika ditahan sehingga balok diam, tegangan tali sebesar . Jika balok dilepas, sehingga balok bergerak ke bawah dengan percepatan', 1),
(20, 'tegangan talinya adalah 0', 1),
(21, 'Tegangan tali lebih kecil dari gaya berat balok m2', 1),
(22, '', 1);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin_db`
--
ALTER TABLE `admin_db`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `db_soal`
--
ALTER TABLE `db_soal`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `hasil_siswa`
--
ALTER TABLE `hasil_siswa`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `kode`
--
ALTER TABLE `kode`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `login_guru`
--
ALTER TABLE `login_guru`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `login_siswa`
--
ALTER TABLE `login_siswa`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `profil_guru`
--
ALTER TABLE `profil_guru`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `profil_siswa`
--
ALTER TABLE `profil_siswa`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `soal_2`
--
ALTER TABLE `soal_2`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `soal_3`
--
ALTER TABLE `soal_3`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `soal_4`
--
ALTER TABLE `soal_4`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `soal_5`
--
ALTER TABLE `soal_5`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `admin_db`
--
ALTER TABLE `admin_db`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `db_soal`
--
ALTER TABLE `db_soal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT untuk tabel `hasil_siswa`
--
ALTER TABLE `hasil_siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=202;

--
-- AUTO_INCREMENT untuk tabel `kode`
--
ALTER TABLE `kode`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `login_guru`
--
ALTER TABLE `login_guru`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT untuk tabel `login_siswa`
--
ALTER TABLE `login_siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT untuk tabel `profil_guru`
--
ALTER TABLE `profil_guru`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `profil_siswa`
--
ALTER TABLE `profil_siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `soal_2`
--
ALTER TABLE `soal_2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT untuk tabel `soal_3`
--
ALTER TABLE `soal_3`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT untuk tabel `soal_4`
--
ALTER TABLE `soal_4`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT untuk tabel `soal_5`
--
ALTER TABLE `soal_5`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
