import tkinter as tk 
class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer App")
        self.master.geometry("300x200")

        self.time_left = 0
        self.timer_running = False

        self.label = tk.Label(master, text="00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False

    def reset_timer(self):
        self.time_left = 0
        self.timer_running = False
        self.update_label()

    def update_timer(self):
        if self.timer_running:
            self.time_left += 1
            self.update_label()
            self.master.after(1000, self.update_timer)

    def update_label(self):
        minutes, seconds, milisecond = divmod(self.time_left, 60)
        time_format = f"{minutes:02}:{seconds:02}"
        self.label.config(text=time_format)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()