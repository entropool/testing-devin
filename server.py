from flask import Flask, jsonify, request
import random
from transformers import pipeline

app = Flask(__name__)

def generate_board(words, spangram, m, n):
    board = [['' for _ in range(n)] for _ in range(m)]

    # Place the spangram on the board
    spangram_start_col = random.randint(0, n - len(spangram))
    for i, char in enumerate(spangram):
        board[0][spangram_start_col + i] = char

    # Place the other words on the board
    word_index = 0
    for row in range(1, m):
        col = 0
        while col < n and word_index < len(words):
            word = words[word_index]
            if col + len(word) <= n:
                for i, char in enumerate(word):
                    board[row][col + i] = char
                col += len(word) + 1  # Add a space between words
                word_index += 1
            else:
                break

    return board

def call_gpt_neox(theme):
    # Use Hugging Face transformers pipeline for text generation
    generator = pipeline('text-generation', model='gpt2')
    prompt = f"Generate a theme and a list of 6 to 8 words aligning with the theme '{theme}'. They should clearly and often cleverly relate to the theme, but not be too easy to guess. One of these words, which we call a spangram, must be longer (but can be two words), with a length of at least 8 characters, and must describe more specifically each of the other words."
    response = generator(prompt, max_length=100, num_return_sequences=1)
    generated_text = response[0]['generated_text']

    # Extract spangram and words from the generated text
    # This is a placeholder extraction logic and should be updated based on the actual format of the generated text
    lines = generated_text.split('\n')
    spangram = None
    words = []

    for line in lines:
        if 'spangram' in line.lower():
            spangram = line.split(': ')[-1]
        elif ':' in line:
            words.append(line.split(': ')[-1])

    if not spangram or not words:
        # Log the generated text for debugging purposes
        print("Generated text:", generated_text)
        raise ValueError("Failed to extract spangram or words from the generated text")

    return {"spangram": spangram, "words": words}

@app.route('/generate_word_set', methods=['POST'])
def generate_word_set():
    data = request.json
    theme = data.get('theme')
    m = data.get('m')
    n = data.get('n')

    if not theme or not m or not n:
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        gpt_response = call_gpt_neox(theme)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    spangram = gpt_response.get('spangram')
    words = gpt_response.get('words')

    if not spangram or not words:
        return jsonify({'error': 'Invalid response from GPT-NeoX'}), 500

    board = generate_board(words, spangram, m, n)
    return jsonify({'theme': theme, 'spangram': spangram, 'board': board})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
