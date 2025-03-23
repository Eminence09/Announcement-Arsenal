#
# Required Modules and packages
# 


import os 
import time
import shutil
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



destination_path = r"D:\\File Storage\\store_files"


class OnMyWatch:
    watchDirectory = r"D:\\File Storage\\watch_files"
    def __init__(self):
        self.observer = Observer()
    def run(self):
        try:
            event_handler = Handler()
            self.observer.schedule(event_handler, self.watchDirectory)
            self.observer.start()
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped")
        finally:
            self.observer.join()



class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print("Watchdog received created event - %s." % event.src_path)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")        
            filePath = event.src_path
            movepath = os.path.join(destination_path, timestamp)
            if (os.path.exists(filePath)): 
                if (os.path.exists(movepath) == False):
                    os.makedirs(movepath)
                    time.sleep(3)
                    shutil.move(filePath, movepath + "\\user_file.pdf")
                 
                 
    # def on_modified(self, event):                               # If any changes made in files, function will be invoke
    #     if not event.is_directory:
    #         print("Watchdog received modified event - %s." % event.src_path)
    #         timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    #         imagePath = event.src_path
    #         if(os.path.exists(imagePath)):           
    #             if(os.path.exists(os.path.join(destination_path,timestamp)) == False):
    #                 os.makedirs(os.path.join(destination_path, timestamp))
    
     

if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()