# Based on https://github.com/bolapara/clipboardToTxt and modified


from datetime import date,datetime
import sys
import pyperclip

today = date.today()
today_date = today.strftime("%b-%d-%Y")

copied = pyperclip.paste()
flag = 0

while True:
    if flag == 1:
        print("Copied and Pasted")
        flag = 0
    paste = pyperclip.paste()
    if paste != copied:
        now = datetime.now()
        try:
            time = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            filename = str(today_date) +".txt"
            with open(filename, 'a') as f:
                f.write('{}\n-----------------------\n{}\n$\n'.format(dt_string,paste))
                copied = paste
                flag = 1
        except Exception as e:
            sys.stderr.write("Error: {}".format(e))
            break