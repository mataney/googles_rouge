from setuptools import setup

setup(name='rouge',
      version='0.1',
      description="This is a cloned version of google-research's rouge.",
      url="https://github.com/matan/googles_rouge",
      author='Matan Eyal',
      author_email='mataneyal1@gmail.com',
      install_requires=['absl-py', 'nltk', 'numpy', 'six']
      packages=['rouge'],
      zip_safe=False)