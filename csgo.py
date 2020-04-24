import pymem
import pymem.process
dwEntityList = 81017524
dwGlowObjectManager = 86554752
m_iGlowIndex = 42024
m_iTeamNum = 244
def main():
    print("injected")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll

    while True:
        glow_manager = pm.read_int(client + dwGlowObjectManager)

        for i in range(1, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                if entity_team_id == 2:
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)

                elif entity_team_id == 3:
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)


if __name__ == '__main__':
    main()