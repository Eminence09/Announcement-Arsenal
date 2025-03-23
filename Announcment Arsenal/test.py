import time
import os.path
from tkinter import messagebox



var1 = r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt"

var2 = time.ctime(os.path.getatime(r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt"))

var3 = time.ctime(os.path.getmtime(r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt"))

var4 = time.ctime(os.path.getctime(r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt"))

var5 = os.path.getsize(r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt")



var_one = {
    
    'file:': var1, 
    'access time': var2, 
    'modified': var3, 
    'change': var4, 
    'size': var5
    
    }



messagebox.showinfo("Properties", var_one)