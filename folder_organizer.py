import shutil
from pathlib import Path


CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "Programs": [".exe", ".bin", ".py"],
    "CompressedFiles": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Music": [".mp3", ".m4a"]
}


def organize_downloads(download_path: Path) -> None:


    if not download_path.exists():
        print(f"[ERROR] The folder {download_path} does not exist")
        return
  
    for category in CATEGORIES:
        (download_path / category).mkdir(exist_ok=True)

    for file in download_path.iterdir():
        if file.is_file():
            ext = file.suffix.lower()

            for category, extensions in CATEGORIES.items():
                if ext in extensions:
                    destination = download_path / category / file.name
                    if destination.exists():
                        print(f"[SKIP] {file.name} already exists in {category}.")
                        break

                    shutil.move(str(file), str(destination))
                    print(f"[OK] {file.name} → {category}")
                    break

    print("Folder Organized!")

def main():
    download_folder = Path.home() / "Downloads"
    organize_downloads(download_folder)


if __name__ == "__main__":
    main()
