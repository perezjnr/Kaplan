# Starter Code for Library Borrowing System

catalogue = {
    "book_001": {"title": "1984", "author": "George Orwell", "copies": 3},
    "book_002": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "copies": 2},
}

def borrowing_allowed(current_books):
    return current_books < 3

def calculate_late_fee(days_late):
    return days_late * 0.50

def is_book_available(book_id):
    return catalogue[book_id]["copies"] > 0

def main():
    print("Library System Starter Template")

if __name__ == "__main__":
    main()
