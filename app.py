from flask import Flask, render_template, request
from algorithms import caesar_cipher_rus, vigenere_encrypt, vigenere_decrypt, block_permutation_encrypt, block_permutation_decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/theory')
def theory():
    return render_template('theory.html')

@app.route('/encryption', methods=['GET', 'POST'])
def encryption():
    if request.method == 'POST':
        text = request.form['inputText']
        method = request.form['methodSelect']
        action = request.form['action']
        
        try:
            if method == 'caesar':
                shift_input = request.form['shift']
                if shift_input:
                    shift = int(shift_input)
                    if action == 'decrypt':
                        result = caesar_cipher_rus(text, shift, decrypt=True)
                    else:
                        result = caesar_cipher_rus(text, shift)
                else:
                    result = "Ошибка: Не указан сдвиг для шифра Цезаря"
            elif method == 'vigenere':
                key = request.form['key']
                if action == 'decrypt':
                    result = vigenere_decrypt(text, key)
                else:
                    result = vigenere_encrypt(text, key)
            elif method == 'block_permutation':
                key = request.form.get('keyBlockPermutation')  # Используйте .get для предотвращения KeyError
                if not key.strip():
                    raise ValueError("Ключ для блочной перестановки не может быть пустым.")
                if action == 'encrypt':
                    result = block_permutation_encrypt(text, key)
                else:
                    result = block_permutation_decrypt(text, key)
            # Можно добавить другие методы шифрования здесь
        except ValueError as e:
            result = str(e)  # Перехват исключения и преобразование в строку для отображения пользователю

        return render_template('encryption.html', output=result, method=method)
    return render_template('encryption.html', method='caesar')

if __name__ == '__main__':
    app.run(debug=True)
