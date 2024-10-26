import requests
import json
import random  # Đảm bảo đã import thư viện random
import time

# Địa chỉ URL của Flask server
url = 'http://localhost:5000/api/rain-data'  # Thay đổi nếu server bạn đang chạy trên địa chỉ khác
headers = {'Content-Type': 'application/json'}

# Danh sách các giá trị lượng mưa cố định
rain_values = ["Heavy rain", "Light rain", "No rain"]

# Tạo và gửi dữ liệu ngẫu nhiên mỗi 5 giây
for i in range(10):  # Gửi 10 lần
    # Lựa chọn một mức mưa ngẫu nhiên từ danh sách
    rain_value = random.choice(rain_values)
    
    # Tạo đối tượng JSON để gửi
    data = {"rain_value": rain_value}
    
    # Gửi yêu cầu POST với dữ liệu ngẫu nhiên tới server Flask
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    # In ra giá trị đã gửi và trạng thái phản hồi từ server
    print(f"Sent rain_value: {rain_value}, Response: {response.status_code}")
    
    # Đợi 5 giây trước khi gửi tiếp
    time.sleep(5)
