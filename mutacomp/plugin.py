"""Installing mutacomp registers the mutacomp throng plugin automatically."""

from pathlib import Path
from typing import List, Optional, Union

from throng import throng

from mutacomp.manager import MutacompManager


@throng.plugin('mutacomp', unique=True)
def mutacomp(path: Union[str, Path] = '.', exclude: Optional[List[str]] = None, prepare: Optional[List[str]] = None, packages: Optional[List[str]] = None) -> MutacompManager:
    return MutacompManager(path, exclude, prepare, packages)
