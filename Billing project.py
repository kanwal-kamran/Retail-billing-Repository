from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib
# functionality part


def clear():
    bath_soap_Entry.delete(0, END)
    face_cream_Entry.delete(0, END)
    face_wash_Entry.delete(0, END)
    hair_spray_Entry.delete(0, END)
    shampoo_Entry.delete(0, END)
    nail_polish_Entry.delete(0, END)

    oil_Entry.delete(0, END)
    rice_Entry.delete(0, END)
    sugar_Entry.delete(0, END)
    flour_Entry.delete(0, END)
    lentils_Entry.delete(0, END)
    tea_Entry.delete(0, END)

    slice_Entry.delete(0, END)
    coca_cola_Entry.delete(0, END)
    pepsi_Entry.delete(0, END)
    shezan_Entry.delete(0, END)
    maaza_Entry.delete(0, END)
    dew_Entry.delete(0, END)

    bath_soap_Entry.insert(0, 0)
    face_cream_Entry.insert(0, 0)
    face_wash_Entry.insert(0, 0)
    hair_spray_Entry.insert(0, 0)
    shampoo_Entry.insert(0, 0)
    nail_polish_Entry.insert(0, 0)

    oil_Entry.insert(0, 0)
    rice_Entry.insert(0, 0)
    sugar_Entry.insert(0, 0)
    flour_Entry.insert(0, 0)
    lentils_Entry.insert(0, 0)
    tea_Entry.insert(0, 0)

    slice_Entry.insert(0, 0)
    coca_cola_Entry.insert(0, 0)
    pepsi_Entry.insert(0, 0)
    shezan_Entry.insert(0, 0)
    maaza_Entry.insert(0, 0)
    dew_Entry.insert(0, 0)

    cosmetics_tax_Entry.delete(0, END)
    grocery_tax_Entry.delete(0, END)
    drinks_tax_Entry.delete(0, END)

    cosmetics_price_Entry.delete(0, END)
    grocery_price_Entry.delete(0, END)
    drinks_price_Entry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    bill_number_Entry.delete(0, END)

    textarea.delete(1.0, END)


def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent', parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error', 'Something went wrong, Please try again', parent=root1)

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        root1 = Toplevel()
        root1.title("Send Gmail")
        root1.config(bg='gray20')
        root1.resizable(0, 0)

        senderFrame = LabelFrame(root1, text="SENDER", font=('arial', 16, 'bold'), bd=6,
                                 bg='gray20', fg='white')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel = Label(senderFrame, text="Sender's Email", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text="RECIPIENT", font=('arial', 16, 'bold'), bd=6,
                                    bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN, width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', '')
                              .replace('\t\t\t', '\t\t'))

        sendButton = Button(root1, text="SEND", font=('arial', 16, 'bold'), width=15, command=send_gmail)
        sendButton.grid(row=2, column=0, pady=20)

        root1.mainloop()


def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == bill_number_Entry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/ {billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'bill number {billnumber} is saved Successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)


def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customers Details are Required')
    elif cosmetics_price_Entry.get() == '' and grocery_price_Entry.get() == '' and drinks_price_Entry.get() == '':
        messagebox.showerror('Error', 'No Products are Selected')
    elif (cosmetics_price_Entry.get() == '0 Rs' and grocery_price_Entry.get() == '0 Rs' and
          drinks_price_Entry.get() == '0 Rs'):
        messagebox.showerror('Error', 'No Products are Selected')
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, '\t\t**WELCOME CUSTOMER**\n')
        textarea.insert(END, f'\nBill Number: {billnumber}')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}')
        textarea.insert(END, '\n=======================================================')
        textarea.insert(END, '\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================')
        if bath_soap_Entry.get() != '0':
            textarea.insert(END, f'\nBath Soap\t\t\t{bath_soap_Entry.get()}\t\t\t{soap_price} Rs')
        if face_cream_Entry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{face_cream_Entry.get()}\t\t\t{face_cream_price} Rs')
        if face_wash_Entry.get() != '0':
            textarea.insert(END, f'\nFace Wash\t\t\t{face_wash_Entry.get()}\t\t\t{face_wash_price} Rs')
        if hair_spray_Entry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{hair_spray_Entry.get()}\t\t\t{hair_spray_price} Rs')
        if shampoo_Entry.get() != '0':
            textarea.insert(END, f'\nShampoo\t\t\t{shampoo_Entry.get()}\t\t\t{shampoo_price} Rs')
        if nail_polish_Entry.get() != '0':
            textarea.insert(END, f'\nNail Polish\t\t\t{nail_polish_Entry.get()}\t\t\t{nail_polish_price} Rs')

        # grocery
        if oil_Entry.get() != '0':
            textarea.insert(END, f'\nOil\t\t\t{oil_Entry.get()}\t\t\t{oil_price} Rs')
        if rice_Entry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{rice_Entry.get()}\t\t\t{rice_price} Rs')
        if sugar_Entry.get() != '0':
            textarea.insert(END, f'\nSugar\t\t\t{sugar_Entry.get()}\t\t\t{sugar_price} Rs')
        if flour_Entry.get() != '0':
            textarea.insert(END, f'\nFlour\t\t\t{flour_Entry.get()}\t\t\t{flour_price} Rs')
        if lentils_Entry.get() != '0':
            textarea.insert(END, f'\nLentils\t\t\t{lentils_Entry.get()}\t\t\t{lentils_price} Rs')
        if tea_Entry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{tea_Entry.get()}\t\t\t{tea_price} Rs')

        # drinks
        if slice_Entry.get() != '0':
            textarea.insert(END, f'\nSlice\t\t\t{slice_Entry.get()}\t\t\t{slice_price} Rs')
        if coca_cola_Entry.get() != '0':
            textarea.insert(END, f'\nCoca Cola\t\t\t{coca_cola_Entry.get()}\t\t\t{coca_cola_price} Rs')
        if pepsi_Entry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsi_Entry.get()}\t\t\t{pepsi_price} Rs')
        if shezan_Entry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{shezan_Entry.get()}\t\t\t{shezan_price} Rs')
        if maaza_Entry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maaza_Entry.get()}\t\t\t{maaza_price} Rs')
        if dew_Entry.get() != '0':
            textarea.insert(END, f'\nDew\t\t\t{dew_Entry.get()}\t\t\t{dew_price} Rs')
        textarea.insert(END, '\n-------------------------------------------------------\n')

        # Tax
        if cosmetics_tax_Entry.get() != '0.0 Rs':
            textarea.insert(END, f'\nCosmetics Tax\t\t\t\t{cosmetics_tax_Entry.get()}')
        if grocery_tax_Entry.get() != '0.0 Rs':
            textarea.insert(END, f'\nGrocery Tax \t\t\t\t{grocery_tax_Entry.get()}')
        if drinks_tax_Entry.get() != '0.0 Rs':
            textarea.insert(END, f'\nDrinks Tax\t\t\t\t{drinks_tax_Entry.get()}')
        textarea.insert(END, f'\n\nTotal Bill \t\t\t\t {total_bill}')
        textarea.insert(END, '\n-------------------------------------------------------\n')
        save_bill()


# COSMETICS PRICE CALCULATION
def total():
    global soap_price, face_cream_price, face_wash_price, hair_spray_price, shampoo_price, nail_polish_price
    global oil_price, rice_price, sugar_price, flour_price, lentils_price, tea_price
    global slice_price, coca_cola_price, pepsi_price, shezan_price, maaza_price, dew_price
    global total_bill
    soap_price = int(bath_soap_Entry.get()) * 50
    face_cream_price = int(face_cream_Entry.get()) * 80
    face_wash_price = int(face_wash_Entry.get()) * 110
    hair_spray_price = int(hair_spray_Entry.get()) * 60
    shampoo_price = int(shampoo_Entry.get()) * 190
    nail_polish_price = int(nail_polish_Entry.get()) * 50

    total_cosmetics_price = soap_price+face_cream_price+face_wash_price+hair_spray_price+shampoo_price+nail_polish_price
    cosmetics_price_Entry.delete(0, END)
    cosmetics_price_Entry.insert(0, f'{total_cosmetics_price} Rs')
    cosmetics_tax = total_cosmetics_price*0.13
    cosmetics_tax_Entry.delete(0, END)
    cosmetics_tax_Entry.insert(0, str(cosmetics_tax) + ' Rs')

    # GROCERY PRICE CALCULATION
    oil_price = int(oil_Entry.get()) * 390
    rice_price = int(rice_Entry.get()) * 220
    sugar_price = int(sugar_Entry.get()) * 150
    flour_price = int(flour_Entry.get()) * 130
    lentils_price = int(lentils_Entry.get()) * 240
    tea_price = int(tea_Entry.get()) * 1600

    total_grocery_price = oil_price + rice_price + sugar_price + flour_price + lentils_price + tea_price
    grocery_price_Entry.delete(0, END)
    grocery_price_Entry.insert(0, str(total_grocery_price)+' Rs')
    grocery_tax = total_grocery_price * 0.06
    grocery_tax_Entry.delete(0, END)
    grocery_tax_Entry.insert(0, str(grocery_tax) + ' Rs')

    # DRINKS PRICE CALCULATION
    slice_price = int(slice_Entry.get()) * 30
    coca_cola_price = int(coca_cola_Entry.get()) * 60
    pepsi_price = int(pepsi_Entry.get()) * 70
    shezan_price = int(shezan_Entry.get()) * 40
    maaza_price = int(maaza_Entry.get()) * 75
    dew_price = int(dew_Entry.get()) * 55

    total_drinks_price = slice_price + coca_cola_price + pepsi_price + shezan_price + maaza_price + dew_price
    drinks_price_Entry.delete(0, END)
    drinks_price_Entry.insert(0, str(total_drinks_price)+' Rs')
    drinks_tax = total_drinks_price * 0.08
    drinks_tax_Entry.delete(0, END)
    drinks_tax_Entry.insert(0, str(drinks_tax) + ' Rs')

    total_bill = total_cosmetics_price+total_grocery_price+total_drinks_price+cosmetics_tax+grocery_tax+drinks_tax


# GUI part
root = Tk()
root.title("Al Rehman Computer Institute")
root.geometry("1270x685")
root.iconbitmap("icon.ico")
headingLabel = Label(root, text="Retail Billing System", font=('Times new Roman', 30, 'bold'),
                                bg='deep sky blue', fg='black', bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 16, 'bold'),
                                    fg='gold', bd=8, relief=GROOVE, bg='gray34')
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 16, 'bold'), fg='white', bg='gray34')
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customer_details_frame, font=('arial', 14), bd=6, width=18)
nameEntry.grid(row=0, column=1, padx=8, pady=2)

phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 16, 'bold'),
                   fg='white', bg='gray34')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 14), bd=6, width=18)
phoneEntry.grid(row=0, column=3, padx=8, pady=2)

bill_number_Label = Label(customer_details_frame, text='Bill Number', font=('times new roman', 16, 'bold'),
                          fg='white', bg='gray34')
bill_number_Label.grid(row=0, column=4, padx=20, pady=2)

bill_number_Entry = Entry(customer_details_frame, font=('arial', 14), bd=6, width=18)
bill_number_Entry.grid(row=0, column=5, padx=8, pady=2)

searchButton = Button(customer_details_frame, text="SEARCH", font=('arial', 15, 'bold'),
                      bd=7, width=8, command=search_bill)
searchButton.grid(row=0, column=6, padx=10, pady=8)

productsFrame = Frame(root)
productsFrame.pack()

cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics', font=('times new roman', 16, 'bold'), fg='gold',
                            bd=8, relief=GROOVE, bg='gray34')
cosmeticsFrame.grid(row=0, column=0)

bath_soap_Label = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), fg='white',
                        bg='gray34')
bath_soap_Label.grid(row=0, column=0, pady=9, padx=6, sticky='w')

bath_soap_Entry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
bath_soap_Entry.grid(row=0, column=1, pady=9, padx=6)
bath_soap_Entry.insert(0, 0)

face_cream_Label = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'),
                         fg='white', bg='gray34')
face_cream_Label.grid(row=1, column=0, pady=9, padx=6)

face_cream_Entry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
face_cream_Entry.grid(row=1, column=1, pady=9, padx=6)
face_cream_Entry.insert(0, 0)

face_wash_Label = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'),
                        fg='white', bg='gray34')
face_wash_Label.grid(row=2, column=0, pady=9, padx=6, sticky='w')

face_wash_Entry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
face_wash_Entry.grid(row=2, column=1, pady=9, padx=6)
face_wash_Entry.insert(0, 0)

hair_spray_Label = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), fg='white',
                         bg='gray34')
hair_spray_Label.grid(row=3, column=0, pady=9, padx=6, sticky='w')

hair_spray_Entry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
hair_spray_Entry.grid(row=3, column=1, pady=9, padx=6)
hair_spray_Entry.insert(0, 0)

shampoo_Label = Label(cosmeticsFrame, text='Shampoo', font=('times new roman', 15, 'bold'), fg='white',
                      bg='gray34')
shampoo_Label.grid(row=4, column=0, pady=9, padx=6, sticky='w')

shampoo_Entry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
shampoo_Entry.grid(row=4, column=1, pady=9, padx=6)
shampoo_Entry.insert(0, 0)

nail_polish_Label = Label(cosmeticsFrame, text='Nail Polish', font=('times new roman', 15, 'bold'), fg='white',
                          bg='gray34')
nail_polish_Label.grid(row=5, column=0, pady=9, padx=6, sticky='w')

nail_polish_Entry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
nail_polish_Entry.grid(row=5, column=1, pady=7, padx=6)
nail_polish_Entry.insert(0, 0)

groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('times new roman', 16, 'bold'), fg='gold', bd=8,
                          relief=GROOVE, bg='gray34')
groceryFrame.grid(row=0, column=1)

oil_Label = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), fg='white',
                  bg='gray34')
oil_Label.grid(row=0, column=0, pady=9, padx=6, sticky='w')

oil_Entry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
oil_Entry.grid(row=0, column=1, pady=9, padx=6)
oil_Entry.insert(0, 0)

rice_Label = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), fg='white',
                   bg='gray34')
rice_Label.grid(row=1, column=0, pady=9, padx=6, sticky='w')

rice_Entry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
rice_Entry.grid(row=1, column=1, pady=9, padx=6)
rice_Entry.insert(0, 0)

sugar_Label = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), fg='white',
                    bg='gray34')
sugar_Label.grid(row=2, column=0, pady=9, padx=6, sticky='w')

sugar_Entry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
sugar_Entry.grid(row=2, column=1, pady=9, padx=6)
sugar_Entry.insert(0,  0)

flour_Label = Label(groceryFrame, text='Flour', font=('times new roman', 15, 'bold'), fg='white',
                    bg='gray34')
flour_Label.grid(row=3, column=0, pady=9, padx=6, sticky='w')

flour_Entry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
flour_Entry.grid(row=3, column=1, pady=9, padx=6)
flour_Entry.insert(0, 0)

lentils_Label = Label(groceryFrame, text='Lentils', font=('times new roman', 15, 'bold'), fg='white',
                      bg='gray34')
lentils_Label.grid(row=4, column=0, pady=9, padx=6, sticky='w')

lentils_Entry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
lentils_Entry.grid(row=4, column=1, pady=9, padx=6)
lentils_Entry.insert(0, 0)

tea_Label = Label(groceryFrame, text='Tea', font=('times new roman', 15, 'bold'), fg='white',
                  bg='gray34')
tea_Label.grid(row=5, column=0, pady=9, padx=6, sticky='w')

tea_Entry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
tea_Entry.grid(row=5, column=1, pady=7, padx=6)
tea_Entry.insert(0, 0)

drinksFrame = LabelFrame(productsFrame, text='Cold Drinks', font=('times new roman', 16, 'bold'),
                         fg='gold', bd=8, relief=GROOVE, bg='gray34')
drinksFrame.grid(row=0, column=2)

slice_Label = Label(drinksFrame, text='Slice', font=('times new roman', 15, 'bold'), fg='white',
                    bg='gray34')
slice_Label.grid(row=0, column=0, pady=9, padx=6, sticky='w')

slice_Entry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
slice_Entry.grid(row=0, column=1, pady=9, padx=6)
slice_Entry.insert(0, 0)

coca_cola_Label = Label(drinksFrame, text='Coca cola', font=('times new roman', 15, 'bold'), fg='white',
                        bg='gray34')
coca_cola_Label.grid(row=1, column=0, pady=9, padx=6, sticky='w')

coca_cola_Entry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
coca_cola_Entry.grid(row=1, column=1, pady=9, padx=6)
coca_cola_Entry.insert(0, 0)

pepsi_Label = Label(drinksFrame, text='Pepsi', font=('times new roman', 15, 'bold'), fg='white',
                    bg='gray34')
pepsi_Label.grid(row=2, column=0, pady=9, padx=6, sticky='w')

pepsi_Entry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
pepsi_Entry.grid(row=2, column=1, pady=9, padx=6)
pepsi_Entry.insert(0, 0)

shezan_Label = Label(drinksFrame, text='Shezan', font=('times new roman', 15, 'bold'), fg='white',
                     bg='gray34')
shezan_Label.grid(row=3, column=0, pady=9, padx=6, sticky='w')

shezan_Entry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
shezan_Entry.grid(row=3, column=1, pady=9, padx=6)
shezan_Entry.insert(0, 0)

maaza_Label = Label(drinksFrame, text='Maaza', font=('times new roman', 15, 'bold'), fg='white',
                    bg='gray34')
maaza_Label.grid(row=4, column=0, pady=9, padx=6, sticky='w')

maaza_Entry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
maaza_Entry.grid(row=4, column=1, pady=9, padx=6)
maaza_Entry.insert(0, 0)

dew_Label = Label(drinksFrame, text='Dew', font=('times new roman', 15, 'bold'), fg='white',
                  bg='gray34')
dew_Label.grid(row=5, column=0, pady=9, padx=6, sticky='w')

dew_Entry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=12, bd=5)
dew_Entry.grid(row=5, column=1, pady=7, padx=6)
dew_Entry.insert(0, 0)

billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

bill_area_Label = Label(billframe, text='Bill Area', font=('times new roman', 17, 'bold'), bd=7,
                        relief=GROOVE)
bill_area_Label.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 16, 'bold'), fg='gold', bd=8,
                           relief=GROOVE, bg='gray34')
billmenuFrame.pack()

cosmetics_price_Label = Label(billmenuFrame, text='Cosmetics Price', font=('times new roman', 13, 'bold'), fg='white',
                              bg='gray34')
cosmetics_price_Label.grid(row=0, column=0, pady=6, sticky='w')

cosmetics_price_Entry = Entry(billmenuFrame, font=('times new roman', 13, 'bold'), width=12, bd=5)
cosmetics_price_Entry.grid(row=0, column=1, pady=6, padx=10)

grocery_price_Label = Label(billmenuFrame, text='Grocery Price', font=('times new roman', 13, 'bold'), fg='white',
                            bg='gray34')
grocery_price_Label.grid(row=1, column=0, pady=6, sticky='w')

grocery_price_Entry = Entry(billmenuFrame, font=('times new roman', 13, 'bold'), width=12, bd=5)
grocery_price_Entry.grid(row=1, column=1, pady=6, padx=10)

drinks_price_Label = Label(billmenuFrame, text='Cold Drinks Price', font=('times new roman', 15, 'bold'), fg='white',
                           bg='gray34')
drinks_price_Label.grid(row=2, column=0, pady=6, sticky='w')

drinks_price_Entry = Entry(billmenuFrame, font=('times new roman', 13, 'bold'), width=12, bd=5)
drinks_price_Entry.grid(row=2, column=1, pady=6, padx=10)

cosmetics_tax_Label = Label(billmenuFrame, text='Cosmetics Tax', font=('times new roman', 13, 'bold'), fg='white',
                            bg='gray34')
cosmetics_tax_Label.grid(row=0, column=2, pady=6, sticky='w')

cosmetics_tax_Entry = Entry(billmenuFrame, font=('times new roman', 13, 'bold'), width=12, bd=5)
cosmetics_tax_Entry.grid(row=0, column=3, pady=6, padx=10)

grocery_tax_Label = Label(billmenuFrame, text='Grocery Tax', font=('times new roman', 13, 'bold'), fg='white',
                          bg='gray34')
grocery_tax_Label.grid(row=1, column=2, pady=6, sticky='w')

grocery_tax_Entry = Entry(billmenuFrame, font=('times new roman', 13, 'bold'), width=12, bd=5)
grocery_tax_Entry.grid(row=1, column=3, pady=6, padx=10)

drinks_tax_Label = Label(billmenuFrame, text='Cold Drinks Tax', font=('times new roman', 13, 'bold'), fg='white',
                         bg='gray34')
drinks_tax_Label.grid(row=2, column=2, pady=6, sticky='w')

drinks_tax_Entry = Entry(billmenuFrame, font=('times new roman', 13, 'bold'), width=12, bd=5)
drinks_tax_Entry.grid(row=2, column=3, pady=6, padx=10)

buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='gray34', fg='white', bd=5,
                     width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='gray34', fg='white', bd=5,
                    width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='gray34', fg='white', bd=5,
                     width=8, pady=10, command=send_email)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='gray34', fg='white', bd=5,
                     width=8, pady=10, command=print_bill)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='gray34', fg='white', bd=5,
                     width=8, pady=10, command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
