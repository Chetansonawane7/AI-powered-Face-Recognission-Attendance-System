import subprocess
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import util
import os
import datetime
import face_recognition

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")
        self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=300)
        self.register_new_user_button_main_window = util.get_button(self.main_window, 'register new user', 'green', self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)
        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)
        self.add_webcam(self.webcam_label)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'


    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)
        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()

        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)


        self._label.after(20, self.process_webcam)


    def login(self):
        unknown_img_path = './.tmp.jpg'

        cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)
        output = str(subprocess.check_output(['face_recognition', self.db_dir, unknown_img_path]))
        name = output.split(',')[1][:-5]
        if name in ['unknown_person']:
            util.msg_box('Uppss..', 'Unknown user. please register or try again')
        elif name in ['no_persons_found']:
            util.msg_box('no face', 'something went wrong, try again')
        else:
            util.msg_box('Your Attendance filled successfully', 'Welcome, {}'.format(name))
            with open(self.log_path, 'a') as f:
                f.write("{},{}\n".format(name,datetime.datetime.now()))
                f.close()
        os.remove(unknown_img_path)


    def register_new_user(self):
        self.registr_new_user_window = tk.Toplevel(self.main_window)
        self.registr_new_user_window.geometry("1200x520+370+120")

        self.accept_button_register_new_user_window = util.get_button(self.registr_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.registr_new_user_window, 'Try again', 'red',self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.registr_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.registr_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=240)

        self.text_label_register_new_user = util.get_text_label(self.registr_new_user_window, 'Division:')
        self.text_label_register_new_user.place(x=750, y=200)

        self.entry_text_register_new_user = util.get_entry_text(self.registr_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=160)

        self.text_label_register_new_user = util.get_text_label(self.registr_new_user_window, 'Roll Number:')
        self.text_label_register_new_user.place(x=750, y=120)

        self.entry_text_register_new_user = util.get_entry_text(self.registr_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=80)

        self.text_label_register_new_user = util.get_text_label(self.registr_new_user_window, 'Student Name:')
        self.text_label_register_new_user.place(x=750, y=40)
    def try_again_register_new_user(self):
        self.registr_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)


        self.register_new_user_capture = self.most_recent_capture_arr.copy()
    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")
        roll = self.entry_text_register_new_user.get(2.0, "end-2c")
        div  = self.entry_text_register_new_user.get(3.0, "end-3c")

        cv2.imwrite(os.path.join(self.db_dir, '{}.jpg'.format(name, roll, div)),self.register_new_user_capture)

        util.msg_box('Success','User registered successfully👍')

        self.registr_new_user_window.destroy()

if __name__ == "__main__":
    app = App()
    app.start()
