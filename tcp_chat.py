from multiprocessing import Process, Queue
import socket

class Chat:
    def __init__(self, nickname, listener_addr, dest_addr_queue, destination_addr=None):
        self.listener_addr = listener_addr
        self.nickname = nickname
        self.destination_addr = destination_addr
        self.dest_addr_queue = dest_addr_queue

    def send(self, msg):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            listener_ip = self.listener_addr[0]
            listener_port = self.listener_addr[1]
            
            if not self.destination_addr and queue.qsize() != 0:
                self.destination_addr = self.dest_addr_queue.get()

            if self.destination_addr:
                sock.sendto(f"{listener_ip}/{listener_port}/{self.nickname}/{msg}".encode('utf-8'), self.destination_addr)
            

    def receiver(self, dest_addr_queue):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.listener_addr[0], self.listener_addr[1]))

        while True:
            data, addr = sock.recvfrom(4096)
            destination_ip, destination_port, nickname, msg = data.decode().split('/')
            dest_addr_queue.put((destination_ip, int(destination_port)))
            print(f'[{nickname}]: {msg}')

    def run_chat(self):
        while True:
            self.send(input())


if __name__ == "__main__":
    nickname = input('Enter your nickname: ')
    print('1) Open connection.\n2) Connect')
    choice = int(input())

    if choice == 1:
        listener_ip = input('Specify listener IP address: ')
        listener_port = int(input('Specify listener port: '))

        queue = Queue()
        chat = Chat(nickname, (listener_ip, listener_port), queue)

        recproc = Process(target=Chat.receiver, args=(chat, queue))
        recproc.start()

        chat.run_chat()

    elif choice == 2: 
        listener_ip = input('Specify listener IP address: ')
        listener_port = int(input('Specify listener port: '))
        destination_ip = input('Specify destination IP address: ')
        destination_port = int(input('Specify destination port: '))

        queue = Queue()
        chat = Chat(nickname, (listener_ip, listener_port), queue, (destination_ip, destination_port))

        recproc = Process(target=Chat.receiver, args=(chat, queue))
        recproc.start()

        chat.run_chat()
