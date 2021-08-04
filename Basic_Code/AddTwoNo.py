# Addition of two number

#===================called Function #=======================
def AddNum(value1, value2):
    ret= value1 + value2
    return ret
  
#====================== Main Function #=====================
def main():
    print("Enter Two number for Addition: ")
    No1=int(input())
    No2=int(input())
    
    Add=AddNum(No1, No2)
    print("Addition of {} and {} is {}".format(No1, No2, Add))
    
#======================= Starter #===========================
if __name__="__main__":
    main()
