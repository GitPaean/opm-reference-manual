### BRANPROP -- Define Network Branch Properties for Extended Network Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

BRANPROP defines network branch properties for the extended network option for when the Extended Network Model has been activated by the NETWORK keyword in the RUNSPEC section. There are two types of network facilities in the simulator, the Standard Network model, which is defined with the GRUPNET keyword in the SCHEDULE section and the Extended Network Model defined by the BRANPROP and NODEPROP keywords, again in the SCHEDULE section.

For the Extended Network Model the group hierarchy can be different to that defined by the GRUPTREE keyword; however, the bottom most nodes in the network tree associated with wells, must be the same as that defined by the GRUPTREE keyword.

| 1 | DOWNNODE | A character string of up to eight characters in length that defines the down stream node name for this branch, that is the node closest to the wells. Thus for a production network, this will be an inlet node as the wells are importing fluid into the branch node. Whereas for an injection node, this is an outlet node as injection fluid is being exported to the wells. | None |
| --- | --- | --- | --- |
| 2 | UPNODE | A character string of up to eight characters in length that defines the up stream node name for this branch, that is the node furthermost from the wells. Thus for a production network, this will be an outlet node as the wells are exporting fluid from the branch node. Whereas for an injection node, this is an inlet node as the wells are importing the injection fluid. | None |
| 3 | VFPTAB | A positive integer greater than or equal to zero that defines the vertical lift performance table to be used for calculating the pressure behavior between the inlet (for production) or outlet (for injection) node (DOWNNODE) and the outlet (for production) or inlet (for injection) node (UPNODE). For a production network this must reference a table associated with the VFPPROD keyword, and for an injection network a table declared via the VFPINJ keyword. Both keywords are in the SCHEDULE section.<br>If the pressure behavior between the two nodes is zero (no pressure loss in the network branch), then a value of 9999 should be entered for this variable.<br>A value of zero for VFPTAB removes the branch from the extended network and the resulting flows are ignored in the network flow stream. | None |
| 4 | ALQ-NODE | A real positive value that defines the artificial lift quantity to be used in conjunction with the VFPPROD assigned to the branch via the VPFTAB variable.<br>VFPTAB vertical lift performance table and the artificial lift quantity ALQ-NODE are used with the branch fluid rates to calculate the pressure behavior through the branch. For a network this can be considered to be either a pump to pump fluid through the network or a compressor to compress gas to a higher export pressure. Basically, ALQ-NODE is used to reduce the pressure loss through the branch.<br>Note that the units for ALQ-NODE are dependent on the associated variable on the VFPPROD keyword.<br>Should be set to zero if ALQ-DEN is set to either DENO or DENG, or if the branch is associated with an automatic compressor. | 0.0 |
| 5 | ALQ-DEN | A defined character string that defines that ALQ-NODE variable represents either as a surface density or as an artificial lift quantity for a pump or a compressor, and should be set to one of the following:<br>1)  DENO: ALQ-NODE represents the average surface oil density flowing through the branch.<br>2)  DENG: ALQ-NODE represents the average surface gas density flowing through the branch.<br>3)  NONE: ALQ-NODE is the artificial lift quantity as defined on the VFPPROD keyword to model a pump or a compressor.<br>The VFPPROD keyword should be consistent with this variable, that is, if ALQ-DEN is set to to DENO then the surface oil should be used as the ALQ variable on the VFPPROD keyword. | NONE |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

*Table 12.9: BRANPROP Keyword Description*
See also the NETWORK keyword in the RUNSPEC section and the NODEPROP keyword in the SCHEDULE section.

#### Example

Given the following Extended Network model in .

First the Extended Network model should be used invoked in the RUNSPEC section, and then the BRANPROP keyword should be used to define the branch network, and finally the NODEPROP keyword is used to describe the node properties.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\--

\-- ACTIVATE THE EXTENDED NETWORK OPTION AND DEFINE PARAMETERS

\--

\-- MAX. MAX NOT

\-- NODE LINK USED

NETWORK

3 2 1\* /

...................

...............

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\--

\-- EXTENDED NETWORK BRANCH PROPERTIES

\--

\-- DOWN UP VFP VFP

\-- NODE NODE TABLE ALFQ

BRANPROP

B1 PLAT-A 5 1\* /

C1 PLAT-A 4 1\* /

/

\--

\-- EXTENDED NETWORK NODE PROPERTIES

\--

\-- NODE NODE CHOKE GAS CHOKE SOURCE NETWORK

\-- NAME PRESS OPTN LIFT GROUP SINK TYPE

NODEPROP

PLAT-A 21.0 NO NO /

B1 1\* NO NO /

C1 1\* NO NO /

/

Here the main platform for the field, PLAT-A, has a fixed 21 barsa pressure applied as an operating constraint.
