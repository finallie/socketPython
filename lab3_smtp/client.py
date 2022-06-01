import base64
from socket import *

msg = "\r\n I love computer networks!\r\n"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
# mailserver = "smtp.qq.com"  # Fill in start #Fill in end
mailserver = "smtp.163.com"  # Fill in start #Fill in end
# mailserver = "smtp.gmail.com"  # Fill in start #Fill in end
port = 25
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(3)
clientSocket.connect((mailserver, port))
# Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
command = 'EHLO 163.com\r\n'
clientSocket.send(command.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

command = 'AUTH LOGIN\r\n'
clientSocket.send(command.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

command = base64.b64encode(b"smtp_ny").decode() + '\r\n'
clientSocket.send(command.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

command = base64.b64encode(b"NHYXWAATZOJNKFGG").decode() + '\r\n'
clientSocket.send(command.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

command = 'MAIL FROM: <smtp_ny@163.com>\r\n'
clientSocket.send(command.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
# command = 'RCPT TO: <1006492957@qq•com>\r\n'
command = 'RCPT TO: <1006492957@qq.com>\r\n'
clientSocket.send(command.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send DATA command and print server response.
# Fill in start
command = 'DATA\r\n'
clientSocket.send(command.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '354':
    print('354 reply not received from server.')
# Fill in end
# Send message data.
# Fill in start
subject = "Subject: SMTP mail client testing \r\n\r\n"
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send QUIT command and get server response.
# Fill in start
clientSocket.send("QUIT\r\n".encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '221':
    print('221 reply not received from server.')
# Fill in end
