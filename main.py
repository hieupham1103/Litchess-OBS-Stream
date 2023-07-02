from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, jsonify, render_template, request
import time

url = "https://lichess.org/oBOzYSz9/black"

driver = webdriver.Chrome()
driver.get(url)
stages_timer1 = driver.find_element(By.XPATH, """//*[@id="main-wrap"]/main/div[1]/div[6]/div[2]""")
stages_timer2 = driver.find_element(By.XPATH, """//*[@id="main-wrap"]/main/div[1]/div[7]/div[2]""")

app = Flask(__name__)


@app.route('/timer1_json', methods = ['GET'])
def timer1_json():
    
    # return jsonify(result=time.time())
    return jsonify(result="".join(stages_timer1.text.split('\n')))

@app.route('/timer2_json', methods = ['GET'])
def timer2_json():
    
    # return jsonify(result=time.time())
    return jsonify(result="".join(stages_timer2.text.split('\n')))

@app.route('/timer1')
def timer1():
    return render_template('timer1.html')

@app.route('/timer2')
def timer2():

    return render_template('timer2.html')
    
if __name__ == '__main__':
    app.run(debug=True)