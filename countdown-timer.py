import time

def main():
    header()
    number = int(input("Enter some time to start: "))
    countdown(number)

def header():
    print(40*"=")
    print("               T I M E R                 ")
    print(40*"=")

def countdown(total_seconds):
    for i in range(total_seconds, 0, -1):
        seconds = i % 60
        minutes = int(i / 60) % 60
        hours = int(i / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
  
    print("Time´s Up!")

if __name__ == "__main__":
    main()
