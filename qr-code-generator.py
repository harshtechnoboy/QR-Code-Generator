import qrcode #importing the qrcode library

def generate_qrcode(text, filename=" qrimg.png "):  #defining a function to generate a QR code image

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,

    ) #creating a QRCode object with specified version, error correction level, box size, and border size

    qr.add_data(text) #adding the provided text to the QRCode object and making it fit the data
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black" , back_color = "white") #creating an image representation of the QR code with black fill color and white background color
    img.save("qr.png") #saving the image as "qr.png" by default or the provided filename

url = input("Enter your url: ") #asking the user to enter a URL

file_name = input ("Enter the name for your QR Code file ending with .png: ") # Prompting the user to enter the filename for the QR code image with ".png" extension

if file_name.strip() == "":
    generate_qrcode(url)  #if the user doesn't provide a filename, generate the QR code with default name "qrimg.png"
else:

    generate_qrcode(url , file_name)  #if the user provides a filename, generate the QR code with the provided name
