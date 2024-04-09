import tkinter as tk

class Data_Entry:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Data Entry Form")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    DataEntry = Data_Entry()
    DataEntry.run()