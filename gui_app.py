# text_generation.py

from transformers import pipeline

# Load GPT-2 Text Generation Pipeline
generator = pipeline("text-generation", model="gpt2-medium", framework="pt")

def generate_gpt2_text(prompt):
    """
    Generate text using GPT-2 model based on input prompt.
    
    Args:
        prompt (str): Starting input text.
    
    Returns:
        str: Generated continuation text.
    """
    if not prompt.strip():
        return "⚠️ Please enter meaningful starting text."

    result = generator(
        prompt,
        max_length=250,
        num_return_sequences=1,
        temperature=0.5,
        top_p=0.9,
        do_sample=True,
        early_stopping=True
    )

    return result[0]['generated_text']

# gui_app.py

import tkinter as tk
from text_generation import generate_gpt2_text  # Importing function from main logic

# Function linked to button click
def generate_text():
    user_input = entry.get()
    output = generate_gpt2_text(user_input)

    output_text.configure(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)
    output_text.configure(state='disabled')

# GUI Setup
root = tk.Tk()
root.title("GPT-2 Text Generator")
root.geometry("800x600")
root.configure(bg="#f5f5f5")

# Title Label
title_label = tk.Label(root, text="GPT-2 Generative Text Model", font=("Segoe UI", 20, "bold"))
title_label.pack(pady=20)

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text=" Enter your starting text:", font=("Segoe UI", 12))
input_label.pack(anchor='w')

entry = tk.Entry(input_frame, width=80, font=("Segoe UI", 12))
entry.pack(pady=8)

# Generate Button
generate_button = tk.Button(root, text=" Generate Text", command=generate_text)
generate_button.pack(pady=10)

# Output Section
output_label = tk.Label(root, text=" Generated Text:", font=("Segoe UI", 12))
output_label.pack(anchor='w', padx=20)

output_text = tk.Text(root, height=20, width=90, font=("Consolas", 12), wrap=tk.WORD, bg="#ffffff")
output_text.pack(padx=20, pady=10)
output_text.configure(state='disabled')

# Run GUI
root.mainloop()
