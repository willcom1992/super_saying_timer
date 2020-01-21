import tkinter.simpledialog as simpledialog
from tkinter import messagebox
import tkinter
from time import sleep
import random
import sys

# メッセージボックス編集
root = tkinter.Tk()
root.attributes('-topmost', True)
root.withdraw()
root.lift()
root.focus_force()

# famous saying.csvから辞書words_dict作成
words_dict = {}
with open('famous_saying.csv', encoding='utf-8') as csvfile:
    for row in csvfile:
        columns = row.strip().split(',')
        name = columns[1]
        meigen = columns[0]
        words_dict[name] = meigen


# secs秒後に名言表示
def timer():
    input_data = simpledialog.askstring("タイマー設定", "何秒後にタイマーを起動しますか？半角数字で入力してください")
    if input_data is None:
        messagebox.showinfo('終了', 'プログラムを終了します')
        sys.exit()
    try:
        sec = int(input_data)
    except ValueError:
        messagebox.showinfo('エラー', '秒数は半角数字で入力してね')
        timer()
    else:
        for i in range(0, sec):
            sleep(1)
        random_name = random.choice(list(words_dict.keys()))
        messagebox.showinfo(random_name, words_dict[random_name])
        ret = messagebox.askyesno('確認', 'プログラムを終了しますか？')
        if not ret:
            timer()


timer()
