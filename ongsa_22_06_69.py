print("โปรแกรมแสดงผลคะแนนรวม\n")
mathscore = int(input("คะแนนวิชาคณิตคาสตร์ 0-100 ได้ "))
sciencescore = int(input("คะแนนวิชาวิทยาศาสตร์ 0-100 ได้ "))
thaiscore = int(input("คะแนนวิชาภาษาไทย 0-100 ได้ "))
allscore = (mathscore + sciencescore +thaiscore)
averagescore = (allscore)/3
print("คะแนนรวมที่ได้ คือ ", allscore , "คะแนน")
print("\nคะแนนเฉลี่ยรวมที่ได้ คือ ", int(averagescore) , "คะแนน")
if averagescore < 60 :
    print("อยู่ในเกณฑ์ ควรปรับปรุง")
elif averagescore < 80 :
    print("อยู่ในเกณฑ์ ผ่าน")
elif averagescore > 79 :
    print("อยู่ในเกณฑ์ ดีเยี่ยม")
print("\nจัดทำโดย นายปรวิศ สังข์งาม ม.4/4 เลขที่2")