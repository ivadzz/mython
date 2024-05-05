from funcoes    import CRIA
from funcoes    import  ARRUMA
from funcoes    import DETALHES
import time

tempo_inicio = time.time()

CRIA()
ARRUMA()
DETALHES()

tempo_final = time.time() - tempo_inicio
print('\n{:.2f} segundos'.format(tempo_final))