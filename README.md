# Monitor energy consumption and carbon emission of a C executable

The steps are the following:
1. Clone this repository
2. Install [CodeCarbon](https://codecarbon.io/), either in your general environment (e.g. using `pipx`) or in a virtual environment inside this repository (see [how to install CodeCarbon](https://mlco2.github.io/codecarbon/installation.html))
3. Create a CodeCarbon account by executing `codecarbon login`
4. Configure CodeCarbon by executing `codecarbon config`
      * Make sure to enter the right country ISO code to make sure that the right electricity mix is used (e.g. `BEL` for Belgium)
6. Run `python monitor.py -o OUTPUT_FILE -e EXECUTABLE args` 
      - `OUTPUT_FILE`: path to output file, by default: `emissions.csv`
      - `EXECUTABLE`: path to the executable to monitor
      - `args`: optional arguments to pass to your executable
7. All the monitored emissions are stored in the `output_file` (by default `emissions.csv`) 
