"""Move JPG images from one folder into another."""

import argparse
import os
import shutil


def move_jpg_files(source_folder: str, destination_folder: str) -> int:
    """Move JPG files directly inside source_folder; return the number moved."""
    source = os.path.abspath(source_folder)
    destination = os.path.abspath(destination_folder)

    if not os.path.isdir(source):
        raise FileNotFoundError(f"Source folder does not exist: {source_folder}")
    if source == destination:
        raise ValueError("Source and destination folders must be different.")

    os.makedirs(destination, exist_ok=True)
    moved_count = 0

    with os.scandir(source) as entries:
        for entry in entries:
            if not entry.is_file() or not entry.name.lower().endswith(".jpg"):
                continue

            target = os.path.join(destination, entry.name)
            name, extension = os.path.splitext(entry.name)
            suffix = 1
            while os.path.exists(target):
                target = os.path.join(destination, f"{name}_{suffix}{extension}")
                suffix += 1

            shutil.move(entry.path, target)
            moved_count += 1

    return moved_count


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Move all .jpg files from one folder to another."
    )
    parser.add_argument("source_folder", help="Folder containing JPG files")
    parser.add_argument("destination_folder", help="Folder to move JPG files into")
    args = parser.parse_args()

    moved_count = move_jpg_files(args.source_folder, args.destination_folder)
    print(f"Moved {moved_count} JPG file(s) to '{args.destination_folder}'.")


if __name__ == "__main__":
    main()
