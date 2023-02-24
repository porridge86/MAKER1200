# Introduction

This is my python code that I presented in the MAKER1200 assignment in 2022. Now that the grades for this subject are out, I decided to publish the code.

I chose to create a program that provide users with weather information from two different places (Oslo and Tokyo), and then saves the data in different sheets in a single excel file by using the basics of Python.

## Main goals of this project

- to create a program that will provide a weather forecast from several locations.
- to deepen my understanding of programming in Python through this project

## Program design

- Use knowledge from MAKER1200 (if/elif/else, for-loop, etc.)
- Get weather information for the specified place(s) through an API. Extract data and display the results.
- Show messages, including emoji, according to the weather information. If possible, do the same for other regions.
- Display a random message such as “Have a nice day”.
- Export data to Excel and save as a predefined name.
- Display a message after saving data as an Excel file.
- The weather information includes a weather forecast with maximum and minimum temperature for today and tomorrow.

## Choice of Weather API

I found two free APIs that provides weather information for various cities over the world;

- OpenWeatherMap
- Open-Meteo <https://open-meteo.com/en/docs#api_form>

For this project, I decided to use Open-Meteo, as it has many variables prepared on the website in advance, and it automatically generates a URL based on which variables were chosen through the UI.
