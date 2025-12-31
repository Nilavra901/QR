import qrcode

data = input("Enter the URL or text to encode in QR Code: ")

file_path = r"C:\Users\NILAVRA GHOSH\OneDrive\Pictures\Saved Pictures\qrcode.png"
rq = qrcode.QRCode()
rq.add_data(data)
rq.make()
img = rq.make_image()
img.save(file_path)

print(f"QR Code saved successfully at {file_path}")
