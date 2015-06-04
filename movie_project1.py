import fresh_tomatoes

import media

#Pulp Fiction Movie Info
pulp_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                           "http://www.movieposter.com/posters/archive/main/16/A70-8455",
                           "https://www.youtube.com/watch?v=wZBfmBvvotE")
#Office Space Movie Info
office_space = media.Movie("Office Space",
                            "The film satirizes the everyday work life of a typical mid-to-late-1990s software company.",
                            "http://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
                            "https://www.youtube.com/watch?v=_IwzZYRejZQ")
#Boondock Saints Movie Info
boondock_saints = media.Movie("Boondock Saints",
                              "Fraternal twins set out to rid Boston of the evil men operating there while being tracked down by an FBI agent.",
                              "http://www.movieposter.com/posters/archive/main/119/MPW-59654",
                              "https://www.youtube.com/watch?v=ydXojYfCF3I")

#Reservoir Dogs Movie Info
reservoir_dogs = media.Movie("Reservoir Dogs",
                             "After a simple jewelery heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant.",
                             "http://moviecultists.com/wp-content/uploads/2009/10/reservoir-dogs-poster.jpg",
                             "https://www.youtube.com/watch?v=qCgulNG5w9g")

#Dazed and Confused Movie Info
dazed_and_confused = media.Movie("Dazed and Confused",
                                 "The adventures of incoming high school and junior high students on the last day of school, in May of 1976.",
                                 "http://www.movieposter.com/posters/archive/main/80/MPW-40398",
                                 "https://www.youtube.com/watch?v=Mvj4Ng6yinA")

#SLC Punk Movie Info
slc_punk = media.Movie("SLC Punk",
                       "In the early 1980s Stevo and Heroin Bob are the only two dedicated punks in conservative Salt Lake City.",
                       "http://images.posterjunction.com/SLC-Punk!-poster-1020252859.jpg",
                       "https://www.youtube.com/watch?v=MsZziQvRWCg")

#Movie Array List
movies = [office_space, pulp_fiction, boondock_saints, reservoir_dogs, dazed_and_confused, slc_punk] 

#Call to web site template
fresh_tomatoes.open_movies_page(movies)



                           
