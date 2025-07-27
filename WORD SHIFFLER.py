import tkinter as tk
import random
import threading
import time

# Calm Input Window
class InputWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Input ")
        self.root.geometry("600x300")
        self.root.configure(bg="#D8E2DC")  # Pleasant Calm Color (Soft Pinkish)

        self.label = tk.Label(self.root, text="Enter Your Sentence:", font=("Arial", 14), bg="#D8E2DC", fg="#333333")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 16), width=40)
        self.entry.pack(pady=10)

        self.button = tk.Button(self.root, text="Start Simulation", command=self.start_simulation, 
                                font=("Arial", 14), bg="#A9DEF9", fg="#333333")
        self.button.pack(pady=20)

        self.root.mainloop()

    def start_simulation(self):
        sentence = self.entry.get().strip()
        if sentence:
            self.root.destroy()  # Close input window
            ResultWindow(sentence)  # Open result window

# Scary Result Window with Jackpot Simulation
class ResultWindow:
    def __init__(self, target):
        self.root = tk.Tk()
        self.root.title("SCARY RESULT 🩸")
        self.root.geometry("700x400")
        self.root.configure(bg="black")  # Scary dark background

        self.output_label = tk.Label(self.root, text="", fg="red", bg="black", font=("Courier", 24, "bold"))
        self.output_label.pack(expand=True)

        # Start simulation in new thread (to avoid freezing)
        threading.Thread(target=self.simulate_jackpot, args=(target,), daemon=True).start()
        self.root.mainloop()

    def simulate_jackpot(self, target):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()_+-=[]{}|;:,.<>?/~`'
        current = [' ' for _ in target]

        for i in range(len(target)):
            for _ in range(20):  # Shuffle effect
                current[i] = random.choice(chars)
                self.update_output("".join(current))
                time.sleep(0.05)

            # Lock correct character
            current[i] = target[i]
            self.update_output("".join(current))
            time.sleep(0.15)

        # Final scary result shown a bit longer
        self.update_output("".join(current))
        time.sleep(1.5)
        self.update_output("".join(current) + "\n\n💀 The SATEN Has Spoken! 💀")

    def update_output(self, text):
        self.output_label.config(text=text)
        self.root.update()

# Run the program
if __name__ == "__main__":
    InputWindow()
