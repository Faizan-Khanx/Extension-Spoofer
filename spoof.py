import webbrowser
import readline
import os
import shutil
import requests
from zipfile import ZipFile
from io import BytesIO
import tempfile
from extspoof import *

wow = Secrets


# Banner
def display_banner():
    banner = """
    \033[1;36m
============================================================================
,--. .   , ,---. ,--. .  .  ,-.  ,  ,-.  .  .    ,-.  ;-.   ,-.   ,-.  ,--. 
|     \ /    |   |    |\ | (   ` | /   \ |\ |   (   ` |  ) /   \ /   \ |    
|-     X     |   |-   | \|  `-.  | |   | | \|    `-.  |-'  |   | |   | |-   
|     / \    |   |    |  | .   ) | \   / |  |   .   ) |    \   / \   / |    
`--' '   `   '   `--' '  '  `-'  '  `-'  '  '    `-'  '     `-'   `-'  '    
============================================================================
                         MADE BY FAIZAN KHAN
          INSTAGRAM ==> EthicalFaizan GITHUB ==> Faizan-Khanx
============================================================================
    \033[1;97m
    """
    print(banner)


# file to jpg func
def file_to_jpg(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}gpj{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file saved \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


# file to pdf func
def file_to_pdf(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}fdp{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file saved \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


# file to txt func
def file_to_txt(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}txt{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file saved \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


# file to docx func
def file_to_docx(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}xcod{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file saved \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


# file to mp4 func
def file_to_mp4(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}4pm{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file saved \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


# file to gif func
def file_to_gif(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}fig{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name,'++wb') as new_file:
                new_file.write(original_file.read())

        print(f"file saved \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


# file to mp3 func
def file_to_mp3(input_path):
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}3pm{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file saved \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


# special extension spoofing
def special_spoofing(input_path, ext):
    rev_ext = ext[::-1]
    if not os.path.isfile(input_path):
        print("no file there")
        return

    file_name, file_extension = os.path.splitext(input_path)
    new_file_name = f"{file_name}{wow}{rev_ext}{file_extension}"

    try:
        with open(input_path, 'rb') as original_file:
            with open(new_file_name, 'wb') as new_file:
                new_file.write(original_file.read())

        print(f"file saved \033[1;32msuccessfully\033[1;97m")
    except Exception as e:
        print(f"err: {e}")


def main():
    display_banner()
    print("\n\033[1;35m-:\033[1;97mChoose an option\033[1;35m:-\033[1;97m")
    choices = """
    [1] ==> Convert file to JPG
    [2] ==> Convert file to PDF
    [3] ==> Convert file to TXT
    [4] ==> Convert file to DPCX
    [5] ==> Convert file to MP4
    [6] ==> Convert file to GIF
    [7] ==> Convert file to MP3
    [8] ==> Developer Instagram
    [9] ==> Developer Github
    [0] ==> Exit
    """
    print(choices)
    while True:
        try:
            user_choice = input("\033[1;35m>>\033[1;97m ")
            if user_choice == '1':
                file_path = input("Enter File Path To Convert Into JPG: ")
                file_to_jpg(file_path)
                break

            elif user_choice == '2':
                file_path = input("Enter File Path To Convert Into PDF: ")
                file_to_pdf(file_path)
                break

            elif user_choice == '3':
                file_path = input("Enter File Path To Convert Into TXT: ")
                file_to_txt(file_path)
                break

            elif user_choice == '4':
                file_path = input("Enter File Path To Convert Into DOCX: ")
                file_to_docx(file_path)
                break

            elif user_choice == '5':
                file_path = input("Enter File Path To Convert Into MP4: ")
                file_to_mp4(file_path)
                break

            elif user_choice == '6':
                file_path = input("Enter File Path To Convert Into GIF: ")
                file_to_gif(file_path)
                break
            
            elif user_choice == '7':
                file_path = input("Enter File Path To Convert Into MP3: ")
                file_to_mp3(file_path)
                break

            elif user_choice == '8':
                 webbrowser.open("https://instagram.com/Ethicalfaizan")
                 break
                 
            elif user_choice == '9':
                 webbrowser.open("https://github.com/faizan-khanx")
                 break

                
            elif user_choice == '0':
                exit()

            else:
                print("please Enter a valid choice")
        except KeyboardInterrupt:
            print("\nEnter '0' to exit")
            pass


if __name__ == '__main__':
    main()
