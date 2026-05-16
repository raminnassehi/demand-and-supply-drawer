import matplotlib.pyplot as plt

# Price range
prices = [i for i in range(1, 11)]

# Demand curve (Qd = a - bP)
demand = [100 - 10*p for p in prices]

# Supply curve (Qs = c + dP)
supply = [20 + 15*p for p in prices]

plt.figure(figsize=(8, 6))
plt.plot(demand, prices, label="Demand Curve", color="blue")
plt.plot(supply, prices, label="Supply Curve", color="orange")
plt.title("Demand and Supply Curve")
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()