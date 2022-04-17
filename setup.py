from setuptools import setup

setup(
    name='sheikahdock',
    version='0.1.0',
    packages=['sheikah_dock'],
    url='https://github.com/lvoytek/SheikahDock',
    license='GPLv3',
    author='Lena Voytek',
    author_email='lena@voytek.dev',
    description='An application dock based on the Sheikah Slate',
    classifiers=[
        'Programming Language:: Python:: 3',
        'License:: OSI Approved:: GNU General Public License v3 or later(GPLv3 +)',
        'Development Status :: 3 - Alpha',
    ],
    install_requires=[
        'PyGObject', 'setuptools'
    ],
    entry_points={
        'console_scripts': ['sheikahdock=sheikah_dock.dock:main']
    }
)
