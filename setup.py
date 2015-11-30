#! /usr/bin/env python


from setuptools import setup
setup(
    name='mdx_customdivclass',
    version='1.0.0',
    author='Jared Short (forked from Konrad Wasowicz)',
    author_email='jshort@trek10.com',
    description='Markdown extension which allows inserting span elements with custom class',
    url='https://github.com/trek10inc/mdx_custom_div_class',
    py_modules=['mdx_custom_div_class'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
