from flask import Flask, request, jsonify
from highlight import process_highlight  # Import the logic from highlight.py
import os

app = Flask(__name__)

@app.route('/highlight', methods=['POST'])
def highlight():
    data = request.json
    paragraph = data.get('paragraph', '')
    words_to_highlight = data.get('words', [])
    underline_style = data.get('underlineStyle', 'solid')
    underline_color = data.get('underlineColor', '#ffdd00')
    text_color = data.get('textColor', '#000000')

    try:
        # Call the highlight processing function
        updated_paragraph = process_highlight(paragraph, words_to_highlight, underline_style, underline_color, text_color)
        return jsonify({'updatedParagraph': updated_paragraph})
    except Exception as e:
        # If any error occurs in processing, return a 500 status with the error message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Use the dynamic PORT assigned by Render
    port = int(os.environ.get('PORT', 3000))  # Fallback to 3000 if PORT is not set
    app.run(host='0.0.0.0', port=port)