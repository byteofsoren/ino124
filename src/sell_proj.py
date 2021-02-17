import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

def objective(x, a, b, c):
	return a * x + b * x**2 + c

def sobjective(x,n,groth):
    """ S-curve fitter
    :param t: time input
    """
    # m = 1500
    # n = min(data.values[:,0])
    # n = 50
    m = 1500
    return m/(1+((m-n)/n)*np.exp(-groth*x))




start=1
stop =10
# Previous data
data = pd.read_csv("../data/sellingresults.csv")
x = data.values[:,0]
y = data.values[:,1]

# polynomial
popt, _ = curve_fit(objective, x,y)
a,b,c = popt
# Scureve fiting
popt, _ = curve_fit(sobjective, x,y)
# sm,sn = 1500,min(data.values[:,0])
# sm,sn = 1500,50
sm = 1500
sn,  sg  = popt
print(f"a,b,c={a,b,c}")
print(sg)
xt = np.linspace(0,10)
yt = objective(xt,a,b,c)
syt = sobjective(xt,sn, sg)
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
plt.plot(xt,yt, label='Polynomial pojection')
plt.plot(xt,syt, label='S-curve projection')
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

