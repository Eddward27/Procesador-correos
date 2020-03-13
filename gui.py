import herramientas, operadores
from tkinter import *

def intoConsole(msg, text, type = 0):
    text.config(state=NORMAL)
    text.insert(END, msg + '\n')
    text.config(state=DISABLED)
    text.yview(END)

def validar(root, textFrame, varDup):
    intoConsole('Validar correos', textFrame)
    intoConsole('Seleccionar un archivo...', textFrame)
    dupFlag = varDup.get()
    path = herramientas.getFile(root)
    if not path:
        intoConsole('No se seleccionó un archivo...', textFrame)
        intoConsole('____________________________________________________________', textFrame)
        return

    extension = herramientas.getExtension(path)
    if extension == '.csv':
        lista = open(path, 'r')
    else:
        lista = operadores.xlsx2list(path)

    if dupFlag:
        intoConsole('Quitando duplicados...', textFrame)
        lista = herramientas.duplicados(lista)
    intoConsole('Validando...', textFrame)
    correctos, erroneos = operadores.validarCorreo(lista)

    if correctos:
        intoConsole('Guardar archivo de correos correctos...', textFrame)
        nombreArchivoCorrectos = herramientas.saveFile(root, correctos, 'Correctos')
        intoConsole('Archivo guardado en la ruta: ' + nombreArchivoCorrectos, textFrame)
    else:
        intoConsole('No se encontraron correos correctos...', textFrame)
    if erroneos:
        intoConsole('Guardar archivo de correos erroneos...', textFrame)
        nombreArchivoErroneos = herramientas.saveFile(root, erroneos, 'Erroneos')
        intoConsole('Archivo guardado en la ruta: ' + nombreArchivoErroneos, textFrame)
    else:
        intoConsole('No se encontraron correos erroneos...', textFrame)
    if extension == '.csv':
        intoConsole('Cerrando archivo original...', textFrame)
        lista.close()
    intoConsole('Listo!', textFrame)
    intoConsole('____________________________________________________________', textFrame)

def concatExcel(root, textFrame, varDup):
    intoConsole('Concatenar archivos Excel', textFrame)
    intoConsole('Seleccionar dos o más archivos...', textFrame)
    dupFlag = varDup.get()
    paths = herramientas.getFilesXlsx(root)
    if len(paths) < 2:
        intoConsole('No se seleccionaron archivos suficientes [Mínimo 2]...', textFrame)
        intoConsole('____________________________________________________________', textFrame)
        return
    intoConsole('Concatenando...', textFrame)
    lista = operadores.concatXlsx(root, paths)
    if not lista:
        intoConsole('Hubo un error al leer los archivos...', textFrame)
        intoConsole('____________________________________________________________', textFrame)
        return

    if dupFlag:
        intoConsole('Quitando duplicados...', textFrame)
        lista = herramientas.duplicados(lista)
    intoConsole('Guardar archivo concatenado...', textFrame)
    nombreArchivo = herramientas.saveFile(root, lista, 'Excel Concatenado')
    if nombreArchivo:
        intoConsole('Archivo guardado en la ruta: ' + nombreArchivo, textFrame)
        intoConsole('____________________________________________________________', textFrame)
    else:
        intoConsole('El archivo no se guardó...', textFrame)
        intoConsole('____________________________________________________________', textFrame)

def concatCSV(root, textFrame, varDup):
    intoConsole('Concatenar archivos CSV', textFrame)
    intoConsole('Seleccionar dos o más archivos...', textFrame)
    dupFlag = varDup.get()
    paths = herramientas.getFilesCSV(root)
    if len(paths) < 2:
        intoConsole('No se seleccionaron archivos suficientes [Mínimo 2]...', textFrame)
        intoConsole('____________________________________________________________', textFrame)
        return
    intoConsole('Concatenando...', textFrame)
    lista = operadores.concatCSV(root, paths)
    if not lista:
        intoConsole('Hubo un error al leer los archivos...', textFrame)
        intoConsole('____________________________________________________________', textFrame)
        return

    if dupFlag:
        intoConsole('Quitando duplicados...', textFrame)
        lista = herramientas.duplicados(lista)
    intoConsole('Guardar archivo concatenado...', textFrame)
    nombreArchivo = herramientas.saveFile(root, lista, 'CSV Concatenado')
    if nombreArchivo:
        intoConsole('Archivo guardado en la ruta: ' + nombreArchivo, textFrame)
        intoConsole('____________________________________________________________', textFrame)
    else:
        intoConsole('El archivo no se guardó...', textFrame)
        intoConsole('____________________________________________________________', textFrame)

def excel2CSV(root, textFrame, varDup):
    intoConsole('Transformar archivo Excel a CSV', textFrame)
    intoConsole('Seleccionar un archivo...', textFrame)
    dupFlag = varDup.get()
    path = herramientas.getFileXlsx(root)
    if not path:
        intoConsole('No se seleccionó un archivo...', textFrame)
        intoConsole('____________________________________________________________', textFrame)
        return
    intoConsole('Transformando', textFrame)
    lista = operadores.xlsx2list(path)
    if not lista:
        intoConsole('Hubo un error al leer los archivos...', textFrame)
        intoConsole('____________________________________________________________', textFrame)
        return
    if dupFlag:
        intoConsole('Quitando duplicados...', textFrame)
        lista = herramientas.duplicados(lista)
    nombreSave = herramientas.getName(path)
    intoConsole('Guardar archivo transformado a CSV...', textFrame)
    nombreArchivo = herramientas.saveFile(root, lista, nombreSave)
    if nombreArchivo:
        intoConsole('Archivo guardado en la ruta: ' + nombreArchivo, textFrame)
        intoConsole('____________________________________________________________', textFrame)
    else:
        intoConsole('El archivo no se guardó...', textFrame)
        intoConsole('____________________________________________________________', textFrame)

def duplicados(root, textFrame):
    intoConsole('Quitar duplicados', textFrame)
    intoConsole('Seleccionar un archivo...', textFrame)
    path = herramientas.getFile(root)
    if not path:
        intoConsole('No se seleccionó un archivo...', textFrame)
        intoConsole('____________________________________________________________', textFrame)
        return
    extension = herramientas.getExtension(path)
    if extension == '.csv':
        lista = open(path, 'r')
    else:
        lista = operadores.xlsx2list(path)
    intoConsole('Quitando duplicados...', textFrame)
    listaSinDup = herramientas.duplicados(lista)
    if extension == '.csv':
        intoConsole('Cerrando archivo original...', textFrame)
        lista.close()
    nombreSave = herramientas.getName(path)
    intoConsole('Guardar archivo sin duplicados...', textFrame)
    nombreArchivo = herramientas.saveFile(root, listaSinDup, nombreSave + ' sin duplicados')
    if nombreArchivo:
        intoConsole('Archivo guardado en la ruta: ' + nombreArchivo, textFrame)
        intoConsole('____________________________________________________________', textFrame)
    else:
        intoConsole('El archivo no se guardó...', textFrame)
        intoConsole('____________________________________________________________', textFrame)

def exit(root):
    root.destroy()
