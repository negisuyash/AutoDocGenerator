

---------------------------------DOCUMENT GENERATOR--------------------------------------


1.) dependencies for this to work are: python 3.6,blockdiag,sphinx

2.) put tree_generator.py in the folder where you want to generate sphinx documentation.

NOTE: __init__ file must be present in same folder in order to get full flow of the code.

3.) run tree_generator.py and fill details in sphinx-quickstart if separate build and source folder doesnt exist already there.

NOTE: always generate source and build folder separately which is first question asked in start of program.

4.) Code will run and generate a separate ReStructure Template(rst) file for each function and a page with full code flow.

5.) Code directly read documentation from docstring provided it is just under the function defination.

NOTE: always right docstring in between '''(triple single quotes) and not in between """(triple double quotes).
      use """(triple double quotes) for other purpose but '''(triple single quotes) are strictly reserved for docstring.

6.) NO need to change any comment or code if quote problem occurs. Just change file associated with function name from Source/<function_name>.rst .
