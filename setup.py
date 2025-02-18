import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import setuptools, UnityPyTypetreeCodegen

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UnityPyTypetreeCodegen",
    version="%d.%d.%d" % UnityPyTypetreeCodegen.__version__,
    author="greats3an",
    author_email="greats3an@gmail.com",
    description="Unity Typetree to Python Module code generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mos9527/UnityPyTypetreeCodegen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=["typetreegeneratorapi", "UnityPy>=1.21"],
    entry_points={
        "console_scripts": [
            "UnityPyTypetreeCodegen = UnityPyTypetreeCodegen.__main__:__main__"
        ]
    },
    python_requires=">=3.10",
)
