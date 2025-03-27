# Monitor energy consumption and carbon emission of a C executable

The steps are the following:
1. Clone this repository
2. Install [CodeCarbon](https://codecarbon.io/), either in your general environment (e.g. using `pipx`) or in a virtual environment inside this repository (see [how to install CodeCarbon](https://mlco2.github.io/codecarbon/installation.html))
3. Create a CodeCarbon account by executing `codecarbon login`
4. Configure CodeCarbon by executing `codecarbon config`
      * Make sure to enter the right country ISO code to make sure that the right electricity mix is used (e.g. `BEL` for Belgium)
6. Run `python monitor.py PATH_TO_EXECUTABLE`, where `PATH_TO_EXECUTABLE` is the path to the C executable (output of `gcc`)
7. All the monitored emissions are stored in `emissions.csv` 
