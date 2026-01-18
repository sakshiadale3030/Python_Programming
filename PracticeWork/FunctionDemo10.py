# One function can call another function

def fun():
    print("Inside Fun")

def gun():
    print("Inside gun")  
    fun()  

def main():
    gun()

if __name__ == "__main__":
    main()