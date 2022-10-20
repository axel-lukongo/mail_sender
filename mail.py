from tkinter import *
from tkinter import filedialog
import smtplib

def send_mail():
	
	sender_mail = "lukongo.axel03@gmail.com"
	password = "arqzueduxqrhbadv"
	message = "j'ai reussi a envoyer un mail a plusieur personnes avec python gros"
	data = open("contact.txt", "r")
	rec_mail = data.readline()

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(sender_mail, password)

	while rec_mail: 
		print(rec_mail)
		server.sendmail(sender_mail, rec_mail, message)
		rec_mail = data.readline()

	server.quit()
	print("mail has been send")



window = Tk()
window.title('menu')
window.geometry("500x700")

def open_txt():
	text_file = open("contact.txt", 'r')
	stuff = text_file.read()

	my_text.insert(END, stuff)
	text_file.close()

def save_txt():
	text_file = open("contact.txt", 'w')
	text_file.write(my_text.get(1.0, END))

my_text = Text(window, width=40, height=20, font=("Helvetica", 16))
my_text.pack(pady=20)

my_button = Button(window, text="Show Contact", command=open_txt)
my_button.pack(pady=20)

save_button = Button(window, text="Save", fg='blue' , command=save_txt)
save_button.pack(pady=20)

button_send = Button(window, text="Send", fg='red', command=send_mail)
button_send.pack(pady=20)

window.mainloop()









