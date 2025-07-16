import qrcode
website_link = 'Paste your link in here' #change with your own link

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('yourImageName.png')#you can change the name of the .png
