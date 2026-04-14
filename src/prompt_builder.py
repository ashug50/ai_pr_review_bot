from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROMPT_FILE = BASE_DIR / "prompts" / "review_prompt.txt"

def build_prompt(file_path, diff_text):
    template = PROMPT_FILE.read_text(encoding="utf-8")
    return template.format(file_path=file_path, diff=diff_text)
