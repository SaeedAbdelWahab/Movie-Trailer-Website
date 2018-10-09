import media
import fresh_tomatoes
import media
import fresh_tomatoes

# The movies wanted to be displayed in browser

the_nun = media.Movie('The Nun',
                      'https://m.media-amazon.com/images/M/MV5BMjEwMDE1NzI3M15B\
    Ml5BanBnXkFtZTgwNjg2NjExNjM@._V1_.jpg,'
                      'https://youtu.be/pzD9zGcUNrw',
                      "A priest with a haunted past and a novice on the thresho\
    ud of her final vows are sent by the Vatican to investigate the death of a\
     young nun in Romania and confront a malevolent force in the form of a dem\
     onic nun."
                      )

venom = media.Movie('Venom',
                    'https://m.media-amazon.com/images/M/MV5BNzAwNzUzNjY4MV5BM\
    l5BanBnXkFtZTgwMTQ5MzM0NjM@._V1_.jpg',
                    'https://youtu.be/u9Mv98Gr5pY',
                    'When Eddie Brock acquires the powers of a symbiote, he wi\
    ll have to release his alter-ego "Venom" to save his life.'
                    )

man_of_steel = media.Movie('Man of Steel',
                           'https://m.media-amazon.com/images/M/MV5BMTk5ODk1ND\
    kxMF5BMl5BanBnXkFtZTcwNTA5OTY0OQ@@._V1_SY1000_CR0,0,676,1000_AL_.jpg',
                           'https://youtu.be/T6DJcgm3wNY',
                           'Clark Kent, one of the last of an extinguished rac\
    e disguised as an unremarkable human, is forced to reveal his identity whe\
    n Earth is invaded by an army of survivors who threaten to bring the plane\
    t to the brink of destruction'
                           )

justice_league = media.Movie('Justice League',
                             'https://m.media-amazon.com/images/M/MV5BYWVhZjZk\
    YTItOGIwYS00NmRkLWJlYjctMWM0ZjFmMDU4ZjEzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_S\
    Y1000_SX675_AL_.jpg',
                             'https://youtu.be/r9-DM9uBtVI',
                             "Fueled by his restored faith in humanity and insp\
    ired by Superman's selfless act, Bruce Wayne enlists the help of his newf\
    ound ally, Diana Prince, to face an even greater enemy."
                             )

the_lion_king = media.Movie('The Lion King',
                            'https://m.media-amazon.com/images/M/MV5BYTYxNGMyZ\
    TYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SY\
    1000_CR0,0,673,1000_AL_.jpg',
                            'https://youtu.be/4sj1MT05lAA',
                            "A Lion cub crown prince is tricked by a treachero\
    us uncle into thinking he caused his father's death and flees into exile i\
    n despair, only to learn in adulthood his identity and his responsibilitie\
    s."
                            )

kung_fu_panda = media.Movie('Kung Fu Panda',
                            'https://m.media-amazon.com/images/M/MV5BODJkZTZhM\
    WItMDI3Yy00ZWZlLTk4NjQtOTI1ZjU5NjBjZTVjXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SY\
    1000_CR0,0,689,1000_AL_.jpg',
                            'https://youtu.be/PXi3Mv6KMzY',
                            "The Dragon Warrior has to clash against the savag\
    e Tai Lung as China's fate hangs in the balance: However, the Dragon Warri\
    or mantle is supposedly mistaken to be bestowed upon an obese panda who is\
     a tyro in martial arts"
                            )

movies_list = [
    the_nun,
    venom,
    man_of_steel,
    justice_league,
    the_lion_king,
    kung_fu_panda,
    ]

# Calling the function which generates the HTML file

fresh_tomatoes.open_movies_page(movies_list)
