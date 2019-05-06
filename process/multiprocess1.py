import os, time, random
from multiprocessing import Process, Pool


def process():
    print('current Process %s start ...' % os.getpid())
    pid = os.fork()
    if pid < 0:
        print('error in fork')
    elif pid == 0:
        print('I am child process(%s) and my parent process is (%s)' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) created a child process (%s)' % (os.getpid(), pid))

# 子进程要执行的代码
def run_proc(name):
    print('Child process %s (%s) Running....' % (name, os.getpid()))


def def_multiprocess():
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i)))
        print('Process will start')
        p.start()
    p.join()
    print('Process end.')

def run_task(name):
    print('Task %s (pid=%s) is running...' %(name, os.getpid()))
    time.sleep(random.random()*3)
    print('Task %s end.' % name)

if __name__ == '__main__':
    print('Current process %s.' % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=str(i))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')