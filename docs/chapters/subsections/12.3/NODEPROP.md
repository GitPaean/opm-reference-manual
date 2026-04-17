### NODEPROP -- Define Network Node Properties for Extended Network

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the network node properties for the extended network option for when the Extended Network Model has been invoked by the NETWORK keyword in the RUNSPEC section. There are two types of network facilities in the simulator, the Standard Network model, which is defined with the GRUPNET keyword in the SCHEDULE section and the Extended Network Model defined by the BRANPROP and NODEPROP keywords, again in the SCHEDULE section.

For the Extended Network Model the group hierarchy can be different to that defined by the GRUPTREE keyword; however, the bottom most nodes in the network tree associated with wells, must be the same as that defined by the GRUPTREE keyword.

| 1 | NODE | A character string of up to eight characters in length that defines the node name for the data on this keyword record. | None |
| --- | --- | --- | --- |
| 2 | PRESS | A real value that sets the terminal fixed pressure for the node, this should be set to:<br>1)  A real positive value to define the fixed pressure for the node if the node is a terminal node, otherwise:<br>2)  PRESS should be set to the default value of 1\* or a real negative value if the node is not a terminal node. | 1\* |
| psia | bars | atm |  |
| 3 | CHOKE | CHOKE is a defined character string that sets if the downstream branch (or uptree branch, being the one closer towards the terminal node) from this node should have the capability to choke back the flow rate in order impose a flow constraint.<br>Here the downstream branch is the node furthermost from the wells. Thus for a production network, this will be an outlet branch as the wells are exporting fluid from the branch node. Whereas for an injection node, this is an inlet branch as the wells are importing the injection fluid. | NO |
| 4 | GASLIFT | A defined character string that sets if the associated subordinate well's produced gas lift gas should be included in the node's flow stream (YES), or not (NO). GASLIFT should be set to either:<br>1)  NO: Do not include gas lift gas in the node\'s production. This means that only the produced gas from the node\'s subordinate wells will be included in the node\'s production stream.<br>2)  YES: Include both gas lift gas and produced gas in the node\'s production. This means that all gas from the subordinate wells will be included in the node\'s production stream.<br>If NODE does not have any subordinate wells or satellite groups (see the GSATPROD keyword in the SCHEDULE section) directly attached to the node, then GASLIFT should be defaulted (1\*) or set to NO. The option is only valid for producing networks | NO |
| 5 | GROUP | A character string of up to eight characters in length that defines the group for which the automatic choke will be applied in order to match the group's target rate (the TARGET variable on the GCONPROD keyword in the SCHEDULE section). The target rate is matched by adjusting the pressure drops across the automatic choke.<br>The default value of 1\* uses NODE (item one) as the group if it exists in the run. In addition, if NODE is just connected to subordinate wells then GROUP should also be defaulted. | 1\* |
| 6 | GRPNAME | GRPNAME defines the name of the source or sink group in the commercial compositional simulator; however, the variable is not used as sources and sinks nodes must have the same name as their comparable groups in the Extended Network Model in both OPM Flow and the commercial black-oil simulator. | 1\* |
| 7 | NETYPE | NETYPE defines the network type in the commercial compositional simulator: PROD, WINJ or GINJ. However, the variable is not used as only production networks are supported in the Extended Network Model in both OPM Flow and the commercial black-oil simulator. | 1\* |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.57: NODEPROP Keyword Description

See also the NETWORK keyword in the RUNSPEC section and the BRANPROP in the SCHEDULE section.

#### Example

Given the following Extended Network model in .

First the Extended Network model should be used invoked in the RUNSPEC section, and then the BRANPROP keyword should be used to define the branch network, and finally the NODEPROP keyword is used to describe the node properties with the network.

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
