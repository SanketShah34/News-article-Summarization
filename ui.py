from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from functools import partial
from controller import input_url, input_textbox, input_browse


def urlbox_clear(input_control, output_control):
    input_control.delete(0, 'end')
    output_control.delete(1.0, 'end')

def textbox_clear(input_control, output_control):
    input_control.delete(1.0, 'end')
    output_control.delete(1.0, 'end')

def browsebox_clear(input_control, output_control):
    input_control.delete(0, 'end')
    output_control.delete(1.0, 'end')

def browse_files(input_contol):
    filename = askopenfilename()
    input_contol.insert(INSERT, filename)

def urlbox_submit(url_input, url_output):
    result = input_url(url_input)
    url_output.insert(INSERT, result)

def textbox_submit(textbox_input, textbox_output):
    result = input_textbox(textbox_input)
    textbox_output.insert(INSERT, result)

def browsebox_submit(browse_input, browse_output):
    result = input_browse(browse_input)
    browse_output.insert(INSERT, result)

def generate_ui():
    top = Tk()
    top.title("AUTO SUMMARIZATION TOOL")
    top.geometry("925x530")

    notebook = ttk.Notebook(top)
    notebook.pack()

    frame1 = ttk.Frame(notebook, width=300, height=500)
    frame2 = ttk.Frame(notebook, width=300, height=500)
    frame3 = ttk.Frame(notebook, width=300, height=500)

    notebook.add(frame1, text='URL')
    url_label_input = Label(frame1, text="INPUT:")
    url_label_input.grid(row=0, column=0, pady="10", padx="5")
    url_input = Entry(frame1, bg="grey", width="140")
    url_input.grid(row=0, column=1, columnspan="2", padx="5")
    url_label_output = Label(frame1, text="OUTPUT:")
    url_label_output.grid(row=1, column=0, pady="10", padx="5")
    url_output = Text(frame1, bg="#adb2ba", height="22", width="105")
    url_output.grid(row=2, column=1, columnspan="2", pady="10", padx="5")
    url_clear = Button(frame1, text="RESET", bg="#3971cc", fg="white", command=partial(urlbox_clear, url_input, url_output))
    url_clear.grid(row=3, column=1, padx="5", pady="10")
    url_submit = Button(frame1, text="SUMMARIZE !!", bg="#3971cc", fg="white", command=partial(urlbox_submit, url_input, url_output))
    url_submit.grid(row=3, column=2, padx="5", pady="10")

    notebook.add(frame2, text='TEXT')
    text_label_input = Label(frame2, text="INPUT:")
    text_label_input.grid(row=0, column=0, pady="10", padx="5")
    textbox_input = Text(frame2, bg="grey", height="7.5", width="105")
    textbox_input.grid(row=0, column=1, columnspan="2", pady="10", padx="5")
    text_label_output = Label(frame2, text="OUTPUT:")
    text_label_output.grid(row=1, column=0, pady="10", padx="5")

    textbox_output = Text(frame2, bg="#adb2ba", height="15", width="105")
    scrollbar = Scrollbar(frame2, orient=VERTICAL, command=textbox_output.yview)
    textbox_output.grid(row=2, column=1, columnspan="2", pady="10", padx="5")
    textbox_output["yscrollcommand"] = scrollbar.set

    text_clear = Button(frame2, text="RESET", bg="#3971cc", fg="white", command=partial(textbox_clear, textbox_input, textbox_output))
    text_clear.grid(row=3, column=1, padx="5", pady="10")
    text_submit = Button(frame2, text="SUMMARIZE !!", bg="#3971cc", fg="white", command=partial(textbox_submit, textbox_input, textbox_output))
    text_submit.grid(row=3, column=2, padx="5", pady="10")

    notebook.add(frame3, text='BROWSE')
    browse_input = Entry(frame3, bg="grey", width="140")
    browse_input.grid(row=0, column=1, columnspan="2", padx="5")
    browse_submit = Button(frame3, text="BROWSE", bg="#3971cc", fg="white", command=partial(browse_files, browse_input))
    browse_submit.grid(row=0, column=0, pady="10", padx="5")

    browse_label1 = Label(frame3, text="OUTPUT:")
    browse_label1.grid(row=1, column=0, pady="10", padx="5")
    browse_output = Text(frame3, bg="#adb2ba", height="22", width="105")
    browse_output.grid(row=2, column=1, columnspan="2", pady="10", padx="5")
    browse_clear = Button(frame3, text="RESET", bg="#3971cc", fg="white", command=partial(browsebox_clear, browse_input, browse_output))
    browse_clear.grid(row=3, column=1, padx="5", pady="10")
    browse_submit = Button(frame3, text="SUMMARIZE !!", bg="#3971cc", fg="white", command=partial(browsebox_submit, browse_input, browse_output))
    browse_submit.grid(row=3, column=2, padx="5", pady="10")

    top.mainloop()


if __name__ == "__main__":
    generate_ui()
