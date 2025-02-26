from data import CountyDemographics

#task1
#fn returns the total population of the year 2014 across all counties.
def population_total(countydemos: list[CountyDemographics]) -> int:
    total = 0
    for i in countydemos:
        total += i.population['2014 Population']
    return total

#task2
#fn that returns a list of county demographics that are in the state passed in the fn param.
def filter_by_state(countydemos: list[CountyDemographics], sab: str) -> list[CountyDemographics]:
    lst = []
    for i in countydemos:
        if i.state == sab:
            lst.append(i)
    return lst

#task3
#fns that return total population across all counties which match the fields of education, ethnicity, and their income which is represented by the "Persons Below Poverty Level" key respectively.
def population_by_education(countydemos: list[CountyDemographics], edu: str) -> float:
    total = 0
    for i in countydemos:
        if edu in i.education:
            total += i.population['2014 Population'] * (i.education[edu]/100)
    return total

def population_by_ethnicity(countydemos: list[CountyDemographics], eth: str) -> float:
    total = 0
    for i in countydemos:
        if eth in i.ethnicities:
            total += i.population['2014 Population'] * (i.ethnicities[eth]/100)
    return total

def population_below_poverty_level(countydemos: list[CountyDemographics]) -> float:
    total = 0
    for i in countydemos:
        total += i.population['2014 Population'] * (i.income["Persons Below Poverty Level"]/100)
    return total

#task4
#fns that return percent of population across all counties that match the fields of education, ethnicity, and their income which is represented by the "Persons Below Poverty Level" key respectively.
def percent_by_education(countydemos: list[CountyDemographics], edu: str) -> float:
    total = population_total(countydemos)
    totaledu = population_by_education(countydemos, edu)
    if totaledu == 0:
        return 0
    return (totaledu/total)*100

def percent_by_ethnicity(countydemos: list[CountyDemographics], eth: str) -> float:
    total = population_total(countydemos)
    totaleth = population_by_ethnicity(countydemos, eth)
    if total == 0:
        return 0
    return (totaleth/total)*100

def percent_below_poverty_level(countydemos: list[CountyDemographics]) -> float:
    total = population_total(countydemos)
    totalbpl = population_below_poverty_level(countydemos)
    if total == 0:
        return 0
    return (totalbpl/total)*100

#task5
#fns that return a list of county demographics that are greater or lesser than the given threshold in the fields of education, ethnicity, and income below poverty level respectively.
def education_greater_than(countydemos: list[CountyDemographics], edu: str, lim: float) -> list[CountyDemographics]:
    return [i for i in countydemos if edu in i.education and i.education[edu] > lim]

def education_less_than(countydemos: list[CountyDemographics], edu: str, lim: float) -> list[CountyDemographics]:
    return [i for i in countydemos if edu in i.education and i.education[edu] < lim]

def ethnicity_greater_than(countydemos: list[CountyDemographics], eth: str, lim: float) -> list[CountyDemographics]:
    return [i for i in countydemos if eth in i.ethnicities and i.ethnicities[eth] > lim]

def ethnicity_less_than(countydemos: list[CountyDemographics], eth: str, lim: float) -> list[CountyDemographics]:
    return [i for i in countydemos if eth in i.ethnicities and i.ethnicities[eth] < lim]

def below_poverty_level_greater_than(countydemos: list[CountyDemographics], lim: float) -> list[CountyDemographics]:
    return [i for i in countydemos if "Persons Below Poverty Level" in i.income and i.income['Persons Below Poverty Level'] > lim]

def below_poverty_level_less_than(countydemos: list[CountyDemographics], lim: float) -> list[CountyDemographics]:
    return [i for i in countydemos if "Persons Below Poverty Level" in i.income and i.income['Persons Below Poverty Level'] < lim]



