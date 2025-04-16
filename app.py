import streamlit as st
from processor import process_pdf
from document_generator import generate_docx_with_comments

st.set_page_config(page_title="Revisore AI per testi giuridici")

st.title("📚 Revisore AI per testi giuridici")
st.markdown("Carica un documento PDF. Il sistema farà una revisione grammaticale, controllerà le note e la formattazione, poi ti restituirà un file Word con i commenti.")

uploaded_file = st.file_uploader("📤 Carica un PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("📖 Estrazione e analisi in corso..."):
        extracted_text, suggestions = process_pdf(uploaded_file)
        docx_file = generate_docx_with_comments(extracted_text, suggestions)

    st.success("✅ Revisione completata!")
    st.download_button("⬇️ Scarica il documento Word con i commenti", docx_file, file_name="revisione_commentata.docx")

    with st.expander("📄 Testo estratto"):
        st.text(extracted_text)

    with st.expander("📝 Suggerimenti di revisione"):
        for s in suggestions:
            st.markdown(f"- **{s['rule']}**: {s['message']}")
