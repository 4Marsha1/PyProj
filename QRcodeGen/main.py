import qrcode

TEXT = input("Enter your link: ")
FILE_NAME = input("Enter your qr code name: ")

def qr_code_gen(text,file_name): 
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_Q,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img =  qr.make_image(fill_color="#dc5371")
    img.save(f"{file_name}.png")

qr_code_gen(TEXT,FILE_NAME)
print(f"QR code generated {FILE_NAME}")