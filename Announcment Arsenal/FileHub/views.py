from FileHub.models import Main_Storage, Raw_Storage
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from tkinter import messagebox 
from tkinter import * 


def files(request):
    if request.method == 'POST':
        pdf_file = request.FILES['document'] if 'document' in request.FILES else None
        main_var = Main_Storage(pdf_file=pdf_file)
        raw_var = Raw_Storage(raw_pdfs=pdf_file)
        main_var.save()
        raw_var.save()

    return render(request, "file_upload.html")



def show_data(request):
    try:
        context = {
                "fileupload_list": Raw_Storage.objects.all(),
            }
        return render(request, "display_files.html", context)
    
    except Exception:
        return HttpResponse("Restart your PC!")
    
    
def delete_all_file(request):
    delete_f = Raw_Storage.objects.all()
    
    if delete_f:
        condition = messagebox.askquestion("Delete All Files", "Do you really want to delete all files!")
        if condition == 'yes':
            for each in delete_f:
                print(each.delete())
            del_obj = {
                "del_object": Raw_Storage.objects.all() 
                }
            return render(request, "display_files.html", del_obj)
        else:
            # messages.add_message(request, messages.INFO, "Files are safe!")
            delete_file = Raw_Storage.objects.all()
            
            second_dict = {
                "filed": delete_file
            }
            
            return render(request, "display_files.html", second_dict)
    else:
        messagebox.showinfo("No files Detected", "Sorry! No files are exist.")
        return render(request, "display_files.html", None)
    
# def file_info(request):
#     property_of_file = Raw_Storage.objects.all()

        
#     var1 = r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt"

#     var2 = time.ctime(os.path.getatime(r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt"))

#     var3 = time.ctime(os.path.getmtime(r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt"))

#     var4 = time.ctime(os.path.getctime(r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt"))

#     var5 = os.path.getsize(r"C:\\Users\\YASH RAVINDRABHAI\\OneDrive\\Desktop\\sqldata.rpt")
    
    
#     var_one = var1, var2, var3, var4, var5
    
    
#     var_ = {
#         "var_dict": messagebox.showinfo("Properties", var_one)
#         }
    
#     if var_ == "ok":
#         show_data()
    
#     else:
#         all_obj = Raw_Storage.objects.all()
        
#         obj_file = {
#             'object_of_files': all_obj,
#         }
        
#         return render(request, "display_files.html", obj_file)
    

