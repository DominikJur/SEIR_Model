# SEIR_Model
## Modeling an epidemic on a fixed population in python
In this project I have made a simple epidemiological compartmental model. The model is the SEIR model, an epidemiological compartmental model based on the initial size of the population and subdeviding it into 4 categories: S - suspectible (not have been infected yet), E - exposed (where in contact with the infected), I - infectious (sick and capable of spreading the virus), R - removed (removed form the equation through death, or  aquireing antibodies). In a closed population with no births or deaths, the SEIR model becomes:

$$
\begin{cases}
\frac{dS}{dt}  = -\frac{\beta SI}{N}\\
\frac{dE}{dt}  = \frac{\beta SI}{N} - \sigma E\\
\frac{dI}{dt}  = \sigma E - \gamma I\\
\frac{dR}{dt}  = \gamma I
 N = S + E + I + R
\end{cases}
$$

where N is the total population, and $\beta$ is the infection parameter, $\sigma$ is the incubation parmeter and $\gamma$ is the recovery parameter.
 
 
 
 
## Usage

In order to try the model yourself, clone the code of this projeckt to a directory on your device. After that run the folowing command on a command prompt of your choise (make sure you are in the directory to which you downlowded the code).

```bash
python app.py
```
After this a link to the web app will apperar in the termianal. Beyond that there is also a Jupyter Notebook with the model.
 
 

## Requirements
Many libraries used in this project do not come preinstalled in vanilla python. In order to get the program running you might need to run the following command in the command prompt (again make sure you are in the directory to which you downlowded the code).

```bash
pip install -r requriements.txt
```

## Project state
This project is finished.

## Preview

https://github.com/DominikJur1/SEIR_Model/assets/162451655/f1715d82-df81-4b4d-bda7-b030c5cfbb8f



