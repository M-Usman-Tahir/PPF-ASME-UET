import sys
import os
import File_Cryption
import Bound_Input

class D_E():
    def __init__(self, Data):
        global Filed, enORde
        if Filed:
            try:
                with open(Data) as Input:
                    file=Input.read()
            except:
                print("DataError: Failed in Opening File!!!")
                sys.exit()
            else:
                Data = file
                print("Data File obtained...")
        
        if enORde=="e" or enORde =="E":
            self.EnCrypt(Data)
        else:
            self.DeCrypt(Data)
            
    def EnCrypt(self, Input):
            global Final_Data
            Final_Data=File_Cryption.encryption_58(Input)
        
    def DeCrypt(self, Input):
            global Final_Data
            Final_Data=File_Cryption.decryption_58(Input)    



enORde, Filed=Bound_Input.check("Encrypt or Decrypt (E/D): ","(e/E/d/D)"), True


if len(sys.argv)==2:
    Loc=sys.argv[1]
    D_E(Loc)
    
elif len(sys.argv)>2:
    print("SystemError: Unknown Arguments!!!")
    sys.exit()
    
else:
    FS=Bound_Input.check("Using File or Simple Input(F/S): ","(f/F/s/S)")
    if FS=="f" or FS=="F":
        Loc=input("File location: ")
        if Loc=="same" or Loc=="Same":
            File_name=input("File Name: ")
            if not "." in File_name:
                print("Extension \'.txt\' has been taken as default...")
                File_name+=".txt"
            Loc=os.getcwd()+File_name
        D_E(Loc)
    else:
        data, Filed =input("Input the data: "), False
        D_E(data)




P_In=Bound_Input.check("Do you want it print(Y/N): ","(y/Y/n/N)")
if P_In=="y" or P_In=="Y":
    print("Crypted Data:",Final_Data)
P_In=Bound_Input.check("Do you want to save \'write\' or \'append\' it in file(W/A/N): ","(w/W/a/A/n/N)")
if P_In=="w" or P_In=="W":
    ext=input("File with extension: ")
    try:
        with open(os.path.join(os.getcwd(),"Crypted"+ext), "w") as new_file:
            new_file.write(Final_Data)
            print("Data Saved Successfully...\nCheck the data at location:",os.path.join(os.getcwd(),"Crypted"+ext))
    except:
        print("DataError: Failed to write the file!!!")
elif P_In=="a" or P_In=="A":
    if Filed:
        with open(Loc,"a") as Append_file:
            Append_file.write(Final_Data)
            print("Data Saved Successfully...\nCheck the data at location:",Loc)
    else:
        A_loc=input("File location: ")
        try:
            with open(A_loc,"a") as Append_file:
                Append_file.write(Final_Data)
                print("Data appended Successfully...\nCheck the data at location:", A_loc)
        except:
            print("DataError: Failed to append to the file!!!")
