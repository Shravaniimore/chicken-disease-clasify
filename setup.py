import setuptools
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME="chicken-disease-clasify"
AUTHOR_USER_NAME="Shravaniimore"
SRC_REPO="src\chicken-disease-clasify"
AUTHOR_EMAIL="shravaniimore4@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for cnn app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)
#script setup metadat n structure for package making  it ready for distribution and installation using tools like pip.