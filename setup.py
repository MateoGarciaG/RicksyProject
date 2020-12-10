import setuptools

with open("README.md", "r", encoding="utf-8") as longDescrip:
    long_description = longDescrip.read()

setuptools.setup(
    name="Menus_Scrapping_Tool",
    version="0.0.1",
    author="Mateo Garcia Gonzalez and Adrià Flexas",author_email="mgarciag@cifpfbmoll.eu aflexas@cifpfbmoll.eu",
    description="Tool for Scrapping websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MateoGarciaG/RicksyProject",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests==2.25.0',
        'pymongo==3.11.2',
        'dnspython==2.0.0',
        'pytest==6.1.2'
    ],
)