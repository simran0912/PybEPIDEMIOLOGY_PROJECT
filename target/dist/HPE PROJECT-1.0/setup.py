#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'HPE PROJECT',
        version = '1.0',
        description = 'Example PyBuilder / Git project',
        long_description = 'An example PyBuilder / Git project for project management\nand file version control. See blog post at http://bit.ly/2QY65wO for a\nmore through explanation.',
        long_description_content_type = None,
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        keywords = '',

        author = 'Simran and Prajna',
        author_email = 'simranhora912@gmail.com',
        maintainer = '',
        maintainer_email = '',

        license = 'None',

        url = '',
        project_urls = {},

        scripts = [],
        packages = ['.'],
        namespace_packages = [],
        py_modules = [
            'SIER_CODE',
            'SIR_CODE',
            'SIS_CODE',
            '__init__'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
