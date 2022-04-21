import sys, os, shutil
from datetime import date
version = 1.0

def safe_err(err):
    if err == 1:
        print("[FATAL] Folder does not exist!")
        exit(1)
    elif err == 2:
        print("[FATAL] An unexpected error occured.")
        exit(1)
    #elif err == 3:
    #    print("[INTERRUPT] Improper compilation type!")
    elif err == 4:
        print("[DEBUG FATAL] Feature not implemented!")
        exit(0) #exit code 0 because were in debug
    else:
        print("[FATAL] An unexpected error occured.")
        exit(1)

def main():
    print(f"NVC {version}. Since 4/20/22.")
    try:
        file = sys.argv[1]
    except:
        safe_err(1)
    dir = os.getcwd() + "/" + file
    if os.path.isdir(dir) == True:
        x = "we good"
    elif os.path.isdir(dir) == False:
        safe_err(1)
    else:
        safe_err(2)

    # passed all beginning checks, check if there is a thingy
    if len(sys.argv) == 3:
        if sys.argv[2] == "zip":
            ztype = "zip"
        elif sys.argv[2] == "7z":
            ztype = "7z"
        elif sys.argv[2] == "tar":
            ztype = "tar"
        else:
            ztype = "zip"
            #safe_err(3)
    else:
        #doesnt exist, so assume zip
        ztype = "zip"

    #passed all final checks, lets start zipping
    if ztype == "zip":
        print("[NVC] Zipping files...")
        td = date.today().strftime("%m-%d-%y")
        shutil.make_archive(td, "zip", dir)
        print(f"[NVC] Zipped as {td}.zip")
    elif ztype == "7z":
        print("[NVC] Zipping files...")
        safe_err(4)
    elif ztype == "tar":
        print("[NVC] Zipping files...")
        td = date.today().strftime("%m-%d-%y")
        shutil.make_archive(td, "tar", dir)
        print(f"[NVC] Zipped as {td}.tar")
    else:
        safe_err(2)

if __name__ == "__main__":
    main()