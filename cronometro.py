from tkinter import *
from datetime import datetime, timedelta

class Cronometro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro")
        self.master.geometry("400x400")
        self.master.configure(bg="#333333")
        
        self.time_var = StringVar()
        self.time_var.set("00:00:00")

        self.timer_label = Label(self.master, textvariable=self.time_var, font=("Helvetica", 48), fg="#FFFFFF", bg="#333333")
        self.timer_label.pack(pady=30)

        self.start_button = Button(self.master, text="Iniciar", font=("Helvetica", 18), bg="#00FF00", command=self.start)
        self.start_button.pack(side=LEFT, padx=10)

        self.pause_button = Button(self.master, text="Pausar", font=("Helvetica", 18), bg="#FFA500", command=self.pause)
        self.pause_button.pack(side=LEFT, padx=10)

        self.reset_button = Button(self.master, text="Resetar", font=("Helvetica", 18), bg="#FF0000", command=self.reset)
        self.reset_button.pack(side=LEFT, padx=10)

        self.paused = False
        self.start_time = None
        self.paused_time = None
        self.total_paused_time = timedelta()

    def start(self):
        if self.paused:
            self.paused_time += datetime.now() - self.pause_start_time
            self.paused = False
        elif self.start_time is None:
            self.start_time = datetime.now()
        else:
            self.total_paused_time += datetime.now() - self.pause_start_time

        self.update()

    def pause(self):
        if not self.paused:
            self.paused = True
            self.pause_start_time = datetime.now()
        else:
            self.paused = False
            self.total_paused_time += datetime.now() - self.pause_start_time
            self.pause_start_time = None

    def reset(self):
        self.start_time = None
        self.paused_time = timedelta()
        self.total_paused_time = timedelta()
        self.paused = False
        self.time_var.set("00:00:00")

    def update(self):
        if not self.paused and self.start_time is not None:
            if self.paused_time is None:
                self.paused_time = timedelta()

            elapsed_time = datetime.now() - self.start_time - self.total_paused_time - self.paused_time
            self.time_var.set(str(elapsed_time).split(".")[0])

        self.master.after(100, self.update)

root = Tk()
cronometro = Cronometro(root)
root.mainloop()
