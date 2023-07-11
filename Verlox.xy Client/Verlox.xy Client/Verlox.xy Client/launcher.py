# importing all modules
import os
from concurrent.futures import ThreadPoolExecutor
from selfnuker import start_self_nuker
from botnuker import start_bot
from webhook import webhook_start
from accountnuker import start_account_nuker

import discord
import configparser
import asyncio
from pystyle import Center, Colorate, Colors

# pull config
config = configparser.ConfigParser()
config.read('config.txt')

# pull variables
prefix = variable_value = config.get('config', 'prefix')

# credits menu
def credits_menu():
    os.system('cls')
    print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""
██╗   ██╗███████╗██████╗ ██╗      ██████╗ ██╗  ██╗   ██╗  ██╗██╗   ██╗
██║   ██║██╔════╝██╔══██╗██║     ██╔═══██╗╚██╗██╔╝   ╚██╗██╔╝╚██╗ ██╔╝
██║   ██║█████╗  ██████╔╝██║     ██║   ██║ ╚███╔╝     ╚███╔╝  ╚████╔╝ 
╚██╗ ██╔╝██╔══╝  ██╔══██╗██║     ██║   ██║ ██╔██╗     ██╔██╗   ╚██╔╝  
 ╚████╔╝ ███████╗██║  ██║███████╗╚██████╔╝██╔╝ ██╗██╗██╔╝ ██╗   ██║   
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                      
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""[ Credits Menu ]
------------------------------------------------------------

x,.-> Discord - https://discord.gg/9pcMSZkyuy
x,.-> Youtube - https://www.youtube.com/channel/UCrV5fk7eClk9RMARy12ObXQ

-> Developers - Verlox.xy#2735
-> Testers - Verlox.xy#2735, AkaneKatsu#4245
-> Indian Scammer - TMJoe_02468#2482

x,.-> Press enter to go back to main menu !!

------------------------------------------------------------
        """,
                1,
            )
        )
    )
    input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    starting_menu()

# server nuker menu
def server_nuker_menu():
    os.system('cls')
    print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""
██╗   ██╗███████╗██████╗ ██╗      ██████╗ ██╗  ██╗   ██╗  ██╗██╗   ██╗
██║   ██║██╔════╝██╔══██╗██║     ██╔═══██╗╚██╗██╔╝   ╚██╗██╔╝╚██╗ ██╔╝
██║   ██║█████╗  ██████╔╝██║     ██║   ██║ ╚███╔╝     ╚███╔╝  ╚████╔╝ 
╚██╗ ██╔╝██╔══╝  ██╔══██╗██║     ██║   ██║ ██╔██╗     ██╔██╗   ╚██╔╝  
 ╚████╔╝ ███████╗██║  ██║███████╗╚██████╔╝██╔╝ ██╗██╗██╔╝ ██╗   ██║   
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                      
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""x,.-> Verlox.xy CLient
x,.-> made by Verlox.xy#2735

Prefix - "{prefix}"
Discord - https://discord.gg/9pcMSZkyuy
Note - Thanks for using my program
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""[ Server Nuker 0ptions / Select a 0ption ]
------------------------------------------------------------
x,.-> Choose if you are either using a bot to nuke or an account ( self nuker )

-> 1 - Bot
-> 2 - Account
-> 3 - Back to Main Menu

------------------------------------------------------------
        """,
                1,
            )
        )
    )
    def choice1():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue,'x,.-> '))
        if choice == '3':
            starting_menu()
        elif choice == '1':
            start_bot()
        elif choice == '2':
            start_self_nuker()
        else:
            server_nuker_menu()
    choice1()

# starting menu
def starting_menu():
    os.system('cls')
    print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""
██╗   ██╗███████╗██████╗ ██╗      ██████╗ ██╗  ██╗   ██╗  ██╗██╗   ██╗
██║   ██║██╔════╝██╔══██╗██║     ██╔═══██╗╚██╗██╔╝   ╚██╗██╔╝╚██╗ ██╔╝
██║   ██║█████╗  ██████╔╝██║     ██║   ██║ ╚███╔╝     ╚███╔╝  ╚████╔╝ 
╚██╗ ██╔╝██╔══╝  ██╔══██╗██║     ██║   ██║ ██╔██╗     ██╔██╗   ╚██╔╝  
 ╚████╔╝ ███████╗██║  ██║███████╗╚██████╔╝██╔╝ ██╗██╗██╔╝ ██╗   ██║   
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                      
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""x,.-> Verlox.xy CLient
x,.-> made by Verlox.xy#2735

Prefix - "{prefix}"
Discord - https://discord.gg/9pcMSZkyuy
Note - Thanks for using my program
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""[ Menu List / Select a 0ption ]
------------------------------------------------------------

-> 0 - Credits Menu
-> 1 - Server Nuker 0ptions
-> 2 - Account Nuker 0ptions
-> 3 - Webhook 0ptions

------------------------------------------------------------
        """,
                1,
            )
        )
    )
    def choice2():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '0':
            credits_menu()
        if choice == '1':
            server_nuker_menu()
        if choice == '2':
            start_account_nuker()
        if choice == '3':
            webhook_start()
        else:
            starting_menu()
    choice2()


starting_menu()
