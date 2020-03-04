from pandas import read_excel

from validate_email import validate_email
import re
from email.utils import parseaddr

def xlsx2list(path):
    df = read_excel(path, header = None)
    lista = df.values.tolist()
    for i in range(0, len(lista)):
        lista[i] = lista[i][0] + '\n'
    return lista

def validarCorreo(lista):
    regEx1 = '^.+@[^\.].*\.[a-z]{2,}$'
    regEx2 = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
    listaBien = []
    listaMal = []
    for linea in lista:
        parse = parseaddr(linea)
        is_valid = validate_email(linea)
        regSearch = re.search(regEx1, linea)
        regMatch = re.match(regEx2, linea)
        if parse and is_valid and regSearch and regMatch:
            listaBien.append(linea)
        else:
            listaMal.append(linea)
    return listaBien, listaMal

def concatXlsx(root, paths):
    listota = []
    for path in paths:
        lista = xlsx2list(path)
        for i in range(0, len(lista)):
            listota.append(lista[i])
    return listota

def concatCSV(root, paths):
    listota = []
    for path in paths:
        lista = open(path, 'r')
        for linea in lista:
            listota.append(linea)
    lista.close()
    return listota
