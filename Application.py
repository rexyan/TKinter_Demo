import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
import tkinter.filedialog


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.label_dest = None
        self.content_dest = None
        self.entry_dest = None
        self.label_suc = None
        self.content_suc = None
        self.entry_suc = None
        self.label_fail = None
        self.content_fail = None
        self.entry_fail = None
        self.button_start = None
        self.text = None
        self.running = None
        self.select_file_btn = None
        master.title('文件选择测试工具')
        self.pack()
        self.createwidgets()

    def __del__(self):
        print('回收垃圾')

    def createwidgets(self):
        """
        创建窗口部件
        :return:
        """
        # 最下方信息显示
        self.text = ScrolledText(self, bg='white')
        self.text.grid(row=4, columnspan=3)

        # 来源路径
        self.label_dest = tk.Label(self)
        self.label_dest["text"] = '来源路径:'
        self.label_dest.grid(row=0, column=0)

        self.content_dest = tk.StringVar()
        self.entry_dest = tk.Entry(self)
        self.entry_dest["textvariable"] = self.content_dest
        self.entry_dest.grid(row=0, column=1)

        # 选择文件按钮1
        self.add_select_file_button('选择文件1', lambda: self.select_file(collback_msg_func=self.content_dest), [0, 2])

        # 成功路径
        self.label_suc = tk.Label(self)
        self.label_suc["text"] = '成功路径:'
        self.label_suc.grid(row=1, column=0)

        self.content_suc = tk.StringVar()
        self.entry_suc = tk.Entry(self)
        self.entry_suc["textvariable"] = self.content_suc
        self.entry_suc.grid(row=1, column=1)

        # 选择文件按钮2
        self.add_select_file_button('选择文件2', lambda: self.select_file(collback_msg_func=self.content_suc), [1, 2])

        # 失败路径
        self.label_fail = tk.Label(self)
        self.label_fail["text"] = '失败路径:'
        self.label_fail.grid(row=2, column=0)

        self.content_fail = tk.StringVar()
        self.entry_fail = tk.Entry(self)
        self.entry_fail["textvariable"] = self.content_fail
        self.entry_fail.grid(row=2, column=1)

        # 选择文件按钮3
        self.add_select_file_button('选择文件3', lambda: self.select_file(collback_msg_func=self.content_fail), [2, 2])

        # 开始按钮
        self.button_start = tk.Button(self, text='开始')
        self.button_start['command'] = self.start
        self.button_start['fg'] = 'green'
        self.button_start.grid(row=3, column=0)

        # 停止按钮
        self.quit = tk.Button(self, text="停止", fg="red", command=self.quit)
        self.quit.grid(row=3, column=1)

    def add_select_file_button(self, text, command, row_column):
        """
        动态增加选择文件按钮
        :param text: 按钮的名称
        :param command: 按钮触发的函数
        :param row_column: 按钮的位置
        :return:
        """
        self.select_file_btn = tk.Button(self)
        self.select_file_btn["text"] = text
        self.select_file_btn.grid(row=row_column[0], column=row_column[1])
        self.select_file_btn['command'] = command

    def select_file(self, collback_msg_func):
        """
        点击选择文件按钮后触发函数
        :param collback_msg_func: 内容回显的对象
        :return:
        """
        filenames = tkinter.filedialog.askopenfilenames()
        if len(filenames) != 0:
            string_filename = ""
            for i in range(0, len(filenames)):
                string_filename += str(filenames[i]) + "\n"

            # 回显选择的文件信息
            if hasattr(collback_msg_func, 'set'):
                getattr(collback_msg_func, 'set')(string_filename)
        else:
            print("您没有选择任何文件")

    def start(self):
        """
        点击开始按钮触发
        :return:
        """
        self.display_message('提示：程序已启动！')
        self.running = True
        self.display_message('信息：' + self.content_dest.get())
        self.display_message('信息：' + self.entry_dest.get())
        self.display_message('信息：' + self.content_fail.get())

    def quit(self):
        """
        添加退出按钮触发
        :return:
        """
        self.running = False
        self.display_message('提示：程序已停止！')

    def display_message(self, message, position='end'):
        """
        将内容显示在下面的ScrolledText中
        :param message: 显示的文字
        :param position: 显示位置，默认为end
        :return:
        """
        if "\n" not in message:  # 换行显示
            message = message + "\n"
        self.text.insert(position, message)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
