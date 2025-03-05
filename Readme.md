# Extractive Text Summarization Using NLP

## 📌 Project Overview
This project implements **Extractive Text Summarization** using **Natural Language Processing (NLP)** techniques. It selects the most important sentences from a given text based on **word frequency analysis**.

## 📜 How It Works
1. **Tokenization** → Splits text into sentences and words.
2. **Stopword Removal** → Filters out common words like "the", "is".
3. **Word Frequency Calculation** → Identifies important words.
4. **Sentence Scoring** → Assigns scores to sentences based on important words.
5. **Top Sentence Selection** → Picks key sentences to form the summary.

## ⚙️ Installation
Before running the script, install the required dependencies:
```bash
pip install nltk
```
Download necessary NLTK datasets:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## 🚀 Usage
1. Clone the repository:
```bash
git clone https://github.com/your-username/text-summarization.git
cd text-summarization
```
2. Run the script:
```bash
python text_summarization.py
```
3. Enter the number of sentences you want in the summary.

## 📝 Example Input & Output
**Input:**
```plaintext
"Artificial intelligence (AI) is the simulation of human intelligence in machines..."
```
**Output:**
```plaintext
"AI is the simulation of human intelligence. AI has various applications in decision-making and automation."
```

## 📂 File Structure
```
📁 text-summarization/
├── text_summarization.py  # Main Python script
├── README.md  # Project documentation
```

## 🌟 Features
- Extracts key sentences from a long document.
- Uses **NLTK** for text processing.
- Adjustable summary length.

## 📌 To-Do
- [ ] Add support for Abstractive Summarization.
- [ ] Implement TF-IDF scoring for better sentence selection.
- [ ] Deploy as a web app using Flask or Streamlit.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.



