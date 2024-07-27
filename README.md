# ISBN Info Fetcher

Fetch book information using ISBN numbers and save it to a CSV file.

## Overview

This script fetches book details (author, title, published date, publisher, thumbnail, and description) from the Google Books API using ISBN numbers and writes the data to a CSV file.

## Usage

1. **Input File**: Create a text file (`input.txt` by default) with one ISBN per line. *Tip: Use a barcode scanner app to quickly generate this list*
2. **Output File**: The script outputs a CSV file (`output.csv` by default) with the book information.

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/danielbarl/isbn-info-fetcher.git
    cd isbn-info-fetcher
    ```

2. Install the required Python packages:
    ```bash
    pip install requests
    ```

3. Run the script:
    ```bash
    python get_isbn_infos.py
    ```

## Example

### Input (`input.txt`)

```txt
9780143128540
9780262033848
9780131103627
```

### Output (`output.csv`)
```csv
ISBN,Author,Title,Published Date,Publisher,Thumbnail,Description
"9780143128540","Paul Kalanithi","When Breath Becomes Air","2016-01-12","Random House","http://books.google.com/books/content?id=wZ4uCgAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",""
"9780262033848","Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein","Introduction to Algorithms","2009-07-31","MIT Press","http://books.google.com/books/content?id=2BdDwmF3P5EC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",""
"9780131103627","Brian W. Kernighan, Dennis M. Ritchie","The C Programming Language","1988","Prentice Hall","http://books.google.com/books/content?id=8G72QgAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",""
```
