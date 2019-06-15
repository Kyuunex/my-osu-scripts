import os 
import shutil 
import configparser
# made by Kyuunex
# licensed under GPL3

source_directory = "D:/osu!/Songs/" # use / slashes and make these end with slash
target_directory = "D:/output/"

def get_background(file_path):
    try:
        if os.path.isfile(file_path):
            with open(file_path) as g:
                data = g.read()
                buffer = data.replace(" ", "_")
            config = configparser.ConfigParser(comment_prefixes=("//", "osu", "\ufeffosu", "_"), allow_no_value=True, strict=False)
            config.read_string(buffer)

            for event in config['Events']:
                line_csv = event.split(',')
                if line_csv[0] == "0" and line_csv[1] == "0":
                    return line_csv[2].strip('"')
        else:
            return None
    except Exception as e:
        print(e)
        print(file_path)
        return None

list_of_all_mapsets = os.listdir(source_directory)
for mapset_folder in list_of_all_mapsets:
    if (not mapset_folder == ".") or (not mapset_folder == ".."):

        mapset_folder_full_path = source_directory + mapset_folder + "/"

        if os.path.isdir(mapset_folder_full_path):
            list_of_files_in_current_mapset = os.listdir(mapset_folder_full_path)
            
            target_directory_mapset = target_directory + mapset_folder + "/"

            if not os.path.isdir(target_directory_mapset):
                os.mkdir(target_directory_mapset)
        
            for one_file in list_of_files_in_current_mapset:
                if (not one_file == ".") or (not one_file == ".."):
                    if one_file.lower().endswith(".osu"):
                        background_filename = get_background(mapset_folder_full_path + one_file)
                        if background_filename:
                            background_full_path = mapset_folder_full_path + background_filename.replace('\\', '/')
                            target_full_path = target_directory_mapset + background_filename.replace('\\', '/')

                            target_full_path_folder_list = (target_full_path.split("/"))
                            del target_full_path_folder_list[-1]
                            target_full_path_folder = "/".join(target_full_path_folder_list)

                            if not os.path.isdir(target_full_path_folder):
                                os.makedirs(target_full_path_folder)
                            if not os.path.isfile(target_full_path_folder):
                                if os.path.isfile(background_full_path):
                                    try:
                                        shutil.move(background_full_path, target_full_path)#
                                    except Exception as e:
                                        print("Errored: " + background_full_path + "\n")
                                        print(e)
                                    #print("Moved: " + background_full_path + "\n")
                    if one_file.lower().endswith(('.osu', '.mp3', '.ogg')):
                        try:
                            shutil.move(mapset_folder_full_path + one_file, target_directory_mapset + one_file)#
                        except Exception as e:
                            print("Errored: " + mapset_folder_full_path + one_file + "\n")
                            print(e)
                        #print("Moved: " + mapset_folder_full_path + one_file + "\n")


print("I am done owo")