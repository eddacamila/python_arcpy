import arcpy
import os
import sys

def exportar(fileDir,folder_salida,res):
    """exporta a png todos los mxd en directorio y sus subdirectorios
    parameters:
    fileDir: directorio que contiene subfolders que alojen los mxd a exportar
    folder_salida: directorio donde se alojaran todos los archivos png resultado
         """
    if not os.path.exists(folder_salida):
        os.mkdir(folder_salida)
    if os.path.exists(fileDir):
        for root, dirs, files in os.walk(fileDir):
            if files:
                for name in files:
                    if name[-4:] == r".mxd":
                        print("exportando: "+os.path.join(root, name))
                        mxd = arcpy.mapping.MapDocument(os.path.join(root, name))
                        arcpy.mapping.ExportToPNG(mxd,os.path.join(folder_salida,  "{}.png".format(name[:-4])), resolution=res)
                        del mxd

if __name__=="__main__":
    if len(sys.argv)>2:
        fileDir=sys.argv[1] 
        folder_salida = sys.argv[2]
        res = sys.argv[3]
        exportar(fileDir,folder_salida, res)
        