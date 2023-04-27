def calculate_bmi(weight, height):
    """
    BMI를 계산하는 함수
    """
    return weight / ((height / 100) ** 2)

def calculate_body_fat_ratio(weight, body_fat_mass):
    """
    체지방률을 계산하는 함수
    """
    return body_fat_mass / weight * 100

def get_body_type(bmi, body_fat_ratio, muscle_mass, age, gender):
    """
    인바디 측정 데이터를 바탕으로 체형을 판정하는 함수
    """
    if bmi < 18.5:
        if muscle_mass >= 30:
            body_type = "저체중 강인"
        else:
            body_type = "저체중 허약"
    elif bmi < 23:
        if body_fat_ratio < 20:
            if muscle_mass >= (19 + (0.25 * (age - 20))) and gender == "남성":
                body_type = "표준 강인"
            elif muscle_mass >= (15.2 + (0.17 * (age - 20))) and gender == "여성":
                body_type = "표준 강인"
            else:
                body_type = "표준"
        else:
            body_type = "과체중 표준"
    elif bmi < 25:
        if body_fat_ratio < 20:
            if muscle_mass >= (19 + (0.25 * (age - 20))) and gender == "남성":
                body_type = "과체중 강인"
            elif muscle_mass >= (15.2 + (0.17 * (age - 20))) and gender == "여성":
                body_type = "과체중 강인"
            else:
                body_type = "과체중 표준"
        else:
            if bmi < 30:
                body_type = "경도비만"
            elif bmi < 35:
                body_type = "중등도비만"
            else:
                body_type = "고도비만"
    else:
        if muscle_mass >= (19 + (0.25 * (age - 20))) and gender == "남성":
            body_type = "과체중 강인"
        elif muscle_mass >= (15.2 + (0.17 * (age - 20))) and gender == "여성":
            body_type = "과체중 강인"
        else:
            if bmi < 30:
                body_type = "경도비만"
            elif bmi < 35:
                body_type = "중등도비만"
            else:
                body_type = "고도비만"
    
    return body_type


def get_muscle_development_type(right_arm_muscle_mass, left_arm_muscle_mass, right_leg_muscle_mass, left_leg_muscle_mass, trunk_muscle_mass):
    """
    인바디 측정 데이터를 바탕으로 근육 발달 형태를 판정하는 함수
    """
    total_arm_muscle_mass = right_arm_muscle_mass + left_arm_muscle_mass
    total_leg_muscle_mass = right_leg_muscle_mass + left_leg_muscle_mass
    if total_arm_muscle_mass > total_leg_muscle_mass and trunk_muscle_mass > total_leg_muscle_mass:
    
        if (total_arm_muscle_mass - total_leg_muscle_mass) >= 1.5:
            return "상체 발달"
        else:
            return "상체 허약"
    
    elif total_leg_muscle_mass > total_arm_muscle_mass and trunk_muscle_mass > total_arm_muscle_mass:
        if (total_leg_muscle_mass - total_arm_muscle_mass) >= 2:
            return "하체 발달"
        else:
            return "하체 허약"
    else:
        return "균형 발달"


def print_body_analysis(weight, height, body_fat, right_arm_muscle_mass, left_arm_muscle_mass, right_leg_muscle_mass, left_leg_muscle_mass, trunk_muscle_mass, age, gender):
    bmi = calculate_bmi(weight, height)
    body_fat_ratio = calculate_body_fat_ratio(weight, body_fat)
    body_type = get_body_type(bmi, body_fat_ratio, (right_arm_muscle_mass + left_arm_muscle_mass + right_leg_muscle_mass + left_leg_muscle_mass + trunk_muscle_mass), age, gender)
    muscle_development_type = get_muscle_development_type(right_arm_muscle_mass, left_arm_muscle_mass, right_leg_muscle_mass, left_leg_muscle_mass, trunk_muscle_mass)
    
    print(f"당신의 체형은 {body_type}입니다.")
    print(f"당신의 근육 발달 형태는 {muscle_development_type}입니다.")