### DUALPERM -- Activate Dual Permeability Model

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [DUALPERM](#__RefHeading___Toc241171_1772380413) keyword activates the Dual Permeability option and the Dual Porosity option for the run. In a dual porosity system flow occurs between the matrix and the fracture only, whereas in a dual permeability system flow also occurs between the matrix grid blocks[^1], [^2], [^3], [^4] and [^5].

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE DUAL PERMEABILITY MODEL

\--

DUALPERM

The above example declares that the Dual Permeability option is active for the run.

[^1]: Warren, J.E. and Root, P.J. 1963. The Behavior of Naturally Fractured Reservoirs. SPE J. 3 (3): 245--255. SPE-426-PA. http://dx.doi.org/10.2118/426-PA.

[^2]: Gringarten, A.C. 1984. Interpretation of Tests in Fissured and Multilayered Reservoirs With Double-Porosity Behavior: Theory and Practice. J Pet Technol 36 (4): 549-564. SPE-10044-PA. http://dx.doi.org/10.2118/10044-PA.

[^3]: Serra, K., Reynolds, A.C., and Raghavan, R. 1983. New Pressure Transient Analysis Methods for Naturally Fractured Reservoirs(includes associated papers 12940 and 13014 ). J Pet Technol 35 (12): 2271-2283. SPE-10780-PA. http://dx.doi.org/10.2118/10780-PA

[^4]:  Barenblatt, G.E., Zheltov, I.P., and Kochina, I.N. 1960. Basic Concepts in the Theory of Homogeneous Liquids in Fissured Rocks. J. Appl. Math. Mech. 24: 1286-1303.

[^5]: Kazemi, H., Merrill JR., L. S., Porterfield, K. L., and Zeman, P. R. "Numerical Simulation of Water-Oil Flow in Naturally Fractured Reservoirs," paper SPE 5719, Society of Petroleum Engineers Journal(1976) 16, No. 6, 317-326.
