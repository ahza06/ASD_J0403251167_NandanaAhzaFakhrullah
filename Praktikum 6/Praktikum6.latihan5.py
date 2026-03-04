__________________________ = "Lengkapi"

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
     if __________________________:
      result.append(left[i])
     i += 1
    else:
     result.append(right[j])
     j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Soal:
# 1. Lengkapi kondisi agar menjadi ascending.
# 2. Jelaskan fungsi result.extend().

#[Jawaban]
# 1. 
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: #Jawaban nomer 1
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 2. Extend berfungsi untuk menambahkan elemen sisa yang belum terbaca keujung list yang sudah ada