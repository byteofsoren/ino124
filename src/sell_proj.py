import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

def objective(x, a, b, c):
	return a * x + b * x**2 + c

start=1
stop =10
# Previous data
data = pd.read_csv("../data/sellingresults.csv")
x = data.values[:,0]
y = data.values[:,1]

popt, _ = curve_fit(objective, x,y)
a,b,c = popt
xt = np.linspace(0,10)
yt = objective(xt,a,b,c)
xproj = np.arange(max(x)+1,stop+1)
yproj = objective(xproj, a,b,c)


# Plot set up
fig, ax = plt.subplots()
plt.xlim(0,stop+1)
plt.title("INO124\nFive year plan")
plt.xlabel("Years")
plt.ylabel("Units sold")

# Plot data
plt.scatter(x,y, label='Input Data')
plt.scatter(xproj,yproj, c='pink', label='Yearly target')
plt.plot(xt,yt, label='Projection')
for k in zip(x,y):
    tx, ty = k
    plt.text(tx + 0.3,ty,f"{int(ty)}")
    pass
for k in zip(xproj,yproj):
    tx, ty = k
    plt.text(tx + 0.3,ty,f"{int(ty)}")
    pass

# Show plot
plt.grid()
ax.legend()
plt.savefig("../results/sell_proj.png")
plt.show()

