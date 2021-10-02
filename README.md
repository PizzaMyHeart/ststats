# ST Stats

ST Stats is a dashboard that illustrates the competitiveness of specialty training for doctors in the UK. 

![Screenshot](./assets/screenshot.png?raw=true "Screenshot")

## Data sources

The data are taken from Health Education England's specialty training [website](https://specialtytraining.hee.nhs.uk/). HEE has published the competition ratios for specialty training posts every year since 2013. Unfortunately, this takes the form of PDF files, which are fine for viewing individually, but an awful headache to use for any form of analysis. The [data folder](./data) in this repo contains CSV file version of each year's competition ratio data, as well as a CSV file (`data.csv`) containing one unified, cleaned table of all the data. 

The original PDF sources can be found [here](https://specialtytraining.hee.nhs.uk/Competition-Ratios) and [here](https://specialtytraining.hee.nhs.uk/Resources-Bank) (because why would you keep them all in one place?).

This is a hobby project unaffiliated with Health Education England in any way.


### Notes on specialties

- Anaesthetics at CT1/ST1 entry includes ACCS

- Emergency Medicine at CT1/ST1 entry is via ACCS

- Core Medical Training (CMT) was changed to Internal Medicine Training (IMT) in 2019. These are all grouped together in the charts.

- CMT/IMT posts include ACCS entry

- Some training posts have only been offered in one year e.g. Trauma & Orthopaedics at ST1. 



## Usage

1. Select the recruitment level (CT/ST1, ST3, ST4) from the dropdown box.

2. Double-click or double-tap quickly on the desired specialty in the legend on the right-hand side of the first chart.

3. Click or tap once on other specialties you want to add to the chart.

4. Click on data points on the first chart to view specific information for that specialty in the bottom two charts.

5. Hover over bars and lines to view more information.


## Packages

- [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/) for dashboard

- [Pandas](pandas.pydata.org/) for data processing

Full list in `requirements.txt`.