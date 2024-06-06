from flask import Flask, jsonify, request
import random
from transformers import pipeline
import re

app = Flask(__name__)

def generate_board(words, spangram, m, n):
    # Validate that the spangram can fit within the board dimensions
    if len(spangram) > n:
        raise ValueError("Spangram length exceeds board width")

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

# Function to log messages to a file
def log_to_file(message):
    with open('/home/ubuntu/testing-devin/gpt-neox/flask_server.log', 'a') as log_file:
        log_file.write(message + '\n')

def call_gpt_neox(theme, n):
    # Use Hugging Face transformers pipeline for text generation
    generator = pipeline('text-generation', model='gpt2')
    prompt = (
        f"Generate a theme and a list of 6 to 8 words aligning with the theme '{theme}'. "
        "One of these words, which we call a spangram, must be longer (but can be two words), with a length of at least 8 characters, "
        "and must describe more specifically each of the other words. Provide the spangram and words in the following format: "
        "Spangram: <spangram>, Words: <word1>, <word2>, <word3>, <word4>, <word5>, <word6>. "
        "Ensure the spangram and words are clearly separated by commas and follow the exact format provided. "
        "Example: Spangram: Birdsong, Words: Cluck, Trill, Warble, Chirp, Screech, Tweet, Whistle."
    )

    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        response = generator(prompt, max_length=300, num_return_sequences=1, temperature=0.9, max_new_tokens=100, truncation=True)
        generated_text = response[0]['generated_text']

        # Extract spangram and words from the generated text
        spangram_match = re.search(r'Spangram:\s*([^,]+)', generated_text)
        words_match = re.search(r'Words:\s*([^\.]+)', generated_text)
        spangram = None
        words = []
        if spangram_match:
            spangram = spangram_match.group(1).strip()
        if words_match:
            words = [word.strip() for word in words_match.group(1).split(',') if word.strip()]

        # Log the generated text and extracted values for debugging purposes
        log_to_file(f"Attempt {attempts + 1}:")
        log_to_file("Generated text: " + generated_text)
        log_to_file("Extracted spangram: " + str(spangram))
        log_to_file("Extracted words: " + str(words))

        if spangram and words and len(spangram) <= n:
            break

        attempts += 1

    if attempts == max_attempts:
        raise ValueError("Failed to generate valid word set after multiple attempts")

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
        gpt_response = call_gpt_neox(theme, n)
    except Exception as e:
        # Log the error and generated text for debugging purposes
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

    spangram = gpt_response.get('spangram')
    words = gpt_response.get('words')

    if not spangram or not words:
        return jsonify({'error': 'Invalid response from GPT-NeoX'}), 500

    try:
        board = generate_board(words, spangram, m, n)
    except ValueError as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'theme': theme, 'spangram': spangram, 'board': board})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
