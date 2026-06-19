from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="BorutaShap",
    version="1.0.14",
    description="A feature selection algorithm.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ekeany/Boruta-Shap",
    author="Eoghan Keany",
    author_email="egnkeany@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    py_modules = ["BorutaShap"],
    package_dir = {"" : "src"},
    install_requires=["scikit-learn>=1.4","tqdm>=4.66",
                      "statsmodels>=0.14","matplotlib>=3.8",
                      "pandas>=2.1","numpy>=1.26","shap>=0.45","seaborn>=0.13",
                      "scipy>=1.11"],
)
