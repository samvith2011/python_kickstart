import tkinter as tk
import random

class MultiplayerJumbleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Guess Word New!")
        self.root.configure(bg="#000000")  # Light blue background

        self.player_turn = 1
        self.score = {1: 0, 2: 0}
        self.original_word = ""
        self.jumbled = ""
        self.timer = 15
        self.timer_id = None
        self.round_active = True

        self.jumbled_word = tk.StringVar()
        self.status_text = tk.StringVar()
        self.score_text = tk.StringVar()
        self.input_label = tk.StringVar()
        self.timer_text = tk.StringVar()
        self.input_label.set("")

        tk.Label(root, text="Word Jumble Game", font=('Arial', 26, 'bold'), bg="#000000").pack(pady=10)
        tk.Label(root, textvariable=self.jumbled_word, font=('Courier', 32, 'bold'), fg='blue', bg="#000000").pack(pady=10)
        tk.Label(root, textvariable=self.input_label, font=('Arial', 18), bg="#000000").pack(pady=5)

        self.entry_frame = tk.Frame(root, bg="#000000")
        self.entry_frame.pack(pady=5)

        self.entry = tk.Entry(self.entry_frame, font=('Arial', 20), width=20, show='*')
        self.entry.pack()

        self.submit_btn = tk.Button(root, text="Submit", font=('Arial', 16), command=self.handle_submit)
        self.submit_btn.pack(pady=10)

        tk.Label(root, textvariable=self.status_text, font=('Arial', 16), bg="#000000").pack(pady=5)
        tk.Label(root, textvariable=self.timer_text, font=('Arial', 16), fg='red', bg="#000000").pack(pady=2)
        tk.Label(root, textvariable=self.score_text, font=('Arial', 16), bg="#000000").pack(pady=5)

        self.score_text.set("Score - Player 1: 0 Points | Player 2: 0 Points")
        self.reset_round()

    def reset_round(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        self.entry.config(state='normal', show='*')
        self.entry.delete(0, tk.END)
        self.original_word = ""
        self.jumbled = ""
        self.jumbled_word.set("")
        self.status_text.set("")
        self.timer_text.set("")
        self.input_label.set(f"Player {self.player_turn}, enter a  REAL word:")
        self.submit_btn.config(text="Submit")
        self.round_active = True

    def jumble_word(self, word):
        return ''.join(random.sample(word, len(word))) if len(word) > 1 else word

    def handle_submit(self):
        if not self.round_active:
            return

        input_text = self.entry.get().strip().lower()

        if not self.original_word:
            if not input_text.isalpha():
                self.status_text.set("Please enter a real word that exists")
                return

            self.original_word = input_text
            self.jumbled = self.jumble_word(self.original_word)
            self.jumbled_word.set(f"Jumbled Word: {self.jumbled}")
            self.entry.delete(0, tk.END)

            # Switch to Player 2 — remove masking
            self.entry.config(show='', font=('Arial', 20))
            self.input_label.set(f"Player {3 - self.player_turn}, guess the word:")
            self.status_text.set("")
            self.submit_btn.config(text="Guess")
            self.start_timer()
        else:
            self.check_guess(input_text)

    def check_guess(self, guess):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        self.round_active = False
        self.entry.config(state='disabled')

        if guess == self.original_word:
            self.status_text.set(f"Correct! Player {3 - self.player_turn} scores a point.")
            self.score[3 - self.player_turn] += 1
        else:
            self.status_text.set(f"Wrong! The word was: {self.original_word}")

        self.update_score_display()
        self.switch_turn()

    def switch_turn(self):
        self.player_turn = 2 if self.player_turn == 1 else 1
        self.root.after(2500, self.reset_round)

    def update_score_display(self):
        self.score_text.set(f"Score - Player 1: {self.score[1]} | Player 2: {self.score[2]}")

    def start_timer(self):
        self.timer = 15
        self.update_timer()

    def update_timer(self):
        self.timer_text.set(f"Time left: {self.timer} seconds")
        if self.timer > 0:
            self.timer -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.status_text.set(f"Time's up! The word was: {self.original_word}")
            self.entry.config(state='disabled')
            self.round_active = False
            self.switch_turn()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")
    app = MultiplayerJumbleGame(root)
    root.mainloop()