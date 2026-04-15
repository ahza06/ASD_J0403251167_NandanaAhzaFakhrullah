#==============================================
#Nama: Nandana Ahza Fakhrullah
#NIM:J0403521167
#Kelas: TPL B1
#==============================================

#==============================================
#Merge Sort dengan Tracing
#==============================================
def merge_sort(data, depth=0):
    indent = " " * depth #Indentasi berdasarkan level rekursif 
    print(f"{indent}merge_sort){data}")

    if len(data) <= 1:
        return data
        #Divide: Membagi data menjadi 2 bagian
    mid = len(data) // 2
    left_half = data[:mid] #slicing kiri
    right_half = data[mid:] #slicing kanan

    print(f"{indent}divide -> left = {left_half} | right = {right_half}")

    #Recursive call
    l_sort = merge_sort(left_half)
    r_sort = merge_sort(right_half)

    merged = merge(l_sort, r_sort)
    print(f"{indent}merge -. {l_sort} + {r_sort} = {merged}")

    return merge(left_half, right_half)

def merge(left_half, right_half):

    result = []
    i = 0
    j = 0

    #Membandingkan elemen kiri dan kanan 
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    #Menambahan sisa elemen jika dipindahkan apabila masih terdapat sisa
    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result

angka = [13, 7, 28, 5, 19, 36, 4]
print("Hasil Sorting", merge_sort(angka)) 
