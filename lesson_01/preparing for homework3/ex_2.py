from book import book

library = [
    book('The master and Margarita', 'Mikhail Bulgakov'),
    book('The Brothers Karamazov', 'Fyodor Dostoevsky'),
    book('The fate of man', 'Mikhail Sholokhov')
]

for book in library:
    print(f'{book.title} - {book.author}')