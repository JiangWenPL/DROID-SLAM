from setuptools import setup
import os.path as osp
ROOT = osp.dirname(osp.abspath(__file__))


setup(
    name="droid_slam",
    packages=['droid_slam'],
    # package_dir={'droid': ROOT},
)
