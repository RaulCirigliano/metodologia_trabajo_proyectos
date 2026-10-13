import json
import os
import sys
import re

def inject_exercises(json_file):
    base_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for lesson_id, questions in data.items():
        filepath = os.path.join(base_dir, f"lesson-{lesson_id}.html")
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if f'2. {questions[0]["q"]}' in content:
            print(f"Lesson {lesson_id} already has exercises.")
            continue
            
        new_html = ""
        for i, q in enumerate(questions, start=2):
            new_html += f'''
        <div class="question-block" style="background:#fff; border:1px solid #e2e8f0; padding:1.5rem; border-radius:10px; margin-bottom:1rem;">
            <p style="font-weight:600; margin-bottom:1rem; font-size:1.1rem;">{i}. {q['q']}</p>
            <div style="display:grid; gap:10px;">'''
            for opt in q['options']:
                correct_str = "true" if opt['correct'] else "false"
                new_html += f'''
                <button class="option-btn" data-correct="{correct_str}" style="padding:1rem; border:2px solid #e2e8f0; border-radius:8px; cursor:pointer; text-align:left; background:#f8fafc; font-family:var(--font-jp);">{opt['text']}</button>'''
            
            new_html += '''
            </div>
            <div class="feedback-msg" style="margin-top:10px; font-weight:600; min-height:24px;"></div>
        </div>'''
        
        # We will insert it just before `    </div>\n\n    <script src="../js/main.js">`
        # Because spacing might vary, let's use regex
        
        pattern = r'(\s*</div>\s*<script src="\.\./js/main\.js">)'
        if re.search(pattern, content):
            new_content = re.sub(pattern, new_html + r'\1', content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added exercises to Lesson {lesson_id}")
        else:
            print(f"Failed to find insert marker in Lesson {lesson_id}")

if __name__ == '__main__':
    inject_exercises(sys.argv[1])
