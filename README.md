# Banglish-OCR

## Important
You are going to need Tesseract OCR engine to run this app, go to the link below to download and install the engine.

      https://tesseract-ocr.github.io/tessdoc/Downloads.html

<h3 align = "center"> Or</h3>

      sudo apt install tesseract-ocr
      
# About this Repository
Banglish OCR is an interactive Optical Character Recognition Prototype for Bangla and English. Made with Gradio and Pytesseract.

## Clone it

      https://github.com/iamzehan/banglish-ocr.git

## Follow the steps below to run this on your local machine.

1. Create Virtual Environment

        virtualenv env
    
2. Activate Virtual Environment
   
   for bash
   
        source env/Scripts/activate
   
   for windows
        
        env/Scripts/activate
    
3. Install requirements

        pip install -r requirements.txt

4. run the program

        python app.py
    
5. open your browser and visit the link below while the program is running

        http://127.0.0.1:7860/  
        
6. The app looks like this -
![alt text](https://res.cloudinary.com/du4udzfii/image/upload/v1651769751/Screenshot_93_48394c5ea6.png)


7. End note

_`runtime.txt` controls your python version, use the current version on your machine and install the packages accordingly.
`Aptfile` contains the name of the packages that needs to be installed on your host server's machine. 
`setup.sh` contains the port and server name. `Procfile` runs the command to start the app on the web._
