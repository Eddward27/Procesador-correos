from tkinter import *
import tkinter.scrolledtext as tkst
import gui, herramientas

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__" :
    root = Tk()
    root.resizable(False, False)
    root.iconbitmap(resource_path('app.ico'))
    root.title('Procesar Correos - COVISA')
    herramientas.pathDesktop()

    labelInstruccion = Label(root, text = 'Haga clic en la opción deseada...')
    btnValidar = Button(root, text = 'Validar Correos', command = lambda: gui.validar(root, textFrame, varDup))
    btnConcatExcel = Button(root, text = 'Concatenar Archivos Excel', command = lambda: gui.concatExcel(root, textFrame, varDup))
    btnConcatCSV = Button(root, text = 'Concatenar Archvos CSV', command = lambda: gui.concatCSV(root, textFrame, varDup))
    btnExcel2CSV = Button(root, text = 'Excel a CSV', command = lambda: gui.excel2CSV(root, textFrame, varDup))
    btnDuplicados = Button(root, text = 'Borrar Duplicados', command = lambda: gui.duplicados(root, textFrame))

    textFrame = tkst.ScrolledText(master = root, wrap = WORD, width = 60, height = 10, state = DISABLED)
    varDup = IntVar()
    Checkbutton(root, text = 'Borrar Duplicados en Operación', variable = varDup).grid(row = 7, column = 2, rowspan=2)

    btnQuit = Button(root, text = 'Salir', command = lambda: gui.exit(root))

    labelInstruccion.grid(row = 1, column = 1)
    btnValidar.grid(row = 2, column = 1)
    btnConcatExcel.grid(row = 3, column = 1)
    btnConcatCSV.grid(row = 4, column = 1)
    btnExcel2CSV.grid(row = 5, column = 1)
    btnDuplicados.grid(row = 6, column = 1)
    textFrame.grid(row = 1, column = 2, columnspan=2, rowspan=6)
    btnQuit.grid(row = 7, column = 3, rowspan=2, sticky = W)

    col_count, row_count = root.grid_size()
    for col in range(col_count):
        root.grid_columnconfigure(col, minsize=20)
    for row in range(row_count):
        root.grid_rowconfigure(row, minsize=20)

    root.mainloop()
