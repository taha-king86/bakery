#install package in (requirements.txt) before run this program
from barcode.barcode_reader import read_barcode_from_camera
from face.face_recog import capture_and_save_face
from db.database import Database
from ui.display import show_last_customers
from utils import print_fa

def add_new_customer():
    print_fa('--- ثبت مشتری جدید ---')
    ticket_number, bread_count = read_barcode_from_camera()
    if not ticket_number or not bread_count:
        print_fa('فرآیند لغو شد یا بارکد معتبر نبود.')
        show_last_customers(n=20, on_add_customer=add_new_customer)
        return

    face_image_path = capture_and_save_face()
    if not face_image_path:
        print_fa('فرآیند لغو شد یا چهره ثبت نشد.')
        show_last_customers(n=20, on_add_customer=add_new_customer)
        return

    db = Database()
    db.add_customer(ticket_number, bread_count, face_image_path)
    db.close()
    print_fa('اطلاعات با موفقیت ذخیره شد.')
    show_last_customers(n=20, on_add_customer=add_new_customer)

if __name__ == '__main__':
    show_last_customers(n=20, on_add_customer=add_new_customer)
