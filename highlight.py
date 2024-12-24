import re

# Highlighting logic
def highlight_word(word, text_color, underline_style, underline_color):
    return f'<span style="color: {text_color}; text-decoration: {underline_style} {underline_color};">{word}</span>'

# Define patterns for each word type (make sure to replace these with real terms)
patterns = {
    "Terminology": r"\b(?:terminology1|terminology2)\b",  # Replace with real terms
    "Newly introduced words": r"\b(?:newword1|newword2)\b",  # Replace with real terms
    "Definitions": r"\b(?:define|meaning|refers to)\b",
    "Formulas and Units": r"\b(?:cm|kg|m/s)\b",  # Example units
    "Dates and Numbers": r"\b(?:\d{1,4}[-/]\d{1,2}[-/]\d{1,4}|\d+)\b",
    "Names": r"\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b",  # Matches proper nouns
    "Processes and Steps": r"\b(?:step|process|method)\b",
    "Examples": r"\b(?:e\.g\.|for example|such as)\b",
    "Exceptions": r"\b(?:except|excluding|other than)\b",
    "Synonyms and Antonyms": r"\b(?:similar|opposite|synonym|antonym)\b",
    "Diagrams and Labels": r"\b(?:diagram|label|figure)\b",
    "Cause-Effect Relationships": r"\b(?:because|therefore|leads to)\b",
    "Foreign Words": r"\b(?:foreignword1|foreignword2)\b",  # Replace with real terms
    "Rules or Theories": r"\b(?:law|theory|principle)\b",
    "Abbreviations and Acronyms": r"\b(?:NASA|UNICEF|etc)\b",
    "Lists": r"\b(?:list|items|bullet points)\b"
}

def process_highlight(paragraph, words_to_highlight, underline_style="solid", underline_color="#ffdd00", text_color="#000000"):
    for category, pattern in patterns.items():
        # Only highlight if the category is in the words_to_highlight list
        if category in words_to_highlight:
            # Apply the regex replacement
            paragraph = re.sub(pattern, lambda match: highlight_word(match.group(0), text_color, underline_style, underline_color), paragraph, flags=re.IGNORECASE)
    
    return paragraph