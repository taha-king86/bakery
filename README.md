cat > install-final.sh << 'EOF'
#!/bin/bash

echo "🥖 نصب نهایی پروژه نانوایی"

# غیرفعال کردن محیط مجازی فعلی
deactivate 2>/dev/null

# نصب dlib از مخازن آرچ
echo "📦 نصب dlib از مخازن آرچ..."
sudo pacman -S python-dlib

# اگر نشد از AUR
if ! python -c "import dlib" 2>/dev/null; then
    echo "📦 نصب dlib از AUR..."
    yay -S python-dlib || (
        git clone https://aur.archlinux.org/python-dlib.git
        cd python-dlib
        makepkg -si
        cd ..
        rm -rf python-dlib
    )
fi

# فعال‌سازی محیط مجازی
source venv10/bin/activate

# نصب بقیه کتابخانه‌ها
echo "📦 نصب بقیه کتابخانه‌ها..."
pip install opencv-python pyzbar Pillow numpy python-dotenv face_recognition

# تست نصب
echo "🧪 تست نصب..."
python -c "
import dlib
import face_recognition
import cv2
import pyzbar
import PIL
import numpy
print('✅ همه چیز درست کار میکنه!')
print(f'📌 dlib version: {dlib.__version__}')
print(f'📌 OpenCV version: {cv2.__version__}')
print(f'📌 face_recognition version: {face_recognition.__version__}')
"

echo "✅ نصب کامل شد!"
EOF

chmod +x install-final.sh
./install-final.sh
