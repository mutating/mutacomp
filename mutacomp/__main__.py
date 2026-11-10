"""Support python -m mutacomp as well as the installed mutacomp executable."""

import sys

from mutacomp.cli import main

sys.exit(main())
