#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Latihan4: Memahami Kode Program
#==============================================

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge_sort(left_sorted, right_sorted)

# Soal:
# 1. Apa yang dimaksud dengan base case?
# 2. Mengapa fungsi memanggil dirinya sendiri?
# 3. Apa tujuan fungsi merge()?

#[Jawaban]
# 1. Kondisi dimana program akan berhenti berjalan
# 2. Ini namanya rekursi, program melakukan rekursi untuk mempermudah suatu proses agar mencapai base case
# 3. Setelah proses rekursi terjadi, data yang sudah dipecah disatukan kembali agar tersusun, rapih atau tidak tergantung coder
