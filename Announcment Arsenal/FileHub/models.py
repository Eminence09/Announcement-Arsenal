from django.db import models



class Main_Storage(models.Model): 
    pdf_file = models.FileField(max_length=1000)
    
    def __str__(self):
        return self.pdf_file.url


class Raw_Storage(models.Model):
    raw_pdfs = models.FileField(max_length=1000)
    
    def __str__(self):
        return self.raw_pdfs.url