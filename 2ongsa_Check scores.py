score1 = int(input("ใส่คะแนนวิชาที่1 0-100 "))
score2 = int(input("ใส่คะแนนวิชาที่2 0-100 "))
score3 = int(input("ใส่คะแนนวิชาที่3 0-100 "))
allscore = (score1 + score2 + score3)/3
print("คะแนนที่ได้ คือ" ,allscore)
if 60>allscore :print("ควรปรับปรุง")
if 79<allscore :print("ดีเยี่ยม")
if 80>allscore>59 :print("ผ่าน")