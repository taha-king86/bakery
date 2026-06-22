import arabic_reshaper
from bidi.algorithm import get_display

def print_fa(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    print(bidi_text)

# اعلان صوتی فارسی
import pyttsx3

def play_voice(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 1)
    # اگر صدای فارسی نصب بود، انتخاب کن
    #فعلا برنامه این جا کار نمیکنه
    #its not worked
    voices = engine.getProperty('voices')
    for v in voices:
        if 'fa' in v.id or 'persian' in v.name.lower():
            engine.setProperty('voice', v.id)
            break
    engine.say(text)
    engine.runAndWait() 