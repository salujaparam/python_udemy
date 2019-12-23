from utils import database

def menu():
    database.create_book_table()
    ans = input('-a for adding a book,\n-r for marking a book as read,\n-l for listing all the books,\n-d for deleting a book and\n-q to quit.')
    while(ans!='q'):
        if ans=='a':
            name = input('Name of the book: ')
            author = input('Author of th book: ')
            database.add(name, author)
        elif ans=='r':
            name = input('Name the book you want to mark as read? ')
            database.read(name)
            print('\n The book has been marked as read \n')
        elif ans=='l':
            books = database.all_books()

            for book in books:
                if len(books) == 0:
                    print('\n No books to show \n')
                    break
                print('\nName of the book:', book['name'])
                print('Author of the book: ', book['author'])
                print('Has the book been read?', book['read'], '\n')
        elif ans=='d':
            name = input('Name the book you want to delete? ')
            database.delete_book(name)
            print('\n The book has been deletd \n')
        else:
            print('Enter correctly...')
        
        ans = input('-a for adding a book,\n-r for marking a book as read,\n-l for listing all the books,\n-d for deleting a book and\n-q to quit.')
menu()