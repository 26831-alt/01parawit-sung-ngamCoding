print("โปรแกรมคำนวนbmiแปลผลสุขภาพ\n")
weight = float(input("น้ำของคุณ (kg) "))
height = float(input("ส่วนสูงของคุณ (m) "))
bmi = weight/(height*height)
print("ค่าbmi = ", bmi)
if bmi< 18.5:
    print("น้ำหนักน้อยกว่าเกณฑ์ ")
elif bmi<= 22.9:
    print("เกณฑ์ปกติ")
elif bmi<= 24.9:
    print("น้ำหนักเกิน ")
else :
    print("อ้วน")