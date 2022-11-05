from importlib.metadata import PackageNotFoundError, version

from pysvelte.build import *
from pysvelte.visualizations.activations import activations
from pysvelte.visualizations.activations.activations import \
    TextNeuronActivations as TextSingle
from pysvelte.visualizations.attention import attention
from pysvelte.visualizations.attention.attention import \
    AttentionPatterns as AttentionMulti
from pysvelte.visualizations.examples import examples

__all__ = [
    "activations",
    "attention",
    "AttentionMulti",  # Legacy export name from PySvelte
    "examples",
    "TextSingle"  # Legacy export name from PySvelte
]

# Version set automatically using setuptools_scm
try:
    __version__ = version("package-name")
except PackageNotFoundError:
    # package is not installed
    pass
