### Visualize Hurricanes data and performed simulation of Conway's game of life using Numpy and Matplotlib libraries.

#### Demonstrating Conway's game of life using 20 * 20 grid. The steps are as follows:
* Generating a random 20x20 matrix using boolean values and then converting into 0's and 1's form.
* There are 4 rules on which game is based. every cell checks its neihbours for alive or dead and then its status is decided.
* These rules are implemented by rotating the 20x20 matrix left,right,up and down. After 4 rotations,these 4 matrices are added.
* After summation, the value at each cell descibes the number of live neighbours of that cell.
* Each cell is designated 0 or 1 after implementing the rules on each cell.
* This gives the 1st generation and next generations can be calculated by first rotating, summation and then applying rules.
