import subprocess

if __name__ == '__main__':
    subprocess.call("python3 zip.py -f test.zip -d dictionary.txt", shell=True)