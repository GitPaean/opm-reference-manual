<a id="__RefHeading___Toc27871_3671211675"></a>

### CPR -- Activate Constrained Pressure Residual ("CPR") Linear Solver

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

Turns on the Constrained Pressure Residual ("CPR")[^1],^\ [^2]\ ^and [^3] preconditioner linear solver option, and declares how the solver should be applied. The keyword is equivalent to using the OPM Flow command line parameter \--linear-solver= "cprw". Note that if the command line has been used, then this will take precedence over the [CPR](#__RefHeading___Toc27871_3671211675) keyword.

+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+
| > No.                                     | > Name    | > Description                                                                                                                                                                                         | > Default  |
+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+
| > 1                                       | > CPROPTN | > A defined character string that determines how the CPR linear solver should be applied, and should be set to one of the following:                                                                  | > ORIGINAL |
|                                           |           |                                                                                                                                                                                                       |            |
|                                           |           | 1)  ORIGINAL: Here the solver is applied for the whole of the simulation.                                                                                                                             |            |
|                                           |           |                                                                                                                                                                                                       |            |
|                                           |           | 2)  ADAPTIVE: This option applies the more computational demanding CPR linear solver, only in parts of the run that would benefit from its use, for example when linear convergence is challenging.   |            |
|                                           |           |                                                                                                                                                                                                       |            |
|                                           |           | > Note that OPM Flow only supports the ORIGINAL option, which is the default value in OPM Flow, whereas the default value in the commercial simulator is ADAPTIVE. .                                  |            |
+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+
| > Notes:                                  |           |                                                                                                                                                                                                       |            |
|                                           |           |                                                                                                                                                                                                       |            |
| 1)  The keyword is terminated by a "/".   |           |                                                                                                                                                                                                       |            |
+-------------------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+

Table 5.8: CPR Keyword Description

See section [Running OPM Flow From The Command Line](#running-opm-flow-from-the-command-line) on how to invoke various numerical schemes via the OPM Flow command line interface.

#### Example

\--

\-- ACTIVATE CONSTRAINED PRESSURE RESIDUAL LINEAR SOLVER FOR THE RUN

\--

CPR

/

The above example activates the Constrained Pressure Residual preconditioner linear solver using the default option, that is the ORIGINAL option for OPM Flow.

To enable the CPR preconditioner linear solver option using the command line parameter, use:

flow \--linear-solver=\"cpr\" CASENAME.DATA

which should usually be combined with the -matrix-add-well-contributions=true option, that is:

flow \--linear-solver=cpr \--matrix-add-well-contributions=true CASENAME.DATA

However, the new CPRW preconditioner, that includes wells does not need the latter option, so in this instance use:

flow \--linear-solver=cprw CASENAME.DATA

As of this release the CPRW preconditioner, should be considered experimental, and the recommended configuration for running this is:

flow \--linear-solver=cprw \--linear-solver-reduction=0.005 \--cpr-reuse-setup=4

\--cpr-reuse-interval=10 CASENAME.DATA

See new Rasmussen et al.[^4] for further information on the available numerical algorithms available in OPM Flow.

[^1]: Wallis, J. R., Little, T. E., and Nolen, J. S.: \"Constrained Residual Acceleration of Conjugate Residual Methods,\" paper SPE 13536 presented at the SPE Reservoir Simulation Symposium, Dallas, Texas, USA (February 10-13, 1985).

[^2]: R. Scheichl, M. Roland, J. Wendebourg, Decoupling and block preconditioning for sedimentary basin simulations, Computational Geosciences 7 (2003) 295{318.

[^3]: Klemetsdal, Ø.S., Møyner, O. & Lie, KA. Accelerating multiscale simulation of complex geomodels by use of dynamically adapted basis functions. Comput Geosci 24, 459--476 (2020). https://doi.org/10.1007/s10596-019-9827-z.

[^4]: Atgeirr Flø Rasmussen, Tor Harald Sandve, Kai Bao, Andreas Lauser, Joakim Hove, Bård Skaflestad, Robert Klöfkorn, Markus Blatt, Alf Birger Rustad, Ove Sævareid, Knut-Andreas Lie, Andreas Thune, The Open Porous Media Flow reservoir simulator, Computers & Mathematics with Applications, Volume 81, 2021, Pages 159-185, ISSN 0898-1221, <https://doi.org/10.1016/j.camwa.2020.05.014>. (https://www.sciencedirect.com/science/article/pii/S0898122120302182).
