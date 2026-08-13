import joblib
from flask import Flask, request

app = Flask(__name__)

# โหลดสมอง (โมเดล) ที่เราเทรนไว้จากขั้นที่แล้วมาเตรียมใช้งาน
model = joblib.load("house_model.pkl")


# ใหม่! เพิ่มหน้าแรกสุดที่มีช่องกรอกตัวเลขและปุ่มกด (ไม่ต้องไปพิมพ์บน URL แล้ว)
@app.route("/")
def home():
    return """
    <h2>ระบบทำนายราคาบ้านจำลอง</h2>
    <form action="/predict" method="get">
        <label>กรอกขนาดบ้าน (ตารางเมตร): </label>
        <input type="number" name="size" required>
        <button type="submit">ทำนายราคา</button>
    </form>
    """


# หน้าเว็บสำหรับคำนวณและแสดงผลลัพธ์
@app.route("/predict")
def predict_price():
    house_size = request.args.get("size", type=float)

    if house_size is None:
        return "กรุณาใส่ขนาดบ้านใน URL เช่น /predict?size=60"

    predicted_price = model.predict([[house_size]])[0]

    # เพิ่มปุ่มกดพากลับหน้าแรกด้วยเพื่อความสะดวก
    return f"""
    <h3>บ้านขนาด {house_size} ตร.ม. โมเดลทำนายว่าราคาประมาณ: {predicted_price:.2f} ล้านบาท</h3>
    <a href="/"><button>กลับหน้าแรก</button></a>
    """


if __name__ == "__main__":
    app.run(debug=True)
