import tkinter as tk#tktktktktktktktkkttktk mustarrddddd
from tkinter import messagebox
import os
import subprocess
import random

DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")#where it is gon save

class Snowflake:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
        self.id = canvas.create_oval(self.x, self.y, self.x+self.size, self.y+self.size, fill="white", outline="white")

    def fall(self):
        self.y += self.speed
        self.canvas.move(self.id, 0, self.speed)
        if self.y > self.canvas.winfo_height():
            self.y = 0
            self.canvas.move(self.id, 0, -self.canvas.winfo_height())

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Yt")# nameeeeeeeeeeeeeee mustard 67
        self.root.geometry("300x200")# resize this if you want idk
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.snowflakes = [Snowflake(self.canvas, 600, 400) for _ in range(100)]
        self.animate_snow()

        self.url_entry = tk.Entry(root, font=("Arial", 14), bg="black", fg="white", insertbackground="white")
        self.canvas.create_window(100, 150, anchor="nw", window=self.url_entry, width=400, height=30)

        self.download_button = tk.Button(root, text="Download Best Quality", command=self.download_video,
                                         font=("Arial", 12, "bold"), bg="dark cyan", fg="white", activebackground="cyan4")##za button 
        self.canvas.create_window(220, 200, anchor="nw", window=self.download_button)

    def animate_snow(self):
        for flake in self.snowflakes:
            flake.fall()
        self.root.after(33, self.animate_snow)

    def download_video(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")# fallback
            return

        try:
            command = [
                "yt-dlp",
                "-f", "bestvideo+bestaudio/best",#i dont think this works
                "-o", os.path.join(DOWNLOAD_PATH, "%(title)s.%(ext)s"),
                url
            ]

            subprocess.run(command, check=True)
            messagebox.showinfo("Success", f" Download complete!\nSaved to: {DOWNLOAD_PATH}")
        except Exception as e:
            messagebox.showerror("Error", f" Download failed:\n{e}")

if __name__ == "__main__":# wohoo
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
