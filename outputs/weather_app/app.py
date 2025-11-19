from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# 天気取得
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')

    # テスト用の無料API（本物のキー不要）
    url = f"https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m"
    response = requests.get(url).json()

    temp = response["hourly"]["temperature_2m"][0]

    return render_template('index.html', temp=temp, city=city)

if __name__ == '__main__':
    app.run(debug=True)
