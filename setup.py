from setuptools import setup, find_packages


setup(
    name='yorda',
    version='0.1.0.dev0',
    description='ICO image format parser',
    long_description=open('README.md').read(),
    url='https://github.com/flother/yorda',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=True,
    install_requires=('attrs',),
    entry_points={
        'console_scripts': [
            'yorda=yorda:main',
        ],
    },
)
