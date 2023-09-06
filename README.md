# Mauna Usb Formatter

Mauna Usb Formatter is an application for format USB drives easily.

It is currently a work in progress. Maintenance is done by <a href="https://maunalinux.top/">Mauna Linux</a> team.

### **Dependencies**

This application is developed based on Python3 and GTK+ 3. Dependencies:
```bash
gir1.2-glib-2.0 gir1.2-gtk-3.0 python3-gi python3-pyudev
```

### **Run Application from Source**

Install dependencies
```bash
sudo apt install gir1.2-glib-2.0 gir1.2-gtk-3.0 python3-gi python3-pyudev
```
Clone the repository
```bash
git clone https://github.com/maunalinux/mauna-usb-formatter.git ~/mauna-usb-formatter
```
Run application
```bash
python3 ~/mauna-usb-formatter/src/Main.py
```

### **Build deb package**

```bash
sudo apt install devscripts git-buildpackage
sudo mk-build-deps -ir
gbp buildpackage --git-export-dir=/tmp/build/mauna-usb-formatter -us -uc
```

### **Screenshots**

![Mauna Usb Formatter 1](screenshots/mauna-usb-formatter-1.png)

![Mauna Usb Formatter 2](screenshots/mauna-usb-formatter-2.png)
