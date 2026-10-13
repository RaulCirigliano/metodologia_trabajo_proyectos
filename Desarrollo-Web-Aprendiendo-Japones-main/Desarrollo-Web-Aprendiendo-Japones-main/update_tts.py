import os
import glob
import re

def update_tts_in_lessons():
    target_dir = r"c:\Users\raulc\Desktop\Desarrollo Web Aprendiendo Japones\nihongo-app\lessons"
    html_files = glob.glob(os.path.join(target_dir, "*.html"))
    
    new_func = """function playAudio(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = 'ja-JP';
                utterance.rate = 0.9;
                
                const setVoiceAndSpeak = () => {
                    const voices = window.speechSynthesis.getVoices();
                    // Priorizar voces premium de Edge o Chrome
                    let bestVoice = voices.find(v => v.lang.includes('ja') && (v.name.includes('Online') || v.name.includes('Natural') || v.name.includes('Google')));
                    if (!bestVoice) {
                        bestVoice = voices.find(v => v.lang.includes('ja'));
                    }
                    if (bestVoice) {
                        utterance.voice = bestVoice;
                    }
                    window.speechSynthesis.speak(utterance);
                };

                if (window.speechSynthesis.getVoices().length === 0) {
                    window.speechSynthesis.onvoiceschanged = setVoiceAndSpeak;
                } else {
                    setVoiceAndSpeak();
                }
            }
        }"""
    
    pattern = re.compile(r"function playAudio\(text\)\s*\{[\s\S]*?window\.speechSynthesis\.speak\(utterance\);\s*\}\s*\}")
    
    updated_count = 0
    failed_count = 0
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "function playAudio(text)" in content:
            new_content, count = pattern.subn(new_func, content)
            if count > 0:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_count += 1
            else:
                # Might have already been updated or different signature
                print(f"Failed to match regex in: {os.path.basename(filepath)}")
                failed_count += 1
                
    print(f"Total files updated: {updated_count}")
    print(f"Total files failed/skipped: {failed_count}")

if __name__ == "__main__":
    update_tts_in_lessons()
