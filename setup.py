from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Core requirements
install_requires = [
    "sanic>=21.12.0",
    "ujson>=5.4.0",
]

extras_require = {
    "aioredis": ["aioredis>=2.0.0"],
    "redis": ["asyncio_redis>=0.16.0"],
    "mongo": [
        "sanic_motor>=2.1.0",
        "pymongo>=4.0.0"
    ],
    "memcache": ["aiomcache>=0.7.0"],
    "full": [
        "aioredis>=2.0.0",
        "asyncio_redis>=0.16.0",
        "sanic_motor>=2.1.0",
        "pymongo>=4.0.0",
        "aiomcache>=0.7.0"
    ],
    "dev": [
        "pytest>=7.0.0",
        "pytest-asyncio>=0.20.0",
        "pytest-cov>=3.0.0",
        "black>=22.0.0",
        "isort>=5.10.0",
        "mypy>=0.950",
        "flake8>=4.0.0",
        "wheel>=0.37.0",
        "twine>=4.0.0"
    ],
    "docs": [
        "sphinx>=5.0.0",
        "sphinx-rtd-theme>=1.0.0"
    ]
}

setup(
    name="sanic_sessions",
    version="0.9.0",
    description="Server-backed sessions for Sanic with InMemory, Redis, Memcache, and MongoDB support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aime-labs/sanic-sessions",
    author="Khaled Abdel Moezz",
    author_email="khaled.a.moezz@gmail.com",
    license="MIT",
    packages=find_packages(include=["sanic_sessions", "sanic_sessions.*"]),
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,
    keywords=["sanic", "sessions", "async", "redis", "memcache", "mongodb"],
    classifiers=[
        "Framework :: AsyncIO",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Session",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Source": "https://github.com/aime-labs/sanic-sessions",
        "Tracker": "https://github.com/aime-labs/sanic-sessions",
    },
)