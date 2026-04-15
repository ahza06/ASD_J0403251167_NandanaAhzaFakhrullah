#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Merge Sort 
#Atur Base Case 
#Slicing
#Sort Hasil Slicing
#Merging kedua Slices
#Function Merging
#Place Holder
#Conditional
#Merging Sisa menggunakan extend
#==============================================
def merge_sort(data):
    if len(data) <= 1:
        return data
    slicing = len(data) // 2
    left_half = data[:slicing]
    right_half = data[slicing:]

    l_sort = merge_sort(left_half)
    r_sort = merge_sort(right_half)
    merged = merge(l_sort, r_sort)
    return merged

def merge(left_half, right_half):
    result = []
    i = 0
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i = i+1
        else:
            result.append(right_half[j])
            j = j+1

    result.extend(left_half[i:])
    result.extend(right_half[j:])
    
    return result
 
angka = [12, 10, 5, 7, 11, 4, 1, 3]
print(f"Angka Sebelum Disortir: ", angka)
print(f"Angka Setelah Disortir: ", merge_sort(angka))