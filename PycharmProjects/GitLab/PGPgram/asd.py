import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('anton2920.ru', 1500))
        s.sendall(b'world!')
        s.shutdown(socket.SHUT_WR)
    print('Fin')


if __name__ == '__main__':
    main()