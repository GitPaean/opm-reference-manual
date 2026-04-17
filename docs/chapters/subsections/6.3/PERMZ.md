### PERMZ -- Define the Permeability in the Z Direction for All the Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PERMZ defines the permeability in the Z direction for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PERMZ | PERMZ is an array of real positive numbers assigning the permeability in the Z direction to each cell in the model.<br>Repeat counts may be used, for example 200\*50.0. | None |
| mD | mD | mD |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.107: PERMZ Keyword Description

See also the PERMX and PERMY keywords to fully define the permeability for the model.

#### Example

The example below defines the PERMZ to be 50.0, 5.0, and 20.0 for the first, second and third layers in the model for all 300 cells, as defined by the DIMENS keyword in the RUNSPEC section.

\--

\-- DEFINE GRID BLOCK PERMZ DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

PERMZ

100\*50.0 100\*5.0 100\*20.0 /

The next example sets PERMX to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the DIMENS keyword in the RUNSPEC section. It then copies the PERMX values to the PERMY and PERMZ arrays, and finally multiplies PERMZ by 0.1 times to get the final values for PERMZ.

\--

\-- DEFINE GRID BLOCK PERMX DATA FOR ALL CELLS

\--

PERMX

100\*500.0 100\*50.0 100\*200.0 /

\--

\-- SOURCE DESTIN. \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

COPY

PERMX PERMY 1\* 1\* 1\* 1\* 1\* 1\* / CREATE PERMY

PERMX PERMZ 1\* 1\* 1\* 1\* 1\* 1\* / CREATE PERMZ

/

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

MULTIPLY

PERMZ 0.10000 1\* 1\* 1\* 1\* 1\* 1\* / PERMZ \* 0.1

/

The above sequence of keywords is quite common in input decks, that is copying the PERMX data to the PERMY and PERMZ arrays and then adjusting the PERMY and PERMZ arrays as required using the MULTIPLY keyword.
