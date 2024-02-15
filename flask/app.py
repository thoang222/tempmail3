from flask import Flask, render_template, request
import subprocess, os
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        command = request.form.get('command')
        output = execute_command(command)
        return render_template('index.html', output=output)
    return render_template('index.html')

def execute_command(command):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.route('/view_mail', methods=['GET'])
def read_file():
    file_path = '/tmp/tmpmail/tmpmail.html'
    try:
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_content = file.read()
            soup = BeautifulSoup(file_content, 'html.parser')
            tiktok_link = soup.find('a', {'href': lambda x: x and 'api.tiktokv.com' in x})
            if tiktok_link:
                href_value = tiktok_link.get('href')
                return href_value
            else:
                return None
        else:
            return f"File '{file_path}'not have"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
