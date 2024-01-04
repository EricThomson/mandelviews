# mandelviews documentation
mandelviews is a package for calculating and visualizing the Mandelbrot set.

There are already many libraries that do this. Here, the focus is not on providing new functionality, but on providing a working instance of a project that follows the suggestions for software projects at the CCN template repo:  
https://github.com/flatironinstitute/ccn-template

## Installation
Install on all platforms using pip:    

    pip install mandelviews

To update to the latest version:

    pip install mandelviews --upgrade

## Quick start
To get started quickly, see the [Quick Start Guide](quick_start.md).

## Usage guide
For more detailed usage notes, including some discussion of the theory behind the algorithms, see the [Usage Guide](usage_guide.md).

## API Reference
For the full documentation for each function by category, see the [API Reference](api_reference.md).
 
## Future directions
In the future, we plan to add numba and cython implementations of the Mandelbrot set calculation. This will allow for expanded demonstration of how to do tricky things like distribute compiled (cython) code at pip, among other things.

## Acknowledgments
Code written with support of Flatiron Center for Computational Neuroscience, and the neuroRSE team. 