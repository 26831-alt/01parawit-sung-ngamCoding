print("โปรแกรมคำนวณBMIและแปลสุขภาพ\n")
weight = float(input("น้ำหนักของตัวคุณ " ))
height = float(input("ส่วนสูงของคุณ "))
averagebmi = (height*height)/weight
if averagebmi>18.5 :
    print("น้ำหนักน้อย")
elif averagebmi == 18.6-22.9 :
    print("ปกติ")
elif averagebmi == 23-24.9 :
    print("น้ำหนักเกิน")
elif averagebmi<25 :
    print("อ้วน")