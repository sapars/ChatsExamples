#Примеры построения графиков

import tkinter as tk

#Функция закрытия прграммы
def do_close():
    window.destroy()


#Создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Программа построения графиков")

#Добавление метки заголовка
lbTitle = tk.Label(text="Примеры построения графиков", font=('Helvetica', 16, 'bold'), fg='#0000cc')
lbTitle.place(x=55, y=25)

#Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text="График 1", font=('Helvetica', 10, 'bold'), fg='#0000cc')
btnChart1.place(x=40, y=115, width=90, height=30)

lbChart1 = tk.Label(text="График синуса matplotlib")
lbChart1.place(x=170, y=122)


#Добавление кнопки закрытия программы
btnClose = tk.Button(window, text="Закрыть", font=('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)

#Запуск окна программы
window.mainloop()
 
