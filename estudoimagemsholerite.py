import pytesseract
from PIL import Image
import re
import glob
import pandas as pd

def get_data(file):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
    tessdata_dir_config = r'--tessdata-dir "C:/Users/USER/AppData/Local/Tesseract-OCR/tessdata"'
    phrase = pytesseract.image_to_string(Image.open(file), "por")
    lista_completa = [content for content in phrase.strip().splitlines() if content]
    lista_limpa= []
    

    for item in lista_completa:
        if item == " ":
            pass
        else:
            lista_limpa.append(item)

    lista_rubricas=[]
    for item in lista_limpa:
        item_slice = item[0:6]
        padrao_basico_rubrica= re.compile(r'\d\d\.\d\d\d')
        mo = padrao_basico_rubrica.search(item_slice)
        if mo != None:
            lista_rubricas.append(item)
    return lista_rubricas

lista_todos = []
listaarquivos = glob.glob("C:/Users/Home/Desktop/testes3/JPEG/*.jpg")
for item in listaarquivos:
    lista_todos.append(get_data(item))
    print(item)
print(lista_todos)
    
dataframe = pd.DataFrame(lista_todos)
dataframe.to_excel('teste1.xlsx')

    
    
    
    
    
    


