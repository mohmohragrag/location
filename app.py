from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-location', methods=['GET'])
def get_location():
 # تشغيل المتصفح بدون واجهة
    driver = webdriver.Edge()

    try:
        driver.get('https://www.google.com/maps')
        time.sleep(5)  # انتظار التحميل
        location = driver.current_url  # يحصل على URL الحالي
        driver.quit()
        return jsonify({"location": location})

    except Exception as e:
        driver.quit()
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
