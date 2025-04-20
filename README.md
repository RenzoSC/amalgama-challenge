# Amalgama challenge - Army modeling exercise
Technical challenge Amalgama

This project requires Python 3.10 or higher

## Project Main Structure

The project is organized as follows:

```
amalgama-challenge/
├── src/                        # Source code files
│   ├── models/                 # Main entities
│   ├── services/               # Classes that handles process between entities
│   ├── settings.py             # Global variables
│   └── exceptions.py           # Custom Exception classes
├── .gitignore                  # Git ignore file
├── main.py                     # Main file to run a simulation
└── README.md                   # Project README file
```

This structure helps in maintaining a clean and organized codebase.

## Usage

Run the following command to see the simulation:
```bash
python main.py
```

## Cases:
1. #### Add new class wizard:
    If you want to add a new class wizard you don't need to make many changes.
    You have to create a new `constant` in `settings.py` with the global name of wizard,
    create a new class Wizard in a new file inside units folder, create a new `TRAINING_COST`
    inside `TrainingService` class and finally create a new `TRANSFORM_RULE` inside `TransformationService` class.

    Also if you want civilizations to have wizards in their armies you need to add
    wizard in `CivilizationArmyDistribution` class.

    Here is an example of how to make the changes to add wizard. [Click here](https://github.com/RenzoSC/amalgama-challenge/tree/wizard).

2. #### What happens if an army trains 3 times and then does a transformation
    If some unit trains X times and then does a transformation, the "new unit" starts
    with default strength. This decision was made because for example, if an archer trains, 
    probably its training is focalized in archers and won't be of value in knights.

    If you want to keep the strength in a transformation or make a formula on transformations
    you can check code [Here](https://github.com/RenzoSC/amalgama-challenge/tree/transformation).

3. #### How does program respond to errors?
    It was coded with a strong error handling, almost every method can raise an exception.
    All methods that could raise an exception were used inside a try-catch block. In this way, 
    if some error happens or an invalid action is done, it raises an error, logs the error 
    with an specific message describing the error and the program continues (an error doesn´t 
    block the running of a program).