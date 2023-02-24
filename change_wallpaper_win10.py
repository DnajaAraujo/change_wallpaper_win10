import ctypes
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

img_paths = [
    f"{dir_path}/park_autumn_trees.jpg", 
    f"{dir_path}/abstract_art_blue_waves.jpg", 
    f"{dir_path}/leaves_drops.jpg"]


def main():
    change_wallpaper()
    

def write_current_wallpaper(value_img):
    archive = open('current_wallpaper.txt', 'w')
    archive.write(value_img)
    archive.close()


def get_current_wallpaper():
    try: 
        archive = open('current_wallpaper.txt', 'r')
        current_wallpaper = archive.read()
        archive.close()
    except:
        write_current_wallpaper('')
        get_current_wallpaper()

    return current_wallpaper
    

def change_wallpaper():
    value_img = get_current_wallpaper()
    new_value_img = 0
    
    if value_img == '0':
        new_value_img = 1

    elif value_img == '1':
        new_value_img = 2

    elif value_img == '2':
        new_value_img = 0

    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_paths[new_value_img], 0)

    write_current_wallpaper(str(new_value_img))



main()
