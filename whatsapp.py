
import keyboard as a
import time
import webbrowser as browser
number = str(input("Enter the mobile number with country code: +"))
message = str(input("\nEnter the message you want to send continuously: "))
count = 0
n=0
while count <= 0:
    try:
        count = int(input("\nHow many times you want to send? "))
    except ValueError:
        print("\nOops!\nIt seems you have entered a text, please enter a number")
print("\nWhatsapp web will open in 5 seconds")
time.sleep(5)
link = "https://web.whatsapp.com/send?phone="+number
browser.open(link)
print("Message(s) will start sending in 25 seconds with 0.5 second delay between each message")

time.sleep(25)
while n<count:
    a.write(message)
    a.press("enter")
    time.sleep(0.5)
    n+=1
    print(n, " sent")
input("Process completed, press enter to exit")