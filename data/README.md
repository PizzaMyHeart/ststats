Two sources of data:
- https://specialtytraining.hee.nhs.uk/Resources-Bank (2013 - 2018)
- https://specialtytraining.hee.nhs.uk/Competition-Ratios (2015 - 2020)
... because why would you list all of them on the same page?

Table formatting is wildly inconsistent, with typos and ambiguous naming for good measure. Plus they are uploaded as PDFs which is a terrible format for data storage. 


All data in `data.csv`.

Notes:
- T&O ST1 Scotland only in 2020
- Anaesthetics at CT1/ST1 include ACCS from 2014
- Emergency Medicine at CT1/ST1 level is ACCS
- CMT and IMT includes ACCS Acute Medicine
- CMT changed to IMT in 2019
- CIT from 2016
- ST3 data only available from 2016 onwards

Steps to add new ratios:
1. Copy the PDF tables to a text file.
2. Break each row into lines: specialty, level, applications, posts, ratios. Save this as `{year}.text`.
3. Run maketables.ipynb on that text file.
4. Run clean.ipynb which will produce a cleaned csv file from all individual `{year}.csv`. files.
5. Update the default value for `year` in `app.py`.