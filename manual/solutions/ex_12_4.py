# Using books.csv, do the following:
# read the CSV file
# create two other CSV files: mathematics_books.csv and
# computer_science_books.csv, containing only books in each genre (Genre column
# should be equal to mathematics or computer_science, respectively), with all
# columns in books.csv except Genre
from pathlib import Path
import csv

# resolve will make the path absolute; it is needed to fetch the parent path
current_path = Path().resolve()
books_file = current_path.parent / "docs" / "books.csv"
math_file = current_path / "mathematics_books.csv"
cs_file = current_path / "computer_science_books.csv"

with books_file.open() as f, math_file.open("w") as math_f, cs_file.open("w") as cs_f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames.copy()
    fieldnames.remove("Genre")

    math_writer = csv.DictWriter(math_f, fieldnames=fieldnames)
    cs_writer = csv.DictWriter(cs_f, fieldnames=fieldnames)

    math_writer.writeheader()
    cs_writer.writeheader()

    for row in reader:
        genre = row.pop("Genre")
        if genre == "mathematics":
            math_writer.writerow(row)
        elif genre == "computer_science":
            cs_writer.writerow(row)
