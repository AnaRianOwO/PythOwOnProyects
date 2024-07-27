import webbrowser
from pyautogui import click, position
from time import sleep

def open_university():
    webbrowser.open('aulavirtual.ibero.edu.co/login/index.php')
    print('Abriendo la universidad...')
    
def click_university():
    sleep(10)
    click(1448, 99)
    
def main():
    open_university()
    click_university()

main()

# def pruebaclicks():
#     while True:
#         x = position().x
#         y = position().y
#         print(f"{x} , {y}")
        
# pruebaclicks()