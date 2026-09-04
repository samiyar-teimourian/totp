import pyotp
import qrcode
import time
import os

project_name = "Your Project Name"

secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)

uri = totp.provisioning_uri(
    name=input("account name: "),
    issuer_name=project_name
)

img = qrcode.make(uri)
img.save("otp_qr.png")

os.startfile("otp_qr.png")

while True:
    code = input("code: ")

    if totp.verify(code):
        print("True")
    else:
        print("False")
