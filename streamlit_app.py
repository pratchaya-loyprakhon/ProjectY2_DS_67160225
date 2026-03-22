import pandas as pd

# สร้างข้อมูลจาก input ของ user
input_data = pd.DataFrame([{
    'Age': age,
    'BusinessTravel': travel_mapped,
    'DailyRate': daily_rate,
    # ... ใส่ให้ครบทุกคอลัมน์ตามลำดับใน Colab ...
}])

# ทำนายผล
prediction = model.predict(input_data)
