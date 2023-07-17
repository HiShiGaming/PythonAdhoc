def is_palindrome(s):
    # Hàm kiểm tra xem chuỗi s có đối xứng hay không
    return s == s[::-1]

def longest_palindrome(s):
    # Hàm trả về chiều dài của chuỗi đối xứng dài nhất trong chuỗi s
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j+1]):
                max_len = max(max_len, j-i+1)
    return max_len

# Nhập chuỗi ký tự S từ bàn phím
S = input("Nhập chuỗi ký tự S: ")
# Nhập dữ liệu vào file
with open("do_dai_chuoi_doi_xung.inp", 'w+') as f:
    f.write(str(S))
# Tìm chiều dài chuỗi đối xứng dài nhất trong S
max_palindrome_len = longest_palindrome(S)

# Xuất kết quả ra file
with open("do_dai_chuoi_doi_xung.out", 'w+') as g:
    g.write(str(max_palindrome_len))
                
