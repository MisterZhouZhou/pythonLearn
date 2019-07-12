import subprocess

if __name__ == '__main__':
    subprocess.call("python3 openpose.py --model pose.caffemodel --proto pose.prototxt --dataset MPI", shell=True)