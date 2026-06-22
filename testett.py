import qrcode
import os
from utils import print_fa

def make_qr(data, filename):
    # ایجاد پوشه اگر وجود نداشته باشد
    os.makedirs("assets/barcodes", exist_ok=True)
    
    # اطمینان از اینکه نام فایل با .png تمام میشود
    if not filename.lower().endswith('.png'):
        filename += '.png'
    
    # ساخت مسیر کامل ذخیره‌سازی
    full_path = os.path.join("assets/barcodes", filename)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="red")
    img.save(full_path)
    print_fa(f"QR کد با موفقیت در {full_path} ذخیره شد")

if __name__ == "__main__":
    print_fa('متن یا لینک مورد نظر را وارد کنید:')
    text = input()
    print_fa('اسم فایل را بنویسید (حتماً در انتها .png را قرار دهید):')
    filename = input()
    make_qr(text, filename)