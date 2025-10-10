import sys
import numpy as np
import pandas as pd

print("Python:", sys.version.split()[0])
print("Numpy:", np.__version__)
print("Pandas:", pd.__version__)

df = pd.DataFrame({"a":[1,2,3],"b":[4,5,6]})
print("DataFrame test:")
print(df)
