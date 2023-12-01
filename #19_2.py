#19.2
import pandas as pd
import numpy as np
import json
with open('tetraedr.json','r') as file:
    peace=json.load(file)
Serias= pd.Series(file)
def pidrahui(x):
    A = np.array(x[1])
    B = np.array(x[2])
    C = np.array(x[3])
    D = np.array(x[4])
    V=np.abs(np.dot(A-D, np.cross(B-D,C-D)))/6
    return V
Result=pidrahui(Serias)
V_peace={'Tetrahedron V=':Result}
with open('volume.json','w') as V_file:
    json.dump(V_peace,V_file)
print(f"Об'єм тетраедра: {Result}.Результат збережено.")
