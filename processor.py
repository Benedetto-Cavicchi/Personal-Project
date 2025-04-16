import fitz  # PyMuPDF
import language_tool_python
import re

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyze_notes(text):
    suggestions = []
    notes = re.findall(r"\[\d+\]", text)
    if not notes:
        suggestions.append({
            "message": "Nessuna nota rilevata. Verifica che le citazioni siano correttamente formattate.",
            "rule": "Controllo Note"
        })
    else:
        note_numbers = [int(n[1:-1]) for n in notes]
        if sorted(note_numbers) != list(range(1, len(note_numbers)+1)):
            suggestions.append({
                "message": "Numerazione delle note non sequenziale.",
                "rule": "Controllo Note"
            })
    return suggestions

def check_formatting(text):
    suggestions = []
    if "  " in text:
        suggestions.append({
            "message": "Trovate doppie spaziature nel testo.",
            "rule": "Controllo Formattazione"
        })
    if any(line.isupper() and len(line) > 10 for line in text.splitlines()):
        suggestions.append({
            "message": "Titoli eccessivamente in maiuscolo.",
            "rule": "Controllo Formattazione"
        })
    return suggestions

def process_pdf(uploaded_file):
    text = extract_text_from_pdf(uploaded_file)

    tool = language_tool_python.LanguageTool('it-IT')
    matches = tool.check(text)

    grammar_suggestions = []
    for match in matches:
        grammar_suggestions.append({
            "message": match.message,
            "rule": match.ruleId,
            "offset": match.offset,
            "length": match.errorLength
        })

    note_suggestions = analyze_notes(text)
    formatting_suggestions = check_formatting(text)

    all_suggestions = grammar_suggestions + note_suggestions + formatting_suggestions
    return text, all_suggestions
