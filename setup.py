"""Setup script."""

from setuptools import find_packages, setup  # noqa: E402


setup(
    name="wavtokenizer",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "einops",
        "huggingface_hub",
        "numpy",
        "pyyaml",
        "scipy",
        "torch",
        "torchaudio"
    ],
)
