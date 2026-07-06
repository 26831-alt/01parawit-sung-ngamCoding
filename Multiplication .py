print("โปรแกรมกาสูตรคูณ\n")
n = int(input("สูตรคูณที่ต้องการ คือ "))
n2 = int(input("สิ้นสุดที่ คือ "))
for k in range(n,n2 +1):
    print("\nสูตรคูณ แม่" ,k, "คือ")
    for i in range(1,13) :
      print(n,"x",i,"=",n*i)
print("\nจัดทำโดย นาย ปรวิศ สังข์งาม เลขที่2 ม.4/4")