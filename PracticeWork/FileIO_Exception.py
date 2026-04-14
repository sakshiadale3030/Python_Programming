def main():
    try:
        open("Demo.txt")
        print("File gets succesfully opened")

    except FileNotFoundError:
        print("Unable to open file as there is no such file")    

    finally:
        print("End of aapplication")    

if __name__ == "__main__":
    main()    