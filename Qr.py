#IMPORTING THE QRCODE MODULE
import qrcode
#MAKE THE QRCODE USING THE MAKE FUNCTION
myqr = qrcode.make("Welcome this is my first task")
#SAVE THE IMAGE FILE
myqr.save("myqr.png", scale = 8)