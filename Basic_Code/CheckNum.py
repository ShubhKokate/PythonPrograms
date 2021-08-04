#check number is even or odd
#====================called Function #=======================
def ChkNum(value):
    if value%2==0:
        return True
    return False
 
#====================== Main Function #=======================
def main():
    print("Enter number: ")
    no=int(input())
    bret=ChkNum(no)
    
    if bret==True:
        print("{} is even number".format(no))
    else:
        print("{} is odd number".format(no))
#======================Starter #==============================        
if __name__=="__main__":
    main()
