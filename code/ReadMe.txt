ispl_generator.py generates .ispl files from .txt files.
- The .ispl files are for model checking (and generating the witness) using MCMAS.

The most useful options (of MCMAS) are:
-s interactive execution (i.e., simulation)
-c [1--3] specify the way counterexamples/witnesses are displayed
-c Number: this option is used to compute counterexamples (for false universal formulae) and witnesses
(for true existential formulae). For each formula for which such computation is possible, option 1 prints a
textual representation on screen; option 2 emits two ﬁles: “formulaN.dot” encoding the graphical repre-
sentation of the counterexample/witness path, and “formulaN.info” ﬁle containing a detailed description
of the states in the path, where N is the number of the formula; option 3 produces both the textual and
graphical representations.

-p specify the path to store counterexample files


- The following command can generate a picture from the .dot file:
  `dot -T png formula1.dot -o formula1.png`