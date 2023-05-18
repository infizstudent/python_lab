import os
import urllib.request


def get_text_from_url(url_text):
    response = urllib.request.urlopen(url_text)
    return response.read().decode('utf-8')


def extract_chapters(text_book, o_file):
    output_dir = 'data'
    if not os.path.exists(output_dir):  # make decorator
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, o_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines([line for line in text_book.split('\n') if line.startswith('CHAPTER')])


if __name__ == ' __main__ ':
    url = 'https://www.gutenberg.org/files/521/521-0.txt'
    output_file = 'chapters.txt'
    text = get_text_from_url(url)
    extract_chapters(text, output_file)
