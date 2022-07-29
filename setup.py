from setuptools import setup
import pathlib
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(name='guilded-webhook',
    version='0.1.2',
    description='guilded-webhook is a basic wrapper for guilded\'s webhooks.',
    long_description=README,
    long_description_content_type="text/markdown",
    author='anytarseir67',
    url='https://github.com/anytarseir67/guilded-webhook',
    license="GPLv3",
    packages=['guilded_webhook'],
    install_requires=requirements,
    )