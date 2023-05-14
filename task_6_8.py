import os
import urllib.request

def get_text_from_url(url):
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    return text

def extract_chapters(text, output_file):
    output_dir = 'data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in text.split('\n'):
            if line.startswith('CHAPTER'):
                f.write(line)

if __name__ == '__main__':
    url = 'https://www.gutenberg.org/files/521/521-0.txt'
    output_file = 'chapters.txt'
    text = get_text_from_url(url)
    extract_chapters(text, output_file)
