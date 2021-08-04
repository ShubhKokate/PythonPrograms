#check number is positive negative or zero
#=======================called Function #============================
def CheckNumber(value):
    if value > 0:
        print("Entered number {} is positive number".format(value))
    elif value < 0:
        print("Entered number {} is negative number".format(value))
    elif value == 0:
        print("Entered number {} is zero".format(value))
        
#============================== Main Function #=========================
def main():
    print("Enter number to check the number is positive, negative or zero: ")
    No=int(input())
    
    Checknumber(No)
    
#=================================== Starter #===========================
if __name__=="__main__":
    main()
