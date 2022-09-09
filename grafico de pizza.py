import matplotlib.pyplot as plt
import numpy as np

# 1) Valores do Gráfico:
y = np.array([31, 23, 17, 10, 8, 7, 17])

# 2) Nomes dos itens do gráfico
mylabels = ['Maças', 'Bananas', 'Laranjas', 'Melancias', 'Cajus', 'Cerejas', 'Pêras']
# 3) Espaço entre as "fatias" do gráfico
myexplode = [0.1, 0, 0, 0, 0, 0, 0]

# 4) Montando o gráfico
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True,
        autopct='%.1f%%', startangle=90,
        colors=['red', 'gold', 'orange', 'limegreen',
                'orangered', 'crimson', 'lightgreen'])

# 5) Mostrando o gráfico:
plt.show()

# 6) Links:
    # Cores: https://matplotlib.org/stable/gallery/color/named_colors.html
    # Matplotlib: https://matplotlib.org/stable/tutorials/introductory/usage.html
    # Numpy: https://numpy.org/doc/stable/numpy-ref.pdf
