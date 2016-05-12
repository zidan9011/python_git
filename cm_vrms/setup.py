from setuptools import setup, find_packages

setup (
    name = "cm_vrms_upload",
    version = "0.0.1",
    url = "",
    license = "The MIT License (MIT)",
    description = "A minimal django project containing a minimal app with a working jquery file upload form based on the work by Sebastian Tschan: http://aquantum-demo.appspot.com/file-upload",
    author = 'Sebastian Tschan / Sigurd Gartmann',
    packages = find_packages(),
    package_dir = {'': '.'},
    install_requires = [],
)