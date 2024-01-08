book_pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

book_time = (book_pages // pages_per_hour)
book_hours = (book_time // days_per_book)

print(book_hours)