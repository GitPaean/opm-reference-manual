<a id="__RefHeading___Toc398952_3017686537"></a>

### SGOFLET -- Gas-Oil LET Relative Permeability Functions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SGOFLET defines the relative permeability and capillary pressure parameters for the gas-oil LET family of models. Both the gas and oil phases should be made active in the model via the GAS and OIL keywords in the RUNSPEC section. See section [Saturation Table Generation - LET Functions](#saturation-table-generation---let-functions) and Lomeland et al.[^1],[^2] [^3] and [^4] for further information on the model.

The keyword is used as a replacement for the SGOF keyword for three-phase oil-gas-water systems, and the LET series of keywords cannot be combined with the standard set of relative permeability keywords.

| 1 | SGL | SGL is a real positive number less than one that defines the connate gas saturation, that is smallest gas saturation in the LET function. | 0,0 |
| --- | --- | --- | --- |
| dimensionless | dimensionless | dimensionless |  |
| 2 | SGCR | SGCR is a real positive number greater than or equal to SGL and less than one, that defines the critical gas saturation, that is the largest gas saturation for which the gas relative permeability is zero. | 0,0 |
| dimensionless | dimensionless | dimensionless |  |
| 3 | LGAS | LGAS is a real positive number that defines the LET Lower empirical parameter Lg for the gas phase with the associated oil phase in the LET relative permeability equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 4 | EGAS | EGAS is a real positive number that defines the LET Elevation empirical parameter Eg for the gas phase with the associated oil phase in the LET relative permeability equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | TGAS | TGAS is a real positive number that defines the LET Top empirical parameter Tg for the gas phase with the associated oil phase in the LET relative permeability equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 6 | KRTGAS | KRTGAS is a real positive number less than one, that defines the relative permeability of gas at the maximum gas saturation Krgt in the LET relative permeability equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 7 | SORG | SORG is a real positive number less than one that defines the residual oil saturation in a gas-oil system in the LET equations. | 0,0 |
| dimensionless | dimensionless | dimensionless |  |
| 8 | SOGCR | SOGCR is a real positive number less than one that defines critical oil-in-gas saturation, that is the largest oil saturation for which the oil relative permeability is zero in a gas-oil system. | 0,0 |
| dimensionless | dimensionless | dimensionless |  |
| 9 | LOIL | LOIL is a real positive number that defines the LET Lower empirical parameter Lo for the oil phase with the associated gas phase in the LET relative permeability equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 10 | EOIL | EOIL is a real positive number that defines the LET Elevation empirical parameter Eo for the oil phase with the associated gas phase in the LET relative permeability equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 11 | TOIL | TOIL is a real positive number that defines the LET Top empirical parameter To for the oil phase with the associated gas phase in the LET relative permeability equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 12 | KRTOIL | KRTOIL is a real positive number less than or equal to one, that defines the relative permeability of oil at the residual oil saturation, Krot in the LET relative permeability equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 13 | LPC | LPC is a real positive number that defines the gas-oil LET Lower empirical parameter L in the LET capillary pressure equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 14 | EPC | EPC is a real positive number that defines the gas-oil LET Elevation empirical parameter E in the LET capillary pressure equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 15 | TPC | TPC is a real positive number that defines the gas-oil LET Top empirical parameter T in the LET capillary pressure equation. | 1,0 |
| dimensionless | dimensionless | dimensionless |  |
| 16 | PCIR | PCIR is a real positive number that defines the gas-oil capillary pressure at connate water saturation (SWL) in the LET capillary pressure equations. | 0,0 |
| psia | bars | atm |  |
| 17 | PCIT | PCIT is a real positive number that defines the gas-oil threshold capillary pressure at the maximum water saturation in the LET capillary pressure equations. | 0,0 |
| psia | bars | atm |  |
| Notes:<br>1)  The keyword is followed by NTSFUN definitions as declared on the TABDIMS keyword in the RUNSPEC section, with each definition consisting of the above 17 LET parameters.<br>2)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.152: SGOFLET Keyword Description

Note there a two versions of the LET functions, LET for two-phase flowing conditions and LETx^[^5]^ for three-phase flowing conditions. This keyword implements the LET version for a gas-oil system.

The functions are dependent on the drainage and imbibition cycle of the wetting phase as well as drainage and inhibition cycle number, since a reservoir may undergo several flooding events. To account for this the system defines the flooding event using the three saturations: Sw, So, and Sg together with the state of the three saturations during the flooding event. The saturation state can be Increasing, Decreasing, or Constant, for a given flooding event cycle number (n). Thus, Sw(D), So(I), Sg(C)1or DIC1, means the water phase is decreasing, the oil phase is increasing and the gas phase is constant for the primary or first cycle (n equals one). This is case for when oil is migrating into the reservoir rock and displacing the initial water contained with the reservoir.

See also the SGWFLET, and SWOFLET keywords in this section.

#### Example

The following example uses the SGOFLET keyword to define two relative gas-oil relative permeability tables, based on NTSFUN equals two on the TABDIMS keyword in the RUNSPEC section.

\--

\-- SGOFLET -- GAS-OIL LET REL. PERMEABILITY FUNCTIONS (OPM FLOW KEYWORD)

\--

SGOFLET

\-- SGL SGCR L-GAS E-GAS T-GAS KRT-GAS

\-- SOR SOGCR L-OIL E-OIL T-OIL KRT-OIL

\-- L-PC E-PC T-PC PCIR PCIT

\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

0.00000 0.0000 1.00000 1.00000 1.00000 1.00000

0.00000 0.0000 1.00000 1.00000 1.00000 1.00000

1\* 1\* 1\* 1\* 1\* / TABLE NO. 01

0.00000 0.0000 1.00000 1.00000 1.00000 1.00000

0.00000 0.0000 1.00000 1.00000 1.00000 1.00000

1\* 1\* 1\* 1\* 1\* / TABLE NO. 02

Here the SGOFLET keyword parameters are all set to their default values.

[^1]: Lomeland F., Ebeltoft E. and Thomas W.H., 2005. A New Versatile Relative Permeability Correlation. Paper SCA2005-32 presented at the International Symposium of the Society of Core Analysts held in Toronto, Canada, 21-25 August, 2005.

[^2]: Lomeland F. and Ebeltoft E., 2008. A New Versatile Capillary Pressure Correlation. Paper SCA2008-08 presented at the International Symposium of the Society of Core Analysts held in Abu Dhabi, UAE, 29 Oct. -- 2 Nov., 2008.

[^3]: Lomeland F., Hasanov B., Ebeltoft E. and Berge M., 2012. A Versatile Representation of Up-scaled Relative Permeability for Field Applications. Paper SPE 154487-MS presented at the EAGE Annual Conference & Exhibition incorporating SPE Europec held in Copenhagen, Denmark, 4-7 June 2012.

[^4]: Lomeland F., 2018.*Overview* *Of* *The* *Let* *Family* *Of* *Versatile* *Correlations* *For* *Flow* *Functions*. Paper SCA2018-056 *presented* at the International Symposium of the Society of Core Analysts held in Trondheim, Norway, 27-30 August 2018.

[^5]: Lomeland F. and Ebeltoft E., 2013. Versatile Three-phase Correlations for Relative Permeability and Capillary Pressure. Paper SCA2013-034 presented at the International Symposium of the Society of Core Analysts held in Napa Valley, California, USA, 16-19 September, 2013.
