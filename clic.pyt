import pyautogui
import time

# Espera 1 segundo antes de capturar a posição do mouse
time.sleep(1)

# Obtém a posição atual do mouse (não será usada para clicar)
posicao_mouse = pyautogui.position()

# Exibe a posição do mouse
print(f'Posição do mouse: {posicao_mouse}')

# Definindo as posições para os cliques
posicao_mouse_2 = (339, 153)  # Para o clique duplo
posicao_mouse_3 = (739, 63)  # Para a entrada de texto 1 (youtube)
posicao_mouse_4 = (480, 144)  # Para a entrada de texto 2 (LOL123)
posicao_mouse_5 = (449, 727)  # Para o clique simples final

# Lista de posições para o mouse (incluso o clique final simples)
posicoes = [posicao_mouse_2, posicao_mouse_3, posicao_mouse_4, posicao_mouse_5]

# Movendo o mouse e clicando nas posições
for idx, posicao in enumerate(posicoes):
    pyautogui.moveTo(posicao[0], posicao[1])  # Move para a posição (x, y)
    time.sleep(3)  # Espera 3 segundos antes de clicar
    
    if idx == 0:
        # Clique duplo na primeira posição
        pyautogui.doubleClick()
        print(f'Clicado duplamente na posição: {posicao}')
    
    elif idx == 1:
        # Clique simples para a entrada de texto 1 (youtube)
        pyautogui.click()
        print(f'Clicado na posição: {posicao}')
        time.sleep(2)
        
        # Entrada de texto 1 (youtube)
        texto_1 = "youtube"
        pyautogui.write(texto_1)  # Digita o texto no campo
        pyautogui.press('enter')  # Pressiona 'Enter' para confirmar a entrada
        print(f'Texto inserido no campo: {texto_1}')
    
    elif idx == 2:
        # Clique simples para a entrada de texto 2 (LOL123)
        pyautogui.click()
        print(f'Clicado na posição: {posicao}')
        time.sleep(2)
        
        # Entrada de texto 2 (LOL123)
        texto_2 = "rocklee e gaara linnkpark"
        pyautogui.write(texto_2)  # Digita o texto no campo
        pyautogui.press('enter')  # Pressiona 'Enter' para confirmar a entrada
        print(f'Texto inserido no campo: {texto_2}')

    elif idx == 3:
        # Clique simples na última posição
        pyautogui.click()
        print(f'Clicado na posição: {posicao}')

# Exibe uma mensagem final
print('Cliques e entradas de texto efetuados.')
