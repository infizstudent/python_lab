import sqlite3
import requests
import re


def connect_to_database():
    conn = sqlite3.connect('books.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS books
                 (title TEXT, content TEXT)''')
    return conn


def download_book(url, conn):
    r = requests.get(url)
    content = r.content.decode('utf-8')
    conn.execute('INSERT INTO books (title, content) VALUES (?, ?)',
                 ('The Life and Adventures of Robinson Crusoe', content))
    conn.close()
    return content


def extract_chapters(content):
    with open("chapters.txt", "w") as f:
        for match in re.findall(r"CHAPTER [IVXLCDM]+—.*\n", content):
            f.write(match.strip() + "\n")


if __name__ == "__main__":
    conn = connect_to_database()
    content = download_book("https://www.gutenberg.org/files/521/521-0.txt", conn)
    extract_chapters(content)
    conn.close()


