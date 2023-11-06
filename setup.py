from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    long_description = f.read()
  
setup(
        name ='ppm-display',
        version ='1.2',
        author ='Hugo (Jin Huang)',
        author_email ='s2050808@ed.ac.uk',
        url ='https://github.com/Trenza1ore/ppm-display',
        description ='PPM/PGM image viewer',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'ppm-disp = ppm_display.ppm_disp:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='ppm pgm image python package ppm-display ppm-disp',
        install_requires = requirements,
        zip_safe = False
)