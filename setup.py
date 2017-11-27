from setuptools import setup

setup(
    name="primefeed",
    version="0.1",
    py_modules=["primefeed"],
    install_requires=[
        "click", "requests",
    ],
    entry_points="""
        [console_scripts]
        primefeed=primefeed:cli
    """,
    )
