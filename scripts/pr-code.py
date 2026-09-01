import os
import subprocess

env = os.environ.copy()
subprocess.run(["gh", "api", "user"], env=env, check=True)