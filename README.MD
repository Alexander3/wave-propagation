# Sound wave simulation

This project uses celural automata to simulate sound wave propagation and dampening by different shapes of walls
based on _Komatsuzaki T., Iwata Y., Morishita S. (2012) Modelling of Incident Sound Wave Propagation around Sound Barriers Using Cellular Automata. In: Sirakoulis G.C., Bandini S. (eds) Cellular Automata. ACRI 2012. Lecture Notes in Computer Science, vol 7495. Springer, Berlin, Heidelberg_

## Development
Use `pipenv` for managing dependencies https://github.com/pypa/pipenv#installation
``` bash
pipenv install
```
Running
``` bash
pipenv shell
python main.py 1 # use 1,2,3 for different walls
```