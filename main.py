import pyotp
import os

os.system('cls')
key = input("Enter 2FA Key (Manual Entry) : ")

totp = pyotp.totp(key)

print("\n  > Current code: " + totp.now())


