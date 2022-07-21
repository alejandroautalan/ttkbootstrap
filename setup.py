import setuptools

long_description = ""

setuptools.setup(
    name="ttkbootstrap",
    version="2.0.0",
    author="Israel Dryer",
    author_email="israel.dryer@gmail.com",
    description="A supercharged theme extension for tkinter that enables on-demand modern flat style themes inspired by Bootstrap.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/israel-dryer/ttkbootstrap",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["pillow>=8.2.0"],
    python_requires=">=3.8",
)
