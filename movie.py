#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 10:28:01 2017

@author: lixiaochi
"""


class Movie:
    """The movie data contains a movie title, post image url and trailer url"""
    def __init__(self, movieName, postUrl, trailerUrl):
        self.title = movieName
        self.poster_image_url = postUrl
        self.trailer_youtube_url = trailerUrl
