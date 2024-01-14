from tkinter import *
from tkinter import filedialog
import smtplib




#here it for my Contact window
def contact():
	window = Tk()
	window.title('Edit Contact')
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
	window.mainloop()





#here it for the window where i wrote my message
def mail_sender():

	window = Tk()
	window.title('write your message')
	window.geometry("500x600")

	def send_mail():
		save_message()
		sender_mail = "legozbishow@gmail.com"
		password = "ikfdodwyyvdelgwg"
		text_file = open("message.txt", 'r')
		stuff = text_file.read()
		message = stuff
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

	def open_message():
		text_file = open("message.txt", 'r')
		stuff = text_file.read()
		my_text.insert(END, stuff)
		text_file.close()

	def save_message():
		text_file = open("message.txt", 'w')
		text_file.write(my_text.get(1.0, END))

	my_text = Text(window, width=40, height=20, font=("Helvetica", 16))
	my_text.pack(pady=20)

	button_message = Button(window, text="Write Message", command=open_message)
	button_message.pack(pady=20)

	button_send = Button(window, text="Send", command=send_mail)
	button_send.pack(pady=20)
 
	window.mainloop()


print("short test")

#here i creat 2 button: 1 button for open the contact windows
#and another button for open a window for write a message
window = Tk()
window.title('menu')
window.geometry("500x200")

my_button = Button(window, text="Edit Contact", command=contact)
my_button.pack(pady=20)

save_button = Button(window, text="Write message", fg='blue' , command=mail_sender)
save_button.pack(pady=20)
window.mainloop()