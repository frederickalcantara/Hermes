import os
import shutil
import secrets
import string

home = os.path.expanduser("~")

def ssh_keygen():
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = "".join(secrets.choice(chars) for i in range(6))
    os.system("ssh-keygen -f picklerick -t ed25519 -N {}".format(password))
    dir_path = os.path.dirname(os.path.realpath(__file__))
    shutil.move(os.path.join(dir_path, "picklerick"), "{}/.ssh".format(home))
    shutil.move(os.path.join(dir_path, "picklerick.pub"), "{}/.ssh".format(home))                

def main():
    ssh_keygen()

if __name__=='__main__':
    main()