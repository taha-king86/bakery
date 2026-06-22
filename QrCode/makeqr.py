import qrcode
import os
from utils import print_fa
# iscon = 0

while True:
    
    def make_qr(data, filename):
        os.makedirs("assets/barcodes", exist_ok=True)
        if not filename.lower().endswith('.png'):
            filename += '.png'
        

        full_path = os.path.join("assets/barcodes", filename)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        

        img = qr.make_image(fill_color="black", back_color="cyan")
        img.save(full_path)
        global iscon
        iscon = 1
        print_fa(f"QR کد با موفقیت در {full_path} ذخیره شد")
        print_fa('آیا می‌خواهید QR کد دیگری بسازید؟ (Y/N)')
        choice = input().strip().lower()
        if choice == 'N'or choice == 'n':
            print_fa('خروج از برنامه...')
            exit()
       
    if __name__ == "__main__":
        print_fa('متن یا لینک مورد نظر را وارد کنید:')
        text = input()
        print_fa('اسم فایل را بنویسید (حتماً در انتها .png را قرار دهید):')
        filename = input()
        make_qr(text, filename)
   
    
    