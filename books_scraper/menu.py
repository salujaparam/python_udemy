import logging

from app import books

logger = logging.getLogger('scrapping.menu')

USER_CHOICE = '''Enter one of the following
- 'b' to lokk at 5-star books
- 'c' to look at the cheapest books
- 'n' to just the next available book on the catalogue
- 'q' to exit
Enter your choice:
'''

def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: (x.rating*-1, x.price))
    b_books = []
    for book in best_books:
        b_books.append(book)
    return b_books


def print_cheapest_books():
    logger.info('Finding cheapest books...')
    cheapest_books = sorted(books, key=lambda x: x.price)
    c_books = []
    for book in cheapest_books:
        c_books.append(book)
    return c_books

books_generator = (x for x in books)
def get_next_book():
    logger.info('Finding the next book in catalogue')
    return [next(books_generator)]

user_choice = {
    'b': print_best_books(),
    'c': print_cheapest_books(),
    'n': get_next_book()
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ['b', 'c', 'n']:
            for book in user_choice[user_input]:
                print(book)
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')

menu() 