import pyautogui as pyag
import pandas as pd
import time

table = pd.read_csv("./formData/produtcs.csv")
print(table)

pyag.PAUSE = 0.5

# Open the HTML Archive
pyag.click(x=259, y=880)         # pyag.click(x=1048, y=1056)
for _ in range(5):
    pyag.press("tab")
pyag.write("E:\DS\DS\L-02 (Formulario)\Ex-01")
pyag.press("enter")
pyag.rightClick(x=625, y=512)    # pyag.rightClick(x=915, y=427)
time.sleep(1)
pyag.click(x=654, y=149)         # pyag.click(x=963, y=552)
pyag.click(x=1110, y=234)        # pyag.click(x=1402, y=634)
time.sleep(5)

# 
for row in table.index:
    pyag.click(x=51, y=286)
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