import csv
import requests

def get_book_info(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()
    if 'items' in data and len(data['items']) > 0:
        book = data['items'][0]['volumeInfo']
        title = book.get('title', '')
        authors = ', '.join(book.get('authors', []))
        published_date = book.get('publishedDate', '')
        publisher = book.get('publisher', '')
        thumbnail = book['imageLinks'].get('thumbnail', '') if 'imageLinks' in book else ''
        description = book.get('description', '')
        return [authors, title, published_date, publisher, thumbnail, description]
    else:
        return None

def main(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='', encoding='utf-8-sig') as outfile:
        isbns = infile.readlines()
        writer = csv.writer(outfile)
        writer.writerow(['Author', 'Title', 'Published Date', 'Publisher', 'Thumbnail', 'Description'])
        for isbn in isbns:
            isbn = isbn.strip()
            book_info = get_book_info(isbn)
            if book_info:
                writer.writerow(book_info)

if __name__ == "__main__":
    input_file = "input.txt"  # Change this to your input text file
    output_file = "output.csv"  # Change this to your desired output CSV file
    main(input_file, output_file)
