import pywhatkit as kit

texto = '''
Texto de teste de Thalles Enrick

Texto escrito usando Python!

Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. 
Fusce magna tellus, imperdiet 
nec interdum ut, mollis sit 
amet massa. Ut pulvinar orci quam,
eu facilisis dolor vehicula quis.
Curabitur a vulputate lorem. 
Nam justo felis, lacinia a varius 
vel, tincidunt ut neque.
'''

kit.text_to_handwriting(texto, save_to='texto_a_mao.png')