import pygame
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

# Initialize Pygame Mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Syntax wave player")
        
        # --- Adjusted Size (Wider) ---
        self.width = 1200
        self.height = 500
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)

        # 1. Background Image Setup
        # Resizing the background to the new wider dimensions
        self.bg_image = Image.open("syntax wave.jpg")
        self.bg_image = self.bg_image.resize((self.width, self.height), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Using Canvas to allow absolute centering on a wider field
        self.bg_canvas = tk.Canvas(self.root, width=self.width, height=self.height, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.bg_canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # 2. Graphical Play Button (Cleaned up)
        try:
            play_img = Image.open("play_icon.png") 
            play_img = play_img.resize((100, 100), Image.Resampling.LANCZOS)
            self.play_photo = ImageTk.PhotoImage(play_img)
            
            self.play_btn = tk.Button(
                root, 
                image=self.play_photo, 
                command=self.load_and_play, 
                bg="black",           
                activebackground="black", 
                borderwidth=0, 
                highlightthickness=0,
                cursor="hand2"
            )
        except FileNotFoundError:
            self.play_btn = tk.Button(root, text="▶ PLAY MUSIC", command=self.load_and_play, 
                                      font=("Arial", 14, "bold"), bg="black", fg="white", 
                                      borderwidth=0, highlightthickness=0)

        # Centering the Play Button on the wider canvas (600 is half of 1200)
        self.bg_canvas.create_window(600, 340, window=self.play_btn)

        # 3. Status Label
        self.label = tk.Label(
            root, 
            text="Select a file from your local dictionary", 
            fg="white", 
            bg="black", 
            font=("Arial", 12)
        )
        self.bg_canvas.create_window(600, 410, window=self.label)

        # 4. Stop Button (Wider and Flat)
        self.stop_btn = tk.Button(
            root, 
            text="STOP", 
            command=self.stop_music, 
            width=15, 
            bg="#c0392b", 
            fg="white",
            relief="flat",
            borderwidth=0
        )
        self.bg_canvas.create_window(600, 460, window=self.stop_btn)

    def load_and_play(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            song_name = os.path.basename(file_path)
            self.label.config(text=f"Playing: {song_name}")
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
   
    def stop_music(self):
        pygame.mixer.music.stop()
        self.label.config(text="Music Stopped")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
