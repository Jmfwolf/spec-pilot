import shutil
import subprocess
import sys
import tempfile
import urllib.request

class Validator:

    def __init__(self):
        if not self.check_vacuum():
            self.install_vacuum()

    def check_vacuum(self):
        return shutil.which("vacuum") is not None

    def install_vacuum(self):
        install_script_url = "https://quobix.com/scripts/install_vacuum.sh"
        try:
            with tempfile.NamedTemporaryFile(suffix=".sh", mode="wb") as tmpfile:
                with urllib.request.urlopen(install_script_url) as response:
                    if response.status != 200:
                        sys.exit("Failed to download install script")
                    tmpfile.write(response.read())
                subprocess.check_call(["/bin/sh", tmpfile.name])
        except (urllib.error.URLError, subprocess.CalledProcessError) as e:
            sys.exit(f"Failed to install vacuum: {e}")

    def vacuum(self, args):
        try:
            return subprocess.check_call(["vacuum"] + args[2:])
        except subprocess.CalledProcessError as e:
            sys.exit(f"Error running vacuum: {e}")

    def validate(self, yaml_path):
        result = self.vacuum(["validate", "-f", yaml_path])
        return {"valid": result == 0}

if __name__ == "__main__":
    validator = Validator()
    validator.vacuum(["help"])