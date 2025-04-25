import os 
from pathlib import Path

main_folder = "src"

Paths = [
    f"{main_folder}/main.py",
    f"{main_folder}/analysis.py",
    f"{main_folder}/llm_service.py",
    "setup.py",
    'requirements.txt',
    'test.py'
]

for path in Paths:
    file_path = Path(path)
    folder = file_path.parent
    os.makedirs(folder,exist_ok=True)
    
    if not os.path.exists(file_path):
        file_path.touch(exist_ok=True)