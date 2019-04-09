from distutils.core import setup

VERSION = '0.1'

setup(
    name='InANutshell',
    version=VERSION,
    author='JoshPrakke',
    author_email='joshprakke@gmail.com',
    url='https://github.com/JPrakke/in-a-nutshell',
    install_requires=['pyperclip == 1.7.0',]
    packages=['nutshell',],
    license='MIT License',
    long_description=open('README.txt').read(),
)