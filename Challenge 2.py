## Imports & pre-proceessing

import os
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np
import pickle

os.chdir('Desktop/ELU 501 Data Science/Challenge 2')


## Load data

G = nx.read_gexf("mediumLinkedin.gexf")

full_college={}
full_location={}
full_employer={}

removed_users = []

college={}
location={}
employer={}

with open('mediumCollege.pickle', 'rb') as handle:
    full_college = pickle.load(handle)
with open('mediumLocation.pickle', 'rb') as handle:
    full_location = pickle.load(handle)
with open('mediumEmployer.pickle', 'rb') as handle:
    full_employer = pickle.load(handle)
    
with open('mediumRemovedNodes_60percent_of_empty_profile.pickle', 'rb') as handle:
        removed_users = pickle.load(handle)
    
with open('mediumCollege_60percent_of_empty_profile.pickle', 'rb') as handle:
    college = pickle.load(handle)
with open('mediumLocation_60percent_of_empty_profile.pickle', 'rb') as handle:
    location = pickle.load(handle)
with open('mediumEmployer_60percent_of_empty_profile.pickle', 'rb') as handle:
    employer = pickle.load(handle)

## Find all attributs

def all_atributs(dict):
    attributs = []
    for key in dict:
        for k in range(len(dict[key])):
            if not(dict[key][k] in attributs):
                attributs += [dict[key][k]]
    return(attributs)

all_colleges = all_atributs(full_college)
all_locations = all_atributs(full_location)
all_employers = all_atributs(full_employer)

dimension_college = len(all_colleges)
dimension_location = len(all_locations)
dimension_employer = len(all_employers)

print("Nb of different colleges : %d" % dimension_college)
print("Nb of different locations : %d" % dimension_location)
print("Nb of different employers : %d" % dimension_employer)

## Find removed users

def removed_users(empty_dict, full_dict):
    removed_users = []
    for key in full_dict:
        if not(key in empty_dict):
            removed_users += [key]
    return(removed_users)
    
removed_college = removed_users(college, full_college)
removed_locations = removed_users(location, full_location)
removed_employers = removed_users(employer, full_employer)

print("Nb of users without college : %d" % len(removed_college))
print("Nb of users without location : %d" % len(removed_locations))
print("Nb of users without employer : %d" % len(removed_employers))

Asdee
aecfa