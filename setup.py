from setuptools import find_packages,setup
setup(name="e-commerce-bot",version = "0.0.1",description="A bot for e-commerce platforms",
      author="Anirudh",
      author_email="anirudh.cec@gmail.com",
      packages=find_packages(),
      install_requires=['langchain-astradb','langchain'])