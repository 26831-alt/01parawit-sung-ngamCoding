import tkinter as tk
from tkinter import messagebox
import webbrowser

# =========================
# ข้อมูลคณิตศาสตร์ ม.1 - ม.3
# =========================

courses = {
    "ม.1": {
        "เทอม 1": [
            "จำนวนเต็ม",
            "เลขยกกำลัง",
            "สมการเชิงเส้นตัวแปรเดียว",
            "กราฟและความสัมพันธ์",
            "เรขาคณิตพื้นฐาน"
        ],
        "เทอม 2": [
            "อัตราส่วนและร้อยละ",
            "สมการเชิงเส้นสองตัวแปร",
            "สถิติ",
            "รูปเรขาคณิต",
            "ทฤษฎีบทพีทาโกรัส"
        ],
        "links": [
            ("Khan Academy",
             "https://www.khanacademy.org/math"),
            ("YouTube คณิต ม.1",
             "https://www.youtube.com/results?search_query=คณิตศาสตร์+ม.1")
        ]
    },

    "ม.2": {
        "เทอม 1": [
            "เลขยกกำลัง",
            "พหุนาม",
            "การแยกตัวประกอบ",
            "สมการ",
            "เรขาคณิต"
        ],
        "เทอม 2": [
            "ทฤษฎีบทพีทาโกรัส",
            "การแปลงทางเรขาคณิต",
            "สถิติ",
            "ความน่าจะเป็น",
            "กราฟ"
        ],
        "links": [
            ("Khan Academy",
             "https://www.khanacademy.org/math"),
            ("YouTube คณิต ม.2",
             "https://www.youtube.com/results?search_query=คณิตศาสตร์+ม.2")
        ]
    },

    "ม.3": {
        "เทอม 1": [
            "อสมการ",
            "ระบบสมการ",
            "พาราโบลา",
            "ความคล้าย",
            "วงกลม"
        ],
        "เทอม 2": [
            "สถิติ",
            "ความน่าจะเป็น",
            "ตรีโกณมิติ",
            "พื้นที่และปริมาตร",
            "การประยุกต์ใช้คณิตศาสตร์"
        ],
        "links": [
            ("Khan Academy",
             "https://www.khanacademy.org/math"),
            ("YouTube คณิต ม.3",
             "https://www.youtube.com/results?search_query=คณิตศาสตร์+ม.3")
        ]
    }
}


# =========================
# เปิดเว็บไซต์
# =========================

def open_link(url):
    webbrowser.open(url)


# =========================
# แสดงข้อมูล
# =========================

def show_course():

    grade = grade_var.get()
    semester = semester_var.get()

    if grade not in courses:
        messagebox.showwarning(
            "แจ้งเตือน",
            "กรุณาเลือกระดับชั้น"
        )
        return

    # ล้างข้อมูลเดิม
    for widget in content_frame.winfo_children():
        widget.destroy()

    # หัวข้อ
    tk.Label(
        content_frame,
        text=f"📚 คณิตศาสตร์ {grade} - {semester}",
        font=("Tahoma", 18, "bold"),
        bg="#FFF8E7",
        fg="#6C3483"
    ).pack(pady=10)

    # หัวข้อเนื้อหา
    tk.Label(
        content_frame,
        text="📖 เนื้อหาที่ต้องเรียน",
        font=("Tahoma", 14, "bold"),
        bg="#FFF8E7",
        fg="#E67E22"
    ).pack(anchor="w", padx=20)

    # แสดงบทเรียน
    for i, topic in enumerate(
        courses[grade][semester], 1
    ):

        tk.Label(
            content_frame,
            text=f"{i}. {topic}",
            font=("Tahoma", 12),
            bg="#FFF8E7",
            fg="#2C3E50",
            anchor="w"
        ).pack(
            fill="x",
            padx=35,
            pady=3
        )

    # เส้นแบ่ง
    tk.Frame(
        content_frame,
        height=2,
        bg="#F5B041"
    ).pack(
        fill="x",
        padx=20,
        pady=15
    )

    # เว็บไซต์
    tk.Label(
        content_frame,
        text="🌐 แหล่งเรียนเพิ่มเติม",
        font=("Tahoma", 14, "bold"),
        bg="#FFF8E7",
        fg="#16A085"
    ).pack(anchor="w", padx=20)

    for name, url in courses[grade]["links"]:

        tk.Button(
            content_frame,
            text=f"🔗 {name}",
            font=("Tahoma", 11, "bold"),
            bg="#5DADE2",
            fg="white",
            activebackground="#3498DB",
            relief="flat",
            cursor="hand2",
            command=lambda link=url: open_link(link)
        ).pack(
            fill="x",
            padx=30,
            pady=5
        )


# =========================
# หน้าต่างหลัก
# =========================

root = tk.Tk()

root.title("โปรแกรมพัฒนาคณิตศาสตร์")
root.geometry("700x600")
root.configure(bg="#EAF2F8")
root.resizable(False, False)


# =========================
# ส่วนหัว
# =========================

header = tk.Frame(
    root,
    bg="#6C5CE7",
    height=100
)

header.pack(fill="x")

tk.Label(
    header,
    text="🧮 โปรแกรมพัฒนาคณิตศาสตร์",
    font=("Tahoma", 24, "bold"),
    bg="#6C5CE7",
    fg="white"
).pack(pady=15)

tk.Label(
    header,
    text="สำหรับนักเรียนระดับ ม.1 - ม.3",
    font=("Tahoma", 12),
    bg="#6C5CE7",
    fg="white"
).pack()


# =========================
# เลือกระดับชั้น
# =========================

select_frame = tk.Frame(
    root,
    bg="white"
)

select_frame.pack(
    fill="x",
    padx=25,
    pady=20
)

tk.Label(
    select_frame,
    text="🎓 ระดับชั้น",
    font=("Tahoma", 12, "bold"),
    bg="white"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=15
)

grade_var = tk.StringVar(
    value="ม.1"
)

grade_menu = tk.OptionMenu(
    select_frame,
    grade_var,
    "ม.1",
    "ม.2",
    "ม.3"
)

grade_menu.config(
    font=("Tahoma", 11),
    bg="#D6EAF8",
    width=8
)

grade_menu.grid(
    row=0,
    column=1,
    padx=10
)


# =========================
# เลือกเทอม
# =========================

tk.Label(
    select_frame,
    text="📅 ภาคเรียน",
    font=("Tahoma", 12, "bold"),
    bg="white"
).grid(
    row=0,
    column=2,
    padx=10
)

semester_var = tk.StringVar(
    value="เทอม 1"
)

semester_menu = tk.OptionMenu(
    select_frame,
    semester_var,
    "เทอม 1",
    "เทอม 2"
)

semester_menu.config(
    font=("Tahoma", 11),
    bg="#D5F5E3",
    width=8
)

semester_menu.grid(
    row=0,
    column=3,
    padx=10
)


# =========================
# ปุ่มค้นหา
# =========================

tk.Button(
    root,
    text="🔍 ดูเนื้อหาการเรียน",
    font=("Tahoma", 13, "bold"),
    bg="#F39C12",
    fg="white",
    activebackground="#E67E22",
    relief="flat",
    cursor="hand2",
    command=show_course
).pack(
    ipadx=25,
    ipady=8
)


# =========================
# พื้นที่แสดงเนื้อหา
# =========================

content_frame = tk.Frame(
    root,
    bg="#FFF8E7"
)

content_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=15
)

tk.Label(
    content_frame,
    text="✨ เลือกระดับชั้นและภาคเรียน\nเพื่อเริ่มต้นการเรียนรู้",
    font=("Tahoma", 17, "bold"),
    bg="#FFF8E7",
    fg="#7D3C98"
).pack(expand=True)


# =========================
# เริ่มโปรแกรม
# =========================

root.mainloop()