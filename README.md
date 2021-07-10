# Sort files

This simple script can sort files by categories (based on the extensions). Written in *python* using some awesome modules - `pathlib`, `argparse` and `logging`.

## Usage

The simplest scenario is to run without any parameters - it will sort *Downloads* directory:

* double-click in **Windows**
* *run* in **Linux**

### **Warning!**

**Check** the location of your *Downloads* directory!

By default it is *'/home/Загрузки'* in **Linux** and *'C:\Users\<user_name>\Downloads'* in Windows

> I'm Russian, so it looks like you need to rename *'Загрузки'* to a suitable directory =)

### **With arguments**

Basic help will be shown by argument *-h*

```bash
sort.py [-h] [-r] [-p PATH]

  -r, --relative        relative or absolute (default) path
  -p PATH, --path PATH  path (default: Downloads)
```

Script will create **logs** named *logs.log* in the folder where it is located.

## Configuration

The user settings of the categories are stored in the [*json*-file](extension_lib.json).

### Other

Thanks to [https://habr.com/ru/post/562362/](https://habr.com/ru/post/562362/)
for idea and extension library.
