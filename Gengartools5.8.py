import itertools
import random
import os
import sys
import time

M_DEGRADADO = "\033[38;5;93m"  
M_BRILLANTE = "\033[38;5;129m" 
CYAN = "\033[38;5;51m"        
GRIS = "\033[38;5;244m"       
VERDE = "\033[38;5;46m"       
ROJO = "\033[38;5;196m"       
RESET = "\033[0m"

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_disenos_propios():
    diseno_1 = """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⢀⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⢀⣀⡸⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⠛⣿⣿⣿⣿⣿⣿⡿⠛⠋⢀⣲⢶⠺⠍⠒⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢠⠒⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢀⠈⠛⠀⢀⠘⠻⣿⣿⠟⠁⢀⠖⡂⠀⢿⣿⣿⡿⠛⠋⣀⣲⠶⣾⠽⢩⠹⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠠⠛⡰⣐⢶⣆⣀⣀⣀⡀⠛⠋⠀⠶⣞⡀⠀⠰⢎⠀⠀⢀⠠⣆⠼⡑⠎⠀⠀⠀⡀⠀⠀⣀⣀⣯⡽⢯⡷⢀⢳⠈⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⢁⠣⢎⡉⣯⢯⣛⣧⣤⣤⠀⢃⠿⣘⠀⢘⡜⡀⢠⢌⠳⣌⠶⣩⠃⠀⠀⡤⠃⠀⣤⠿⣽⠾⣝⠯⢉⡜⠠⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠉⢎⠲⡉⣯⠉⣞⣧⠿⠤⢈⠳⣌⢣⡍⣖⢩⠖⣩⢓⡬⢲⠅⡯⢜⡱⣉⠧⢤⡉⠿⢁⠾⢉⢮⠱⠈⠀⠐⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠈⠧⣡⢃⡤⡙⠾⠏⠀⠌⣷⣬⣥⡼⣬⢇⡾⣥⢚⠴⣋⠼⣘⢎⡱⡱⢎⢣⠞⣡⢯⠰⣩⠲⢀⠀⠄⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠦⣙⠴⠃⠀⢠⣟⡿⣳⢾⡼⣽⢶⡙⣶⡍⣏⠲⡍⣎⠵⣊⠵⣱⠩⠞⣌⢇⡎⢧⡱⢉⠀⠀⠄⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⡀⠁⠆⠀⢻⣟⣼⣳⢯⣳⡟⣼⢯⡓⢦⡙⡴⢋⡴⢃⡞⣡⠞⣔⢫⡙⣬⠲⡜⣡⠚⠀⠀⡐⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⡅⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠻⢿⣿⣿⣿⣿⣿⡇⠀⠀⣓⢛⣮⢷⣹⣏⣷⢛⡹⢦⡙⢦⡙⡴⢋⡴⢋⡴⠣⠞⡬⡒⣍⠦⣓⡍⡖⠀⢀⠐⠀⠀⠀⠀⠈⠙⠛⠛⠡⣤⡤⣤⡄⠳⢤⡀⢻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢁⣠⣀⣴⣆⡀⠛⠛⠛⠛⣿⡇⠀⠆⠁⢏⡴⢊⡖⡜⣤⠫⣔⢣⡚⢥⡚⢁⣭⡐⠫⠄⠁⣀⠀⠑⡎⡼⢡⠎⠐⠀⠠⢀⠐⠀⠀⢀⡰⡒⢦⡔⢢⣾⡹⡗⠁⡀⠃⠂⣀⠀⠿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠘⢳⡛⢶⣏⡷⡆⢂⡀⠀⠀⠀⢀⡒⠂⠀⠈⢳⡘⡼⢄⡳⣌⢣⠞⣡⠰⣞⡗⠃⠀⣠⡄⠀⠁⠀⡳⣘⠣⠃⡔⠀⢀⠂⠠⠈⢰⣊⠵⣩⡜⢃⡜⠳⣽⣳⣆⣀⡶⠁⠀⣰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢀⢠⡙⡖⣢⠖⡜⡃⠀⠀⠂⠀⢧⡁⠀⠑⣂⡀⠀⠑⢪⠱⡜⣢⢏⠲⡘⠛⠀⠀⠀⣿⢷⡆⠀⠀⢧⡑⠋⠀⣜⣀⠀⢀⠂⠄⠐⢨⢲⠱⣢⠝⣌⢳⡘⢧⢋⡄⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⢆⠱⡎⢱⢎⡱⠁⡀⠀⠁⠀⠱⠶⠆⠀⢿⡏⠀⠀⠀⢸⠸⣁⠎⣇⢱⠀⠀⢷⣶⠿⡇⠁⠀⠆⠁⠈⠀⢸⢰⢆⠀⢀⠀⠆⠀⠸⣆⠿⣀⢏⡸⢆⡹⠈⠁⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣀⠈⠈⠁⠎⠀⡁⠀⠄⠀⠀⢰⡀⠁⠀⠀⠙⠋⠙⠠⣌⠳⢬⡙⢦⠹⡸⠄⠄⠠⠀⠀⠀⡬⣥⣤⠋⠤⣌⢲⡩⠀⠀⠄⠂⢈⠀⠈⠀⠉⠀⠈⠁⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⠀⠀⠀⠂⠠⠀⠀⢎⡤⡀⠛⣤⠀⠂⠉⠓⠈⠙⠂⠙⠊⠑⠉⠀⢠⣤⡄⢸⣿⣿⣟⠛⡀⠼⢤⢣⠕⠀⢈⠀⡐⠀⡀⠂⠁⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⣀⣀⡀⠀⠮⡔⢣⡀⠛⠀⣿⣿⣿⠀⢸⣿⣿⣿⡇⢸⣿⣿⣿⣧⡟⠻⣿⠃⢠⡜⢭⠲⣩⠐⠀⠠⠀⠄⠐⠀⡐⠀⠠⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⣍⠳⣘⠦⡀⠟⣿⣿⣼⡛⢿⣿⣿⣧⡜⢻⣿⣿⡿⠇⠀⡀⣔⢣⡜⢎⡕⢃⠀⢀⠂⠐⡀⠌⢀⠠⠈⠀⠄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡀⠈⣇⠳⡜⣱⢢⢀⡀⠛⠁⠘⠛⠛⠛⠃⠘⠃⣀⡀⡖⣰⡑⢎⡖⡜⢣⠂⠀⠠⠀⠐⡀⠠⠀⠂⠀⠄⠁⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠌⢳⡘⣥⠚⣬⢱⣂⠖⣰⢂⡖⣰⢂⢖⡰⣡⠞⡬⡱⢜⢣⡜⡜⠣⠈⠀⠄⠁⠄⠠⠐⠀⡁⠈⠠⠀⠀⠈⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡀⠃⠞⡤⢛⡤⢣⢎⡚⢥⡚⡜⡴⢩⢎⠲⢥⡚⢥⠓⢮⡱⠜⠈⠁⡀⠌⢀⠈⠠⠐⠀⡁⠀⠐⠀⠀⢀⠀⡀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠉⠧⠜⢣⢎⡙⢦⡙⡴⣉⠧⢎⡝⡢⢝⡪⠙⠦⠁⠀⡐⠀⠄⣀⢂⡀⣁⢀⠂⡀⠈⠀⡀⠠⠀⠄⠀⠁⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠐⡀⠀⠈⠁⠈⠉⠖⠩⠖⠩⠞⠬⠒⠉⠈⠁⠁⢀⠀⠂⠀⡖⣰⢢⢣⡹⢄⡼⣶⣈⠠⠀⠀⠐⠀⣀⣀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡄⠀⠤⢤⣀⠀⠀⠀⠀⠄⠀⠠⠀⡀⠀⠄⠂⠁⡐⠈⢀⠀⠀⡇⢼⢡⠎⡵⣘⢯⡽⣶⣻⠀⡟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠉⠲⣌⠹⠰⠤⡀⠀⠀⠀⠀⠀⠈⠀⠄⠁⠠⠐⠀⠀⠀⠉⠆⡫⢜⢲⣉⢦⢛⣧⠛⡤⣹⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠁⠠⠀⠠⠜⠁⠈⠀⢠⣾⣿⣧⣤⣤⣤⣤⣤⣤⣴⣿⣿⣧⡀⠈⢣⣃⢎⠖⣣⠆⣏⠴⠁⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠌⠎⠞⡰⠙⠨⢄⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⢀⠀⠈⠐⠀⠀⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

    diseno_2 = """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⠟⣽⣿⣿⣿⠁⠀⣿⣿⡿⣿⣿⡿⣿⣿⣿⣿⣿⡿⠛⠁
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠛⠿⠟⠁⠀⠀⠀⣿⡟⠀⣿⡏⢠⣿⣿⠿⠋⠁⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠙⠛⠀⠀⢰⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⠙⢿⡇⠀⠀⠀⢸⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠈⣿⣇⠙⠿⣷⣦⡀⠀⠀⠀⠀⣤⡄⠀⠀⠀⠀⢠⣤⡄⠀⠀⣸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠙⠿⣿⣤⡀⠀⢠⣿⡿⠀⠀⢀⣤⣾⡿⠁⠀⢰⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣷⣄⠀⠀⢀⡀⠀⠹⣿⣆⠀⠀⠈⡿⣿⣷⣿⣿⡇⠀⠀⣼⣿⣿⣀⣀⣤⣾⣿⣿⡿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠙⠛⠀⠐⣿⣿⡀⠀⠹⣿⣶⣦⣤⣤⣤⣽⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣦⣄⣄⡉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⡉⢻⣿⢿⣷⣦⣤⣤⣄⣠⣤⣤⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣼⣿⠀⠀⠉⣿⠉⠛⠛⠛⠛⠛⠛⠋⠉⢹⡏⠉⠉⢹⡏⠉⠉
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡇⢀⣴
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠙⣿⣦⡀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠘⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣤⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣠⣶⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⣤⣼⣻⡿⠿⣶⣶⣦⣴⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿"""

    diseno_3 = """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠘⣿⣿⠟⠋⠉⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠋⠉⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠹⣿⡿⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠻⠿⠟⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠀⠀⠈⠉⠉⠛⠛⠛⠛⠿⠿⠿⠿⠿⠏⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠆⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠋⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢹⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠠⠾⣿⠀⢿⠿⠛⠁⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠒⠛⢋⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⡇⢸⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠷⠆⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⡆⢸⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡦⠀⠀⠀⠀⠀⠀⢻⣦⣄⠀⣀⣀⣀⡀⢀⣤⣤⣤⣶⣶⣾⡇⠀⣿⣿⣿⣿⡇⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⡇⢸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⠇⢸⣿⣿⣿⣿⣿⣿⡇⠀⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⣿⣿⣿
⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣤⡀⠀⢀⠀⠀⠀⣿⣿⣿
⣿⣿⣿⡇⠀⠀⠀⠀⠀⣴⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣄⣾⣆⣾⣤⣿⣿⣿⣿
⣿⣿⣿⣧⣶⡀⣸⣦⣸⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

    diseno_4 = """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣷⣄⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢹⣿⣿⣷⣄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣿⣿⣿⣿⣷⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣦⡈⠻⣿⠀⠈⠻⡿⠛⢿⣿⣿⡿⠿⠛⠉⢉⣀⡤⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠓⣄⠀⢠⠀⠉⣁⣤⣴⣶⣿⣿⡟⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠇⢀⠉⠻⠿⣿⣿⣿⣿⣇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠘⠛⠋⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡀⠠⣤⣴⣿⣶⣤⣀⠙⠻⣿⣿⠀⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠐⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻
⡿⠂⢈⣿⣿⣿⣿⣿⣷⣦⣄⠉⠀⠛⠉⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⡿⠗⢀⣴
⣧⣄⡈⠙⢿⣿⣿⣿⣿⣿⣿⡟⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⣴⣿⣿
⣿⣿⣿⣆⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣠⣶⣿⣿⣿⣿
⣿⣿⣿⣿⣆⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣆⠈⠟⢀⣿⣿⣿⣿⣿⣿⡟⠀⣼⣧⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠇⢠⣿⣿⣿⣿⢿⣿⣿⠁⢸⣿⣿⡆⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⣁⣿⣿⣿⣿⣿⠀⠻⠋⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠀⣾⣿⣿⣿⣿⠀⢻⣿⡆⠘⣿⣿⡇⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢉⣠⣴⠀⣿⣿⣿⣿⣿⣿⡇⠀⠾⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⠀⡀⠻⣿⣦⡈⠛⠻⠷⠀⢿⣿⣿⣿⣿⣿⣿⡿⠛⠁⣠⣴⣿⣿⡇⢀⣿⣿⣿⣿⣿⣿⡇⢰⣶⣶⣦⣤⣤⣤⣤⣤⣈⠉⠉⢻⣿⣿
⣿⣿⣿⣿⣿⠁⢸⣿⣿⣿⣿⣿⠀⣷⣄⠙⠻⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⠟⠁⣠⣦⣰⣿⣿⣿⠟⢀⣾⣿⣿⣿⣿⣿⣿⣇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄⠉⢻⣿
⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⠀⢻⡟⢀⣤⡈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣶⣦⣀⡉⠙⠋⠉⣁⣴⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠇⢠⣴⣾⣿
⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣧⠀⠃⣸⣿⣿⣷⠂⣠⣈⡉⠛⠛⠿⠿⢿⣿⣿⣿⣿⣿⠿⠿⠛⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⣁⣤⣤⣄⣼⣿⣿⣿
⣿⣿⣿⣿⣿⠇⠸⣿⣿⣿⣿⣿⣿⣷⣄⠙⠿⣿⡏⢀⣿⣿⣿⣿⣶⣦⠀⣠⣤⣤⣤⡄⢀⣤⡔⠀⣼⣿⣿⣿⣿⣿⡟⠀⠿⠟⠋⢉⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⢀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣷⣄⡈⠁⠸⣿⣿⣿⣿⣿⡟⠀⣿⣿⣿⣿⠃⠸⠋⣠⣾⣿⣿⣿⣿⣿⣿⠃⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡏⢀⣿⣆⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⡉⠙⠛⠻⠃⠸⠿⠟⠛⠋⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⠃⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⢸⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣇⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠙⠻⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣄⠈⢿⣿⣿⣿⣧⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣄⠈⠛⢿⡿⠷⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⡀⠘⠑⠀⠀⠀⣦⣀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣾⣿⣿⣿⣿⣶⣤⠀⠈⠉⠉⠉⠉⢉⡉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠻⠃⢠⣿⣿⣄⠘⣿⡿⣵⣝⣫⡎⢿⢿⠟⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⡄⠸⣿⣿⣿⣿⣿⡿⠁⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠈⠛⠛⠋⢁⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

    diseno_5 = """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢻⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⢿⣿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣿⣮⡻⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠸⣿⣿⣿⣿⣿⣮⡻⠏⣶⣝⠿⣯⢿⡿⠿⣛⣯⣽⣶⣿⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡟⠿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣦⣿⣿⣷⣿⣷⣾⣿⣿⣿⣿⣿⠃⣾⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡋⠉⠁⠀⢠⣍⡛⠿⣿⣿⣿⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠠⠾⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⡿⣿
⣿⠗⠀⠀⠈⠻⣿⣷⣮⣝⣻⣤⣤⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⣡⣾
⣷⣶⣄⠀⠀⠀⠈⠻⣿⠛⠛⠛⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⢈⣽⣿⣿⣿⣿⡿⠿⠛⠉⠀⢀⣠⣾⣿⣿
⣿⣿⣿⣷⡀⠀⠀⠀⠘⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⣡⣾⠿⠛⠋⠁⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣹⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡹⣿⣿⡿⣿⣿⣿⣿⣿⣿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡷⠉⠉⠁⠀⠙⠛⣻⣿⣿⡟⠀⠀⠀⢀⣠⡄⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⢀⠀⠀⠈⠻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠾⠋⠀⢀⣠⣶⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣭⣭⣭⣛⣛⣛⣿⡿⠿⢿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣷⡄⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⢀⣤⣦⣼⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣈⠿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⢇⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠚⠛⠿⣿⣿⣿⣿⣿⣿⣿⠿⢳⣾⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠈⢿⢸⣿⣿⣿⢇⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣾⣿⠿⠟⢛⣩⣥⣶⣶⣾⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡿⣼⣿⣿⣿⣿⣿⡖⣶⣶⣶⣶⡄⣶⣶⠖⠀⠀⠀⠀⠀⠀⠀⠀⢈⣁⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠣⢿⣿⣿⣿⣿⣿⢧⣿⣿⣿⣿⠃⠟⠁⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠸⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⣰⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

    return [diseno_1, diseno_2, diseno_3, diseno_4, diseno_5]

def imprimir_diseno_centrado():
    diseno = random.choice(obtener_disenos_propios())
    try:
        columnas_totales = os.get_terminal_size().columns
    except OSError:
        columnas_totales = 120  
        
    lineas = diseno.splitlines()
    print(M_BRILLANTE, end="")
    for linea in lineas:
        if linea.strip():
            print(linea.rstrip())
    print(RESET, end="")

def imprimir_cabecera(titulo):
    print(f"\n{M_DEGRADADO}┌────────────────────────────────────────────────────────────────────────┐")
    print(f"  {CYAN}» {titulo.upper()}{M_DEGRADADO}")
    print(f"└────────────────────────────────────────────────────────────────────────┘{RESET}")

def imprimir_interfaz_inicio():
    limpiar_pantalla()
    
    try:
        ancho_terminal = os.get_terminal_size().columns
    except OSError:
        ancho_terminal = 80

    print(f"{GRIS}[{CYAN}*{GRIS}] INICIANDO GENGAR ENGINE v5.8...")
    time.sleep(0.4)
    
    servidores = [
        ("Core Engine Core Modules", "ONLINE"),
        ("OSINT API Mapping Target", "ONLINE"),
        ("Payload Database Matrix", "READY "),
        ("Leet Mutation Dictionary", "ONLINE"),
        ("Local Encryption Bypass", "ACTIVE")
    ]
    
    for modulo, estado in servidores:
        sys.stdout.write(f" {GRIS}➔ Checking {modulo.ljust(30)} ... [{VERDE}{estado}{GRIS}]\n")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print(f"\n{GRIS}Estableciendo conexión segura con sockets locales...")
    for i in range(1, 101, 5):
        barra = "█" * (i // 5) + " " * (20 - (i // 5))
        sys.stdout.write(f"\r [{M_BRILLANTE}{barra}{GRIS}] {i}% | Handshake Completo")
        sys.stdout.flush()
        time.sleep(0.04)
        
    time.sleep(0.3)
    limpiar_pantalla()

    imprimir_diseno_centrado()

    lineas_ascii = [
        "  ________ ______ _   _  _____       _______ ____   ____  _      ",
        " /  ______|  ____| \\ | |/ ____|     |__   __/ __ \\ / __ \\| |     ",
        "| |  __  | |__  |  \\| | |  __         | | | |  | | |  | | |     ",
        "| | |_ | |  __| | . ` | | |_ |        | | | |  | | |  | | |     ",
        "| |__| | | |____| |\\  | |__| |        | | | |__| | |__| | |____ ",
        " \\______| |______|_| \\_|\\_____|        |_|  \\____/ \\____/|______|"
    ]
    
    print(M_DEGRADADO)
    for linea in lineas_ascii:
        print(linea.rstrip())
        
    subtitulo = "        G E N G A R   S O C I A L   E N G I N E E R I N G   T O O L   v5.8"
    
    print(f"{GRIS}{subtitulo}{RESET}")
    print(f"{M_DEGRADADO}{'─' * min(ancho_terminal, 75)}{RESET}")

def aplicar_leet(palabra):
    tabla = {'e': '3', 'a': '4', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    return "".join(tabla.get(char, char) for char in palabra)

def generar_formatos_fecha(dia, mes, anio):
    formatos = set()
    if not dia or not mes: return formatos
    d_2d, m_2d = dia.zfill(2), mes.zfill(2)
    formatos.update([f"{d_2d}{m_2d}", f"{m_2d}{d_2d}", f"{dia}{mes}"])
    if anio:
        formatos.update([f"{d_2d}{m_2d}{anio}", f"{d_2d}{m_2d}{anio[-2:]}", f"{anio}{m_2d}{d_2d}"])
    return formatos

def pedir_nombre_archivo():
    print(f"\n{GRIS}┌──({CYAN}Configuración del Archivo de Salida{GRIS})")
    nombre = input(f"└─{M_BRILLANTE}»{RESET} Nombre del archivo .txt {GRIS}[Predeterminado: diccionario_gengar]:{RESET} ").strip()
    if not nombre: nombre = "diccionario_gengar"
    return nombre if nombre.endswith(".txt") else f"{nombre}.txt"

def limitar_volumen_payload(contrasenas):
    print(f"\n{GRIS}┌──({CYAN}Cuota de Generación Extrema{GRIS})")
    try:
        limite = input(f"└─{M_BRILLANTE}»{RESET} Límite numérico de contraseñas (100 - 1000000000) {GRIS}[100000]:{RESET} ").strip()
        limite = int(limite) if limite else 100000
        if limite < 100: limite = 100
    except ValueError:
        limite = 100000
    
    lista_pwd = list(contrasenas)
    if len(lista_pwd) > limite:
        random.shuffle(lista_pwd)
        return lista_pwd[:limite]
    return lista_pwd

def exportar_diccionario(contrasenas, nombre_archivo, largo_minimo=3):
    filtradas = {pwd for pwd in contrasenas if len(pwd) >= largo_minimo}
    lista_final = limitar_volumen_payload(filtradas)
    
    sys.stdout.write(f"\n{GRIS}[{CYAN}*{GRIS}] Volcando {len(lista_final)} vectores indexados en '{nombre_archivo}'...\n")
    sys.stdout.flush()
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            for pwd in sorted(lista_final):
                f.write(f"{pwd}\n")
        print(f"\n{VERDE}┌─── [ EXPORTACIÓN EXITOSA ] ─────────────────────────────────────────────┐")
        print(f"  {GRIS}Total de combinaciones en el payload: {CYAN}{len(lista_final)}")
        print(f"  {GRIS}Filtro de longitud aplicado:          {CYAN}>= {largo_minimo} caracteres")
        print(f"  {GRIS}Ubicación del archivo físico:        {M_BRILLANTE}./{nombre_archivo}")
        print(f"{VERDE}└────────────────────────────────────────────────────────────────────────┘{RESET}\n")
    except Exception as e:
        print(f"\n{ROJO}[-] Error crítico al escribir archivo: {e}{RESET}")

def robustecer_masivo(datos):
    resultados = set(datos)
    anios = [str(x) for x in range(1970, 2027)]
    secuencias = ["123", "1234", "12345", "123456", "01", "11", "22", "33", "123456789"]
    especiales = ["!", "@", "#", "$", "%", "?", "*", "_", "-"]
    
    variaciones = set()
    for d in datos:
        variaciones.update([d, d.capitalize(), d.upper()])
        
    v_list = list(variaciones)
    for v in v_list:
        for a in anios:
            resultados.update([f"{v}{a}", f"{a}{v}"])
        for s in secuencias:
            resultados.update([f"{v}{s}", f"{s}{v}"])
        for ce in especiales:
            resultados.update([f"{v}{ce}", f"{ce}{v}"])
            for item_a in ["2024", "2025", "2026"]:
                resultados.add(f"{v}{item_a}{ce}")

    if len(v_list) > 1:
        for p1, p2 in itertools.permutations(v_list, 2):
            if len(p1) + len(p2) < 25:
                resultados.update([f"{p1}{p2}", f"{p1}_{p2}"])
    return resultados

def ejecutar_cuestionario_dinamico(banco, num_min, num_max, titulo):
    imprimir_cabecera(titulo)
    try:
        num_preguntas = int(input(f" {CYAN}»{RESET} ¿Cuántas preguntas deseas responder? ({num_min}-{num_max}) {GRIS}[{num_min}]:{RESET} "))
        if num_preguntas < num_min or num_preguntas > num_max: num_preguntas = num_min
    except ValueError:
        num_preguntas = num_min

    try:
        largo_minimo = int(input(f" {CYAN}»{RESET} Longitud mínima del vector de salida {GRIS}[8]:{RESET} "))
    except ValueError:
        largo_minimo = 8

    print(f"\n{GRIS}[*] Use 's' o presione ENTER para omitir la variable en el diccionario.{RESET}\n")
    datos_recolectados = set()
    preguntas_respondidas = 0
    indice_banco = 0

    while preguntas_respondidas < num_preguntas and indice_banco < len(banco):
        pregunta, ejemplo = banco[indice_banco]
        respuesta = input(f"  {GRIS}➔ [{preguntas_respondidas + 1}/{num_preguntas}] {pregunta} {CYAN}({ejemplo}){GRIS}:{RESET} ").strip()
        
        if respuesta.lower() == 's' or not respuesta:
            print(f"      {GRIS}└─» Variable omitida.{RESET}\n")
            indice_banco += 1
            continue
            
        datos_recolectados.add(respuesta.lower())
        preguntas_respondidas += 1
        indice_banco += 1

    print(f"\n{M_DEGRADADO}┌──({CYAN}Inyección Cronológica Target{M_DEGRADADO})")
    tipo_fecha = input(f"│ {GRIS}¿Deseas ingresar fecha completa (F) o solo el año (A)? [F]:{RESET} ").strip().upper()
    
    if tipo_fecha == "A":
        anio_input = input(f"└─{CYAN}➔{RESET} Introduce solo el año {CYAN}(AAAA):{RESET} ").strip()
        if anio_input: datos_recolectados.add(anio_input)
    else:
        fecha_input = input(f"└─{CYAN}➔{RESET} Introduce la fecha del objetivo {CYAN}(DD/MM/AAAA):{RESET} ").strip()
        for sep in ["/", "-", "."]:
            if sep in fecha_input:
                partes = fecha_input.split(sep)
                if len(partes) == 3:
                    datos_recolectados.add(partes[2])
                    datos_recolectados.update(generar_formatos_fecha(partes[0], partes[1], partes[2]))
                    break

    contrasenas = robustecer_masivo(datos_recolectados)
    exportar_diccionario(contrasenas, pedir_nombre_archivo(), largo_minimo)

def main():
    banco_total = [
        ("Nombre del objetivo principal", "Ej: carlos"), ("Primer apellido del objetivo", "Ej: mendoza"),
        ("Nombre de su madre", "Ej: maria"), ("Nombre de su padre", "Ej: jorge"),
        ("Nombre de su pareja o ex", "Ej: andrea"), ("Nombre de su mascota principal", "Ej: toby"),
        ("Ciudad de residencia actual", "Ej: madrid"), ("Marca de su coche favorito", "Ej: toyota"),
        ("Club deportivo o fútbol", "Ej: barca"), ("Apodo o pseudónimo común", "Ej: charlie"),
        ("Segundo apellido", "Ej: ruiz"), ("Nombre de su hijo/a mayor", "Ej: kevin"),
        ("Nombre de su hermano/a", "Ej: sofia"), ("Universidad o escuela", "Ej: unam"),
        ("Profesión u ocupación", "Ej: ingeniero"), ("Empresa de trabajo actual", "Ej: indra"),
        ("Nombre de su jefe o supervisor", "Ej: ramon"), ("Hobby o pasatiempo", "Ej: gaming"),
        ("Comida o plato favorito", "Ej: pizza"), ("Red social favorita", "Ej: instagram"),
        ("Color preferido", "Ej: azul"), ("Nombre de su comunidad/barrio", "Ej: norte"),
        ("Nombre de su primer novio/a", "Ej: lucia"), ("Marca de su teléfono", "Ej: iphone"),
        ("Grupo musical o cantante", "Ej: coldplay"), ("Película o serie favorita", "Ej: batman"),
        ("Nombre de su segundo hijo/a", "Ej: valeria"), ("Destino de viaje soñado", "Ej: japon"),
        ("Segundo nombre del objetivo", "Ej: alberto"), ("Nombre de su abuelo/a", "Ej: manuel"),
        ("Mes de aniversario", "Ej: octubre"), ("Número de la suerte", "Ej: 7"),
        ("Animal favorito", "Ej: lobo"), ("Bebida favorita", "Ej: cafe"), ("Año de graduación", "Ej: 2018")
    ]

    while True:
        imprimir_interfaz_inicio()
        print(f" {M_BRILLANTE}[01]{RESET} Perfilado OSINT Esencial     {GRIS}(Rápido: 5-10 preguntas){RESET}")
        print(f" {M_BRILLANTE}[02]{RESET} Perfilado OSINT Intermedio   {GRIS}(Estándar: 10-20 preguntas){RESET}")
        print(f" {M_BRILLANTE}[03]{RESET} Perfilado OSINT Avanzado     {GRIS}(Exhaustivo: 20-30 preguntas){RESET}")
        print(f" {M_BRILLANTE}[04]{RESET} Cuestionario Estructurado    {GRIS}(Inyección dinámica manual){RESET}")
        print(f" {M_BRILLANTE}[05]{RESET} Patrones de Diccionario Global{GRIS}(Basado en comportamientos raíz){RESET}")
        print(f" {M_BRILLANTE}[06]{RESET} Matrices de Entorno (Target)  {GRIS}(Fusión Corporativa / Personal){RESET}")
        print(f" {M_BRILLANTE}[07]{RESET} Secuenciadores Numéricos Puros{GRIS}(Rangos y líneas temporales){RESET}")
        print(f" {M_BRILLANTE}[08]{RESET} Vectores Alfanuméricos Complejos{GRIS}(Estructuras semilla + símbolos){RESET}")
        print(f" {M_BRILLANTE}[09]{RESET} Algoritmos de Mutación Inversa {GRIS}(Menú alternativo de transformaciones){RESET}")
        print(f" {M_BRILLANTE}[10]{RESET} Terminar Operación")
        print(f"{M_DEGRADADO}───────────────────────────────────────────────────────────────────────────{RESET}")
        
        try:
            opcion = int(input(f"{CYAN}gengar-cli{GRIS}@{RESET}shell:~# "))
        except ValueError: 
            continue

        if opcion == 1:
            ejecutar_cuestionario_dinamico(banco_total, 5, 10, "Perfilado OSINT Esencial")
        elif opcion == 2:
            ejecutar_cuestionario_dinamico(banco_total, 10, 20, "Perfilado OSINT Intermedio")
        elif opcion == 3:
            ejecutar_cuestionario_dinamico(banco_total, 20, 30, "Perfilado OSINT Avanzado")
        elif opcion == 4:
            imprimir_cabecera("Cuestionario Personalizado Estructurado")
            print(f"{GRIS}[*] Ingrese sus propios vectores personalizados.")
            print(f"    Escribre {ROJO}'YA'{GRIS} en el campo de pregunta para detener la captura y compilar.\n")
            
            datos_recolectados = set()
            contador = 1
            
            while True:
                pregunta_custom = input(f"  {M_BRILLANTE}┌──({CYAN}Pregunta Personalizada #{contador}{M_BRILLANTE}){RESET}\n  {GRIS}└─» Enunciado o descriptor:{RESET} ").strip()
                if pregunta_custom.upper() == 'YA': break
                if not pregunta_custom: continue
                    
                respuesta_custom = input(f"      {VERDE}└── Valor / Respuesta:{RESET} ").strip()
                if respuesta_custom:
                    datos_recolectados.add(respuesta_custom.lower())
                    contador += 1

            if datos_recolectados:
                try:
                    largo_minimo = int(input(f"\n {CYAN}»{RESET} Longitud mínima de caracteres [8]: "))
                except ValueError:
                    largo_minimo = 8
                contrasenas = robustecer_masivo(datos_recolectados)
                exportar_diccionario(contrasenas, pedir_nombre_archivo(), largo_minimo)

        elif opcion == 5:
            imprimir_cabecera("Patrones de Diccionario Global")
            palabra = input(f" {GRIS}➔ Palabra Clave Base (Root Word) [administrador]: {RESET}").strip().lower()
            if palabra:
                contrasenas = {f"{palabra.capitalize()}123", f"{palabra.capitalize()}2025", f"{palabra.capitalize()}2026", 
                               f"123456{palabra}", f"{palabra}!", f"{palabra.upper()}123!", f"{palabra.capitalize()}123*"}
                exportar_diccionario(contrasenas, pedir_nombre_archivo())

        elif opcion == 6:
            imprimir_cabecera("Matrices de Entorno Específicas")
            nombre = input(f" {GRIS}➔ Nombre o Identificador del Target [fernando]: {RESET}").strip().capitalize()
            empresa = input(f" {GRIS}➔ Nombre de Entidad o Entorno [movistar]: {RESET}").strip().capitalize()
            if nombre or empresa:
                contrasenas = {f"{nombre}{empresa}2026", f"{empresa}_{nombre}", f"{nombre}*2026", f"Admin.{empresa}"}
                exportar_diccionario(contrasenas, pedir_nombre_archivo())

        elif opcion == 7:
            imprimir_cabecera("Secuenciadores Numéricos Puros")
            try:
                inicio = int(input(f" {GRIS}➔ Punto de Inicio del Rango [1990]: {RESET}"))
                fin = int(input(f" {GRIS}➔ Punto de Cierre del Rango [2026]: {RESET}"))
            except ValueError: 
                inicio, fin = 2000, 2026
            contrasenas = {str(x) for x in range(inicio, fin + 1)}
            exportar_diccionario(contrasenas, pedir_nombre_archivo())

        elif opcion == 8:
            imprimir_cabecera("Vectores Alfanuméricos Complejos")
            base = input(f" {GRIS}➔ Palabra Semilla para Robustecer [gautama]: {RESET}").strip()
            if base:
                simbolos = ["!", "@", "#", "$", "%", "*"]
                contrasenas = set()
                for s in simbolos:
                    contrasenas.update([f"{base.capitalize()}123{s}", f"{s}{base.upper()}2026"])
                exportar_diccionario(contrasenas, pedir_nombre_archivo())

        elif opcion == 9:
            while True:
                limpiar_pantalla()
                imprimir_cabecera("Algoritmos de Mutación Inversa")
                print(f" {M_BRILLANTE}[1]{RESET} Transformación Compleja [Leet Avanzado]        {GRIS}(p455w0rd){RESET}")
                print(f" {M_BRILLANTE}[2]{RESET} Inversión de Vectores [Reverse Mirror]       {GRIS}(nimda){RESET}")
                print(f" {M_BRILLANTE}[3]{RESET} Hibridación Completa [Leet + Espejo]          {GRIS}(nd1mb4){RESET}")
                print(f" {M_BRILLANTE}[4]{RESET} Alternancia de Case [Upper/Lower Mix]        {GRIS}(RoOt){RESET}")
                print(f" {M_BRILLANTE}[5]{RESET} Bloques Duplicados en Espejo [Mirror Pad]    {GRIS}(tokiooikot){RESET}")
                print(f" {M_BRILLANTE}[00]{RESET} Regresar al Menú Principal")
                print(f"{M_DEGRADADO}───────────────────────────────────────────────────────────────────────────{RESET}")
                
                sub_opc = input(f"{CYAN}gengar-mutations{GRIS}@{RESET}shell:~# ").strip()
                if sub_opc in ["00", "0"]: break
                if sub_opc not in ["1", "2", "3", "4", "5"]: continue

                palabra = input(f"\n {GRIS}➔ Ingrese la palabra bajo análisis: {RESET}").strip()
                if not palabra: continue

                contrasenas = set()
                if sub_opc == "1":
                    contrasenas.update([aplicar_leet(palabra), aplicar_leet(palabra).upper()])
                elif sub_opc == "2":
                    contrasenas.update([palabra[::-1], palabra.capitalize()[::-1]])
                elif sub_opc == "3":
                    leet = aplicar_leet(palabra)
                    contrasenas.update([leet[::-1], palabra[::-1].upper()])
                elif sub_opc == "4":
                    contrasenas.update([
                        "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(palabra)),
                        "".join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(palabra))
                    ])
                elif sub_opc == "5":
                    contrasenas.add(f"{palabra}{palabra[::-1]}")
                    
                exportar_diccionario(contrasenas, pedir_nombre_archivo(), largo_minimo=1)
                input(f"\n{GRIS}Presione ENTER para continuar...{RESET}")

        elif opcion == 10:
            print(f"\n{VERDE}[*] Operación finalizada correctamente. Entorno cerrado.{RESET}\n")
            break

if __name__ == "__main__":
    main()