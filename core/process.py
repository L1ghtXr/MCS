import subprocess


def run_shell(command, check=False, capture=True):
    try:
        return subprocess.run(
            command,
            shell=True,
            capture_output=capture,
            text=True,
            check=check,
        )
    except (OSError, subprocess.SubprocessError):
        return None
