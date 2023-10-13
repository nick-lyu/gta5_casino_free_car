from pywinauto import keyboard
from pywinauto import findwindows
from pywinauto import win32_hooks
from pywinauto.application import Application
from subprocess import Popen
from pywinauto import Desktop
import time

from theeye import action_on_screen_event, win_func


def calc_test():
    Popen('calc.exe', shell=True)
    dlg = Desktop(backend="uia").Calculator
    dlg.wait('visible')


def keypress_after_keypressed():
    print("START")
    process_id_gta = 6348
    process_id_notepad = 10132

    for i in range(5):
        print(i)
        time.sleep(1)
    print("GO!!!")
    app = Application().connect(process=process_id_gta)
    # print(app)
    # dlg = app.top_window()
    # dlg.wait('visible')
    dlg = app['grcWindow']

    def on_event(args):
        if isinstance(args, win32_hooks.KeyboardEvent):
            if args.current_key == 'E' and args.event_type == 'key down':
                print('OK lets DO IT!')
                time.sleep(7.4)      # 3.4 + 7
                keyboard.send_keys('{s down}', 0.3, vk_packet=True)
                keyboard.send_keys('{s up}', vk_packet=True)
                print('Done!')
    my_hook = win32_hooks.Hook()
    my_hook.handler = on_event
    my_hook.hook()


# Simple test keyboard listening on key pressed
def test_hook():
    def on_event(args):
        if isinstance(args, win32_hooks.KeyboardEvent):
            if args.current_key == 'O' and args.event_type == 'key down':
                print('"O" was pressed.')
    my_hook = win32_hooks.Hook()
    my_hook.handler = on_event
    my_hook.hook()


# Print info about opened app windows
def info():
    # app = Application().connect(process=10132)
    # dlg = app['Notepad']
    print('ELEMENTS:')
    e = findwindows.find_elements()
    print(*e, sep='\n')
    print(len(e))
    print('WINDOWS:')
    w = findwindows.find_windows()
    print(*w, sep='\n')
    print(len(w))
    # print(app.windows())
    # print(dlg)
    # print(*app.dlg.print_control_identifiers(), sep='\n')


# симулирует нажатие клавиши по таймеру
def sending_key(delay):
    # не докрутил: 3.95 (1), 3.92 (3) 3.89
    # перекрутил: 3.85, 3.7, 3.83
    time.sleep(delay)
    keyboard.send_keys('{s down}', 0.3, vk_packet=True)
    keyboard.send_keys('{s up}', vk_packet=True)


if __name__ == '__main__':
    print("Input delay in sec(float):")
    w8time = float(input())
    action_on_screen_event(sending_key, w8time)
