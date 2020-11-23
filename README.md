# 626 Project
### Analyzing the effects of COVID-19 on film permits issued in NYC.

* Initial Question
- Many industries took a hit during the covid-19 pandemic. One industry that especially took a large hit was the film industry. Production all over the country was delayed as it requires large film crews to make a film work. One of the most popular places in the world to film is NYC. For my project I would like to look at open NYC data set for 'Film Permits' and compare that dataset with the 'Covid 19 Daily Count of Cases, Hospitalization, and Deaths' dataset and see if there is a connection between what I presume is to be less film permits while the number of Covid cases rise. This is obviously a very rough outline for what I intend to do with my final project, but I would like to hear your input to see if this is a reasonable project idea. I have an idea what story the data might tell, but like you said a lot of this class deals with the preprocessing and cleaning of data and I think these datasets could offer that.

* Outline

- Downloaded the COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv and Film_Permits.csv from the website NYC Open Data
- Created subsets of each dataset with the columns of data that I needed to access.  
      - For film permit subset just included 2020 data since virus data did not start until 2/29/2020
- Merged the two csv files
- Created dictionary to see number of permits issued each date
      - Created new subset which I was able to merge into csv file that I could compare the total number of permits issues each day compared to the number of virus cases each day
- Wanted to make dictionary with dates from 1/1/2020 to 9/1/2020 returning values of number of cases and permit for each day

* Results
![2020 NYC Film Permits Issued](Images/filmpermits.png)
![2020 NYC COVID-19 Cases](Images/covid19cases.png)
![NYC Film Permits Issued vs COVID-19 Cases](Images/626project.png)
* Summary
