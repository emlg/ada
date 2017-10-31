# Understanding EPF Tuition Fee raise

# Abstract

The idea of the project is to gain insight about why the EPF (both Lausanne and Zurich) will raise their tuition fee. Tuition fees raise are a source of great debate. We can understand that, in order to provide higher quality teaching, universities need more money. However, we can also understand that wealth should not be the criterion to access higher education.  
By analyzing the evolution of the different costs, the different funds, the number of students, the number of graduate, the number of scholarships, the number of staff and the projection of future number of students in the Swiss universities. Thanks to the Federal Institute of Statistics we have all those datasets available and detailed by canton. We will investigate for links explaining the need for greater fund from the students and whether the different cantons or domain of study have different schemes.


# Research questions

- What is the trend of the costs of universities ?
- How does the repartition between private and public funds evolve ?
- Do the private funds prefer EPF rather than universities ?
- Should the Tuition fee depend on your domain ?
- Are the number of staff and the number of students correlated ?
- In what criteria do the EPF situation differ from the Swiss universities situation ?
- Should we differentiate Swiss students from international students regarding tuition fees ?
- How many month/year of salary does it take to refund your tuition fee, depending on domain ?
- Can we relate the Tuition Fees evolution to the Research funds ?
- Can we spot some differences between EPFL and ETHZ ?

# Dataset

The files from opendata.swiss that are useful to us all come from the OFS (Office Fédéral de la Statistique). They are in a format called PC-AXIS. We found online a Python module that converts PC-AXIS files to Pandas Dataframes, which is the format we are used to (source : https://github.com/miseran/opendata/blob/master/px_reader.py).
With the following links, we can easily have a look at the data and select which part we want to download. Once on the website, click on "Preview" (or "Aperçu" in French). You will arrive on a temporary OFS website where you can select the years, universities and categories that you would like to see. You will now be able to download the file corresponding to the previewed data.

- Scholarship numbers : https://opendata.swiss/fr/dataset/stipendien-bezugerinnen-und-bezuger-nach-kanton-geschlecht-und-altersklasse
- Scholarship amount depending on level of diploma : https://opendata.swiss/fr/dataset/stipendien-betrag-bezugerinnen-und-bezuger-nach-kanton-und-bildungsstufe/resource/43b63d21-8593-463d-96be-aeb14c33c4a1
- Cost coverage : https://opendata.swiss/fr/dataset/deckung-der-kosten-der-universitaren-hochschulen-nach-fachbereich-leistung-erloskategorie-und-hochsc
- Cost coverage by financial source : https://opendata.swiss/fr/dataset/deckung-des-aufwands-der-universitaren-hochschulen-nach-finanzquelle-und-hochschule/resource/6adb1f81-bd84-4fff-827c-56e00fe3d106
- Cost (running, staff, buildings) : https://opendata.swiss/fr/dataset/aufwand-der-universitaren-hochschulen-nach-hochschule-fachbereich-aufwandsart-und-finanzierungstyp/resource/4602599f-393d-492d-84cf-ec6035b9811b
- Staff per domain and category : https://opendata.swiss/fr/dataset/personal-der-universitaren-hochschulen-nach-fachbereich-personalkategorie-und-hochschule-in-personen/resource/e85ba97e-153a-45e1-bfa8-fa684f27efb6
- Diplomas per domain and nationality : https://opendata.swiss/fr/dataset/abschlusse-der-universitaren-hochschulen-nach-jahr-examensstufe-fachrichtung-staatsangehorigkeit-und/resource/3582eeb3-e871-4d31-b3a0-a815b99e47ce
- Students entering at Bachelor level : https://opendata.swiss/fr/dataset/px-x-1502040100_124
- Students by domain : https://opendata.swiss/fr/dataset/studierende-an-den-universitaren-hochschulen-nach-jahr-fachrichtung-staatsangehorigkeit-und-hochschu/resource/d3835acf-266f-472f-882f-21a3e301094b
- Prediction of students : https://opendata.swiss/fr/dataset/px-x-1509090000_111/resource/ea5dd8a2-ccde-4dac-b110-249ea81a6a5c

We can see that the data is well organized with some index similar to the Pandas dataframe. We can see that the variables names are consistent form one file to the other.

# A list of internal milestones up until project milestone 2

- Retrieve all the data files from the Swiss Institute of Statistics
- Correctly import them into Pandas dataframes
- Check for missing data
- Visualize data by canton, by university, by domain but keep the x-axis for time
- Determine if they are correlations (exploratory analysis)
- Determine if we keep data before the last raise of tuition fee

# Questions for TAs

- How much of our project should be spent on visualization ?
- Is our subject too general ?
- Is it okay to process only numerical data ?
- Can we get additional external datasets (for example inflation of Swiss franc over the years, or salary after diploma depending on field of study)?
