# 📚 Legal Reviewer AI – Revisore per Testi Giuridici

Questa applicazione Streamlit consente di caricare un file PDF con testo giuridico e ricevere in output un documento Word con:

- ✅ Revisione grammaticale e sintattica automatica (commenti)
- 📝 Verifica della correttezza delle **note** (es. numerazione, presenza)
- 🧾 Controllo basilare della **formattazione** (es. doppie spaziature, titoli in maiuscolo)

## 🚀 Come funziona

1. **Carica un PDF** contenente testo giuridico (no immagini/scansioni).
2. Il sistema analizza il testo con strumenti AI open source (`language_tool_python`).
3. Genera un file `.docx` con i commenti e suggerimenti.
4. Puoi **scaricare il file Word** o vedere il testo e gli avvisi direttamente online.

## 📦 Librerie utilizzate

- `streamlit`
- `python-docx`
- `language-tool-python`
- `PyMuPDF` per l'estrazione del testo dai PDF
- `markdown2` (per uso futuro)

## 💻 Esegui localmente (opzionale)

```bash
pip install -r requirements.txt
streamlit run app.py

