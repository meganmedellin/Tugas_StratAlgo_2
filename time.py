import time

# List bilangan yang akan dihitung rata-ratanya
bilangan = [7, 2, 5, 11, 9]

# Catat waktu awal
start_time = time.time()

# Hitung rata-rata bilangan
rata_rata = sum(bilangan) / len(bilangan)

# Catat waktu akhir
end_time = time.time()

# Hitung selisih waktu
elapsed_time = end_time - start_time

# Mengonversi waktu menjadi satuan milisecond
time_milisecond = elapsed_time * 1000

# Tampilkan hasil rata-rata dan waktu yang dibutuhkan
print("Rata-rata: ", rata_rata)
print("Waktu yang dibutuhkan: ", time_milisecond, " milisecond")
