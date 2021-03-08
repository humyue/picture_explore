from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import tkinter.filedialog
import glob
import os


class Picture(object):
    def __init__(self, init_window_name):
        self.window = init_window_name
        self.image_path = []
        self.img_num = 0
        self.welcome_path = './welcome.jpg'  # 初始化图片

    def init_window(self):
        self.window.geometry('800x520+500+100')
        self.window.resizable(0, 0)  # 防止用户调整尺寸
        self.window.title("图片预览器")
        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.window, tearoff=0)
        self.aboutmenu = Menu(self.window, tearoff=0)
        self.menubar.add_cascade(label='文件', menu=self.filemenu)
        self.menubar.add_cascade(label='关于', menu=self.aboutmenu)
        self.filemenu.add_command(label='打开', command=self.select_file)
        self.aboutmenu.add_command(label='版本号: 1.0')
        self.aboutmenu.add_command(label='作者: Humy')

        self.welcome = Label(self.window, text='图片预览器', fg='white', bg='#126bae', font=('Arial', 12), width=34,
                             height=2).place(x=230, y=10)
        self.img_open = Image.open(self.welcome_path).resize((258, 258))
        self.image = ImageTk.PhotoImage(self.img_open)
        self.label_img = Label(self.window, image=self.image)
        self.label_img.place(x=250, y=100)

        self.var_path = StringVar()

        self.path = Label(self.window,textvariable=self.var_path,
                         highlightcolor='red', font=('Arial', 12), height=1).place(x=250, y=380)

        self.pre_btn = Button(self.window, text='上一张', font=('Arial', 12), fg='white', width=10, height=1,
                              command=self.pre_img, bg='#126bae', state=DISABLED)
        self.pre_btn.place(x=250, y=430)
        self.next_btn = Button(self.window, text='下一张', font=('Arial', 12), fg='white', width=10, height=1,
                               command=self.next_img,bg='#126bae', state=DISABLED)
        self.next_btn.place(x=410, y=430)
        self.window.config(menu=self.menubar)
        self.window.mainloop()

    def select_file(self):
        chose_dir = tkinter.filedialog.askdirectory()
        path = glob.glob(os.path.join(chose_dir, '*.[jp][pn]g'))
        self.num = 0
        self.img_num = len(path)
        self.image_path = path
        if self.img_num == 0:
            tkinter.messagebox.showinfo(title='提示', message='当前文件夹文件没有图片!')
        else:
            self.var_path.set(self.image_path[0].replace('\\', '/'))
            img_open = Image.open(path[0]).resize((258, 258))
            image = ImageTk.PhotoImage(img_open)
            self.label_img.configure(image=image)
            self.label_img.image = image
            self.next_btn['state'] = NORMAL
            self.pre_btn['state'] = NORMAL

    def next_img(self):
        self.num += 1
        if self.num >= self.img_num:
            self.num = self.img_num - 1
            tkinter.messagebox.showinfo(title='提示', message='到头了哦！')
        img_open = Image.open(self.image_path[self.num]).resize((258, 258))
        self.var_path.set(self.image_path[self.num].replace('\\', '/'))
        image = ImageTk.PhotoImage(img_open)
        self.label_img.configure(image=image)
        self.label_img.image = image

    def pre_img(self):
        self.num -= 1
        if self.num < 0:
            self.num = 0
            tkinter.messagebox.showinfo(title='提示', message='啊偶！没有图片了')
        img_open = Image.open(self.image_path[self.num]).resize((258, 258))
        self.var_path.set(self.image_path[self.num].replace('\\', '/'))
        image = ImageTk.PhotoImage(img_open)
        self.label_img.configure(image=image)
        self.label_img.image = image


if __name__ == "__main__":
    windows = Tk()
    picture = Picture(windows)
    picture.init_window()
