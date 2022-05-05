import gradio as gr
import pytesseract
import flag
import re
from PIL import ImageEnhance, ImageFilter
from datetime import date

""" 👉 Line 9 👇👇👇 is for windows users, you have to install Tesseract OCR Engine for windows, on your windows machine"""
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

""" 👉Line 12 👇👇👇 is for ubuntu users, you have to install Tesseract OCR Engine for ubuntu by running 👉 sudo apt install tesseract-ocr"""
pytesseract.pytesseract.tesseract_cmd ='/app/.apt/usr/bin/tesseract'
BD=flag.flag("BD")
EN=flag.flag("US")
def ocr_tool(lang,image):
    im = image
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    if re.search(r'\bEnglish',lang):
        lang='eng'
    elif re.search(r'\bBangla',lang):
        lang='ben'
    text = pytesseract.image_to_string(im,lang=lang)
    return text
iface=gr.Interface(ocr_tool,[
                gr.inputs.Dropdown(choices=[f'{EN} English' , f'{BD} Bangla'], type="value", default=None, label='Choose your language', optional=False),
                gr.inputs.Image(label='Upload an image',image_mode='L',tool='select',type='pil'),
                ],
                gr.outputs.Textbox(label='Results'),
                flagging_options=None,
                title='English and Bangla OCR',
                description='Perform OCR on Bengali and English texts in Images',
                theme='dark-grass',
                css='./style.css',article=f'<footer> ©{date.today().year} Copyright | Made by <a href="https://codingwithzk.netlify.app/"><strong>Ziaul Karim</strong></a> | with  <a href="https://gradio.app/"><strong>Gradio</strong></a></footer>',
                )

iface.launch(debug=True,height=300,width=500)
