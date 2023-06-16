#!/usr/bin/env python3
import vk_api, pyfiglet, random
from colorama import Fore
from datetime import date
from getpass import getpass
from platform import system as pls
from os import system as osexec
from time import sleep
from threading import Thread

def windynamic():
    for i in ['Vk revenge', 'vK revenge', 'vk Revenge', 'vk rEvenge', 'vk reVenge', 'vk revEnge', 'vk reveNge', 'vk revenGe', 'vk revengE']:
        sleep(0.2)
        osexec('title '+i)
    windynamic()

if pls() == 'Windows':
    Thread(target=windynamic).start()

year=date.today().year

ascii_art = pyfiglet.figlet_format('VK Revenge')

print(Fore.BLUE+ascii_art+Fore.RESET)
print(f'Social Engineering Phone Storm {year}\n')

blogers=['Ивана Золо', 'Димы Масленникова', 'Некоглая', 'Дудя', 'Путина', 'Влада Бумаги'] # В Родительном падеже

message="{}\nВ сеть слили номер {}! Новая база данных {} слита ОСТАЛЬНЫЕ ФЕЙКИ! Звоните пока не сменили номер :)"

vklogin=input(Fore.YELLOW + 'Enter your phone number (VK): ' + Fore.RESET)
vkpassword=getpass(Fore.YELLOW + 'Enter your password (VK): ' + Fore.RESET)

def two_factor():
    code = input(Fore.CYAN+'[2FA] Enter code from your device: '+Fore.RESET)
    return code

try:
    vk_session = vk_api.VkApi(vklogin, vkpassword, app_id=2685278, auth_handler=two_factor)
    vk_session.auth()
    vk = vk_session.get_api()
    print(Fore.GREEN + '[+] Successfully autrorized!' + Fore.RESET)
except Exception as E1:
    print(Fore.RED + '[-] Error: ' + str(E1) + Fore.RESET)
    input('Press any key to exit...'); exit()
    
filename=input(Fore.YELLOW + 'Enter groups ID filename / path: ' + Fore.RESET)

def spam(ids):
    for group_id in ids:
        try:
            bloger=random.choice(blogers)
            vk.wall.post(owner_id='-' + group_id, message=message.format(enemy_phone, bloger, year))
            print(Fore.GREEN + f'[+] Posted in @club{group_id} - bloger line: "{bloger}"' + Fore.RESET)
        except Exception as E3:
            print(Fore.RED + '[-] Error with spam in {}: '.format(group_id) + str(E3) + Fore.RESET)

try:
    ids=open(filename, 'r', encoding='utf-8').readlines()
except Exception as E2:
    print(Fore.RED + '[-] Error: ' + str(E2) + Fore.RESET)
    input('Press any key to exit...'); exit()

enemy_phone=input(Fore.YELLOW + "☢ ️Enter your enemie's phone number: " + Fore.RESET)
spam(ids)
print(Fore.BLUE + 'End of program - total: {}'.format(str(len(ids))) + Fore.RESET)
input('Press any key to exit...')
