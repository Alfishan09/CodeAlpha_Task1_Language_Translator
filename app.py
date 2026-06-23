import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

st.set_page_config(
page_title="Language Translation Tool",
page_icon="🌍",
layout="centered"
)

st.markdown(
"""
<h1 style='text-align: center;'>🌍 Language Translation Tool</h1>
<p style='text-align: center; color: gray;'>
Translate text instantly into multiple languages.
</p>
""",
unsafe_allow_html=True
)

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

source_lang = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

text = st.text_area("Enter Text")

if st.button("Translate"):

    if text == "":
        st.warning("Please enter text")

    else:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Completed")

    st.write("### Translated Text")
    st.write(translated)

    tts = gTTS(text=translated, lang="hi")

    tts.save("translation.mp3")

    audio_file = open("translation.mp3", "rb")
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/mp3")
st.markdown(
    """
    <div style="text-align: center; margin-top: 30px;">
        <p style="font-size:18px; margin-bottom:0;">
            🚀 Developed by Alfishan Khan
        </p>
        <p style="font-size:15px; color:#5f6368; font-style:italic; margin-top:2px;">
            Artificial Intelligence Intern at CodeAlpha
        </p>
    </div>
    """,
    unsafe_allow_html=True
)