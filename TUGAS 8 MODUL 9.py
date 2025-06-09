import os
import time
from termcolor import cprint, colored

def clear_screen():
    os.system('cls')

def loading_animation():
    for i in range(15):
        clear_screen()
        print_capcut_icon()
        dots = '.'*(i%4)
        cprint(f"\nMemuat Aplikasi CapCut{dots}", "cyan", attrs=["bold"])
        time.sleep(0.5)

def print_capcut_icon():
    capcut_logo ="""
╭────────────────────────────────────────────╮
│ █████████                         █████████│
│ █      ███                     ███        █│
│ █        ███                 ███          █│
│ █          ███             ███            █│
│ █            ███         ███              █│
│ █              ███     ███                █│
│ █                ███████                  █│
│ █              ███     ███                █│
│ █            ███         ███              █│
│ █          ███             ███            █│
│ █        ███                 ███          █│
│ █      ███                     ███        █│
│ █████████                         █████████│
╰────────────────────────────────────────────╯
"""
    cprint(capcut_logo, "white", "on_black", attrs=["bold"])

def show_loading_screen():
    clear_screen()
    print_capcut_icon()
    cprint("\n   Selamat Datang di CapCut Terminal Edition!", "yellow", attrs=["bold"])
    time.sleep(3)
    loading_animation()
    clear_screen()
    print_capcut_icon()
    cprint("\n✅ Aplikasi CapCut siap digunakan!", "green", attrs=["bold"])

# Jalankan
show_loading_screen()