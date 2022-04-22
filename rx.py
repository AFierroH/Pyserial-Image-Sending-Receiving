import serial, io
from PIL import Image

c = ["1","2","3","4","5","6","7"]
ser = serial.Serial('COM1', 9600)
data = b""
d = []
data_in = ser.readline()
for i in range(len(c)+1):
    while True:
        data += data_in
        data_in = ser.readline()
        ser.timeout = 3
        starts = data_in.startswith(b'\x1a\n')
        if starts == True:
            d.append(data)
            data = b'\x89PNG\r\n\x1a\n'
            data_in = ser.readline()
        if not data_in:
            d.append(data)
            break
inp = input("Que imagen quieres mostrar?: ")
ind = c.index(inp)
x = Image.open(io.BytesIO(d[ind+1]))
gray = x.convert('L')
gray.show()