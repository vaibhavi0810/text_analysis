import streamlit as st
from collections import Counter
import string
def file_statistics(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    # Number of characters
    num_chars = len(text)
    # Number of lines
    num_lines = text.count('\n') + 1
    # Remove punctuation and convert to lower case for word analysis
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    # Number of words
    num_words = len(words)
    # Unique words
    unique_words = set(words)
    num_unique_words = len(unique_words)
    # Most common words
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(10)  # Top 10 most common words
    return {
        'characters': num_chars,
        'lines': num_lines,
        'words': num_words,
        'unique_words': num_unique_words,
        'most_common_words': most_common_words,
    }
# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        font-family: Arial, sans-serif;
    }
    h1, h2, h3 {
        color: #3f51b5;
    }
    .stButton button {
        background-color: #3f51b5;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #303f9f;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# App title
st.title("Text File Analysis")
# File uploader
uploaded_file = st.file_uploader("Choose a text file", type="txt")
if uploaded_file is not None:
    # Save the uploaded file
    with open("uploaded_file.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    # Perform file analysis
    stats = file_statistics("uploaded_file.txt")
    # Display results
    st.header("File Statistics")
    st.write(f"**Number of characters**: {stats['characters']}")
    st.write(f"**Number of lines**: {stats['lines']}")
    st.write(f"**Number of words**: {stats['words']}")
    st.write(f"**Number of unique words**: {stats['unique_words']}")
    st.header("Most Common Words")
    for word, count in stats['most_common_words']:
        st.write(f"**{word}**: {count} times")
    # Optional: Download analyzed data
    if st.button("Download Analysis"):
        analysis_text = (
            f"Number of characters: {stats['characters']}\n"
            f"Number of lines: {stats['lines']}\n"
            f"Number of words: {stats['words']}\n"
            f"Number of unique words: {stats['unique_words']}\n\n"
            "Most Common Words:\n"
        )
        for word, count in stats['most_common_words']:
            analysis_text += f"{word}: {count} times\n"
        
        with open("analysis.txt", "w") as f:
            f.write(analysis_text)
        st.success("Analysis saved as analysis.txt")
else:
    st.info("Please upload a text file to analyze.")