# python3.7
# encoding: utf-8
"""
@author: Chenjin.Qian
@email:  chenjin.qian@xquant.com
@file:   setup.py
@time:   2020-07-10 14:29
"""

from setuptools import setup, find_packages
import exception_sms


def read(f):
    return open(f, encoding="utf-8").read()


setup(
    name="exception-sms",
    version=exception_sms.__version__,
    description='A package to notify developer that program catched a exception',
    long_description=read('README.rst'),
    license='MIT License',
    author="Jingxuan",
    author_email="jingxuan@lynchow.com",
    url="https://github.com/Thchoonlophon/exception-sms",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["qiniu"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
