import os
import shutil
import time


class PATH_CLEANER:
    def __init__(self):
        self.path = ""

    def Folder_Cleaner(self, path: str):
        self.path = path
        if os.path.exists(self.path):
            files = []
            try:
                files = os.listdir(self.path)
            except Exception as msg:
                print(f"ERROR: {msg}")
            if len(files) == 0:
                print("ERROR: [PATH CLEANER] The file to be deleted was not found in the folder")
            else:
                for file in files:
                    PATH_file = f"{self.path}/{file}"
                    try:
                        if os.path.isfile(PATH_file):
                            os.remove(PATH_file)
                            print(f"Deleted file: {PATH_file}")
                        else:
                            shutil.rmtree(PATH_file)
                            print(f"Deleted file: {PATH_file}")
                    except Exception as msg:
                        print(f"ERROR: {msg}")
                print("\nThe file deletion process is completed! :)")
        else:
            print("ERROR: [PATH CLEANER] The file was not found")

    def Cleaner(self):
        self.Folder_Cleaner("C:/Windows/Temp")
        time.sleep(0.001)
        self.Folder_Cleaner(f"C:/Users/{os.environ['USERNAME']}/AppData/Local/Temp")
        time.sleep(0.001)
        self.Folder_Cleaner("C:/Windows/Prefetch")
        time.sleep(0.001)
        self.Folder_Cleaner("C:/Windows/SoftwareDistribution/Download")
        time.sleep(0.001)
        self.Folder_Cleaner(f"C:/Users/{os.environ['USERNAME']}/Recent")
        time.sleep(0.001)
