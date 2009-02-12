#!/usr/bin
# -*- coding: utf-8 -*-

import imdb,sys

searchterm = sys.argv[1]

film_list = []

i = imdb.IMDb()
# movie_list is a list of Movie objects, with only attributes like 'title'
# and 'year' defined.
movie_list = i.search_movie(searchterm)

# the first movie in the list.
first_match = movie_list[0]
# only basic information like the title will be printed.
print (first_match.summary())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~bla~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# update the information for this movie.
i.update(first_match)

# a lot of information will be printed!
print (first_match.summary())

# retrieve trivia information and print it.
i.update(first_match, 'trivia')
print (m['trivia'])

# retrieve both 'quotes' and 'goofs' information (with a list or tuple)
i.update(m, ['quotes', 'goofs'])
print (m['quotes'])
print (m['goofs'])
# retrieve every available information.
i.update(m, 'all')
