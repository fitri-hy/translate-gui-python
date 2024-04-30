import tkinter as tk
from tkinter import ttk
import requests

def translate_text():
    query = input_text.get("1.0", "end-1c")
    target_lang = language_choice.get()
    api_url = f"https://api.hy-tech.my.id/api/translate?text={query}&target={target_lang}"

    try:
        response = requests.get(api_url)
        data = response.json()
        translation = data["translation"]
        output_text.delete("1.0", "end")
        output_text.insert("end", translation)
    except Exception as e:
        output_text.delete("1.0", "end")
        output_text.insert("end", f"Error: {str(e)}")

root = tk.Tk()
root.title("Translator")

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

input_text = tk.Text(main_frame, height=5, font=("Helvetica", 10))
input_text.pack(fill="both", expand=True)

button_frame = ttk.Frame(main_frame)
button_frame.pack(fill="x", pady=10)

languages = ["id", "en", "es", "fr", "ar", "bn", "bs", "ca", "cs", "cy", "da", "de", "el", "fi", "fil", "he", "hi", "hr", "ht", "hu", "hy", "it", "ja", "kk", "ko", "lt", "lv", "ms", "mt", "mww", "nl", "no", "pl", "pt", "ro", "ru", "sk", "sl", "sr", "sv", "sw", "ta", "te", "th", "tlh", "tr", "uk", "ur", "vi", "yua", "zh-Hans", "zh-Hant"]
language_choice = ttk.Combobox(button_frame, values=languages, font=("Helvetica", 10))
language_choice.set("id")
language_choice.pack(side="left", padx=(0, 10))

translate_button = ttk.Button(button_frame, text="Terjemahkan", command=translate_text, style="TButton")
translate_button.pack(side="right", padx=(10, 0))

output_text = tk.Text(main_frame, height=5, font=("Helvetica", 10))
output_text.pack(fill="both", expand=True, padx=0, pady=10)

root.mainloop()
