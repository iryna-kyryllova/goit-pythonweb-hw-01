from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> list[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> list[Book]:
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.show_books()
        for book in books:
            logging.info(
                f"Title: {book.title}, Author: {book.author}, Year: {book.year}"
            )


def main():

    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = int(input("Enter book year: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
