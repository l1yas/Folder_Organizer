# **Folder Organizer : an Automatic Folder Sorting Script**

A small Python utility that automatically organizes the user's **Downloads** folder by sorting files into categorized subfolders based on their file extensions.

This script is simple, efficient, and ready to use on any system running Python 3.

---

## Features :

* Automatically detects your `~/Downloads` folder
* Sorts files into predefined categories:

  * Images
  * Videos
  * Documents
  * Programs
  * Compressed files
  * Music
* Creates missing folders automatically
* Avoids overwriting files (skips if a file already exists)
* Lightweight: no external dependencies

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/l1yas/Folder_Organizer
```

2. Navigate inside the project:

```bash
cd Folder_Organizer
```

3. Run the script:

```bash
python3 folder_organizer.py
```

---

## Usage

Simply run the script.
It will automatically detect your **Downloads** folder:

```bash
python3 folder_organizer.py
```

If you want to modify the target folder, edit the `main()` function:

```python
download_folder = Path("/path/to/your/folder")
```
---

## License

This project is released under the **MIT License**, allowing free use, modification, and distribution.

---

## Author

Script developed and maintained by **Ilyas Yahia-Cherif**.
