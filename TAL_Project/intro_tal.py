#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk import Text
from nltk.book import *
#from nltk.tokenize import word_tokenize
from nltk import probability
# on récupere la declaration universelle des droits de l'homme
from nltk.corpus import udhr

import numpy as np

import re

import operator

###### VARS

is_word = re.compile("[a-zA-Z]", re.I)
is_letter = re.compile("[a-z]", re.I)
gutenberg = nltk.corpus.gutenberg

####### FCT
# EXERCICE 1
def exo1 () :
    print "***************** Exercice 1 *******************"
    # dans text5
    mots_4 = list()
    for wd in set(text5) :
        # on vérifie la longueur et la validité du mot
        if (len(wd) == 4 and re.match(is_word,wd)):
            mots_4.append(wd.lower())
            print "--> Mots de 4 lettres dans le texte 5"
            #print mots_4
            # on ordonne les mots par fréquence
    fdist_1 = probability.FreqDist()
    for wd in list(text5) :
        fdist_1[wd] += 1
    sorted_mots_4 = map(lambda x: x[0],sorted(fdist_1.items(), key=operator.itemgetter(1), reverse=True))
    print sorted_mots_4
    print "+++++++++++++++++ DONE ++++++++++++++++\n"

# EXERCICE 2
def exo2 () :
    print "***************** Exercice 2 *******************"
    hat_reg = re.compile("hat")
    z_reg = re.compile("z")
    pt_reg = re.compile("pt")
    mots_ex2 = list()
    for wd in set(text6) :
        if (wd.endswith("hat") or re.match(z_reg, wd) or re.match(pt_reg, wd)) :
            mots_ex2.append(wd.lower())
    print mots_ex2
    print "+++++++++++++++++ DONE ++++++++++++++++\n"

# EXERCICE 3
def exo3 (text) :
    print "***************** Exercice 3 *******************"
    #text = text1
    #print "# text1"
    freq_lettre_1 = probability.FreqDist()
    for wd in list(text) :
        for letter in list(wd) :
        # s'il s'agit bien d'une lettre
            if (re.match(is_letter,letter)) :
                freq_lettre_1[letter.lower()] += 1
    sorted_letters_ex3 = map(lambda x: x[0], sorted(freq_lettre_1.items(), key=operator.itemgetter(1), reverse=True))
    print sorted_letters_ex3
    print "+++++++++++++++++ DONE ++++++++++++++++\n"

# EXERCICE 4
def exo4_1 () :
    print "***************** Exercice 4 *******************"
    mots = probability.FreqDist()
    #print gutenberg.words()
    for wd in (gutenberg.raw()) :
        print wd
    print "+++++++++++++++++ DONE ++++++++++++++++\n"

    
# TESTS
exo4_1()
