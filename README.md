# LindenmayerSystem
Lindenmayer system for GE IPDP
Lindenmayer systems
Introduction
In this project you must develop, test, and document a program for computing and plotting Lindenmayer
systems. You must implement the functions and main script described in the following according to the specifications.
Lindenmayer systems A Lindenmayer system is defined iteratively, and it consists of: a) an alphabet of
symbols which can be used to create strings, b) an initial string used to begin the iterative construction and
c) replacement rules that specify how to replace selected symbols of the string by strings of symbols (from the
same alphabet). Originally, these Lindenmayer systems were used to describe the behaviour of plant cells and
to model the growth processes of plant development. In this exercise you will work with two systems called the
Koch curve and the Sierpinski triangle.
Koch curve The Koch curve can be generated using a) an alphabet consisting of the symbols S, L and R, b) the
initial string ’S’ and c) the replacement rules
S → SLSRSLS
L → L
R → R
The initial string is S. After the first iteration one obtains the string SLSRSLS. After the second iteration
one obtains the string SLSRSLSLSLSRSLSRSLSRSLSLSLSRSLS. The first three iterations are visualized using
turtle graphics (see below) in Fig. 2D.1.
Sierpinski triangle The Sierpinski triangle can be generated using a) an alphabet consisting of the symbols A,
B, L and R, b) the initial string A and c) the replacement rules for each step of the iteration.
A → BRARB
B → ALBLA
L → L
R → R
The initial string is A. After the first iteration one obtains the string BRARB. After the second iteration
one obtains the string ALBLARBRARBRALBLA. The inititalization and the result after iteration 4 and 8 is
visualized using turtle graphics (see below) in Fig. 2D.2.
Visualization using turtle graphices The sequence of symbols in the string will be visualized graphically
by translating each symbol in a command for a so-called turtle graphics: S, A, and B is interpreted as the line
segment from an initial location (we will use the origin of the planar coordinate system for this) drawn along
an initial direction — we use for this the canonical basis vector (1, 0)T
. L is interpreted as turning left with
the angle 1
3
π and R as turning right with the angle −
2
3
π (Koch) or −
1
3
π (Sierpinski). The length of the line
segment is scaled by a factor 1
3
(Koch) or 1
2
(Sierpinski) after each iteration step.
Iteration 0 Iteration 1 Iteration 2
Figure 2D.1: Graphical representation of the first iterations of the Koch curve.
17
Project 2D. Lindenmayer systems
Iteration 0 Iteration 4 Iteration 8
Figure 2D.2: Graphical representation of the initial, fourth and eights iteration of the Sierpinski triangle.
Lindenmayer Iteration
Interface def LindIter(System, N):
# Insert your code here
return LindenmayerString
Input arguments System: A string containing the name of the Lindenmayer system currently under
scrutiny. The input can take the values Koch or Sierpinski.
N: The number of iterations that should be calculated.
Output arguments LindenmayerString: A string containing the output after N iterations of the chosen
Lindenmayer system.
User input No.
Screen output No.
Description The function must calculate N iterations of the system specified by System according
to the replacement rules for the Koch curve and Sierpinski triangle respectively.
The output of the iteration function should be stored in the string
LindenmayerString.
Translation to turtle graphics commands
Interface def turtleGraph(LindenmayerString):
# Insert your code here
return turtleCommands
Input arguments LindenmayerString: A string of symbols representing the state of the system after
the Lindemayer iteration.
Output arguments turtleCommands: A row vector containing the turtle graphics commands consisting
of alternating length and angle specifications [l1, φ1, l2, φ2, . . . ].
User input No.
Screen output No.
Description This function translates the string of symbols in LindenmayerString into a sequence
of turtle graphics commands. The output consists of a row vector of numbers, which
alternate between a number specifying the length of a line to be drawn and a number
specifying the angle of the new line segment with respect to the drawing direction of
the last line segment.
Your function function should use the replacement rules consistent with the Lindenmayer system you choose to investigate. Which system this is can either be inferred
18
Project 2D. Lindenmayer systems
from the input LindenmayerString directly, or passed to the function by augmenting
it by further input or output variables in the functions you program. You are free to
choose how to implement this and creativity is appreciated.
Turtle graphics plot function
Interface def turtlePlot(turtleCommands):
# Insert your code here
Input arguments turtleCommands: A row vector consisting of alternating length and angle specifications [l1, φ1, l2, φ2, . . . ].
Output arguments No.
User input No.
Screen output Yes (plot, see specifications below.)
Description The plot function should turn the input vector turtleCommands into a graphical
visualisation. This can be done by specifying the coordinates of the corners ~x = (x, y)
of the straight line segments with a plot command. To find these coordinates, your
function should follow the input vector, starting at the origin of the planar coordinate
system and adding a new pair of coordinates after every line segment. The line
segment has the length li
, and must be drawn at an angle φi with respect to the
previous line (as specified in the input vector of turtleCommands). The initial point
is ~x0 = (0, 0)T and the initial direction is along a unit vector ~d0 = (1, 0)T
. Here a
positive angle corresponds to turning left, and a negative one to turning right. The
computation of the vector pointing to the point ~xi+1 by using the previous point ~xi
and previous drawing direction ~di with
~di+1 =

cos(φi+1) − sin(φi+1)
sin(φi+1) cos(φi+1)

·
~di (2D.1)
~xi+1 = ~xi + li+1 ·
~di+1 (2D.2)
The results can be checked by comparing them with Fig. 2D.1 and 2D.2. The plots
should include a suitable title, descriptive axis labels, and a data legend where appropriate. You are allowed to present the plots in separate figure windows or as sub-plots
in a single figure window.
Main script
Interface Must be implemented as a script.
Input arguments No.
Output arguments No.
User input Yes (see specifications below.)
Screen output Yes (see specifications below.)
Description The user interacts with the program through the main script. When the user runs
the main script he/she must have at least the following options:
1. Choose the type of Lindenmayer system and the number of iterations.
2. Generate plots.
3. Quit.
19
Project 2D. Lindenmayer systems
The user must be allowed to perform any reasonable number of Lindenmayer iterations
for the chosen Lindenmayer system and subsequent graphical presentation of the
obtained strings. The details of how the main script is designed and implemented is
for you to determine. It is a requirement that the program is interactive, and you
should strive to make it user friendly by providing sensible dialogue options. Consider
what you would expect if you were to use such a script, and what you think would
be fun. Play around and make a cool script.
Error handling You must test that all input provided by the user are valid. If the user gives invalid
input, you must provide informative feedback to the user and allow the user to provide
the correct input. This includes also unreasonable choices with respect to the number
of iterations (e.g. because of computational time).
1. Choose Lindenmayer system When the user chooses a Lindenmayer system, you must ask the user to input
one of the options listed in the following table.
Input Option Name
1 Koch curve
2 Sierpinski triangle
2. Generate plots If the user chooses to generate plots, call the turtlePlot function to display the plots
corresponding to the current Lindenmayer system.
3. Quit If the user chooses to quit the program, the main script should stop.
Possible extension As a possible extension (not required) you could allow a user to define a new Lindenmayer system and to compute iterations of that and visualize this graphically.
Further possibilities are to compute certain properties of the Lindenmayer systems
like the curve length depending on the number of iterations.
