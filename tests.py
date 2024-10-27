from main import preprocess_text

def test_preprocess_text(tmp_path):
    # Define um dicionário onde a chave é o resultado esperado e o valor é a frase de entrada
    test_subjects = {
        "hello world": "Hello, world!",
        "test multiple punctuations": "This is a test... with multiple punctuations!!!",
        "clean text": "Can you clean this text? @#%&*()",
        "numbers 1234567890 symbols": "Numbers 1234567890 and symbols #$%^&*()",
        "mixed text numbers 123 symbols": "Mixed: text, numbers 123, and symbols #@!"
    }

    # Cria um arquivo temporário com as frases de entrada
    test_file = tmp_path / "test.txt"
    with open(test_file, 'w', encoding='utf-8') as file:
        for phrase in test_subjects.values():
            file.write(phrase + "\n")

    # Processa o arquivo temporário
    processed_text = preprocess_text(test_file)

    # Gera uma lista plana de todas as palavras esperadas
    expected_words = [word for expected in test_subjects.keys() for word in expected.split()]

    # Compara a lista plana de palavras processadas com a lista esperada
    assert expected_words == processed_text, f"{expected_words} != {processed_text}"

