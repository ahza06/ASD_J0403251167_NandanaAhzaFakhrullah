#=================================================
#Nama   : Nandana Ahza Fakhrullah
#NIM    : J0403251167
#Kelas  : B1
#=================================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
# Representasi weighted graph menggunakan dictionary bersarang
# Bikin peta rute dan jarak antar titik
graph = {
    'A': {'B': 4, 'C': 2}, # Dari A ke B jaraknya 4, ke C jaraknya 2
    'B': {'D': 5},         # Dari B ke D jaraknya 5
    'C': {'D': 1},         # Dari C ke D jaraknya 1
    'D': {}                # D adalah tujuan akhir, jadi gak ada jalan lagi
}

# Hitung total jarak untuk masing-masing pilihan rute
jalur_1 = graph['A']['B'] + graph['B']['D']  # Rute pertama lewat B (A -> B -> D)
jalur_2 = graph['A']['C'] + graph['C']['D']  # Rute kedua lewat C (A -> C -> D)

# Tampilkan hasil hitungannya ke layar
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Bandingkan, mana jalur yang angkanya lebih kecil (lebih cepat sampai)
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")
    
'''
Pertanyaan:
1. Berapa total bobot jalur A -> B -> D?
2. Berapa total bobot jalur A -> C -> D?
3. Jalur mana yang dipilih sebagai jalur terpendek?
4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
'''
'''
Jawaban:
1.  9
2.  3
3.  A -> C -> D
4.  Karena bobot edge dapat bervariasi, dan jalur terpendek ditentukan berdasarkan total bobot, bukan jumlah edge.
'''
