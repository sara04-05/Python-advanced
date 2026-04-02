import pandas as pd

data = {"Name":["Egzon", "Liron", "Melina"],
        "Age": [17,18,19],
        "City":["Fushe Kosove", "Presheve", "Prishtine"]}

df = pd.DataFrame(data)
print(df)