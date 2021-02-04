import logging
import platform

if platform.system() == "Windows":
    # Windows OS > 7
    from sugaroid.platform.windows import Windows as System
elif platform.system() == "Linux":
    # GNU/Linux OS
    from sugaroid.platform.linux import Linux as System
elif platform.system() == "Darwin":
    # MacOS
    from sugaroid.platform.darwin import Darwin as System
else:
    logging.warning("Attempting to run guiscrcpy on utested OS")
    from sugaroid.platform.linux import Linux as System

    # Other OSes should benefit from Linux config

System()
