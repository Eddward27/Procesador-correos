import os
from pathlib import Path
from tkinter import filedialog

typeAll = [('(CSV) Delimitado por comas','*.csv'), ('Documentos de texto', '*.txt'), ('Libro de Microsoft Excel','*.xlsx *.xls')]
typeXlsx = [('Libro de Microsoft Excel','*.xlsx *.xls')]
typeCSV = [('(CSV) Delimitado por comas','*.csv *.txt')]

def getName(path):
    nombre = os.path.basename(path)
    nombre, file_extension = os.path.splitext(nombre)
    return nombre

def pathDesktop():
    desk = str(Path.home()) + '/Desktop'
    os.chdir(desk)

def getFile(root):
    filePath = filedialog.askopenfilename(parent = root, title = 'Seleccione un archivo', filetypes = typeAll)
    if filePath:
        os.chdir(os.path.split(filePath)[0])
    return filePath

def getExtension(path):
    filename, file_extension = os.path.splitext(path)
    return file_extension

def duplicados(lista):
    sinDup = list(dict.fromkeys(lista))
    return sinDup

def saveFile(root, list, file_save=''):
    file = filedialog.asksaveasfile(
        title='Guardar archivo',
        initialdir=os.getcwd(),
        initialfile=file_save,
        defaultextension='.csv',
        filetypes=typeCSV)

    if not file:
        return False
    for linea in list:
        file.write(linea)
    file.close()
    os.chdir(os.path.split(file.name)[0])
    return file.name

def getFilesXlsx(root):
    filePath = filedialog.askopenfilenames(parent = root, title = 'Seleccione dos o más archivos', filetypes = typeXlsx)
    if filePath:
        os.chdir(os.path.split(filePath[0])[0])
    return filePath

def getFilesCSV(root):
    filePath = filedialog.askopenfilenames(parent = root, title = 'Seleccione dos o más archivos', filetypes = typeCSV)
    if filePath:
        os.chdir(os.path.split(filePath[0])[0])
    return filePath

def getFileXlsx(root):
    filePath = filedialog.askopenfilename(parent = root, title = 'Seleccione un archivo', filetypes = typeXlsx)
    if filePath:
        os.chdir(os.path.split(filePath)[0])
    return filePath
