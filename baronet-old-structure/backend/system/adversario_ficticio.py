import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

from backend.system.adversarios import AdversarioMonstro

slime = AdversarioMonstro("slime", 50, 1.0, 3, 100, 2, 3, 4, 5, None, None)