import os
import shutil
import configparser


def copy_everything(subdir, target):
    if not os.path.isdir(target):
        os.mkdir(target)

    files = os.scandir(subdir)
    for file in files:
        shutil.copy(file, target)


def zip_without_compression(target_subdir):
    root = os.path.dirname(target_subdir)
    subdir_name = os.path.basename(target_subdir)
    shutil.make_archive(target_subdir, "tar", root, subdir_name)


def flatten_subdirs_to_target(directory, target):
    print("Working on " + directory.name, end="...")
    subdirs = os.scandir(directory)
    for subdir in subdirs:
        target_subdir = os.path.join(target, directory.name)
        copy_everything(subdir, target_subdir)
        zip_without_compression(target_subdir)

    print(" Done\n")


def main():
    config = configparser.ConfigParser()
    config.read("config.ini")
    root = config["ARGS"]["root"]
    target = config["ARGS"]["target"]

    if not os.path.exists(target):
        os.makedirs(target)

    directories = os.scandir(root)
    for directory in directories:
        if "Volume" in directory.name:
            flatten_subdirs_to_target(directory=directory, target=target)


if __name__ == '__main__':
    main()
