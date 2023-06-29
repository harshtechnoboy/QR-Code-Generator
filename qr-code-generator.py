import qrcode

def generate_qrcode(text, filename=" qrimg.png "):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,

    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black" , back_color = "white")
    img.save("qr.png")

url = input("Enter your url: ")

file_name = input ("Enter the name for your QR Code file ending with .png: ")

if file_name.strip() == "":
    generate_qrcode(url)
else:

    generate_qrcode(url , file_name)
