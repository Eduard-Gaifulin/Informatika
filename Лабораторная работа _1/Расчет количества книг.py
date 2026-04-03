# TODO Найдите количество книг, которое можно разместить на дискете
# Параметры дискеты
disk_mb = 1.44  # Мб

# Параметры книги
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Вычисляем объем одной книги в байтах
total_chars = pages * lines_per_page * chars_per_line
book_bytes = total_chars * bytes_per_char

# Переводим объем дискеты в байты
disk_bytes = disk_mb * 1024 * 1024

# Рассчитываем количество книг
books_count = int(disk_bytes // book_bytes)

print("Количество книг, помещающихся на дискету:", books_count)
