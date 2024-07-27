import requests  # Library to handle HTTP requests
import csv  # Library to handle CSV file operations

def get_book_info(isbn):
    # Construct the URL for Google Books API
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the JSON response
    data = response.json()
    # Check if the response contains book information
    if 'items' in data and len(data['items']) > 0:
        book = data['items'][0]['volumeInfo']
        # Extract book details
        title = book.get('title', '')
        authors = ', '.join(book.get('authors', []))
        published_date = book.get('publishedDate', '')
        publisher = book.get('publisher', '')
        thumbnail = book['imageLinks'].get('thumbnail', '') if 'imageLinks' in book else ''
        description = book.get('description', '')
        return [isbn, authors, title, published_date, publisher, thumbnail, description]
    else:
        return None  # Return None if no book information is found

def main(input_file, output_file):
    # Open the input and output files
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='', encoding='utf-8-sig') as outfile:
        isbns = infile.readlines()  # Read ISBNs from the input file
        writer = csv.writer(outfile)  # Initialize CSV writer
        # Write CSV header
        writer.writerow(['ISBN', 'Author', 'Title', 'Published Date', 'Publisher', 'Thumbnail', 'Description'])
        for isbn in isbns:
            isbn = isbn.strip()  # Remove any leading/trailing whitespace
            book_info = get_book_info(isbn)  # Get book information
            if book_info:
                writer.writerow(book_info)  # Write book information to CSV
                print("[+] ISBN " + isbn + " added succesfully")
            else:
                print("[ERROR] No information found for ISBN " + isbn)

if __name__ == "__main__":
    input_file = "input.txt"  # Change this to your input text file
    output_file = "output.csv"  # Change this to your desired output CSV file
    main(input_file, output_file)  # Call the main function with input and output file paths
