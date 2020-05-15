from PIL import Image
from tqdm import tqdm
import random
import sys
import os
import time

def load_file(path):
    File = None
    
    for i in tqdm(range(20)):
        time.sleep(random.random()/10)
        if i == 10:
            try:
                File = Image.open(path)
            except:
                print("Encounted error loading the file")
                input('press enter to exit. ')
                sys.exit()
                
    return File


def save_file(File, Path):
    directory_path = os.path.dirname(Path)
    file_name = os.path.basename(Path)
    
    file_name_parts = file_name.split('.')
    file_name_parts[-2] = file_name_parts[-2]+"_clean"
    file_name = None
    for file_name_part in file_name_parts:
        if file_name == None:
            file_name = file_name_part
        else:
            file_name += "." + file_name_part
    Path = os.path.join(directory_path, file_name)            
    for i in tqdm(range(20)):
        time.sleep(random.random()/10)
    
    
    File.save(Path)
    return Path


if __name__ =="__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print("Selected file: "+path)
        
        print("\nLoading file... ")
        File = load_file(path)
        print("File loaded!")
        
        print("\nCleaning file")
        for i in tqdm(range(20)):
            time.sleep(random.random()/20)
        print("File cleaned!")
              
        print("\nSaving file...")
        new_file_path=save_file(File, path)
        print("Saved file to: "+new_file_path)

        print("\nTask completed succesfully! :)")
    else:
        print('Drag a single file on top of this file to clean it.')

        
#except:
#    print("Fatal error, quiting in 5 seconds")
#    time.sleep(5)
#    sys.exit(0)
    
    
input("Press enter to exit")
