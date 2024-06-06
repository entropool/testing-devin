from flask import Flask, jsonify, request
import random
from transformers import pipeline
import re
import torch

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
    generator = pipeline('text-generation', model='EleutherAI/gpt-neox-20b', model_kwargs={"torch_dtype": torch.bfloat16}, device=-1)
    # Refined prompt to be more explicit and clear
    prompt = (
        f"Theme: {theme}\n"
        "Generate a spangram and a list of 6 to 8 words related to the theme. "
        "The spangram must be a single word or a hyphenated word with at least 8 characters. "
        "Provide the spangram and words in the following format: "
        "Spangram: [spangram], Words: [word1], [word2], [word3], [word4], [word5], [word6]. "
        "Do not include placeholders like [spangram] or [word1]."
    )

    max_attempts = 5
    attempts = 0
    generated_text = ""

    while attempts < max_attempts:
        try:
            response = generator(prompt, max_new_tokens=200, num_return_sequences=1, temperature=0.7, top_p=0.9)
            generated_text = response[0]['generated_text']

            # Log the full response for debugging purposes
            log_to_file(f"Full response: {response}")

            # Adjusted regular expressions to correctly capture the generated spangram and words
            spangram_match = re.search(r'Spangram:\s*([A-Za-z-]+)', generated_text)
            words_match = re.search(r'Words:\s*([A-Za-z,\s]+)', generated_text)
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
        except Exception as e:
            log_to_file(f"Error during generation attempt {attempts + 1}: {str(e)}")
            log_to_file("Generated text: " + generated_text)

        attempts += 1

    if attempts == max_attempts:
        raise ValueError("Failed to generate valid word set after multiple attempts")

    return {"spangram": spangram, "words": words}

@app.route('/generate_word_set', methods=['POST'])
def generate_word_set():
    log_to_file("Received request for /generate_word_set endpoint")
    data = request.json
    theme = data.get('theme')
    m = data.get('m')
    n = data.get('n')

    log_to_file(f"Extracted parameters - Theme: {theme}, m: {m}, n: {n}")

    if not theme or not m or not n:
        log_to_file("Error: Missing required parameters")
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        log_to_file("Calling call_gpt_neox function")
        gpt_response = call_gpt_neox(theme, n)
    except Exception as e:
        log_to_file(f"Error in call_gpt_neox: {str(e)}")
        return jsonify({'error': str(e)}), 500

    spangram = gpt_response.get('spangram')
    words = gpt_response.get('words')

    if not spangram or not words:
        log_to_file("Error: Invalid response from GPT-NeoX")
        return jsonify({'error': 'Invalid response from GPT-NeoX'}), 500

    try:
        log_to_file("Calling generate_board function")
        board = generate_board(words, spangram, m, n)
    except ValueError as e:
        log_to_file(f"Error in generate_board: {str(e)}")
        return jsonify({'error': str(e)}), 500

    log_to_file("Successfully generated response")
    return jsonify({'theme': theme, 'spangram': spangram, 'board': board})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
