def Phoenix():
    print("Inside Phoenix")
    def zara():
        print("Inside zara")

def main():
    Phoenix.zara()     #ERROR

if __name__ == "__main__":
    main()