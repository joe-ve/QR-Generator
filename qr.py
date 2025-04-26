#PROGRAM TO GENERATE QR CODE

#This library lets us perform all of our QR code related operations
import qrcode

#Taking input from user for the link
website_link = input("Enter link to generate QR Code :- ")

#Test URL
#https://youtu.be/dQw4w9WgXcQ

#Taking input for specifications of QR
ver = int(input("Enter size of QR Code(1-40) :- "))
bs = int(input("Enter the pixel size :- "))
bd = int(input("Enter thickness :- "))
#Passing the parameters
qr = qrcode.QRCode(version=(ver), box_size=(bs), border=(bd))

#The data is added to the QR Code
qr.add_data(website_link)
#The QR is made now
qr.make()

#Color specifications of QR
fc = input("Enter color to fill :- ")
bc = input("Enter back color :- ")
#Passing the parameters
img = qr.make_image(fill_color = (fc), back_color = (bc))

#Taking input for file name
image = input("Enter file name to save PNG(add .png at last) :- ")
#Saving the file
img.save(image)