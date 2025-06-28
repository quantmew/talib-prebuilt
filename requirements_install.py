import sys
import os

import os
import platform

def is_alpine_linux() -> bool:
    """
    检查当前系统是否为 Alpine Linux
    
    返回:
        bool: 如果是 Alpine Linux 返回 True，否则返回 False
    """
    # 方法 1: 检查 /etc/os-release 文件
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release", "r") as f:
            content = f.read().lower()
            if "alpine" in content:
                return True
    
    # 方法 2: 检查 apk 包管理器是否存在
    if os.system("which apk >/dev/null 2>&1") == 0:
        return True
    
    # 方法 3: 检查系统发行版信息
    system = platform.system().lower()
    if system == "linux":
        try:
            # 尝试获取 Linux 发行版信息
            distro = platform.freedesktop_os_release().get("id", "").lower()
            if "alpine" in distro:
                return True
        except Exception:
            # 回退到检查 /etc/issue 文件
            if os.path.exists("/etc/issue"):
                with open("/etc/issue", "r") as f:
                    if "alpine" in f.read().lower():
                        return True
    
    return False


def install_requirements(arch: str):
    try:
        import pip
    except ImportError:
        print("pip is not installed. Please install pip and try again.")
        sys.exit(1)
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    if sys.platform == "win32":
        requirements_path = os.path.join("requirements", "windows", arch)
        if python_version.startswith("3.4"):
            print("Python 3.4 is not supported. Please use Python 3.5 or higher.")
            sys.exit(1)
        elif python_version.startswith("3.5"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.5.txt")
        elif python_version.startswith("3.6"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.6.txt")
        elif python_version.startswith("3.7"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.7.txt")
        elif python_version.startswith("3.8"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.8.txt")
        elif python_version.startswith("3.9"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.9.txt")
        elif python_version.startswith("3.10"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.10.txt")
        elif python_version.startswith("3.11"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.11.txt")
        elif python_version.startswith("3.12"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.12.txt")
        elif python_version.startswith("3.13"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.13.txt")
        elif python_version.startswith("3.14"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.14.txt")
        elif python_version.startswith("3.15"):
            requirements_file = os.path.join(requirements_path, "requirements_windows_3.15.txt")
        else:
            print("Unsupported Python version. Please use Python 3.5 or higher.")
            sys.exit(1)
    elif sys.platform == "darwin":
        requirements_file = os.path.join("requirements", "mac", arch, "requirements_mac.txt")
        if python_version.startswith("3.4"):
            print("Python 3.4 is not supported. Please use Python 3.5 or higher.")
            sys.exit(1)
        elif python_version.startswith("3.5"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.5.txt")
        elif python_version.startswith("3.6"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.6.txt")
        elif python_version.startswith("3.7"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.7.txt")
        elif python_version.startswith("3.8"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.8.txt")
        elif python_version.startswith("3.9"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.9.txt")
        elif python_version.startswith("3.10"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.10.txt")
        elif python_version.startswith("3.11"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.11.txt")
        elif python_version.startswith("3.12"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.12.txt")
        elif python_version.startswith("3.13"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.13.txt")
        elif python_version.startswith("3.14"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.14.txt")
        elif python_version.startswith("3.15"):
            requirements_file = os.path.join(requirements_path, "requirements_mac_3.15.txt")
        else:
            print("Unsupported Python version. Please use Python 3.5 or higher.")
            sys.exit(1)
    elif sys.platform.startswith("linux"):
        requirements_file = os.path.join("requirements", "linux", arch, "requirements_linux.txt")

        if is_alpine_linux():
            requirements_path = os.path.join("requirements", "linux", arch, "alpine")
            linux_type = "musllinux"
        else:
            requirements_path = os.path.join("requirements", "linux", arch, "manylinux")
            linux_type = "manylinux"

        if python_version.startswith("3.4"):
            print("Python 3.4 is not supported. Please use Python 3.5 or higher.")
            sys.exit(1)
        elif python_version.startswith("3.5"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.5.txt")
        elif python_version.startswith("3.6"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.6.txt")
        elif python_version.startswith("3.7"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.7.txt")
        elif python_version.startswith("3.8"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.8.txt")
        elif python_version.startswith("3.9"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.9.txt")
        elif python_version.startswith("3.10"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.10.txt")
        elif python_version.startswith("3.11"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.11.txt")
        elif python_version.startswith("3.12"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.12.txt")
        elif python_version.startswith("3.13"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.13.txt")
        elif python_version.startswith("3.14"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.14.txt")
        elif python_version.startswith("3.15"):
            requirements_file = os.path.join(requirements_path, "requirements_linux_3.15.txt")
        else:
            print("Unsupported Python version. Please use Python 3.5 or higher.")
            sys.exit(1)
    else:
        print("Unsupported platform. Please run this script on Windows, macOS, or Linux.")
        sys.exit(1)
    
    if not os.path.exists(requirements_file):
        print(f"Requirements file not found: {requirements_file}")
        sys.exit(1)
    
    print(f"Installing requirements from {requirements_file}...")
    try:
        with open(requirements_file, "r") as f:
            requirements = f.read().splitlines()
        for requirement in requirements:
            if requirement and not requirement.startswith("#"):
                print(f"Installing {requirement}...")
                pip.main(["install", requirement])
    except Exception as e:
        print(f"An error occurred while installing requirements: {e}")
        sys.exit(1)

import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Install requirements based on Python version and platform.")
    parser.add_argument("--arch", type=str, default="x86_64", help="Specify the architecture for the requirements file.")
    args = parser.parse_args()
    install_requirements(arch=args.arch)
