# Feature_Engineering

About
=====
This Git repo is sponsored by the [Hack My Life] (https://meetup.com/hack-my-life/) meetup group of Richardson, TX. Special thanks also goes out the slack community of [RemoteCoder.net] (http://www.remotecoder.net) for their support. 

This project's aim is mung a dataset consisting of corporate information and US Census data (specifically in relation to population by zip code). Once our new feature is created we will use KNN to create three clusters of the data. These will then be displayed on a map of North Texas. 

Dependencies
============
Python 3.6.1  
Pandas  
Numpy  
Sklearn  

Places to Contribute
====================
Creation of the initial Python file. If you need inspiration, kindly review our "Target Market" repo. This initial file should pull in the census data via Pandas and merge the data with our corporate info, for the relevant zip codes. 

The main independent variable (IV) that we want to engineer will be calculated by taking the corporate revenue and dividing by the population of the zip code where their primary business activities occur. We will be clustering based on the two columns which make up this data (after scaling).

After companies have been sorted into one of three clusters, we will then be mapping these three types of companies (via color coding) onto a map or the local area. We will also be producing three additional maps, one for each type of cluster.

How to Run
============
<python file yet to be created>
