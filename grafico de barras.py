from matplotlib import pyplot as plt
import numpy as np

# 1) Quantitativo de vendas para o produto A:
valores_produtos_A = [6, 7, 8, 4, 4]

# 2) Quantitativo de vendas para o produto B:
valores_produtos_B = [3, 12, 3, 4.1, 6]

# 3) Quantitativo de vendas para o produto C:
valores_produtos_C = [4, 10, 3, 5, 7]

# 3) Quantitativo de vendas para o produto D:
valores_produtos_D = [2, 7, 9, 11, 1]

# 4) Cria eixo "x" para produto A e produto B com uma separação de 0,25 entre as barras:
x1 = np.arange(len(valores_produtos_A))
x2 = [x + 0.20 for x in x1]
x3 = [x + 0.20 for x in x2]
x4 = [x + 0.20 for x in x3]

# 5) Plota as barras:
plt.bar(x1, valores_produtos_A, width=0.20, label='Produto A', color='lightpink')
plt.bar(x2, valores_produtos_B, width=0.20, label='Produto B', color='salmon')
plt.bar(x3, valores_produtos_C, width=0.20, label='Produto C', color='darkorange')
plt.bar(x4, valores_produtos_D, width=0.20, label='Produto D', color='gold')

# 6) Coloca o nome dos meses como label no eixo x
meses = ['Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
plt.xticks([x + 0.25 for x in range(len(valores_produtos_A))], meses)

# 7) Insere uma legenda no gráfico
plt.legend()

# 8) Insere um titulo no gráfico
plt.title('Quantidade de Vendas')

# 9) Mostrando o gráfico:
plt.show()

# 10) Links:
    # Cores: https://matplotlib.org/stable/gallery/color/named_colors.html
    # Matplotlib: https://matplotlib.org/stable/tutorials/introductory/usage.html
    # Numpy: https://numpy.org/doc/stable/numpy-ref.pdf
