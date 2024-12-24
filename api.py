
from flask import Flask, request, jsonify
from highlight import process_highlight  # Import the logic from highlight.py
import os
import logging

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Home route to check if the service is running
@app.route('/')
def home():
    return jsonify({'message': 'Service is running'}), 200

@app.route('/highlight', methods=['POST'])
def highlight():
    try:
        data = request.get_json()  # Use get_json() for better compatibility
        paragraph = data.get('paragraph', '')
        words_to_highlight = data.get('words', [])
        underline_style = data.get('underlineStyle', 'solid')
        underline_color = data.get('underlineColor', '#ffdd00')
        text_color = data.get('textColor', '#000000')

        # Validate input
        if not paragraph or not isinstance(words_to_highlight, list):
            return jsonify({'error': 'Invalid input data'}), 400

        # Call the highlight processing function
        updated_paragraph = process_highlight(
            paragraph, words_to_highlight, underline_style, underline_color, text_color
        )
        return jsonify({'updatedParagraph': updated_paragraph}), 200
    except Exception as e:
        # Handle errors gracefully and return an informative error message
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Test payload for local testing (remove this block when deploying)
    test_data = {
        "paragraph": "This is a test paragraph.",
        "words": ["test"],
        "underlineStyle": "dotted",
        "underlineColor": "#ff0000",
        "textColor": "#000000"
    }
    print("Test payload:", test_data)

    # Dynamic port from environment variable
    port = int(os.environ.get('PORT', 3000))  # Default to 3000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
