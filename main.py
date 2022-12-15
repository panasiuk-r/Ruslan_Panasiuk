import dropbox

class Cloud_Storage:
    def init(self, access_token):
        self.tkn = access_token
    def uploadFile(self, file_from, file_to):
        f = open(file_from, 'rb')
        f = f.read()
        dbx = dropbox.Dropbox(self.tkn)
        if file_from != '' and file_to != '':
            dbx.files_upload(f, file_to)
            print("Successfully upload")
        else:
            print("Wrong input")

    def deleteFile(self, path):
        dbx = dropbox.Dropbox(self.tkn)
        dbx.files_delete_v2(path)
        print("Successfully delete")

    def getMetadata(self, path):
        dbx = dropbox.Dropbox(self.tkn)
        res = dbx.files_get_metadata(path)
        print(res)

def main():
    tkn = input("Enter token:")
    user = Cloud_Storage(tkn)
    ff = input("Enter the name file you want to upload")
    ft = input("Enter the folder where you want to upload your file")
    ft = '/'+ft+'/'+ff
    user.uploadFile(ff, ft)
    user.getMetadata(ft)
    user.deleteFile(ft)

if __name__ == 'main':
    main()