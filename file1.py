import os
import shutil

def list_files(path='.'):
    print(f"\nContents of directory: {os.path.abspath(path)}")
    for item in os.listdir(path):
        print("📁" if os.path.isdir(os.path.join(path, item)) else "📄", item)
    print()

def create_file(filename):
    with open(filename, 'w') as f:
        f.write('')
    print(f"✅ File '{filename}' created.")

def create_folder(foldername):
    os.makedirs(foldername, exist_ok=True)
    print(f"✅ Folder '{foldername}' created.")

def delete_file_or_folder(name):
    if os.path.isdir(name):
        shutil.rmtree(name)
        print(f"🗑️ Folder '{name}' deleted.")
    elif os.path.isfile(name):
        os.remove(name)
        print(f"🗑️ File '{name}' deleted.")
    else:
        print("❌ File or folder not found.")

def move_file(source, destination):
    shutil.move(source, destination)
    print(f"🚚 Moved '{source}' to '{destination}'.")

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"✏️ Renamed '{old_name}' to '{new_name}'.")

def search_file(name, path='.'):
    print(f"\n🔍 Searching for '{name}' in '{os.path.abspath(path)}'...")
    found = False
    for root, dirs, files in os.walk(path):
        if name in files or name in dirs:
            print("✅ Found:", os.path.join(root, name))
            found = True
    if not found:
        print("❌ Not found.")
    print()

def main():
    while True:
        print("\n--- File Management System ---")
        print("1. List Files")
        print("2. Create File")
        print("3. Create Folder")
        print("4. Delete File/Folder")
        print("5. Move File/Folder")
        print("6. Rename File/Folder")
        print("7. Search File/Folder")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            list_files()
        elif choice == '2':
            name = input("Enter file name to create: ")
            create_file(name)
        elif choice == '3':
            name = input("Enter folder name to create: ")
            create_folder(name)
        elif choice == '4':
            name = input("Enter file/folder name to delete: ")
            delete_file_or_folder(name)
        elif choice == '5':
            src = input("Enter source path: ")
            dest = input("Enter destination path: ")
            move_file(src, dest)
        elif choice == '6':
            old = input("Enter current name: ")
            new = input("Enter new name: ")
            rename_file(old, new)
        elif choice == '7':
            name = input("Enter file/folder name to search: ")
            search_file(name)
        elif choice == '8':
            print("👋 Exiting File Management System.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
