# Import required libraries
import nltk  # Natural Language Toolkit for text processing
import heapq  # Used for selecting top-ranked sentences
import re  # Regular expressions for text preprocessing
from nltk.tokenize import sent_tokenize, word_tokenize  # For sentence and word tokenization
from nltk.corpus import stopwords  # Stopwords (common words like 'the', 'is', etc.)

# Download necessary NLTK datasets
nltk.download('punkt')  # For tokenizing sentences and words
nltk.download('stopwords')  # Stopwords for filtering out common words

def extractive_summarization(text, num_sentences=3):
    """
    Performs extractive text summarization by selecting the most important sentences.

    Parameters:
        text (str): The input text to summarize.
        num_sentences (int): The number of sentences to include in the summary.

    Returns:
        str: The summarized text.
    """
    
    # Step 1: Tokenize the text into sentences
    sentences = sent_tokenize(text)  # Splits text into a list of sentences

    # Step 2: Preprocess the text (remove special characters and stopwords)
    word_frequencies = {}  # Dictionary to store word frequencies
    stop_words = set(stopwords.words('english'))  # Get stopwords in English

    for sentence in sentences:  # Loop through each sentence
        # Remove non-alphabetic characters and convert to lowercase
        words = word_tokenize(re.sub(r'[^a-zA-Z]', ' ', sentence.lower()))  
        for word in words:  # Process each word
            if word not in stop_words:  # Exclude stopwords
                word_frequencies[word] = word_frequencies.get(word, 0) + 1  # Increment frequency

    # Step 3: Compute sentence scores based on word frequencies
    sentence_scores = {}  # Dictionary to store sentence importance scores
    for sentence in sentences:  # Loop through sentences again
        for word in word_tokenize(sentence.lower()):  # Process each word
            if word in word_frequencies:  # If the word is important
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    # Step 4: Select the top-ranked sentences for the summary
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)  # Combine selected sentences into final summary

    return summary  # Return the summarized text

# Example Usage
text = """Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language.
It enables machines to understand, interpret, and generate human language in a way that is both meaningful and useful.
Some common applications of NLP include chatbots, sentiment analysis, and language translation.
By leveraging NLP techniques, businesses can automate tasks such as summarizing long documents and extracting key information."""

summary = extractive_summarization(text, num_sentences=2)  # Generate summary with 2 sentences
print("Summary:", summary)  # Print summarized text
