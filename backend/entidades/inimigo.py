import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

from tests.teste1 import slime
inimigo = slime