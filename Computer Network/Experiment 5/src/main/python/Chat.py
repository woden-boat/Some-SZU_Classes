import socket
import tkinter as tk
import threading
from tkinter import messagebox
import sys

class Chat:
    def __init__(self, root, my_port, peer_ip, peer_port):
        self.root = root
        self.root.title("UDP聊天程序")
        # self.root.geometry("500x400")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.peer_ip = peer_ip
        self.peer_port = peer_port
        self.my_port = my_port
        
    def start(self):
        self.my_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.my_socket.bind(("", self.my_port))
        
        self.create_widgets()
        
        self.receive_thread = threading.Thread(target=self.receive_message)
        self.receive_thread.daemon = True
        self.receive_thread.start()
        
    def create_widgets(self):
        # history message
        self.history_frame = tk.Frame(self.root)
        self.history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.history_scrollbar = tk.Scrollbar(self.history_frame)
        self.history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.history_text = tk.Text(
            self.history_frame,
            wrap=tk.WORD,
            state=tk.DISABLED,
            yscrollcommand=self.history_scrollbar.set
        )
        
        self.history_text.pack(fill=tk.BOTH, expand=True)
        self.history_scrollbar.config(command=self.history_text.yview)
        
        # input area
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.input_label = tk.Label(self.input_frame, text="please input text: ")
        self.input_label.pack(side=tk.LEFT)
        
        self.input_text = tk.Entry(self.input_frame)
        self.input_text.pack(side=tk.LEFT, fill=tk.X)
        
        # botton area
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.send_button = tk.Button(self.button_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_input)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.on_closing)
        self.exit_button.pack(side=tk.LEFT, padx=5)
        
    def send_message(self):
        message = self.input_text.get()
        if message:
            self.my_socket.sendto(message.encode('utf-8'), (self.peer_ip, self.peer_port))
            
            self.clear_input()
            self.add_history(f"me: {message}")
            
    def receive_message(self):
        while True:
            try:
                message, _ = self.my_socket.recvfrom(1024)
                message = message.decode('utf-8')
                self.add_history(f"friend: {message}")
            except:
                break
        
    def add_history(self,text):
        self.history_text.config(state=tk.NORMAL)
        
        self.history_text.insert(tk.END, text + '\n')
        self.history_text.see(tk.END)
        
        self.history_text.config(state=tk.END)
    
    def clear_input(self):
        self.input_text.delete(0,tk.END)
    
    def on_closing(self):
            if messagebox.askokcancel("退出", "确定要退出聊天程序吗?"):
                self.my_socket.close()
                self.root.destroy()
        
if __name__ == "__main__":
    my_port = int(sys.argv[1])
    peer_ip = str(sys.argv[2])
    peer_port = int(sys.argv[3])
    
    root = tk.Tk()
    app = Chat(root, my_port, peer_ip, peer_port)
    app.start()
    root.mainloop()