from tkinter import *

def click(key):
    if key == '=':       # '='버튼이면 수식을 계산하여 결과를 표시한다
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.insert(END, "오류!!!!!")
    elif key == 'C':
        entry.delete(0, END)
    else:
        entry.insert(END, key)


window = Tk()
window.title("간단한 계산기")

buttons = ['7', '8', '9', '+', 'C',
           '4', '5', '6', '-', ' ',
           '1', '2', '3', '*', ' ',
           '0', '.', '=', '/', ' ']

#반복문으로 버튼을 생성한다.
i = 0
for b in buttons:
    cmd = lambda x=b: click(x)
    but = Button(window, text=b, width=5, relief='ridge', command=cmd)
    but.grid(row=i//5+1, column=i%5)
    i += 1

#엔트리 위젯은 맨 윗줄의 5개의 셀에 걸쳐서 배치된다
entry = Entry(window, width=33, bg='yellow')
entry.grid(row=0, column=0, columnspan=5)

window.mainloop()
