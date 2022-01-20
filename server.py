import socket

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(5)
conn, addr = sock.accept()
print('Connected', addr)
data = conn.recv(8192)
msg = data.decode()
print(msg)

with open('index.html', 'r') as f:
    text = f.read()

with open('style.css', 'r') as f:
    css = f.read()

resp = f"""HTTP/1.1 200 OK

{text}"""

#  css_mes = f"""HTTP/1.1 200 OK

#  {css}"""
conn.send(resp.encode())
#  conn.send(css_mes.encode())

conn.close()
