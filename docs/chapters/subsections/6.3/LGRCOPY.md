### LGRCOPY -- Activate Local Grid Refinement Inheritance

The LGRCOPY keyword actives Local Grid Refinement ("LGR") Inheritance option that allows the LGR to inherit the properties of the global or host cell containing a LGR grid block at the start of the GRID section, as oppose to the normal process of applying this transform at the end of the GRID section. LGRCOPY can be used in the RUNSPEC, GRID and EDIT sections. If used in the RUNSPEC section then the option is applied to all LGRs defined in the input file, whereas if used in the GRID and EDIT sections the keyword must be placed inside a LGR definition section, that is between a CARFIN (Cartesian LGR grid) or RADIN/RADIN4 (radial LGR grid) and the ENDFIN keyword. In the latter case inheritance is applied on an individual LGR basis.

See [LGRCOPY -- Activate Local Grid Refinement Inheritance](#anchor-1) in the RUNSPEC section for a full description.
