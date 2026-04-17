### FIP -- Define the Fluid In-Place Names and Region and Numbers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FIP keyword defines the fluid in-place name and the associated region numbers for each grid block. The simulator can print out summaries of the fluid in-place in each region, the current flow rates between regions, and the cumulative flows between regions. This keyword is not in the standard keyword format due to the fluid in-place name being concatenated to the keyword FIP to fully define the keyword.

Note that the total number of FIP and FIPNUM regions must be defined by the NMFIPR variable on the REGDIMS keyword, or the NTFIP variable on the TABDIMS keyword. Both keywords are in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | FIPNAME | A character string of up to eight characters, consisting of FIP as the first three characters followed by up to a five letter character string defining the fluid in-place's name. | None |
| 2 | FIPNUM | FIPNUM defines an array of positive integers greater than or equal to one, that assigns a grid cell to a particular fluid in-place region named by FIPNAME.<br>The maximum number of FIP and FIPNUM regions is set by the REGDIMS(NMFIPR) or the TABDIMS(NTFIP) keywords(variables) in the RUNSPEC section. If both REGDIMS(NMFIPR) and TABDIMS(NTFIP) have been defined then the maximum of the two is used. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If a cell is not assigned a FIP region number by the end of the REGION section then the fault value of one will be used.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 9.4: FIP Keyword Description

The keyword behaves the same as the FIPNUM keyword except the full name of the keyword, including the concatenated characters, are used as the property region name. For example, if we wish define a fluid in-place region name called UNIT, then the keyword would be FIPUNIT.

The region property data for FIP arrays can be written to the SUMMARY file, and the RSM file if requested, similar to the FIPNUM regions, with some caveats:

3)  1)  1)  Only SUMMARY keywords for regions may be used, that is the SUMMARY variable name must begin with the letter R.

        2)  The SUMMARY variable name must consist of a character string length of exactly five characters, if less than five characters, then the "\_" character should be used to fill out the SUMMARY variable name. For example, instead of RPRUNIT, use RPR\_\_UNI, or instead of ROIPUNIT, use ROIP_UNI.

        3)  Only the first three characters of the FIP region name should be concatenated with the SUMMARY variable name. This means if the FIP region name is UNIT, the FIP keyword would be FIPUNIT; however, to access the regional pressures for FIPUNIT, one should use RPR\_\_UNI, or to access the regional oil in-place one would use ROIP_UNI.

See also the FIPOWG keyword in the REGIONS section that automatically defines the fluid-in-place regions at the start of the run based the gas, oil and water zones at the time the model was initialized.

#### Example

The example below defines a region name of UNIT and sets three FIPUNIT regions for a 4 x 5 x 2 model.

\--

\-- DEFINE FIPUNIT FIP REGIONS FOR ALL CELLS

\--

FIPUNIT

2 2 1 1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 3 1 1 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

/

The second example is based on the Norne model that defines two FIP regions based on geological layers and numerical layers using the EQUALS keyword.

\-- FIPGL BASED ON GEOLOGICAL LAYERS

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

FIPGL 1 1 46 1 112 1 3 / Garn

FIPGL 2 1 46 1 112 4 4 / Not

FIPGL 3 1 46 1 112 5 5 / Ile 2.2

FIPGL 4 1 46 1 112 6 8 / Ile 2.1

FIPGL 5 1 46 1 112 9 11 / Ile 1

FIPGL 6 1 46 1 112 12 12 / Tofte 2.2

FIPGL 7 1 46 1 112 13 15 / Tofte 2.1

FIPGL 8 1 46 1 112 16 18 / Tofte 1

FIPGL 9 1 46 1 112 19 22 / Tilje

\--

\-- FIPNL BASED ON NUMERICAL LAYERS

\--

FIPNL 1 1 46 1 112 1 1 / Garn 3

FIPNL 2 1 46 1 112 2 2 / Garn 2

FIPNL 3 1 46 1 112 3 3 / Garn 1w

FIPNL 4 1 46 1 112 4 4 / Not

FIPNL 5 1 46 1 112 5 5 / Ile 2.2

FIPNL 6 1 46 1 112 6 6 / Ile 2.1.3

FIPNL 7 1 46 1 112 7 7 / Ile 2.1.2

FIPNL 8 1 46 1 112 8 8 / Ile 2.1.1

FIPNL 9 1 46 1 112 9 9 / Ile 1.3

FIPNL 10 1 46 1 112 10 10 / Ile 1.2

FIPNL 11 1 46 1 112 11 11 / Ile 1.1

FIPNL 12 1 46 1 112 12 12 / Tofte 2.2

FIPNL 13 1 46 1 112 13 13 / Tofte 2.1.3

FIPNL 14 1 46 1 112 14 14 / Tofte 2.1.2

FIPNL 15 1 46 1 112 15 15 / Tofte 2.1.1

FIPNL 16 1 46 1 112 16 16 / Tofte 1.2.2

FIPNL 17 1 46 1 112 17 17 / Tofte 1.2.1

FIPNL 18 1 46 1 112 18 18 / Tofte 1.1

FIPNL 19 1 46 1 112 19 19 / Tilje 4

FIPNL 20 1 46 1 112 20 20 / Tilje 3

FIPNL 21 1 46 1 112 21 21 / Tilje 2

FIPNL 22 1 46 1 112 22 22 / Tilje 1

/

Then in order to get the reservoir pressure for the regions and the in-place oil volumes SUMMARY variables written to the SUMMARY file, one would use the following SUMMARY variable names in the SUMMARY section

\-- ==============================================================================

\--

\-- SUMMARY SECTION

\--

\-- ==============================================================================

SUMMARY

\-- FIP REGION REPORTING

\--

ROIP_GL

/

ROIP_NL

/

RPR\_\_GL

/

RPR\_\_NL

/

Notice how the "\_" character has been used to extend the SUMMARY variable name to five characters.
