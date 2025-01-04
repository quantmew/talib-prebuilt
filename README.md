# talib-prebuilt
Build [TA-Lib](https://github.com/ta-lib/ta-lib-python) wheels for Python using GitHub Actions.

Supported platforms:
- Windows 64-bit
- Windows 32-bit
- macOS x86_64
- macOS arm64
- Linux 64-bit

Supported Python versions:
- 3.6
- 3.7
- 3.8
- 3.9
- 3.10
- 3.11
- 3.12
- 3.13

The wheels can be downloaded from the [Releases](https://github.com/quantmew/talib-prebuilt/releases) page.

Install a wheel on the command line, for example for Python 3.13 64-bit:

    $ py.exe -3.13 -m pip install ta_lib-0.5.2-cp313-cp313-win_amd64.whl

# Acknowledgments
Some scripts for the Windows portion are derived from [cgohlke](https://github.com/cgohlke/talib-build/).