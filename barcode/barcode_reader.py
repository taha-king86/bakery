from pyzbar import pyzbar
import cv2
from utils import print_fa

def read_barcode_from_camera():
    cap = cv2.VideoCapture(0)
    print_fa('لطفاً رسید را جلوی دوربین بگیرید و کلید "Space" را فشار دهید.')
    ticket_number = None
    bread_count = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print_fa('خطا در دریافت تصویر از دوربین!')
            break
        cv2.imshow('اسکن بارکد/QR - برای ثبت تصویر Space را بزنید', frame)
        key = cv2.waitKey(1)
        if key == 32:  
            barcodes = pyzbar.decode(frame)
            if not barcodes:
                print_fa('هیچ بارکد یا QRی شناسایی نشد. دوباره تلاش کنید.')
                continue
            for barcode in barcodes:
                data = barcode.data.decode('utf-8')
                # فرض: داده به صورت "ticket_number,bread_count" است
                try:
                    ticket_number, bread_count = data.split(',')
                    bread_count = int(bread_count)
                    print_fa(f'شماره نوبت: {ticket_number} | تعداد نان: {bread_count}')
                    break
                except Exception as e:
                    print_fa('فرمت بارکد صحیح نیست!')
                    continue
            if ticket_number and bread_count:
                break
        elif key == 27:  # ESC
            print_fa('لغو شد.')
            break
    cap.release()
    cv2.destroyAllWindows()
    return ticket_number, bread_count
