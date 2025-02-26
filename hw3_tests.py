from functools import reduce
from idlelib.debugger_r import restart_subprocess_debugger
from unittest import expectedFailure, removeResult

import data
import build_data
import unittest

from hw3 import population_total, population_by_ethnicity, filter_by_state, population_by_education, \
    population_below_poverty_level, percent_by_education, percent_by_ethnicity, percent_below_poverty_level, \
    education_greater_than, education_less_than, ethnicity_greater_than, ethnicity_less_than, \
    below_poverty_level_less_than, below_poverty_level_greater_than

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass
    # Part 1
    # test population_total
    def test1(self):
        self.assertEqual(population_total(reduced_data), 655813)

    def test12(self):
        self.assertEqual(population_total(full_data), 318857056)


    # Part 2
    # test filter_by_state
    def test21(self):
        self.assertEqual(len(filter_by_state(reduced_data, "CA")), 2)

    def test22(self):
        self.assertEqual(len(filter_by_state(full_data, "AR")), 75)


    # Part 3
    # test population_by_education
    def test311(self):
        result = population_by_education(reduced_data, "Bachelor's Degree or Higher")
        expected = sum([(i.education["Bachelor's Degree or Higher"] * i.population['2014 Population'])/100 for i in reduced_data])
        self.assertEqual(expected, result)

    def test312(self):
        result = population_by_education(reduced_data, "Bachelor's Degree or Higher")
        expected = sum([(i.education["High School or Higher"] * i.population['2014 Population'])/100 for i in reduced_data])
        self.assertNotEqual(expected, result)

    # test population_by_ethnicity
    def test321(self):
        result = population_by_ethnicity(reduced_data, "Black Alone" )
        expected = sum([(i.ethnicities["Black Alone"] * i.population['2014 Population'])/100 for i in reduced_data])
        self.assertEqual(expected, result)


    def test322(self):
        result = population_by_ethnicity(reduced_data, "Black Alone" )
        expected = sum([(i.ethnicities["Asian Alone"] * i.population['2014 Population'])/100 for i in reduced_data])
        self.assertNotEqual(expected, result)

    # test population_below_poverty_level
    def test331(self):
        result = population_below_poverty_level(reduced_data)
        expected = sum([(i.income["Persons Below Poverty Level"] * i.population['2014 Population'])/100 for i in reduced_data])
        self.assertEqual(expected, result)

    def test332(self):
        result = population_below_poverty_level(reduced_data)
        expected = sum([(i.income['Median Household Income'] * i.population['2014 Population'])/100 for i in reduced_data])
        self.assertNotEqual(expected, result)


    # Part 4
    # test percent_by_education
    def test411(self):
        result = percent_by_education(reduced_data, "High School or Higher")
        expected = (population_by_education(reduced_data, "High School or Higher")/population_total(reduced_data))*100
        self.assertEqual(expected, result)

    def test412(self):
        result = percent_by_education(reduced_data, "High School or Higher")
        expected = (population_by_education(reduced_data, "Bachelor's Degree or Higher")/population_total(reduced_data))*100
        self.assertNotEqual(expected, result)


    # test percent_by_ethnicity
    def test421(self):
        result = percent_by_ethnicity(reduced_data, "Asian Alone")
        expected = (population_by_ethnicity(reduced_data, "Asian Alone")/population_total(reduced_data))*100
        self.assertEqual(expected, result)

    def test422(self):
        result = percent_by_ethnicity(reduced_data, "Asian Alone")
        expected = (population_by_ethnicity(reduced_data, "Black Alone")/population_total(reduced_data))*100
        self.assertNotEqual(expected, result)

    # test percent_below_poverty_level
    def test431(self):
        result = percent_below_poverty_level(reduced_data)
        expected = (population_below_poverty_level(reduced_data)/population_total(reduced_data))*100
        self.assertEqual(expected, result)

    def test432(self):
        result = percent_below_poverty_level(reduced_data)
        expected = (population_below_poverty_level(reduced_data)/population_total(reduced_data))*1000
        self.assertNotEqual(expected, result)

    # Part 5
    # test education_greater_than
    def test511(self):
        result = education_greater_than(reduced_data, "Bachelor's Degree or Higher", 2.0)
        expected = [i for i in reduced_data if "Bachelor's Degree or Higher" in i.education and i.education["Bachelor's Degree or Higher"] > 2.0]
        self.assertEqual(expected, result)

    def test512(self):
        result = education_greater_than(reduced_data, "High School or Higher", 2.0)
        expected = [i for i in reduced_data if "High School or Higher" in i.education and i.education["High School or Higher"] > 2.0]
        self.assertEqual(expected, result)

    # test education_less_than
    def test521(self):
        result = education_less_than(reduced_data, "High School or Higher", 3.0)
        expected = [i for i in reduced_data if "High School or Higher" in i.education and i.education["High School or Higher"] < 3.0]
        self.assertEqual(expected, result)

    def test522(self):
        result = education_less_than(reduced_data, "Bachelor's Degree or Higher", 3.0)
        expected = [i for i in reduced_data if "Bachelor's Degree or Higher" in i.education and i.education["Bachelor's Degree or Higher"] < 3.0]
        self.assertEqual(expected, result)

    # test ethnicity_greater_than
    def test531(self):
        result = ethnicity_greater_than(reduced_data, "Black Asian", 2.0)
        expected = [i for i in reduced_data if "Black Asian" in i.ethnicities and i.ethnicities["Black Asian"] > 2.0]
        self.assertEqual(expected, result)

    def test532(self):
        result = ethnicity_greater_than(reduced_data, "White Alone", 2.0)
        expected = [i for i in reduced_data if "White Alone" in i.ethnicities and i.ethnicities["White Alone"] > 2.0]
        self.assertEqual(expected, result)

    # test ethnicity_less_than
    def test541(self):
        result = ethnicity_less_than(reduced_data, "Asian Alone", 49.0)
        expected = [i for i in reduced_data if "Asian Alone" in i.ethnicities and i.ethnicities["Asian Alone"] < 49.0]
        self.assertEqual(expected, result)

    def test542(self):
        result = ethnicity_less_than(reduced_data, "Black Alone", 49.0)
        expected = [i for i in reduced_data if "Black Alone" in i.ethnicities and i.ethnicities["Black Alone"] < 9.0]
        self.assertNotEqual(expected, result)

    # test below_poverty_level_greater_than
    def test551(self):
        result = below_poverty_level_greater_than(reduced_data, 19.9)
        expected = [i for i in reduced_data if "Persons Below Poverty Level" in i.income and i.income['Persons Below Poverty Level'] > 19.9]
        self.assertEqual(set(expected), set(result))

    def test552(self):
        result = below_poverty_level_greater_than(reduced_data, 14.9)
        expected = [i for i in reduced_data if "Persons Below Poverty Level" in i.income and i.income['Persons Below Poverty Level'] > 4.9]
        self.assertNotEqual(expected, result)

    # test below_poverty_level_less_than
    def test561(self):
        result = below_poverty_level_less_than(reduced_data, 13.4)
        expected = [i for i in reduced_data if "Persons Below Poverty Level" in i.income and i.income['Persons Below Poverty Level'] < 13.4]
        self.assertEqual(expected, result)

    def test562(self):
        result = below_poverty_level_less_than(reduced_data, 1.4)
        expected = [i for i in reduced_data if "Persons Below Poverty Level" in i.income and i.income['Persons Below Poverty Level'] < 12.4]
        self.assertNotEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
