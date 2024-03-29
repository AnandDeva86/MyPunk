import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="punk",
    version="0.0.2",
    author="Anand Deva",
    author_email="ananddevarajan@live.com",
    description="This is a example python CLI application",
    long_description=long_description,
    long_description_content_type="",
    # url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'punk = punk_main:main'
        ]
    }
)
