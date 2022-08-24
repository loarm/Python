from tkinter import *
import base64

root = Tk()
root['bg'] = '#C1B5B2'
root.geometry('500x350')
root.resizable(0, 0)
root.title("LoarMode - Encode/Decode Program")
Label(root, text='ENCODE or DECODE', font='arial 20 bold',
      bg='#C1B5B2', fg='#fafafa', pady='5').pack()
Label(root, text='LoarMode', font='arial 10 bold',
      bg='#C1B5B2', justify='center').pack(side=BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    if (mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif (mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# buttons and input fields

Label(root, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=Text,
      bg='ghost white').place(x=250, y=60)

Label(root, font='arial 12 bold', text='KEY').place(x=60, y=100)
Entry(root, font='arial 10', textvariable=private_key,
      bg='ghost white').place(x=250, y=100)

Label(root, font='arial 12 bold', text='MODE\n(e-encode, d-decode)',
      justify='left').place(x=60, y=140)
Entry(root, font='arial 10', textvariable=mode,
      bg='ghost white').place(x=250, y=150)

Button(root, font='arial 10 bold', text='RESULT', padx=2,
       bg='LightGray', command=Mode).place(x=60, y=210)
Entry(root, font='arial 10', textvariable=Result,
      bg='ghost white').place(x=250, y=215)

Button(root, font='arial 10 bold', text='RESET', width=6,
       padx=2, bg='LimeGreen', command=Reset).place(x=220, y=270)


# run the program

root.mainloop()
