"""
Reconstruction of image data from raw data.
"""

# TODO: define reconstruction algorithm independent device
# configurations, some reconstruction algorithms may choose to ignore
# some of that information, this way the number of electrodes and
# so on can be set as a free parameter!

# TODO: define an abstract interface for reconstruction algorithms.

from .worker import ReconstructionWorker

# for testing and debugging purposes below. 
from .greit import GreitReconstruction
from .pyeit import mesh 
from .pyeit.eit.utils import eit_scan_lines
from .pyeit.eit.greit import GREIT as greit
from .pyeit.eit.fem import Forward