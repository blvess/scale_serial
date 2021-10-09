import serial.tools.list_ports

def main():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        print()
        print(f"Name:\t\t{p.name}")
        print(f"Device:\t\t{p.device}")
        print(f"Description:\t{p.description}")

    input("\nPress any key to exit")

if __name__ == "__main__":
    main()
list