# TODO Найдите количество книг, которое можно разместить на дискете

disk_capacity = 1.44
amount_of_pages = 100
str_in_pages = 50
symbols_in_str = 25
code_size = 4

size_of_one_book = code_size * symbols_in_str * str_in_pages * amount_of_pages
books_amount = (disk_capacity*1024*1024)//size_of_one_book

print("Количество книг, помещающихся на дискету:", int(books_amount))
