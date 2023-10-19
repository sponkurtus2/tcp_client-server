import socket
import html

'''
    One of the main modules in Python for networking is
    socket, its purposes are for braking in or maintain access
    to target machines
    
    TCP clients are used for test services, send garbage data,
    fuzz or more tasks
'''



# target_host = 'proyecta.utch.edu.mx'
# For some reason, it only works with http protocol
# target_host = 'piccolomondocuuintegradora.000webhostapp.com'
# target_port = 80    # 53 -> domain : 80 -> http : 443 -> https

# Host and port to combine with the TCP_server
target_host = '0.0.0.0'
target_port = 9999

#   Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Connect the client
client.connect((target_host, target_port))

#   Send some data
request = f'GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n'
client.send(request.encode())

#   Receive all the some html data
response = b''

while True:
    data = client.recv(4096)
    if not data:
        break
    response += data


#   Decode and print the data (HTML content)
html_content = response.split(b'r\n\r\n', 1)[-1]  # Extract the html content from the response
decoded_html = html.unescape(html_content.decode('utf-8'))

print(decoded_html)
