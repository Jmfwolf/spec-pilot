import shutil
import subprocess
import sys
import tempfile
import urllib.request


def check_vacuum():
    """
    Check if 'vacuum' command is available in the system.
    
    Returns:
        bool: True if 'vacuum' command is found, False otherwise.
    """
    return shutil.which("vacuum") is not None


def install_vacuum():
    """
    Download and run a script to install 'vacuum' command.
    
    The script is downloaded from a specified URL and then run using '/bin/sh'.
    In case of any errors during downloading or execution of the script, the function will exit the program.
    """
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


def vacuum(args):
    """
    Run the 'vacuum' command with the given arguments.
    
    Args:
        args (list): List of arguments to pass to the 'vacuum' command.
        
    In case of any errors during execution of the 'vacuum' command, the function will exit the program.
    """
    try:
        subprocess.check_call(["vacuum"] + args)
    except subprocess.CalledProcessError as e:
        sys.exit(f"Error running vacuum: {e}")


if not check_vacuum():
    install_vacuum()


def main():
    """
    Main function of the script.
    
    Checks if 'vacuum' is installed, if not it installs it.
    Then it runs 'vacuum' command with 'help' argument.
    """
    vacuum(["help"])


if __name__ == "__main__":
    main()
