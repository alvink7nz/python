import tkinter as tk
from translate import Translator

def translate_to_chinese():
    text = entry_text.get("1.0", "end-1c")
    translator = Translator(to_lang="zh")
    translated_text = translator.translate(text)
    entry_translated.delete("1.0", "end")
    entry_translated.insert("1.0", translated_text)

# Create the main window
root = tk.Tk()
root.title("Language Converter")

# Style
root.configure(bg="#f0f0f0")
font_style = ("Arial", 12)

# Text Entry
label_text = tk.Label(root, text="Enter text:", bg="#f0f0f0", font=font_style)
label_text.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_text = tk.Text(root, font=font_style, height=5, width=30)
entry_text.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

# Translation Entry
label_translated = tk.Label(root, text="Translated text:", bg="#f0f0f0", font=font_style)
label_translated.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_translated = tk.Text(root, font=font_style, height=5, width=30)
entry_translated.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

# Translate Buttons
button_translate_to_chinese = tk.Button(root, text="Translate to Chinese", command=translate_to_chinese, font=font_style)
button_translate_to_chinese.grid(row=2, column=1, padx=5, pady=5, sticky="we")

root.mainloop()
