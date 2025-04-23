import tkinter as tk
from PIL import Image,ImageTk
import time
import math

root = tk.Tk()
root.title("Analog Clock")

# Canvas সেটআপ
canvas_size = 400
center_x, center_y = canvas_size // 2, canvas_size // 2
clock_radius = 180
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="DarkSeaGreen")
canvas.pack()
try:
    bg_image = Image.open("c:/Users/HP/OneDrive/Desktop/My projects/716jC8ycE7L._AC_UL600_SR600,600_.jpg")
    bg_image = bg_image.resize((canvas_size,canvas_size))
    bg_image = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0,0,Image=bg_photo,anchor="nw")
except Exception as e:
    print("Image load failed:",e)
    


# ঘড়ির বডি আঁকা
canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                   center_x + clock_radius, center_y + clock_radius,
                   outline="#654321", width=6)

# 1-12 সংখ্যাগুলো বসানো
for i in range(1, 13):
    angle = math.radians(i * 30 - 90)
    x = center_x + (clock_radius - 20) * math.cos(angle)
    y = center_y + (clock_radius - 20) * math.sin(angle)
    canvas.create_text(x, y, text=str(i), font=("Times New Roman", 22, "bold"),fill="darkblue")

# টিক মার্ক (ঘণ্টা ও মিনিট)
for i in range(60):
    angle = math.radians(i * 6 - 90)
    x1 = center_x + (clock_radius - 10) * math.cos(angle)
    y1 = center_y + (clock_radius - 10) * math.sin(angle)
    x2 = center_x + (clock_radius - (5 if i % 5 == 0 else 2)) * math.cos(angle)
    y2 = center_y + (clock_radius - (5 if i % 5 == 0 else 2)) * math.sin(angle)
    canvas.create_line(x1, y1, x2, y2, fill="black", width=1)

# কাঁটার দৈর্ঘ্য
hour_hand_length = 70
minute_hand_length = 110
second_hand_length = 140

# মূল ফাংশন: ঘড়ির কাঁটা আপডেট করা
def update_clock():
    canvas.delete("hands")

    # সময় বের করা
    t = time.localtime()
    hours = t.tm_hour % 12
    minutes = t.tm_min
    seconds = t.tm_sec + (time.time() % 1)  # ⬅️ **এখানেই আগে ভুল ছিল!**

    # কোণ নির্ণয়
    second_angle = math.radians(6 * seconds - 90)
    minute_angle = math.radians(6 * minutes + 0.1 * seconds - 90)
    hour_angle = math.radians(30 * hours + 0.5 * minutes - 90)

    # কাঁটার শেষ বিন্দুর অবস্থান বের করা
    second_x = center_x + second_hand_length * math.cos(second_angle)
    second_y = center_y + second_hand_length * math.sin(second_angle)

    minute_x = center_x + minute_hand_length * math.cos(minute_angle)
    minute_y = center_y + minute_hand_length * math.sin(minute_angle)

    hour_x = center_x + hour_hand_length * math.cos(hour_angle)
    hour_y = center_y + hour_hand_length * math.sin(hour_angle)

    # কাঁটা আঁকা
    canvas.create_line(center_x, center_y, hour_x, hour_y, fill="black", width=7, tags="hands")
    canvas.create_line(center_x, center_y, minute_x, minute_y, fill="black", width=5, tags="hands")
    canvas.create_line(center_x, center_y, second_x, second_y, fill="red", width=2, tags="hands")

    # সেন্টার ডট
    canvas.create_oval(center_x - 8, center_y - 8, center_x + 8, center_y + 8, fill="black", outline="gold", width=3,tags="hands")

    # প্রতি ৫০ms পর ঘড়ি আপডেট করো
    root.after(50, update_clock)

# ঘড়ি চালু করা
update_clock()
root.mainloop()
