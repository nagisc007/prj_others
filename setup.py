from setuptools import setup, find_packages
import sys

sys.path.append('./storybuilder/builder')
sys.path.append('./src')
sys.path.append('./tests')

setup(
        name = 'Novels for contests',
        version = '0.0.1',
        description = "This is novels that apply to official contests",
        packages = find_packages(),
        test_suite = 'test_all.suite'
)
