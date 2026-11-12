class Book:
    def __init__(self, pages=0, author="", price=0, edition=1, title=""):
        self.__pages = pages
        self.__author = author
        self.__price = price
        self.edition = edition
        self.title = title

    def get_pages(self):
        return self.__pages

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def __str__(self):
        return self.title + ", " + self.__author + ", " + str(self.__pages) + " стор., " + str(self.__price) + " грн"

    def __repr__(self):
        return "Book(" + str(self.__pages) + ", " + self.__author + ", " + str(self.__price) + ")"

    def __del__(self):
        print("Об'єкт знищено:", self.title)

def main():
    book1 = Book(title="Абетка")
    book2 = Book(256, "Іван Франко", 400, 2, "Захар Беркут")
    book3 = Book(352, "Іван Котляревський", 230, 1, "Енеїда")
    book4 = Book(256, "Леся Українка", 350, 3, "Лісова пісня")

    for book in [book1, book2, book3, book4]:
        print("Назва:", book.title)
        print("Видання:", book.edition)
        print("Автор:", book.get_author())
        print("Сторінок:", book.get_pages())
        print("Ціна:", book.get_price())
        print(str(book))
        print(repr(book))
        print()

main()
