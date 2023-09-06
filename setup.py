#!/usr/bin/env python3
import os
import subprocess
from shutil import copyfile
from setuptools import setup, find_packages


def create_mo_files():
    podir = "po"
    mo = []
    for po in os.listdir(podir):
        if po.endswith(".po"):
            os.makedirs("{}/{}/LC_MESSAGES".format(podir, po.split(".po")[0]), exist_ok=True)
            mo_file = "{}/{}/LC_MESSAGES/{}".format(podir, po.split(".po")[0], "mauna-usb-formatter.mo")
            msgfmt_cmd = 'msgfmt {} -o {}'.format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(("/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                       ["po/" + po.split(".po")[0] + "/LC_MESSAGES/mauna-usb-formatter.mo"]))
    return mo


changelog = 'debian/changelog'
version = "0.1.0"
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
    f = open('src/__version__', 'w')
    f.write(version)
    f.close()

copyfile("icon.svg", "mauna-usb-formatter.svg")

data_files = [
 ("/usr/share/applications/", ["top.mauna.usb-formatter.desktop"]),
 ("/usr/share/mauna/mauna-usb-formatter/", ["icon.svg", "main.svg"]),
 ("/usr/share/mauna/mauna-usb-formatter/src",
  ["src/Main.py", "src/MainWindow.py", "src/USBFormatter.py", "src/USBDeviceManager.py",
   "src/__version__"]),
 ("/usr/share/mauna/mauna-usb-formatter/ui", ["ui/MainWindow.glade"]),
 ("/usr/share/polkit-1/actions", ["top.mauna.pkexec.mauna-usb-formatter.policy"]),
 ("/usr/bin/", ["mauna-usb-formatter"]),
 ("/usr/share/icons/hicolor/scalable/apps/", ["mauna-usb-formatter.svg"])
] + create_mo_files()

setup(
    name="Mauna USB Formatter",
    version=version,
    packages=find_packages(),
    scripts=["mauna-usb-formatter"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Mauna Linux",
    author_email="dev@maunalinux.top",
    description="Mauna USB Formatter.",
    license="GPLv3",
    keywords="usb format mauna",
    url="https://github.com/maunalinux/mauna-usb-formatter",
)
