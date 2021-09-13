import pymem
import pymem.process
import time
import win32api
import win32gui
import win32process
import ctypes
readprocmem =  ctypes.windll.kernel32.ReadProcessMemory
hWnd = win32gui.FindWindow(0, ("Among Us"))
if(hWnd):
    pid=win32process.GetWindowThreadProcessId(hWnd)
    handle = pymem.Pymem()
    handle.open_process_from_id(pid[1])
    csgo_entry = handle.process_base
else:
    print("Not Found!")
list_of_modules=handle.list_modules()
while(list_of_modules!=None):
    tmp=next(list_of_modules)
    print(tmp.name)
    if(tmp.name=="GameAssembly.dll"):
        client_dll=tmp.lpBaseOfDll
        break

#pm = pymem.Pymem("Among Us.exe")
#dll = get_base_adress(pm)
#client = pymem.process.module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll
while True:
    #print(pymem.process.base_adress(client))
    """print("crewmate",pm.read_int(client+0x00DA5A84+0x28),pm.read_bytes(client+0x00DA5A84+0x28,1))
    print("impostor",pm.read_int(client+0x00DA5A84+0x29),pm.read_bytes(client+0x00DA5A84+0x29,1))
    print("visual tasks",pm.read_int(client+0x00DA5A84+0x5C))"""
    print("crewmate",handle.read_int(client_dll+0xDA5A84+0x28),handle.read_bytes(client_dll+0xDA5A84+0x28,1))
    print("impostor",handle.read_int(client_dll+0xDA5A84+0x29),handle.read_bytes(client_dll+0xDA5A84+0x29,1))
    print("kill",handle.read_int(client_dll+0xDA5A84+0x20+0x4+0x5C),handle.read_bytes(client_dll+0xDA5A84+0x20,1))
    print(readprocmem(pid[1],client_dll,))

    time.sleep(3)