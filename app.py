from flask import Flask, render_template, request
import os
from model import model

app = Flask(__name__)

@app.route('/')
def index():
    T2E_exam = str(request.remote_addr) + ".txt"
    with open(T2E_exam, "w") as file:
        file.write("")
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    T2E_exam = str(request.remote_addr) + ".txt"
    text = request.form['text']
    cefr_level = request.form['cefr_level']

    # Call your Python function here to process the data
    output = model(text, cefr_level)

    # Save the output to a file
    count = 0
    max_choice = 4

    with open(T2E_exam, "a") as file:
        file.write("__________ T2E Vocabulary Exam Generator __________\n")
        file.write("|    Welcome to T2E Vocabulary Exam Generator!     |\n")
        file.write("|  We are glad that our service is useful to you.  |\n")
        file.write("|                                                  |\n")
        file.write("|        Copyrights 2023, Nutnornont Chamadol      |\n")
        file.write("|             Email: nontc49@gmail.com             |\n")
        file.write("|     Visit https://nontgcob.com to learn more     |\n")
        file.write("|                                                  |\n")
        file.write("|            Your exam is generated below.         |\n")
        file.write("|  - Happy using T2E Vocabulary Exam Generator! -  |\n")
        file.write("|__________________________________________________|\n")
        file.write("\n")

    for key, value in output.items():
        vvocab, sentence = key.split(" = ")
        # print(f'What does the word "{vvocab}" means in this sentence "{sentence}"?')
        with open(T2E_exam, "a") as file:
            file.write(f'What does the word "{vvocab}" means in this sentence "{sentence}"?\n')

        for choice in value:
            ai_score, choice = choice.split(", ")
            # print(f"- {choice}")
            with open(T2E_exam, "a") as file:
                file.write(f"- {choice}\n")
            count += 1
            # if count > (max_choice + 1):
            #     break
        with open(T2E_exam, "a") as file:
            file.write("\n")

    return render_template('result.html', output="Exam successfully generated!", file_path="T2E_exam.txt")

from flask import send_file

@app.route('/send')
def get_file():
    T2E_exam = str(request.remote_addr) + ".txt"
    return send_file(
        str(request.remote_addr) + ".txt",
        # download_name = "T2E_exam.txt"
    )

if __name__ == '__main__':
    app.run()
