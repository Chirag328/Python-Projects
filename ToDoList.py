import tkinter as tk
from tkinter import messagebox, filedialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("420x500")
        self.root.configure(bg="#fff8f0")  # Light background

        self.tasks = []

        # Heading
        self.heading = tk.Label(root, text="📝 To-Do List", font=("Arial", 20, "bold"), bg="#fff8f0", fg="#ff6f61")
        self.heading.pack(pady=15)

        # Entry Box
        self.task_entry = tk.Entry(root, width=28, font=("Arial", 14), bd=2, relief=tk.GROOVE, fg="#333")
        self.task_entry.pack(pady=10)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="#fff8f0")
        self.button_frame.pack()

        self.create_colored_button(self.button_frame, "Add Task", self.add_task, "#61d4b3", 0, 0)
        self.create_colored_button(self.button_frame, "Remove Task", self.remove_task, "#ff9a76", 0, 1)
        self.create_colored_button(self.button_frame, "Save Tasks", self.save_tasks, "#6c5ce7", 1, 0)
        self.create_colored_button(self.button_frame, "Load Tasks", self.load_tasks, "#fab1a0", 1, 1)

        # Listbox for tasks
        self.task_listbox = tk.Listbox(root, width=40, height=14, font=("Arial", 12), bd=2, relief=tk.SUNKEN,
                                       bg="#fefefe", fg="#2d3436", selectbackground="#ffeaa7")
        self.task_listbox.pack(pady=15)

    def create_colored_button(self, frame, text, command, color, row, column):
        button = tk.Button(frame, text=text, command=command, width=12, bg=color, fg="white",
                           font=("Arial", 10, "bold"), activebackground="#333", activeforeground="white")
        button.grid(row=row, column=column, padx=10, pady=6)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for task in tasks:
                    f.write(task + "\n")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                tasks = f.readlines()
            self.task_listbox.delete(0, tk.END)
            for task in tasks:
                self.task_listbox.insert(tk.END, task.strip())

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
