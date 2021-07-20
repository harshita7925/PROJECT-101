from os import access
import dropbox
 
class TransferData:
    def _init_(self,access_token):
         self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root, filename)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
        with open(local_path,"rb") as f:
            dbx.files_upload(f.read(),dropbox_path,mode=WriteMode("overwrite"))

def main():
    access_token="sl.A0O4yA4SCJmRo3IrI_uhkAmew3puE5W7cDcyE2cfr0wArceze5Aux1KCPklH1XAVlIwwZojE2RSUftNT5NBtB3GagSraCs1RtJtLCak79ZZcvjMB4o5ffgjfn8G0dxESA4Z1UxE"
    transferData=TransferData(access_token)
    file_from=input("Enter the folder that you want to upload :")
    file_to=input("Enter the name of the full path :")

    transferData.upload_file(file_from,file_to)
    print("Folder has been successfully uploaded")

main()