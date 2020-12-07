import random
import tkinter
import sys
import tkinter.messagebox


def cai_shu_zi():
    global i
    if Button1['text'] == "游戏结束":
        sys.exit()
    else:
        try:
            text_check = ''.join(j for j in Entry1.get() if j in '0123456789')
            int_cin = int(text_check)
            if i == 5 and int_cin != n:
                Label2['text'] = "你已经猜了5次了，并且都没有猜中，本局是你的败北"
                Button1['text'] = "游戏结束"
                Entry1.delete(0, 'end')
            elif int_cin < n:
                Label2['text'] = "你输入的数比较小"
                i += 1
                Button1['text'] = "输入下一个数字"
                Entry1.delete(0, 'end')
            elif int_cin > n:
                Label2['text'] = "你输入的数比较大"
                i += 1
                Button1['text'] = "输入下一个数字"
                Entry1.delete(0, 'end')
            elif int_cin == n:
                Label2['text'] = "恭喜你猜对了"
                Button1['text'] = "游戏结束"
                Entry1.delete(0, 'end')
        except ValueError:
            tkinter.messagebox.showerror(title='Error', message='请输入数字')


if __name__ == "__main__":
    n = int(random.random() * 50 + 1)
    i = 0
    window = tkinter.Tk()
    window.title('猜数字游戏')
    window.geometry('500x200')
    Label1 = tkinter.Label(window, text='猜数字游戏', font=('Arial', 12), width=30, height=2)
    Label1.place(x=110, y=0, anchor='nw')
    Button1 = tkinter.Button(window, text='开始游戏', font=('Arial', 12), width=20, height=1, command=cai_shu_zi)
    Button1.place(x=150, y=50, anchor='nw')
    Label2 = tkinter.Label(window, text='游戏未开始', bg='green', font=('Arial', 12), width=50, height=2)
    Label2.pack(side='bottom')
    Entry1 = tkinter.Entry(window, width=7, show=None)
    Entry1.place(x=220, y=90, anchor='nw')
    window.mainloop()
