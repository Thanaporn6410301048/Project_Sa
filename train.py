import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. เตรียมข้อมูลสมมติ (ขนาดบ้าน ตารางเมตร กับ ราคา ล้านบาท)
# บ้านขนาด 30, 50, 80, 100 ตารางเมตร
X = np.array([[10], [50], [80], [100]])
# ราคา 1.5, 2.5, 4.0, 5.0 ล้านบาท (ตามลำดับ)
y = np.array([1.5, 2.5, 4.0, 5.0])

# 2. สร้างโมเดลและสั่งให้เรียนรู้ (Train)
model = LinearRegression()
model.fit(X, y)

# 3. เซฟสมองก้อนนี้เก็บไว้ในไฟล์ชื่อ house_model.pkl
joblib.dump(model, "house_model.pkl")
print("เทรนโมเดลเสร็จแล้ว และเซฟไฟล์เรียบร้อย!")