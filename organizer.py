import os
import customtkinter



os.chdir("../Desktop")
wd = os.getcwd()




def cleanAll() :
    organizeImages() 
    clearEmptyFolders()
    organizePDFs()

    finishLabel.configure(text="Organization of all complete.")





def organizeImages() :
    try :
        os.mkdir("Images")

    except:
        print("Images folder already exists")
        
        


    imageExtensions = [".png",".jpg",".jpeg",".gif", ".HEIC", ".heic"]
    imagePath = os.path.join(wd,"Images")


    for item in os.scandir() :
        isFile = item.is_file() 
        if (isFile) :
            for extension in imageExtensions:
                if item.name.endswith(extension) :
                    newLocation = os.path.join(imagePath,item.name)
                    os.rename(item.name,newLocation)
                    print(newLocation)
                    break


    finishLabel.configure(text="Image organization completed.")



def clearEmptyFolders() :

    for item in os.scandir() :
        isDir = item.is_dir()
        if (isDir) :
            try :
                os.rmdir(item.name)
                print("Removed: " + item.name)
            except:
                #print("Folder is not empty")
                continue

    finishLabel.configure(text="Empty folders cleared.")


def organizePDFs() :
    try:
        os.mkdir("PDFs")

    except:
        print("PDFs already exists")

    pdfPath = os.path.join(wd,"PDFs") 


    for item in os.scandir() :
        isFile = item.is_file()
        if isFile and item.name.endswith(".pdf")  :
            newLocation = os.path.join(pdfPath,item.name)
            #print(newLocation)
            os.rename(item.name, newLocation)


    finishLabel.configure(text="PDFs organized.")

            
            
            
            
#System Settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("File Organizer")

#Adding UI Elements

title = customtkinter.CTkLabel(app, text="Please choose what to organize.")
title.pack(padx=200,pady=5)

#Create buttons for options

cleanAll = customtkinter.CTkButton(app, text="Organize All", command=cleanAll)
cleanAll.pack(padx=10,pady=1)

pdfsButton = customtkinter.CTkButton(app, text="Organize PDFs", command=organizePDFs)
pdfsButton.pack(padx=10,pady=1)


imagesButton = customtkinter.CTkButton(app, text="Organize Images", command=organizeImages)
imagesButton.pack(padx=10, pady=1)

emptyButton = customtkinter.CTkButton(app, text="Clear Empty", command=organizeImages)
emptyButton.pack(padx=10, pady=1)


#Finished Organizing
finishLabel = customtkinter.CTkLabel(app,text="")
#finishLabel.pack() ;
#finishLabel.place(x=350,y=170)
finishLabel.pack(padx=10, pady=1)

            
                
                
                
        
