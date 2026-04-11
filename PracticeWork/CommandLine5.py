import sys

def main():
   if(len(sys.argv) < 3 or len(sys.argv) > 3):
       print("Invalid number of arguments")

   else:
      Sum = 0
      Sum = int(sys.argv[1]) + int(sys.argv[2])
      print(Sum)
      

if __name__=="__main__":
    main()    