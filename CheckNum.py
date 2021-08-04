#function to check the number is odd or even
#=================CheckNumber Function#==========================
def CheckNum(No):
    if no%2==0:
        return True
    return False
 
#======================Main Function #===========================
 def main():
    print("Enter number to check even or odd:")
    num=int(input())
    
    if num==True:
        print("Entered number is Even number")
    else:
        print("Entered number is Odd number")
 
#=====================Starter #==================================
 if __name__=="__main__":
    main()
