import pyautogui as pyag
import pandas as pd
import time

table = pd.read_csv("./formData/produtcs.csv")
print(table)

pyag.PAUSE = 0.4

# Open the HTML Archive
pyag.click(x=259, y=880)
pyag.click(x=407, y=75)
pyag.write("E:\DS\DS\L-02 (Formulario)\Ex-01")
pyag.press("enter")
pyag.doubleClick(x=334, y=198)
time.sleep(3)

# 
for row in table.index:
    pyag.click(x=47, y=178)
    pyag.write(str(table.loc[row, "codigo"]))
    pyag.press("tab")
    pyag.write(str(table.loc[row, "marca"]))
    pyag.press("tab")
    pyag.write(str(table.loc[row, "tipo"]))
    pyag.press("tab")
    pyag.write(str(table.loc[row, "categoria"]))
    pyag.press("tab")
    pyag.write(str(table.loc[row, "preco_unitario"]))
    pyag.press("tab")
    pyag.write(str(table.loc[row, "custo"]))
    pyag.press("tab")
    pyag.press("enter")