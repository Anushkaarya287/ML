import os

folder_path = "textfile"
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)

        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        print("="*40)
        print(f"📄 File: {file_name}")
        print("------ Extracted Text ------")
        print(content)
        print("="*40)