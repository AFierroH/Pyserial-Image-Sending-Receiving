import serial
ser = serial.Serial('COM1', 9600)
c = ["1","2","3","4","5","6","7"]
for i in c:
    with open(f'C:/Users/armin/PycharmProjects/hardware/imagenes/img0{i}.jpg', "rb") as image:
        f = image.read()
        b = bytearray(f)
        print(f)
    ser.write(b)