### NETWORK -- Activate the Extended Network Option and Define Parameters

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the Extended Network option and defines the maximum number of nodes and links (branches) in the network. The Extended Network option is a different facility to the Standard Network facility, as such, this keyword should only be used if the former network is required for the run.

| 1 | NODMAX | NODMAX is a positive integer that defines the maximum number of nodes in the Extended Network model. | None |
| --- | --- | --- | --- |
| 2 | NBRMAX | NBRMAX is a positive integer that defines the maximum number of links in the Extended Network model. | None |
| 3 | NBCMAX | NBCMAX is a positive integer that defines the maximum number of branches that can be connected to a node in the Extended Network model, used in the commercial compositional simulator.<br>The parameter is ignored by OPM Flow and should be defaulted or set to the default value of 20. | 20 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.25: NETWORK Keyword Description

#### Example

\--

\-- ACTIVATE THE EXTENDED NETWORK OPTION AND DEFINE PARAMETERS

\--

\-- MAX. MAX NOT

\-- NODE LINK USED

NETWORK

10 12 1\* /

In the above example the maximum number of nodes is set equal to ten and the maximum number of links (or branches) is set equal to 12, for the Extended Network option.
