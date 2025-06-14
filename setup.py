import os
import sys

from setuptools import find_packages
from setuptools import setup

version = "3.0.0"

install_requires = [
    "requests>=2.25.1",
    "setuptools>=41.6.0",
]

if os.environ.get("SNAP_BUILD"):
    install_requires.append("packaging")
else:
    install_requires.extend(
        [
            # We specify the minimum acme and certbot version as the current plugin
            # version for simplicity. See
            # https://github.com/certbot/certbot/issues/8761 for more info.
            f"acme>={version}",
            f"certbot>={version}",
        ]
    )

docs_extras = [
    "Sphinx>=1.0",  # autodoc_member_order = 'bysource', autodoc_default_flags
    "sphinx_rtd_theme",
]

# Load readme to use on PyPI
with open("README.rst", encoding="utf8") as f:
    readme = f.read()

setup(
    name="certbot-dns-jeffdev",
    version=version,
    description="JeffDev DNS Authenticator plugin for Certbot",
    url="https://github.com/jeffrey-dev/certbot-dns-jeffdev",
    author="Jeffrey van Barneveld",
    author_email="jeffrey.barneveld@jeffdev.nl",
    license="BSD-2-Clause",
    long_description="Certbot plugin for automating the DNS-01 challenge using Jeffdev DNS API.",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        "docs": docs_extras,
    },
    entry_points={
        "certbot.plugins": [
            "dns-jeffdev = certbot_dns_jeffdev._internal.dns_jeffdev:Authenticator",
        ],
    },
)
