import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from db.database import Database
# from utils import print_fa, play_voice

def show_last_customers(n=5, on_add_customer=None):
    def refresh(play_next_voice=False):
        for widget in frame.winfo_children():
            widget.destroy()
        for widget in info_frame.winfo_children():
            widget.destroy()
        for widget in next_frame.winfo_children():
            widget.destroy()
        db = Database()
        customers = db.get_today_customers()
        last_delivered = db.get_last_delivered_ticket()
        total_bread = db.get_today_total_bread_count()
        total_today = db.get_today_total_customers()
        db.close()
        last_ticket = customers[-1][1] if customers else '-'
        delivered_text = f' | آخرین نوبتی که نان گرفت: {last_delivered}' if last_delivered else ''
        bread_text = f' | مجموع نان‌های پخته شده امروز: {total_bread}'
        # نمایش نفر بعدی
        if customers:
            next_customer = customers[0]
            next_number = next_customer[1]
            next_bread = next_customer[2]
            next_text = f'نفر بعدی: نوبت {next_number}  |  تعداد نان: {next_bread}'
        
                
        else:
            next_text = 'در حال حاضر صفی وجود ندارد.'
        next_label = ttk.Label(next_frame, text=next_text, font=("B Nazanin", 28, "bold"), foreground='blue')
        next_label.pack(pady=10)
        # نمایش اطلاعات بالای صفحه
        info_label = ttk.Label(info_frame, text=f'تعداد نوبت‌های امروز: {total_today}   |   شماره نوبت آخرین نفر: {last_ticket}{delivered_text}{bread_text}', font=("B Nazanin", 14, "bold"))
        info_label.pack(pady=5)
        # فقط n نفر آخر را نمایش بده
        show_customers = customers[-n:] if n < len(customers) else customers
        for idx, customer in enumerate(show_customers):
            customer_id, ticket_number, bread_count, face_image_path, created_at = customer
            info = f'نوبت: {ticket_number}\nتعداد نان: {bread_count}\nزمان: {created_at}'
            # عکس چهره
            try:
                img = Image.open(face_image_path)
                img = img.resize((100, 100))
                photo = ImageTk.PhotoImage(img)
            except Exception:
                img = Image.new('RGB', (100, 100), color='gray')
                photo = ImageTk.PhotoImage(img)
                info += '\n(عکس یافت نشد)'
            panel = ttk.Label(frame, image=photo)
            panel.image = photo
            panel.grid(row=0, column=idx, padx=10, pady=10)
            label = ttk.Label(frame, text=info, justify='center')
            label.grid(row=1, column=idx, padx=10)
            # دکمه حذف
            def make_delete_func(cid=customer_id):
                return lambda: delete_customer(cid)
            del_btn = ttk.Button(frame, text='تحویل شد', command=make_delete_func())
            del_btn.grid(row=2, column=idx, pady=5)

    def delete_customer(customer_id):
        db = Database()
        db.delete_customer(customer_id)
        db.close()
        refresh(play_next_voice=True)

    def add_customer():
        if on_add_customer:
            root.destroy()
            on_add_customer()

    def reset_data():
        answer = tk.messagebox.askquestion('تایید ریست', 'آیا مطمئن هستید که می‌خواهید همه نوبت‌ها و داده‌ها را ریست کنید؟')
        if answer == 'yes':
            db = Database()
            db.reset_all_data()
            db.close()
            refresh()

    root = tk.Tk()
    root.title('به برنامه نانیکا  خوش امدید')
    root.geometry('1300x650')

    # دکمه تعریف مشتری جدید بالا سمت راست
    add_btn = ttk.Button(root, text='تعریف مشتری جدید', command=add_customer)
    add_btn.pack(anchor='ne', padx=20, pady=10)

    info_frame = ttk.Frame(root)
    info_frame.pack(fill=tk.X, side=tk.TOP, anchor='n')

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

    next_frame = ttk.Frame(root)
    next_frame.pack(fill=tk.X, side=tk.TOP, anchor='n')

    refresh()

    # دکمه ریست کوچک پایین سمت راست
    reset_btn = ttk.Button(root, text='ریست', width=6, command=reset_data)
    reset_btn.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # لیبل توسعه‌دهنده پایین صفحه
    dev_label = ttk.Label(root, text=' Shortcut Mt توسعه یافته توسط شرکت ', font=("B Nazanin", 9), foreground='gray')
    dev_label.pack(side=tk.BOTTOM, pady=3)
    
    root.mainloop()
