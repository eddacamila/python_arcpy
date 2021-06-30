# encoding=utf8
#Calculando latitud decimal y longitud decimales a partir de expresiones regulares
# Para latitud
import sys 
reload(sys)  
sys.setdefaultencoding('utf8')
import re
def todec(texto):
    texto=texto.replace("°","g")
    m = re.search(r"^\w?\s?(\d{1,2})g\s?(\d{1,2})'\s?(\d{1,2}\.\d+)\"?", texto)
    a= (float(m.group(1))+(float(m.group(2))/60)+(float(m.group(3))/3600))*
    return a
#Para longitud
import sys 
reload(sys)  
sys.setdefaultencoding('utf8')
import re
def todec(texto):
    texto=texto.replace("°","g")
    m = re.search(r"^\w?\s?(\d{1,2})g\s?(\d{1,2})'\s?(\d{1,2}\.\d+)\"?", texto)
    a= (float(m.group(1))+(float(m.group(2))/60)+(float(m.group(3))/3600))*-1
    return a