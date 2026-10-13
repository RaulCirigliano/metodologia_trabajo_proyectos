import os
import re
from bs4 import BeautifulSoup
import pykakasi

kks = pykakasi.kakasi()

def kanji_to_ruby(text):
    result = kks.convert(text)
    ruby_text = ""
    for item in result:
        orig = item['orig']
        hira = item['hira']
        
        # Check if orig contains any kanji
        if not re.search(r'[\u4e00-\u9faf]', orig):
            ruby_text += orig
            continue
            
        # It has Kanji. Find the common suffix between orig and hira
        suffix_len = 0
        while suffix_len < len(orig) and suffix_len < len(hira) and orig[-(suffix_len+1)] == hira[-(suffix_len+1)]:
            suffix_len += 1
            
        if suffix_len > 0:
            kanji_part = orig[:-suffix_len]
            reading_part = hira[:-suffix_len]
            okurigana = orig[-suffix_len:]
            
            if kanji_part:
                ruby_text += f"<ruby>{kanji_part}<rt>{reading_part}</rt></ruby>{okurigana}"
            else:
                ruby_text += orig
        else:
            ruby_text += f"<ruby>{orig}<rt>{hira}</rt></ruby>"
            
    return ruby_text

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    modified = False
    for text_node in soup.find_all(string=True):
        parent = text_node.parent
        if parent.name in ['script', 'style', 'head', 'title', 'iframe', 'ruby', 'rt']:
            continue
            
        if re.search(r'[\u4e00-\u9faf]', text_node):
            new_html = kanji_to_ruby(text_node)
            if new_html != text_node:
                new_soup = BeautifulSoup(new_html, 'html.parser')
                text_node.replace_with(new_soup)
                modified = True
                
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Added furigana to {filepath}")
    else:
        print(f"No kanji found in {filepath}")

if __name__ == '__main__':
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    for filename in os.listdir(base_dir):
        if filename.endswith(".html"):
            process_file(os.path.join(base_dir, filename))
    print("Done!")
