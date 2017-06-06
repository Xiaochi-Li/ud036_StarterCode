#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 11:01:15 2017

@author: lixiaochi
"""
import fresh_tomatoes
import movie


movies = []  # list of movie

# the movie wonder women
wonderWomen = movie.Movie("Wonder Women",
                          'http://cdn2-www.comingsoon.net/assets/'
                          'uploads/gallery/wonder-woman/14883647_5619'
                          '31980643670_384850897829389102_o.jpg',
                          "https://youtu.be/1Q8fG0TtVAY")

# the movie justice league
justiceLeague = movie.Movie("Justice League",
                            'https://upload.wikimedia.org/wikipedia/'
                            'en/3/31/Justice_League_film_poster.jpg',
                            "https://youtu.be/3cxixDgHUYw")

# the movie 
batmanSuperman = movie.Movie("Batman v Superman",
                             'https://upload.wikimedia.org/wikipedia/'
                             'en/2/20/Batman_v_Superman_poster.jpg',
                             "https://youtu.be/fis-9Zqu2Ro")

# add movies to the list
movies.append(wonderWomen)
movies.append(justiceLeague)
movies.append(batmanSuperman)

fresh_tomatoes.open_movies_page(movies)
