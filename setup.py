from setuptools import setup

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(name='guilded-webhook',
    version='1.0.0',
    description='guilded-webhook is a basic wrapper for guilded\'s webhooks.',
    author='anytarseir67',
    url='https://github.com/anytarseir67/guilded-webhook',
    packages=['guilded_webhook'],
    install_requires=requirements,
    )