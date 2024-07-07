from mongoengine import *

class Book(Document):
    title = StringField()
    author = StringField()
    genre = StringField()
    published_year = IntField()

# Filter books where the author is 'Jane Austen' and the genre is 'Fiction'
books = Book.objects(author='Jane Austen', genre='Fiction')

# Filter books where the author is 'Jane Austen' and the published year is greater than 1800
books = Book.objects(author='Jane Austen', published_year__gt=1800)


from mongoengine.queryset.visitor import Q

# Filter books where the author is 'Jane Austen' and the genre is 'Fiction' or 'Romance'
books = Book.objects(Q(author='Jane Austen') & (Q(genre='Fiction') | Q(genre='Romance')))

# Filter books where the author is 'Jane Austen' or 'Charles Dickens', and the published year is greater than 1800
books = Book.objects((Q(author='Jane Austen') | Q(author='Charles Dickens')) & Q(published_year__gt=1800))


# Filter books where the genre is 'Fiction' or 'Romance'
genres = ['Fiction', 'Romance']
books = Book.objects(genre__in=genres)
