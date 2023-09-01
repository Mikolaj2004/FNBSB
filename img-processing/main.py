import os
import glob
from matplotlib import pyplot as plt
#Import funkcji zdefiniowanych w zewnętrznych plikach
import edge_detection
import count

#Przypisanie lokalizacji folderów do zmiennych
path = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(path,"source")
output_path = os.path.join(path,"output")


#Zabezpieczenie przed brakiem folderu source
if not os.path.exists(source_path):
    print("Source directory does not exist.")
    input("Press Enter to Exit...")
    exit()
    
if not os.path.exists(output_path):
        os.makedirs(output_path)

filepaths = glob.glob(source_path + "/*")
file = open((output_path + "/results.txt"), 'w')

#Wywołanie funkcji dla poszczególnych plików żródłowych
for filepath in filepaths:

     filename = os.path.basename(filepath)
     granularity = count.count(edge_detection.edge_detection(filepath,output_path))
     file.write("Calculated granularity for " + filename + " is: " + str(granularity) + " micrometre \n\n")

file.close()

