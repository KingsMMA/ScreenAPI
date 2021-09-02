from distutils.core import setup

setup(
    name = "ScreenAPI",
    packages = ["ScreenAPI"],
    version = "Beta 1.0",
    description = "A python library used for making custom screens easier.",
    author = "IKings",
    author_email = "adking08@hotmail.com",
    url = "https://github.com/KingsMMA/ScreenAPI",
    download_url = "https://github.com/KingsMMA/ScreenAPI/archive/beta_v1_0.tar.gz",
    keywords = ["screen", "api", "screenapi", "utility", "tkinter"],
    install_requires = [
        "tkinter",
        "math"
    ]
    classifiers =[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
