### LGRCOPY -- Activate Local Grid Refinement Inheritance

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The LGRCOPY keyword actives the Local Grid Refinement ("LGR") Inheritance option that allows the LGR to inherit the properties of the global or host cell containing an LGR grid block when it is defined, as opposed to the normal process of applying this transform at the end of the GRID section. LGRCOPY can be used in the RUNSPEC, GRID and EDIT sections. If used in the RUNSPEC section then the option is applied to all LGRs defined in the input file, whereas if used in the GRID or EDIT sections the keyword must be placed inside a LGR definition section, that is between a CARFIN (Cartesian LGR grid) or RADFIN/RADFIN4 (radial LGR grid) keyword and an ENDFIN keyword. In the latter case inheritance is applied on an individual LGR basis.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator.

#### Example

The following example activates the LGR Inheritance option for all LGRs in the model.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\--

\-- ACTIVATE LOCAL GRID REFINEMENT INHERITANCE

\--

LGRCOPY
