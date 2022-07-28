import tkinter as tk

LABEL_FONT = ("Helvetica", 16, "bold")
COUNT_C = "#FF869E"
KEEP_C = "#6CC4A1"


def clock(count, length):
    """ Counts seconds and compares text length after each sec, starts countdown if length doesn't change."""
    count_sec = count % 60
    length2 = len(text_box.get("1.0", tk.END).strip(" "))
    # Compares length
    if length2 > length:
        count = 6
        length = length2
        label_clock["text"] = f"Keep it up!"
        label_clock["fg"] = KEEP_C

    else:
        # Check if time is finished
        if count == 0:
            clear_text()
            label_clock["text"] = f"Cleared!"
            return
        else:
            label_clock["text"] = f"Timer: 0{count_sec}"
            label_clock["fg"] = COUNT_C

    timer = window.after(1000, clock, count - 1, length)


def start_countdown():
    """ Clear primary text and starts clock function."""
    clear_text()
    text_box.focus()
    count = 5
    length = len(text_box.get("1.0",tk.END).strip(" "))
    clock(count, length)


def clear_text():
    """Clears text."""
    text_box.delete("1.0", tk.END)


# APP UI
window = tk.Tk()
window.title("Write write write!")
window.minsize(600,300)
window.config(padx=20, pady=30)

label_clock = tk.Label(text="Press start and write!", font=LABEL_FONT, fg=KEEP_C)
label_clock.pack()

label_info = tk.Label(text="Write your text without stopping, if you stop for 5 secs, text will disappear... 😭")
label_info.config(padx=0, pady=10)
label_info.pack()

text_box = tk.Text(height=20, width=60)
text_box.insert('end', "Write your text here....")
text_box.pack()

button_start = tk.Button(text="Start", command=start_countdown)
button_start.pack()


window.mainloop()