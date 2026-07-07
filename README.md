# Maze Search - BFS & DFS

Program ini merupakan implementasi algoritma **Breadth First Search (BFS)** dan **Depth First Search (DFS)** untuk mencari jalur pada sebuah labirin yang dihasilkan secara otomatis (Maze Generator).

Selain pencarian jalur, program juga dapat membandingkan performa kedua algoritma berdasarkan:

- Panjang jalur
- Jumlah node yang dieksplorasi
- Waktu eksekusi
- Penggunaan memori

---

# Fitur

- Generate labirin secara otomatis
- Pencarian jalur menggunakan BFS
- Pencarian jalur menggunakan DFS
- Perbandingan performa BFS dan DFS
- Benchmark pada berbagai ukuran labirin
- Menampilkan hasil benchmark

---

# Persyaratan

Program dibuat menggunakan **Python 3** dan hanya menggunakan library bawaan Python.

Library yang digunakan:

- random
- time
- csv
- tracemalloc
- collections (deque)

Tidak memerlukan instalasi package tambahan.

---

# Cara Menjalankan Program

Buka terminal atau Command Prompt, kemudian jalankan:

```bash
python MazeSearch.py
```

Apabila nama file berbeda, sesuaikan dengan nama file Anda.

---

# Menu Program

Saat program dijalankan akan muncul menu berikut.

```
=============================================
      SISTEM PENCARIAN JALUR LABIRIN
=============================================

1. Generate Labirin
2. Cari Jalur
3. Bandingkan BFS vs DFS
4. Benchmark
0. Keluar
```

---

# Petunjuk Penggunaan

## 1. Generate Labirin

Pilih menu:

```
1
```

Kemudian masukkan ukuran labirin.

Contoh:

```
Jumlah node baris : 10
Jumlah node kolom : 10
```

Program akan menghasilkan labirin beserta titik:

- **S** = Start
- **E** = Goal

---

## 2. Cari Jalur

Setelah labirin berhasil dibuat, pilih:

```
2
```

Kemudian pilih algoritma.

```
1. Breadth First Search (BFS)
2. Depth First Search (DFS)
```

Program akan menampilkan:

- Jalur yang ditemukan
- Status pencarian
- Panjang jalur
- Jumlah node yang dieksplorasi
- Waktu eksekusi
- Penggunaan memori

Jalur hasil pencarian akan ditandai dengan simbol:

```
★
```

---

## 3. Bandingkan BFS dan DFS

Pilih menu:

```
3
```

Program akan menjalankan kedua algoritma kemudian menampilkan tabel perbandingan meliputi:

- Status pencarian
- Panjang jalur
- Node yang dieksplorasi
- Waktu eksekusi
- Penggunaan memori

---

## 4. Benchmark

Pilih menu:

```
4
```

Program akan menguji performa BFS dan DFS pada beberapa ukuran labirin:

- 7 × 7
- 10 × 10
- 16 × 16
- 23 × 23

Hasil benchmark otomatis disimpan ke file:

```
benchmark.csv
```

---

# Simbol Labirin

| Simbol | Keterangan |
|---------|------------|
| █ | Dinding |
| · | Jalur |
| S | Titik awal |
| E | Titik tujuan |
| ★ | Jalur hasil pencarian |

---

# Struktur Program

Program terdiri dari tiga bagian utama.

### Part 1
- Maze Generator
- Helper Function
- Tampilan Labirin

### Part 2
- Breadth First Search (BFS)
- Depth First Search (DFS)
- Perbandingan Algoritma
- Benchmark

### Part 3
- Menu Utama
- Generate Labirin
- Cari Jalur
- Benchmark
- Perbandingan Algoritma

---

# Output Program

Program menghasilkan beberapa output, antara lain:

- Visualisasi labirin
- Jalur hasil pencarian
- Statistik algoritma
- Tabel perbandingan BFS dan DFS
- File benchmark (`benchmark.csv`)

---

# Penulis

Program ini dibuat sebagai implementasi algoritma pencarian (Graph Search) menggunakan **Breadth First Search (BFS)** dan **Depth First Search (DFS)** pada kasus pencarian jalur dalam labirin.