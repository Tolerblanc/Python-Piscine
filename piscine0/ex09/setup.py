import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ft_package",
    version="0.0.1",
    author="Tolerblanc",
    author_email="hihj070914@icloud.com",
    description="Python Piscine Day 00",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tolerblanc/Python-Piscine",
    project_urls={
        "Bug Tracker": "https://github.com/Tolerblanc/Python-Piscine/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
