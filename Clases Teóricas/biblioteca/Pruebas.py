

import csv

class FileData:
    
    def __init__(self,filename):
        self.filename = filename

    
    def get_file_data(self):  
        try: 
            
            with open(self.filename,'r',encoding='utf-8') as fd:
                
                
                # extraigo los medios de transportes del csv
                t = ((fd.readline()[:-1].lower()).split(','))[2:]
        
                # genero claves de los medios de transporte disponibles 
                self.d = dict.fromkeys(t)
                total_date = []
                
                colectivo = []
                lancha = []
                subte = []
                tren = []
                
                lector = csv.reader(fd)
                for line in lector:
                    fecha = line[0].split('-')
                    total_date.append(list((fecha,line[1])))
                    colectivo.append(list((fecha,line[2])))
                    lancha.append(list((fecha,line[3])))
                    subte.append(list((fecha,line[4])))
                    tren.append(list((fecha,line[5])))
                    
            
                self.d[t[0]] = colectivo
                self.d[t[1]] = lancha
                self.d[t[2]] = subte
                self.d[t[3]] = tren
        
        
        except FileNotFoundError:
            print('No se encontro el archivo')    
                
                    

datos = FileData('total-usuarios-por-dia.csv')




















        