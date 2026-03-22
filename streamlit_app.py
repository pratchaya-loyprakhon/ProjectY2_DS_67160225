import pandas as pd

# สร้างข้อมูลจาก input ของ user
input_data = pd.DataFrame([{
    'Age': age,
    'BusinessTravel': travel_mapped,
    'DailyRate': daily_rate,
    # ... ใส่ให้ครบทุกคอลัมน์ตามลำดับใน Colab ...
}])

# สร้าง Dictionary สำหรับแปลงค่า (ต้องตรงกับตอนใช้ LabelEncoder ใน Colab)
business_travel_map = {'Non-Travel': 0, 'Travel_Rarely': 1, 'Travel_Frequently': 2}
department_map = {'Human Resources': 0, 'Research & Development': 1, 'Sales': 2}
education_field_map = {'Human Resources': 0, 'Life Sciences': 1, 'Marketing': 2, 'Medical': 3, 'Other': 4, 'Technical Degree': 5}
gender_map = {'Female': 0, 'Male': 1}
job_role_map = {'Healthcare Representative': 0, 'Human Resources': 1, 'Laboratory Technician': 2, 'Manager': 3, 'Manufacturing Director': 4, 'Research Director': 5, 'Research Scientist': 6, 'Sales Executive': 7, 'Sales Representative': 8}
marital_status_map = {'Divorced': 0, 'Married': 1, 'Single': 2}
overtime_map = {'No': 0, 'Yes': 1}

# แปลงค่าจาก Input ของ User ให้เป็นตัวเลข
travel_num = business_travel_map[business_travel_input]
dept_num = department_map[department_input]
field_num = education_field_map[education_field_input]
gender_num = gender_map[gender_input]
role_num = job_role_map[job_role_input]
marital_num = marital_status_map[marital_status_input]
overtime_num = overtime_map[overtime_input]

# รวมเป็น List โดยต้อง "เรียงลำดับคอลัมน์" ให้ตรงกับข้อ 1
features = [age, travel_num, daily_rate, dept_num, distance, education, field_num, ..., overtime_num, ...]
# ทำนายผล
prediction = model.predict(input_data)
