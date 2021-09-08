import cv2
import dropbox
import time
import random

def takesnapshot():
    number=random.randint(0,50)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False
        return imageName
    print("printing snapshot")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadfiles(imageName):
    access_token = 'sl.A4EHYonVRASnbCAvcHK6bjjVs343ZrZwIC6u36JDGEpSoURX2Nw071qYcEqKvkZ5uwV9ZGukJdrZ85kgcbhX5HTfdIK6NIwqmqnTzfX_J4KZMv3YPTn8mk8OlDMmgWiJzIJ0ieJLE6HE'
    file=imageName
    file_from = file
    file_to = '/test_dropbox/'+(imageName)  # The full path to upload the file to, including the file name
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")
def main():
    startTime=time.time()
    while(True):
        if(time.time()-startTime >=5):
            name=takesnapshot()
            uploadfiles(name)
main()
