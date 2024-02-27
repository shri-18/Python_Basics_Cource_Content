file_path = 'C:/1-python/Day 5 (File Handling)/pi_digits.txt'
with open (file_path) as filex:
    content = filex.read()
print(content.rstrip())    