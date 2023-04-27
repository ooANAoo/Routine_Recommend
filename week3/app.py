from flask import Flask, render_template, request
from body_analysis import calculate_bmi, calculate_body_fat_ratio, get_body_type, get_muscle_development_type, print_body_analysis
import logging
from logging.handlers import RotatingFileHandler
from datetime import time

app = Flask(__name__)
if not app.debug:
    # 로그 파일의 위치와 파일명을 지정합니다.
    log_file = 'web/week3/log/flaskapp.log'
    # 로그 파일의 크기는 최대 1MB로 지정합니다.
    max_size = 1024 * 1024
    # 로그 파일의 개수는 최대 10개까지 지정합니다.
    backup_count = 10
    # 로그 레벨을 설정합니다.
    log_level = logging.INFO

    # 로그 핸들러를 생성합니다.
    file_handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    # 로그 포맷을 지정합니다.
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    # 애플리케이션에 핸들러를 추가합니다.
    app.logger.addHandler(file_handler)
    app.logger.setLevel(log_level)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Routine', methods=['POST'])
def Routine():
    purpose = request.form['purpose']
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    body_fat_mass = float(request.form['body_fat_mass'])
    right_arm_muscle_mass = float(request.form['right_arm_muscle_mass'])
    left_arm_muscle_mass = float(request.form['left_arm_muscle_mass'])
    right_leg_muscle_mass = float(request.form['right_leg_muscle_mass'])
    left_leg_muscle_mass = float(request.form['left_leg_muscle_mass'])
    trunk_muscle_mass = float(request.form['trunk_muscle_mass'])
    age = int(request.form['age'])
    gender = request.form['gender']

    bmi = calculate_bmi(weight, height)
    body_fat_ratio = calculate_body_fat_ratio(weight, body_fat_mass)
    body_type = get_body_type(bmi, body_fat_ratio, (right_arm_muscle_mass + left_arm_muscle_mass + right_leg_muscle_mass + left_leg_muscle_mass + trunk_muscle_mass), age, gender)
    muscle_development_type = get_muscle_development_type(right_arm_muscle_mass, left_arm_muscle_mass, right_leg_muscle_mass, left_leg_muscle_mass, trunk_muscle_mass)
    routine = []
    if request.form.get('monday'):
        routine.append(('Monday', time.fromisoformat(request.form['monday-start-time']), time.fromisoformat(request.form['monday-end-time'])))
    if request.form.get('tuesday'):
        routine.append(('Tuesday', time.fromisoformat(request.form['tuesday-start-time']), time.fromisoformat(request.form['tuesday-end-time'])))
    if request.form.get('wednesday'):
        routine.append(('Wednesday', time.fromisoformat(request.form['wednesday-start-time']), time.fromisoformat(request.form['wednesday-end-time'])))
    if request.form.get('thursday'):
        routine.append(('Thursday', time.fromisoformat(request.form['thursday-start-time']), time.fromisoformat(request.form['thursday-end-time'])))
    if request.form.get('friday'):
        routine.append(('Friday', time.fromisoformat(request.form['friday-start-time']), time.fromisoformat(request.form['friday-end-time'])))
    if request.form.get('saturday'):
        routine.append(('Saturday', time.fromisoformat(request.form['saturday-start-time']), time.fromisoformat(request.form['saturday-end-time'])))
    if request.form.get('sunday'):
        routine.append(('Sunday', time.fromisoformat(request.form['sunday-start-time']), time.fromisoformat(request.form['sunday-end-time'])))
        
    return render_template('Routine.html', purpose=purpose, body_type=body_type, muscle_development_type=muscle_development_type, routine=routine, age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)
