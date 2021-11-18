from app import db, app
from database.Directors import Directors
from database.Films import Films
from database.Users import Users
from database.Genres import Genres
from flask_script import Manager
from database.Films_Directors import Films_Directors
from database.Films_Genres import Films_Genres


manager = Manager(app)


@manager.command
def fill_db():
    u1 = Users(username='user', password='pass', isAdmin=False)
    u2 = Users(username='admin', password='pass', isAdmin=True)
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

    director = []
    director.append(Directors(first_name='Christopher', last_name='Nolan'))
    director.append(Directors(first_name='Steven', last_name='Spielberg'))
    director.append(Directors(first_name='Alfred', last_name='Hitchcock'))
    director.append(Directors(first_name='Quentin', last_name='Tarantino'))
    director.append(Directors(first_name='James', last_name='Cameron'))
    director.append(Directors(first_name='Hayao', last_name='Miyazaki'))
    director.append(Directors(first_name='Justin', last_name='Lin'))
    director.append(Directors(first_name='Bill', last_name='Condon'))
    director.append(Directors(first_name='Frank', last_name='Darabont'))
    director.append(Directors(first_name='Denis', last_name='Villeneuve'))
    director.append(Directors(first_name='Sam', last_name='Raimi'))
    director.append(Directors(first_name='Anthony', last_name='Russo'))
    director.append(Directors(first_name='Joss', last_name='Whedon'))
    director.append(Directors(first_name='Andrew', last_name='Bernstein'))
    director.append(Directors(first_name='Daniel', last_name='Attias'))
    director.append(Directors(first_name='Colin', last_name='Bucksey'))
    director.append(Directors(first_name='Vince', last_name='Gilligan'))
    director.append(Directors(first_name='Michelle', last_name='MacLaren'))
    director.append(Directors(first_name='Adam', last_name='Bernstein'))
    for i in director:
        db.session.add(i)
    db.session.commit()

    genre = []
    genre.append(Genres(genre='Science Fiction'))
    genre.append(Genres(genre='Action'))
    genre.append(Genres(genre='Thriller'))
    genre.append(Genres(genre='Drama'))
    genre.append(Genres(genre='Adventure'))
    genre.append(Genres(genre='Crime'))
    genre.append(Genres(genre='War'))
    genre.append(Genres(genre='Fantasy'))
    genre.append(Genres(genre='Family'))
    genre.append(Genres(genre='Animation'))
    genre.append(Genres(genre='TV Movie'))
    genre.append(Genres(genre='Horror'))
    genre.append(Genres(genre='Mystery'))
    genre.append(Genres(genre='History'))
    genre.append(Genres(genre='Romance'))
    genre.append(Genres(genre='Comedy'))
    genre.append(Genres(genre='Western'))
    genre.append(Genres(genre='Music'))

    for i in genre:
        db.session.add(i)
    db.session.commit()

    film = []
    film.append(Films(film_title='Tenet', release_date='2020/08/26', \
                      film_desc='Armed with only one word - Tenet - and fighting for the survival of the entire world, the Protagonist journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time.',
                      poster='https://static.hdrezka.ac/i/2021/11/14/ob50385403394vm48z94i.png', user_id=1, \
                      rating=7.3))
    film.append(Films(film_title='Interstellar', release_date='2014/11/06', \
                      film_desc='The adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.',
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
                      user_id=2, rating=8.4))
    film.append(Films(film_title='The dark knight', release_date='2008/04/14', \
                      film_desc='Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/qJ2tW6WMUDux911r6m7haRef0WH.jpg',
                      user_id=2, rating=8.5))
    film.append(Films(film_title='The dark knight rises', release_date='2012/07/26', \
                      film_desc='Following the death of District Attorney Harvey Dent, Batman assumes responsibility for Dent\'s crimes to protect the late attorney\'s reputation and is subsequently hunted by the Gotham City Police Department. Eight years later, Batman encounters the mysterious Selina Kyle and the villainous Bane, a new terrorist leader who overwhelms Gotham\'s finest. The Dark Knight resurfaces to protect a city that has branded him an enemy.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/vzvKcPQ4o7TjWeGIn0aGC9FeVNu.jpg',
                      user_id=2,rating=7.8))
    film.append(Films(film_title='Batman Begins', release_date='2015/08/04', \
                      film_desc='Driven by tragedy, billionaire Bruce Wayne dedicates his life to uncovering and defeating the corruption that plagues his home, Gotham City. Unable to work within the system, he instead creates a new identity, a symbol of fear for the criminal underworld - The Batman.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8RW2runSEc34IwKN2D1aPcJd2UL.jpg',
                      user_id=2, rating=7.7))
    film.append(Films(film_title='Dunkirk', release_date='2017/07/20', \
                      film_desc='The story of the miraculous evacuation of Allied soldiers from Belgium, Britain, Canada and France, who were cut off and surrounded by the German army from the beaches and harbour of Dunkirk between May 26th and June 4th 1940 during World War II.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/ebSnODDg9lbsMIaWg2uAbjn7TO5.jpg',
                      user_id=2, rating=7.5))
    film.append(Films(film_title='The prestige', release_date='2006/10/19', \
                      film_desc='A mysterious story of two magicians whose intense rivalry leads them on a life-long battle for supremacy -- full of obsession, deceit and jealousy with dangerous and deadly consequences.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/bdN3gXuIZYaJP7ftKK2sU0nPtEA.jpg',
                      user_id=2, rating=8.2))
    film.append(Films(film_title='Memento', release_date='2001/03/16', \
                      film_desc='Leonard Shelby is tracking down the man who raped and murdered his wife. The difficulty of locating his wife\'s killer, however, is compounded by the fact that he suffers from a rare, untreatable form of short-term memory loss. Although he can recall details of life before his accident, Leonard cannot remember what happened fifteen minutes ago, where he\'s going, or why.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/yuNs09hvpHVU1cBTCAk9zxsL2oW.jpg',
                      user_id=2, rating=8.2))
    film.append(Films(film_title='Jurassic Park', release_date='1993/06/11', \
                      film_desc='A wealthy entrepreneur secretly creates a theme park featuring living dinosaurs drawn from prehistoric DNA. Before opening day, he invites a team of experts and his two eager grandchildren to experience the park and help calm anxious investors. However, the park is anything but amusing as the security systems go off-line and the dinosaurs escape.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/oU7Oq2kFAAlGqbU4VoAE36g4hoI.jpg',
                      user_id=2, rating=7.9))
    film.append(Films(film_title='Saving Private Ryan', release_date='1998/07/24', \
                      film_desc='As U.S. troops storm the beaches of Normandy, three brothers lie dead on the battlefield, with a fourth trapped behind enemy lines. Ranger captain John Miller and seven men are tasked with penetrating German-held territory and bringing the boy home.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/JC8KQ2BXaAIFEU8zEuakiwUQSr.jpg',
                      user_id=2, rating=8.2))
    film.append(Films(film_title='Ready Player One', release_date='2018/03/29', \
                      film_desc='When the creator of a popular video game system dies, a virtual contest is created to compete for his fortune.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/pU1ULUq8D3iRxl1fdX2lZIzdHuI.jpg',
                      user_id=2, rating=7.6))
    film.append(Films(film_title='Schindler\'s List', release_date='1993/02/04', \
                      film_desc='The true story of how businessman Oskar Schindler saved over a thousand Jewish lives from the Nazis while they worked as slaves in his factory during World War II.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg',
                      user_id=2, rating=8.6))
    film.append(Films(film_title='Catch Me If You Can', release_date='2002/12/25', \
                      film_desc='A true story about Frank Abagnale Jr. who, before his 19th birthday, successfully conned millions of dollars worth of checks as a Pan Am pilot, doctor, and legal prosecutor. An FBI agent makes it his mission to put him behind bars. But Frank not only eludes capture, he revels in the pursuit.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/ctjEj2xM32OvBXCq8zAdK3ZrsAj.jpg',
                      user_id=2, rating=7.9))
    film.append(Films(film_title='Star Wars: Episode III - Revenge of the Sith', release_date='2005/05/19', \
                      film_desc='The evil Darth Sidious enacts his final plan for unlimited power -- and the heroic Jedi Anakin Skywalker must choose a side.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/xfSAoBEm9MNBjmlNcDYLvLSMlnq.jpg',
                      user_id=2, rating=7.4))
    film.append(Films(film_title='Raiders of the Lost Ark', release_date='1981/06/12', \
                      film_desc='When Dr. Indiana Jones – the tweed-suited professor who just happens to be a celebrated archaeologist – is hired by the government to locate the legendary Ark of the Covenant, he finds himself up against the entire Nazi regime.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/awUGN7ZCNq2EUTdpVaHDX23anOZ.jpg', user_id=2, \
                      rating=7.9))
    film.append(Films(film_title='E.T. the Extra-Terrestrial', release_date='06/11/1982', \
                      film_desc='After a gentle alien becomes stranded on Earth, the being is discovered and befriended by a young boy named Elliott. Bringing the extraterrestrial into his suburban California house, Elliott introduces E.T., as the alien is dubbed, to his brother and his little sister, Gertie, and the children decide to keep its existence a secret. Soon, however, E.T. falls ill, resulting in government intervention and a dire situation for both Elliott and the alien.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/an0nD6uq6byfxXCfk6lQBzdL2J1.jpg', user_id=2, \
                      rating=7.5))
    film.append(Films(film_title='Rebecca', release_date='1940/04/12', \
                      film_desc='Story of a young woman who marries a fascinating widower only to find out that she must live in the shadow of his former wife, Rebecca, who died mysteriously several years earlier. The young wife must come to grips with the terrible secret of her handsome, cold husband, Max De Winter. She must also deal with the jealous, obsessed Mrs. Danvers, the housekeeper, who will not accept her as the mistress of the house.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/3Gla0nxHboX3nxQzaU4SoqOtTjh.jpg', user_id=2, \
                      rating=7.9))
    film.append(Films(film_title='Psycho', release_date='2006/09/08', \
                      film_desc='When larcenous real estate clerk Marion Crane goes on the lam with a wad of cash and hopes of starting a new life, she ends up at the notorious Bates Motel, where manager Norman Bates cares for his housebound mother.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/nXjkXxpsE7ZGRCVd6PKkrf9tgsL.jpg', \
                      user_id=2, rating=8.4))
    film.append(Films(film_title='Rear Window', release_date='1954/09/01', \
                      film_desc='A wheelchair-bound photographer spies on his neighbors from his apartment window and becomes convinced one of them has committed murder.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/qitnZcLP7C9DLRuPpmvZ7GiEjJN.jpg', \
                      user_id=2, rating=8.4))
    film.append(Films(film_title='Vertigo', release_date='1958/05/28', \
                      film_desc='A retired San Francisco detective suffering from acrophobia investigates the strange activities of an old friend\'s wife, all the while becoming dangerously obsessed with her.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dg9escdBIAAATxlUeTya9gurTtI.jpg', \
                      user_id=2, rating=8.2))
    film.append(Films(film_title='North by Northwest', release_date='1959/08/06', \
                      film_desc='Advertising man Roger Thornhill is mistaken for a spy, triggering a deadly cross-country chase.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/2XhojYqG4ICe68Iqf2bN8xfVgz8.jpg', \
                      user_id=2, rating=8.0))
    film.append(Films(film_title='The Birds', release_date='1963/03/29', \
                      film_desc='Chic socialite Melanie Daniels enjoys a passing flirtation with an eligible attorney in a San Francisco pet shop and, on an impulse, follows him to his hometown bearing a gift of lovebirds. But upon her arrival, the bird population runs amok. Suddenly, the townsfolk face a massive avian onslaught, with the feathered fiends inexplicably attacking people all over Bodega Bay.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/z0iYrJ6GsAMP3abOha7uGMuc5kZ.jpg', \
                      user_id=2, rating=7.5))
    film.append(Films(film_title='Rope', release_date='1948/09/25', \
                      film_desc='Two men attempt to prove they committed the perfect crime by hosting a dinner party after strangling their former classmate to death.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/j6jYX3IO49Z1U20sViIEsQfAI10.jpg', \
                      user_id=2, rating=8.0))
    film.append(Films(film_title='Dial M for Murder', release_date='1954/05/29', \
                      film_desc='An ex-tennis pro carries out a plot to have his wife murdered after discovering she is having an affair, and assumes she will soon leave him for the other man anyway. When things go wrong, he improvises a new plan—to frame her for murder instead.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/4KKiFDvtEusJzqzlwHp7iMceXKS.jpg', \
                      user_id=2, rating=8.0))
    film.append(Films(film_title='Once Upon a Time… in Hollywood', release_date='2019/08/15', \
                      film_desc='Los Angeles, 1969. TV star Rick Dalton, a struggling actor specializing in westerns, and stuntman Cliff Booth, his best friend, try to survive in a constantly changing movie industry. Dalton is the neighbor of the young and promising actress and model Sharon Tate, who has just married the prestigious Polish director Roman Polanski…', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8j58iEBw9pOXFD2L0nt0ZXeHviB.jpg', \
                      user_id=2, rating=7.4))
    film.append(Films(film_title='Pulp Fiction', release_date='1994/10/14', \
                      film_desc='A burger-loving hit man, his philosophical partner, a drug-addled gangster\'s moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.',
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg', \
                      user_id=2, rating=8.5))
    film.append(Films(film_title='Django Unchained', release_date='2012/12/25', \
                      film_desc='With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/7oWY8VDWW7thTzWh3OKYRkWUlD5.jpg', \
                      user_id=2, rating=8.1))
    film.append(Films(film_title='Inglourious Basterds', release_date='2009/08/12', \
                      film_desc='In Nazi-occupied France during World War II, a group of Jewish-American soldiers known as "The Basterds" are chosen specifically to spread fear throughout the Third Reich by scalping and brutally killing Nazis. The Basterds, lead by Lt. Aldo Raine soon cross paths with a French-Jewish teenage girl who runs a movie theater in Paris which is targeted by the soldiers.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/7sfbEnaARXDDhKm0CZ7D7uc2sbo.jpg', \
                      user_id=2, rating=8.2))
    film.append(Films(film_title='Kill Bill: Vol. 1', release_date='2003/10/10', \
                      film_desc='An assassin is shot by her ruthless employer, Bill, and other members of their assassination circle – but she lives to plot her vengeance.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/v7TaX8kXMXs5yFFGR41guUDNcnB.jpg', \
                      user_id=2, rating=8.0))
    film.append(Films(film_title='The Hateful Eight', release_date='2016/01/14', \
                      film_desc='Bounty hunters seek shelter from a raging blizzard and get caught up in a plot of betrayal and deception.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/k02LLl5tsukIEGhV016N09oHVEF.jpg', \
                      user_id=2, rating=7.7))
    film.append(Films(film_title='Reservoir Dogs', release_date='1992/09/02', \
                      film_desc='A botched robbery indicates a police informant, and the pressure mounts in the aftermath at a warehouse. Crime begets violence as the survivors -- veteran Mr. White, newcomer Mr. Orange, psychopathic parolee Mr. Blonde, bickering weasel Mr. Pink and Nice Guy Eddie -- unravel.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/lsBnfheKZBO3UKU7lVHIeGZLWuF.jpg', \
                      user_id=2, rating=8.2))
    film.append(Films(film_title='Kill Bill: Vol. 2', release_date='2004/04/16', \
                      film_desc='The Bride unwaveringly continues on her roaring rampage of revenge against the band of assassins who had tried to kill her and her unborn child. She visits each of her former associates one-by-one, checking off the victims on her Death List Five until there\'s nothing left to do … but kill Bill.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/2yhg0mZQMhDyvUQ4rG1IZ4oIA8L.jpg', \
                      user_id=2, rating=7.9))
    film.append(Films(film_title='Avatar', release_date='2009/12/17', \
                      film_desc='In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg', \
                      user_id=2, rating=7.5))
    film.append(Films(film_title='Titanic', release_date='1997/12/19', \
                      film_desc='101-year-old Rose DeWitt Bukater tells the story of her life aboard the Titanic, 84 years later. A young Rose boards the ship with her mother and fiancé. Meanwhile, Jack Dawson and Fabrizio De Rossi win third-class tickets aboard the ship. Rose tells the whole story from Titanic\'s departure through to its death—on its first and last voyage—on April 15, 1912.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg', \
                      user_id=2, rating=7.9))
    film.append(Films(film_title='The Terminator', release_date='1984/10/26', \
                      film_desc='In the post-apocalyptic future, reigning tyrannical supercomputers teleport a cyborg assassin known as the "Terminator" back to 1984 to kill Sarah Connor, whose unborn son is destined to lead insurgents against 21st century mechanical hegemony. Meanwhile, the human-resistance movement dispatches a lone warrior to safeguard Sarah. Can he stop the virtually indestructible killing machine?', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/qvktm0BHcnmDpul4Hz01GIazWPr.jpg', \
                      user_id=2, rating=7.6))
    film.append(Films(film_title='Terminator 2: Judgment Day', release_date='1991/12/25', \
                      film_desc='Nearly 10 years have passed since Sarah Connor was targeted for termination by a cyborg from the future. Now her son, John, the future leader of the resistance, is the target for a newer, more deadly terminator. Once again, the resistance has managed to send a protector back to attempt to save John and his mother Sarah.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/weVXMD5QBGeQil4HEATZqAkXeEc.jpg', \
                      user_id=2, rating=8.1))
    film.append(Films(film_title='Aliens', release_date='1986/07/18', \
                      film_desc='When Ripley\'s lifepod is found by a salvage crew over 50 years later, she finds that terra-formers are on the very planet they found the alien species. When the company sends a family of colonists out to investigate her story—all contact is lost with the planet and colonists. They enlist Ripley and the colonial marines to return and search for answers.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/r1x5JGpyqZU8PYhbs4UcrO1Xb6x.jpg', \
                      user_id=2, rating=7.9))
    film.append(Films(film_title='True Lies', release_date='1994/07/15', \
                      film_desc='A fearless, globe-trotting, terrorist-battling secret agent has his life turned upside down when he discovers his wife might be having an affair with a used car salesman while terrorists smuggle nuclear war heads into the United States.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/pweFTnzzTfGK68woSVkiTgjLzWm.jpg', \
                      user_id=2, rating=7.0))
    film.append(Films(film_title='The Abyss', release_date='1989/08/09', \
                      film_desc='A civilian oil rig crew is recruited to conduct a search and rescue effort when a nuclear submarine mysteriously sinks. One diver soon finds himself on a spectacular odyssey 25,000 feet below the ocean\'s surface where he confronts a mysterious force that has the power to change the world or destroy it.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/jel2BuDv7Bq4fuv2pUrTfiBm69o.jpg', \
                      user_id=2, rating=7.3))
    film.append(Films(film_title='Spirited Away', release_date='2001/07/20', \
                      film_desc='A young girl, Chihiro, becomes trapped in a strange new world of spirits. When her parents undergo a mysterious transformation, she must call upon the courage she never knew she had to free her family.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg', \
                      user_id=2, rating=8.5))
    film.append(Films(film_title='Howl\'s Moving Castle', release_date='2004/12/16', \
                      film_desc='When Sophie, a shy young woman, is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking castle.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/TkTPELv4kC3u1lkloush8skOjE.jpg', \
                      user_id=2, rating=8.4))
    film.append(Films(film_title='Princess Mononoke', release_date='1997/07/12', \
                      film_desc='Ashitaka, a prince of the disappearing Emishi people, is cursed by a demonized boar god and must journey to the west to find a cure. Along the way, he encounters San, a young human woman fighting to protect the forest, and Lady Eboshi, who is trying to destroy it. Ashitaka must find a way to bring balance to this conflict.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/pdtzEreKvKAlqa2YEBaGwiA45V8.jpg', \
                      user_id=2, rating=8.4))
    film.append(Films(film_title='My Neighbor Totoro', release_date='1990/07/13', \
                      film_desc='Two sisters move to the country with their father in order to be closer to their hospitalized mother, and discover the surrounding trees are inhabited by Totoros, magical spirits of the forest. When the youngest runs away from home, the older sister seeks help from the spirits to find her.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/rtGDOeG9LzoerkDGZF9dnVeLppL.jpg', \
                      user_id=2, rating=8.1))
    film.append(Films(film_title='Ponyo', release_date='2008/08/14', \
                      film_desc='The son of a sailor, 5-year old Sosuke, lives a quiet life on an oceanside cliff with his mother Lisa. One fateful day, he finds a beautiful goldfish trapped in a bottle on the beach and upon rescuing her, names her Ponyo. But she is no ordinary goldfish.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/yp8vEZflGynlEylxEesbYasc06i.jpg', \
                      user_id=2, rating=7.7))
    film.append(Films(film_title='Castle in the Sky', release_date='1989/04/01', \
                      film_desc='A young boy and a girl with a magic crystal must race against pirates and foreign agents in a search for a legendary floating castle.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/npOnzAbLh6VOIu3naU5QaEcTepo.jpg', \
                      user_id=2, rating=8.0))
    film.append(Films(film_title='Kiki\'s Delivery Service', release_date='1998/12/31', \
                      film_desc='A young witch, on her mandatory year of independent life, finds fitting into a new community difficult while she supports herself by running an air courier service.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/7nO5DUMnGUuXrA4r2h6ESOKQRrx.jpg', \
                      user_id=2, rating=7.8))
    film.append(Films(film_title='Nausicaa of the Valley of the Wind', release_date='2005/03/03', \
                      film_desc='After a global war, the seaside kingdom known as the Valley of the Wind remains one of the last strongholds on Earth untouched by a poisonous jungle and the powerful insects that guard it. Led by the courageous Princess Nausicaä, the people of the Valley engage in an epic struggle to restore the bond between humanity and Earth.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/sIpcATxMrKHRRUJAGI5UIUT7XMG.jpg', \
                      user_id=2, rating=7.9))
    film.append(Films(film_title='Fast & Furious 6', release_date='2013/05/23', \
                      film_desc='Hobbs has Dominic and Brian reassemble their crew to take down a team of mercenaries: Dominic unexpectedly gets convoluted also facing his presumed deceased girlfriend, Letty.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/n31VRDodbaZxkrZmmzyYSFNVpW5.jpg', \
                      user_id=2, rating=6.8))
    film.append(Films(film_title='Fast Five', release_date='2011/04/28', \
                      film_desc='Former cop Brian O\'Conner partners with ex-con Dom Toretto on the opposite side of the law. Since Brian and Mia Toretto broke Dom out of custody, they\'ve blown across many borders to elude authorities. Now backed into a corner in Rio de Janeiro, they must pull one last job in order to gain their freedom.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/wXXYH1VGyVEE2PQS6WvzejZdsou.jpg', \
                      user_id=2, rating=7.3))
    film.append(Films(film_title='Fast & Furious', release_date='2009/04/03', \
                      film_desc='When a crime brings them back to L.A., fugitive ex-con Dom Toretto reignites his feud with agent Brian O\'Conner. But as they are forced to confront a shared enemy, Dom and Brian must give in to an uncertain new trust if they hope to outmaneuver him. And the two men will find the best way to get revenge: push the limits of what\'s possible behind the wheel.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/fjGCa4oLvgpMVF2jawbjXBWp91v.jpg', \
                      user_id=2, rating=6.7))
    film.append(Films(film_title='Star Trek Beyond', release_date='2016/07/21', \
                      film_desc='The USS Enterprise crew explores the furthest reaches of uncharted space, where they encounter a mysterious new enemy who puts them and everything the Federation stands for to the test.',
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/cnQp8GmOWahIgQaH60Kwez3TNzw.jpg',\
                      user_id=1, rating=6.8))
    film.append(Films(film_title='The Fast and the Furious: Tokyo Drift', release_date='2006/06/03', \
                      film_desc='In order to avoid a jail sentence, Sean Boswell heads to Tokyo to live with his military father. In a low-rent section of the city, Shaun gets caught up in the underground world of drift racing', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/cm2ffqb3XovzA5ZSzyN3jnn8qv0.jpg', \
                      user_id=2, rating=6.4))
    film.append(Films(film_title='F9', release_date='2021/06/17', \
                      film_desc='Dominic Toretto and his crew battle the most skilled assassin and high-performance driver they\'ve ever encountered: his forsaken brother.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/bOFaAXmWWXC3Rbv4u4uM9ZSzRXP.jpg', \
                      user_id=2, rating=7.4))
    film.append(Films(film_title='Kinsey', release_date='2004/09/04', \
                      film_desc='Kinsey is a portrait of researcher Alfred Kinsey, driven to uncover the most private secrets of a nation. What begins for Kinsey as a scientific endeavor soon takes on an intensely personal relevance, ultimately becoming an unexpected journey into the mystery of human behavior.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/cODCjWNRcZkwe4ONQs1GzRqYtRb.jpg', \
                      user_id=2, rating=6.7))
    film.append(Films(film_title='Beauty and the Beast', release_date='2017/03/17', \
                      film_desc='A live-action adaptation of Disney\'s version of the classic tale of a cursed prince and a beautiful young woman who helps him break the spell.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/tWqifoYuwLETmmasnGHO7xBjEtt.jpg', \
                      user_id=2, rating=7.0))
    film.append(Films(film_title='The Twilight Saga: Breaking Dawn - Part 2', release_date='2012/11/15', \
                      film_desc='After the birth of Renesmee, the Cullens gather other vampire clans in order to protect the child from a false allegation that puts the family in front of the Volturi.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/jHE7WUf3FDod8vw3O3twh0JVZun.jpg', \
                      user_id=2, rating=6.5))
    film.append(Films(film_title='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dSSzv6JrlwS48pBeTNSswLJXOYF.jpg', release_date='2011/11/17', \
                      film_desc='The new found married bliss of Bella Swan and vampire Edward Cullen is cut short when a series of betrayals and misfortunes threatens to destroy their world.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dSSzv6JrlwS48pBeTNSswLJXOYF.jpg', \
                      user_id=2, rating=6.2))
    film.append(Films(film_title='Mr. Holmes', release_date='2016/01/14', \
                      film_desc='The story is set in 1947, following a long-retired Holmes living in a Sussex village with his housekeeper and rising detective son. But then he finds himself haunted by an unsolved 50-year old case. Holmes\' memory isn\'t what it used to be, so he only remembers fragments of the case: a confrontation with an angry husband, a secret bond with his beautiful but unstable wife.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/iNnHMoj2oldH7O9uL08iGhfHzh.jpg', \
                      user_id=2, rating=6.5))
    film.append(Films(film_title='The Fifth Estate', release_date='2013/10/18', \
                      film_desc='A look at the relationship between WikiLeaks founder Julian Assange and his early supporter and eventual colleague Daniel Domscheit-Berg, and how the website\'s growth and influence led to an irreparable rift between the two friends.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/1dzLHy1AN8hgppJp1LDzMI4fbHY.jpg', \
                      user_id=2, rating=6.0))
    film.append(Films(film_title='Dreamgirls', release_date='2006/12/25', \
                      film_desc='Three young women dream of becoming pop stars—and get their wish when they\'re chosen to be backup singers for the legendary James \'Thunder\' Early.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/q7cw1vHRVrhn0lCtwLxXLmVkwWn.jpg', \
                      user_id=2, rating=6.8))
    film.append(Films(film_title='The Good Liar', release_date='2019/11/21', \
                      film_desc='Career con man Roy sets his sights on his latest mark: recently widowed Betty, worth millions. And he means to take it all. But as the two draw closer, what should have been another simple swindle takes on the ultimate stakes.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/6kmxXfg3aSWrzUlEPt2L0YD4jz9.jpg', \
                      user_id=2, rating=6.7))
    film.append(Films(film_title='The Shawshank Redemption', release_date='1994/09/23', \
                      film_desc='Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg', \
                      user_id=2, rating=8.7))
    film.append(Films(film_title='The Green Mile', release_date='1999/12/10', \
                      film_desc='A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people\'s ailments. When the cell block\'s head guard, Paul Edgecomb, recognizes Coffey\'s miraculous gift, he tries desperately to help stave off the condemned man\'s execution.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/velWPhVMQeQKcxggNEU8YmIo52R.jpg', \
                      user_id=2, rating=8.5))
    film.append(Films(film_title='The Mist', release_date='2007/11/21', \
                      film_desc='After a violent storm, a dense cloud of mist envelops a small Maine town, trapping artist David Drayton and his five-year-old son in a local grocery store with other people. They soon discover that the mist conceals deadly horrors that threaten their lives, and worse, their sanity.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/1CvJ6diBACKPVGOpcWuY4XPQdqX.jpg', \
                      user_id=2, rating=6.8))
    film.append(Films(film_title='The Majestic', release_date='2001/12/21', \
                      film_desc='Set in 1951, a blacklisted Hollywood writer gets into a car accident, loses his memory and settles down in a small town where he is mistaken for a long-lost son.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/mRO7mC66hxc4wUVft4wnZrMrXdL.jpg', \
                      user_id=2, rating=6.7))
    film.append(Films(film_title='Buried Alive', release_date='1990/05/09', \
                      film_desc='A married woman and her lover plot to kill her husband to make off with the insurance money. However, their attempt to murder him using poisonous fish toxins backfires when he awakens inside his coffin and returns from the grave, hellbent on revenge.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/gS4p3eByOtu89mVX4jccNcLcFk7.jpg', \
                      user_id=2, rating=6.7))
    film.append(Films(film_title='Polytechnique', release_date='2009/02/06', \
                      film_desc='A dramatization of the Montreal Massacre of 1989 where several female engineering students were murdered by an unstable misogynist.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/k0xmtct9cSseksuFKMSXxM8hfni.jpg', \
                      user_id=2, rating=7.2))
    film.append(Films(film_title='Arrival', release_date='2016/11/10', \
                      film_desc='Taking place after alien crafts land around the world, an expert linguist is recruited by the military to determine whether they come in peace or are a threat.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/x2FJsf1ElAgr63Y3PNPtJrcmpoe.jpg', \
                      user_id=2, rating=7.6))
    film.append(Films(film_title='Blade Runner 2049', release_date='2017/10/05', \
                      film_desc='Thirty years after the events of the first film, a new blade runner, LAPD Officer K, unearths a long-buried secret that has the potential to plunge what\'s left of society into chaos. K\'s discovery leads him on a quest to find Rick Deckard, a former LAPD blade runner who has been missing for 30 years.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg', \
                      user_id=2, rating=7.5))
    film.append(Films(film_title='Prisoners', release_date='2013/10/10', \
                      film_desc='Keller Dover faces a parent\'s worst nightmare when his 6-year-old daughter, Anna, and her friend go missing. The only lead is an old motorhome that had been parked on their street. The head of the investigation, Detective Loki, arrests the driver, but a lack of evidence forces Loki to release his only suspect. Dover, knowing that his daughter\'s life is at stake, decides that he has no choice but to take matters into his own hands.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/tuZhZ6biFMr5n9YSVuHOJnNL1uU.jpg', \
                      user_id=2, rating=8.0))
    film.append(Films(film_title='Sicario', release_date='2015/11/26', \
                      film_desc='An idealistic FBI agent is enlisted by a government task force to aid in the escalating war against drugs at the border area between the U.S. and Mexico.',  \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/tw0lXhbNkklvseuJ4aYldkVyXV7.jpg', \
                      user_id=2, rating=7.4))
    film.append(Films(film_title='Enemy', release_date='2014/03/14', \
                      film_desc='A mild-mannered college professor discovers a look-alike actor and delves into the other man\'s private affairs.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/coJzyPTkSp4RMRGdgE7pXmJbCiG.jpg', \
                      user_id=2, rating=6.9))
    film.append(Films(film_title='Dune', release_date='2021/09/16', \
                      film_desc='Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet\'s exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity\'s greatest potential-only those who can conquer their fear will survive.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/d5NXSklXo0qyIYkgV94XAgMIckC.jpg', \
                      user_id=2, rating=8.0))
    film.append(Films(film_title='Incendies', release_date='2010/09/04', \
                      film_desc='A mother\'s last wishes send twins Jeanne and Simon on a journey to Middle East in search of their tangled roots. Adapted from Wajdi Mouawad\'s acclaimed play, Incendies tells the powerful and moving tale of two young adults\' voyage to the core of deep-rooted hatred, never-ending wars and enduring love.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/jO6VMoZco5jaAVm2QJ2VgPolUnx.jpg', \
                      user_id=2, rating=8.1))
    film.append(Films(film_title='Battle Creek', release_date='2015/05/08', \
                      film_desc='In this mismatched buddy cop dramedy, an amazingly handsome, happy-go-lucky FBI agent is paired with a local, hard scrabble Michigan homicide detective. As they solve crimes together, their polar opposite methods only slightly outweigh their disdain for each other.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/5oqPaAiwflr1o4PlNvkAGRC9DCX.jpg',\
                      user_id=2, rating=7.2))
    film.append(Films(film_title='Breaking Bad ', release_date='2008/01/20', \
                      film_desc='When Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family\'s financial future at any cost as he enters the dangerous world of drugs and crime.',
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/ggFHVNu6YYI5L9pCfOacjizRGt.jpg', \
                      user_id=1, rating=8.7))
    film.append(Films(film_title='Hancock', release_date='2008/07/01', \
                      film_desc='Hancock is a down-and-out superhero who\'s forced to employ a PR expert to help repair his image when the public grows weary of all the damage he\'s inflicted during his lifesaving heroics. The agent\'s idea of imprisoning the antihero to make the world miss him proves successful, but will Hancock stick to his new sense of purpose or slip back into old habits?', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/7DyuV2G0hLEqHeueDfOqhZ2DVut.jpg', \
                      user_id=2, rating=6.3))
    film.append(Films(film_title='El Camino: A Breaking Bad Movie', release_date='2019/10/11', \
                      film_desc='In the wake of his dramatic escape from captivity, Jesse Pinkman must come to terms with his past in order to forge some kind of future.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/ePXuKdXZuJx8hHMNr2yM4jY2L7Z.jpg', \
                      user_id=2, rating=6.9))
    film.append(Films(film_title='Better Call Saul', release_date='2016/02/08', \
                      film_desc='Six years before Saul Goodman meets Walter White. We meet him when the man who will become Saul Goodman is known as Jimmy McGill, a small-time lawyer searching for his destiny, and, more immediately, hustling to make ends meet. Working alongside, and, often, against Jimmy, is “fixer” Mike Ehrmantraut. The series tracks Jimmy’s transformation into Saul Goodman, the man who puts “criminal” in “criminal lawyer".', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/cU0kAjGjA6d2XjBzJMUIEVKiGDb.jpg', \
                      user_id=2, rating=8.4))
    film.append(Films(film_title='The X-Files', release_date='1993/09/10', \
                      film_desc='The exploits of FBI Special Agents Fox Mulder and Dana Scully who investigate X-Files: marginalized, unsolved cases involving paranormal phenomena. Mulder believes in the existence of aliens and the paranormal while Scully, a skeptic, is assigned to make scientific analyses of Mulder\'s discoveries that debunk Mulder\'s work and thus return him to mainstream cases.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/5BD0kiTGnDxONqdrsswTewnk6WH.jpg', \
                      user_id=2, rating=8.4))
    film.append(Films(film_title='Home Fries', release_date='1998/11/25', \
                      film_desc='Dorian and Angus chase down their womanizing stepfather with a helicopter, frightening him to death. In his effort to cover their tracks, Dorian begins investigating his stepfather\'s mistress, Sally. She works at a fast-food drive-through, she\'s pregnant and Dorian quickly falls in love with her. Unfortunately, his scheming mother wants Sally dead. And Sally isn\'t sure she wants Dorian to be her child\'s father and also his brother.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/9Qwi6NdS4lBAv1WIkw04050FFE9.jpg', \
                      user_id=2, rating=5.1))
    film.append(Films(film_title=' The Lone Gunmen', release_date='2001/03/01', \
                      film_desc='After years of playing second fiddle to Agents Mulder and Scully on  The X-Files, the trio of computer-hacking conspiracy geeks popularly known as The Lone Gunmen are finally heading out on their own. Never ones to stray far from the center of corporate and government intrigue, the threesome play like a misguided Mission Impossible team, embarking on a series of comic adventures that simultaneously highlight their genius and ineptitude.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/yEiwTVIbB8oSQ5k6JBnVTxgjOPX.jpg', \
                      user_id=2, rating=7.3))
    film.append(Films(film_title='Evil Dead II', release_date='1987/03/13', \
                      film_desc='Ash Williams and his girlfriend Linda find a log cabin in the woods with a voice recording from an archeologist who had recorded himself reciting ancient chants from "The Book of the Dead." As they play the recording an evil power is unleashed taking over Linda\'s body.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/4zqCKJVHUolGs6C5AZwAZqLWixW.jpg', \
                      user_id=2, rating=7.5))
    film.append(Films(film_title='Spider-Man', release_date='2002/05/03', \
                      film_desc='After being bitten by a genetically altered spider at Oscorp, nerdy but endearing high school student Peter Parker is endowed with amazing powers to become the superhero known as Spider-Man.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/gSZyYEK5AfZuOFFjnVPUCLvdOD6.jpg', \
                      user_id=2, rating=7.2))
    film.append(Films(film_title='Spider-Man 2', release_date='2004/07/02', \
                      film_desc='Peter Parker is going through a major identity crisis. Burned out from being Spider-Man, he decides to shelve his superhero alter ego, which leaves the city suffering in the wake of carnage left by the evil Doc Ock. In the meantime, Parker still can\'t act on his feelings for Mary Jane Watson, a girl he\'s loved since childhood. A certain anger begins to brew in his best friend Harry Osborn as well...', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/olxpyq9kJAZ2NU1siLshhhXEPR7.jpg', \
                      user_id=2, rating=7.1))
    film.append(Films(film_title='Spider-Man 3', release_date='2007/05/03', \
                      film_desc='The seemingly invincible Spider-Man goes up against an all-new crop of villains—including the shape-shifting Sandman. While Spider-Man’s superpowers are altered by an alien organism, his alter ego, Peter Parker, deals with nemesis Eddie Brock and also gets caught up in a love triangle.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/sqZKCRYGovZ8aN99VVJSdL8Ja9k.jpg', \
                      user_id=2, rating=6.3))
    film.append(Films(film_title='Oz the Great and Powerful', release_date='2013/03/07', \
                      film_desc='Oscar Diggs, a small-time circus illusionist and con-artist, is whisked from Kansas to the Land of Oz where the inhabitants assume he\'s the great wizard of prophecy, there to save Oz from the clutches of evil.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/7lBgN59T5m1DaC9XcLkHOXdK9ax.jpg', \
                      user_id=2, rating=5.9))
    film.append(Films(film_title='Drag Me to Hell', release_date='2009/03/15', \
                      film_desc='After denying a woman the extension she needs to keep her home, loan officer Christine Brown sees her once-promising life take a startling turn for the worse. Christine is convinced she\'s been cursed by a Gypsy, but her boyfriend is skeptical. Her only hope seems to lie in a psychic who claims he can help her lift the curse and keep her soul from being dragged straight to hell.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/fdyejM5Zd6dsa0YyWa02ZAKwQzK.jpg', \
                      user_id=2, rating=6.3))
    film.append(Films(film_title='The Evil Dead', release_date='1981/10/15', \
                      film_desc='When a group of college students finds a mysterious book and recording in the old wilderness cabin they\'ve rented for the weekend, they unwittingly unleash a demonic force from the surrounding forest.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/uYxQ6xhP3WjqPZtxyAOnZQWnZqn.jpg', \
                      user_id=2, rating=7.3))
    film.append(Films(film_title='Army of Darkness', release_date='1993/02/19', \
                      film_desc='Ash is transported back to medieval days, where he is captured by the dreaded Lord Arthur. Aided by the deadly chainsaw that has become his only friend, Ash is sent on a perilous mission to recover the Book of the Dead, a powerful tome that gives its owner the power to summon an army of ghouls.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/mOsWtjRGABrPrqqtm0U6WQp4GVw.jpg', \
                      user_id=2, rating=7.3))
    film.append(Films(film_title='Serenity', release_date='2005/10/13', \
                      film_desc='When the renegade crew of Serenity agrees to hide a fugitive on their ship, they find themselves in an action-packed battle between the relentless military might of a totalitarian regime who will destroy anything – or anyone – to get the girl back and the bloodthirsty creatures who roam the uncharted areas of space. But... the greatest danger of all may be on their ship.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/2ZOm4cedJanmN85ZiWrwZPUNv0d.jpg', \
                      user_id=2, rating=7.4))
    film.append(Films(film_title='The Avengers', release_date='2012/05/03', \
                      film_desc='When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg', \
                      user_id=2, rating=7.7))
    film.append(Films(film_title='Avengers: Age of Ultron', release_date='2015/04/23', \
                      film_desc='When Tony Stark tries to jumpstart a dormant peacekeeping program, things go awry and Earth’s Mightiest Heroes are put to the ultimate test as the fate of the planet hangs in the balance. As the villainous Ultron emerges, it is up to The Avengers to stop him from enacting his terrible plans, and soon uneasy alliances and unexpected action pave the way for an epic and unique global adventure.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/4ssDuvEDkSArWEdyBl2X5EHvYKU.jpg', \
                      user_id=2, rating=7.3))
    film.append(Films(film_title='Toy Story', release_date='1995/11/21', \
                      film_desc='Led by Woody, Andy\'s toys live happily in his room until Andy\'s birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy\'s heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg', \
                      user_id=2, rating=8.0))
    film.append(Films(film_title='Justice League', release_date='2017/11/16', \
                      film_desc='Fuelled by his restored faith in humanity and inspired by Superman\'s selfless act, Bruce Wayne and Diana Prince assemble a team of metahumans consisting of Barry Allen, Arthur Curry and Victor Stone to face the catastrophic threat of Steppenwolf and the Parademons who are on the hunt for three Mother Boxes on Earth.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/eifGNCSDuxJeS1loAXil5bIGgvC.jpg', \
                      user_id=2, rating=6.2))
    film.append(Films(film_title='The Cabin in the Woods', release_date='2012/04/12', \
                      film_desc='Five college friends spend the weekend at a remote cabin in the woods, where they get more than they bargained for. Together, they must discover the truth behind the cabin in the woods.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/zZZe5wn0udlhMtdlDjN4NB72R6e.jpg', \
                      user_id=2, rating=6.6))
    film.append(Films(film_title='Atlantis: The Lost Empire', release_date='2001/12/21', \
                      film_desc='The world\'s most highly qualified crew of archaeologists and explorers is led by historian Milo Thatch as they board the incredible 1,000-foot submarine Ulysses and head deep into the mysteries of the sea. The underwater expedition takes an unexpected turn when the team\'s mission must switch from exploring Atlantis to protecting it.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8fUEFPUTF7kBMuKPiSQHxPvd8EZ.jpg', \
                      user_id=2, rating=6.9))
    film.append(Films(film_title='Alien Resurrection', release_date='1997/11/26', \
                      film_desc='Two hundred years after Lt. Ripley died, a group of scientists clone her, hoping to breed the ultimate weapon. But the new Ripley is full of surprises … as are the new aliens. Ripley must team with a band of smugglers to keep the creatures from reaching Earth.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/13162IOGtPQaZgnnY3raCJbUsW5.jpg', \
                      user_id=2, rating=6.1))
    film.append(Films(film_title='Avengers: Endgame', release_date='2019/04/25', \
                      film_desc='After the devastating events of Avengers: Infinity War, the universe is in ruins due to the efforts of the Mad Titan, Thanos. With the help of remaining allies, the Avengers must assemble once more in order to undo Thanos\' actions and restore order to the universe once and for all, no matter what consequences may be in store.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/or06FN3Dka5tukK1e9sl16pB3iy.jpg', \
                      user_id=2, rating=8.3))
    film.append(Films(film_title='Avengers: Infinity War', release_date='2018/05/03', \
                      film_desc='As the Avengers and their allies have continued to protect the world from threats too large for any one hero to handle, a new danger has emerged from the cosmic shadows: Thanos. A despot of intergalactic infamy, his goal is to collect all six Infinity Stones, artifacts of unimaginable power, and use them to inflict his twisted will on all of reality. Everything the Avengers have fought for has led up to this moment - the fate of Earth and existence itself has never been more uncertain.', \
                      poster='https://www.themoviedb.org/t/p/w600_and_h900_bestv2/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg', \
                      user_id=2, rating=8.3))
    for i in range(len(film)):
        db.session.add(film[i])
    db.session.commit()

    film_genre = []
    film_genre.append(Films_Genres(film_id=41, genre_id=28))
    film_genre.append(Films_Genres(film_id=41, genre_id=29))
    film_genre.append(Films_Genres(film_id=41, genre_id=27))
    film_genre.append(Films_Genres(film_id=42, genre_id=27))
    film_genre.append(Films_Genres(film_id=42, genre_id=30))
    film_genre.append(Films_Genres(film_id=42, genre_id=31))
    film_genre.append(Films_Genres(film_id=43, genre_id=28))
    film_genre.append(Films_Genres(film_id=43, genre_id=30))
    film_genre.append(Films_Genres(film_id=43, genre_id=32))
    film_genre.append(Films_Genres(film_id=43, genre_id=29))
    film_genre.append(Films_Genres(film_id=44, genre_id=28))
    film_genre.append(Films_Genres(film_id=44, genre_id=30))
    film_genre.append(Films_Genres(film_id=44, genre_id=32))
    film_genre.append(Films_Genres(film_id=44, genre_id=29))
    film_genre.append(Films_Genres(film_id=45, genre_id=28))
    film_genre.append(Films_Genres(film_id=45, genre_id=30))
    film_genre.append(Films_Genres(film_id=45, genre_id=32))
    film_genre.append(Films_Genres(film_id=46, genre_id=28))
    film_genre.append(Films_Genres(film_id=46, genre_id=30))
    film_genre.append(Films_Genres(film_id=46, genre_id=33))
    film_genre.append(Films_Genres(film_id=47, genre_id=29))
    film_genre.append(Films_Genres(film_id=47, genre_id=30))
    film_genre.append(Films_Genres(film_id=47, genre_id=39))
    film_genre.append(Films_Genres(film_id=49, genre_id=29))
    film_genre.append(Films_Genres(film_id=49, genre_id=39))
    film_genre.append(Films_Genres(film_id=50, genre_id=27))
    film_genre.append(Films_Genres(film_id=50, genre_id=31))
    film_genre.append(Films_Genres(film_id=51, genre_id=33))
    film_genre.append(Films_Genres(film_id=51, genre_id=40))
    film_genre.append(Films_Genres(film_id=51, genre_id=30))
    film_genre.append(Films_Genres(film_id=52, genre_id=27))
    film_genre.append(Films_Genres(film_id=52, genre_id=28))
    film_genre.append(Films_Genres(film_id=52, genre_id=31))
    film_genre.append(Films_Genres(film_id=53, genre_id=30))
    film_genre.append(Films_Genres(film_id=53, genre_id=40))
    film_genre.append(Films_Genres(film_id=53, genre_id=33))
    film_genre.append(Films_Genres(film_id=54, genre_id=30))
    film_genre.append(Films_Genres(film_id=54, genre_id=32))
    film_genre.append(Films_Genres(film_id=55, genre_id=27))
    film_genre.append(Films_Genres(film_id=55, genre_id=31))
    film_genre.append(Films_Genres(film_id=55, genre_id=28))
    film_genre.append(Films_Genres(film_id=56, genre_id=28))
    film_genre.append(Films_Genres(film_id=56, genre_id=31))
    film_genre.append(Films_Genres(film_id=57, genre_id=27))
    film_genre.append(Films_Genres(film_id=57, genre_id=31))
    film_genre.append(Films_Genres(film_id=57, genre_id=35))
    film_genre.append(Films_Genres(film_id=57, genre_id=34))
    film_genre.append(Films_Genres(film_id=58, genre_id=41))
    film_genre.append(Films_Genres(film_id=58, genre_id=39))
    film_genre.append(Films_Genres(film_id=58, genre_id=30))
    film_genre.append(Films_Genres(film_id=58, genre_id=29))
    film_genre.append(Films_Genres(film_id=59, genre_id=30))
    film_genre.append(Films_Genres(film_id=59, genre_id=38))
    film_genre.append(Films_Genres(film_id=59, genre_id=29))
    film_genre.append(Films_Genres(film_id=60, genre_id=39))
    film_genre.append(Films_Genres(film_id=60, genre_id=29))
    film_genre.append(Films_Genres(film_id=61, genre_id=41))
    film_genre.append(Films_Genres(film_id=61, genre_id=39))
    film_genre.append(Films_Genres(film_id=61, genre_id=29))
    film_genre.append(Films_Genres(film_id=62, genre_id=39))
    film_genre.append(Films_Genres(film_id=62, genre_id=29))
    film_genre.append(Films_Genres(film_id=63, genre_id=38))
    film_genre.append(Films_Genres(film_id=64, genre_id=32))
    film_genre.append(Films_Genres(film_id=64, genre_id=29))
    film_genre.append(Films_Genres(film_id=65, genre_id=32))
    film_genre.append(Films_Genres(film_id=65, genre_id=29))
    film_genre.append(Films_Genres(film_id=66, genre_id=42))
    film_genre.append(Films_Genres(film_id=66, genre_id=30))
    film_genre.append(Films_Genres(film_id=66, genre_id=29))
    film_genre.append(Films_Genres(film_id=67, genre_id=29))
    film_genre.append(Films_Genres(film_id=67, genre_id=32))
    film_genre.append(Films_Genres(film_id=68, genre_id=30))
    film_genre.append(Films_Genres(film_id=68, genre_id=43))
    film_genre.append(Films_Genres(film_id=69, genre_id=30))
    film_genre.append(Films_Genres(film_id=69, genre_id=28))
    film_genre.append(Films_Genres(film_id=69, genre_id=29))
    film_genre.append(Films_Genres(film_id=69, genre_id=33))
    film_genre.append(Films_Genres(film_id=70, genre_id=28))
    film_genre.append(Films_Genres(film_id=70, genre_id=32))
    film_genre.append(Films_Genres(film_id=71, genre_id=32))
    film_genre.append(Films_Genres(film_id=71, genre_id=30))
    film_genre.append(Films_Genres(film_id=71, genre_id=43))
    film_genre.append(Films_Genres(film_id=71, genre_id=39))
    film_genre.append(Films_Genres(film_id=72, genre_id=32))
    film_genre.append(Films_Genres(film_id=72, genre_id=29))
    film_genre.append(Films_Genres(film_id=73, genre_id=32))
    film_genre.append(Films_Genres(film_id=73, genre_id=28))
    film_genre.append(Films_Genres(film_id=73, genre_id=29))
    film_genre.append(Films_Genres(film_id=74, genre_id=28))
    film_genre.append(Films_Genres(film_id=74, genre_id=31))
    film_genre.append(Films_Genres(film_id=74, genre_id=34))
    film_genre.append(Films_Genres(film_id=74, genre_id=27))
    film_genre.append(Films_Genres(film_id=75, genre_id=30))
    film_genre.append(Films_Genres(film_id=75, genre_id=41))
    film_genre.append(Films_Genres(film_id=76, genre_id=28))
    film_genre.append(Films_Genres(film_id=76, genre_id=29))
    film_genre.append(Films_Genres(film_id=76, genre_id=27))
    film_genre.append(Films_Genres(film_id=77, genre_id=28))
    film_genre.append(Films_Genres(film_id=77, genre_id=29))
    film_genre.append(Films_Genres(film_id=77, genre_id=27))
    film_genre.append(Films_Genres(film_id=78, genre_id=28))
    film_genre.append(Films_Genres(film_id=78, genre_id=29))
    film_genre.append(Films_Genres(film_id=78, genre_id=27))
    film_genre.append(Films_Genres(film_id=79, genre_id=28))
    film_genre.append(Films_Genres(film_id=79, genre_id=29))
    film_genre.append(Films_Genres(film_id=80, genre_id=29))
    film_genre.append(Films_Genres(film_id=80, genre_id=28))
    film_genre.append(Films_Genres(film_id=80, genre_id=31))
    film_genre.append(Films_Genres(film_id=80, genre_id=27))
    film_genre.append(Films_Genres(film_id=81, genre_id=36))
    film_genre.append(Films_Genres(film_id=81, genre_id=35))
    film_genre.append(Films_Genres(film_id=81, genre_id=34))
    film_genre.append(Films_Genres(film_id=82, genre_id=36))
    film_genre.append(Films_Genres(film_id=82, genre_id=34))
    film_genre.append(Films_Genres(film_id=82, genre_id=31))
    film_genre.append(Films_Genres(film_id=83, genre_id=34))
    film_genre.append(Films_Genres(film_id=83, genre_id=31))
    film_genre.append(Films_Genres(film_id=83, genre_id=36))
    film_genre.append(Films_Genres(film_id=84, genre_id=36))
    film_genre.append(Films_Genres(film_id=84, genre_id=34))
    film_genre.append(Films_Genres(film_id=84, genre_id=35))
    film_genre.append(Films_Genres(film_id=85, genre_id=34))
    film_genre.append(Films_Genres(film_id=85, genre_id=35))
    film_genre.append(Films_Genres(film_id=85, genre_id=36))
    film_genre.append(Films_Genres(film_id=86, genre_id=34))
    film_genre.append(Films_Genres(film_id=86, genre_id=35))
    film_genre.append(Films_Genres(film_id=86, genre_id=36))
    film_genre.append(Films_Genres(film_id=86, genre_id=41))
    film_genre.append(Films_Genres(film_id=86, genre_id=28))
    film_genre.append(Films_Genres(film_id=87, genre_id=34))
    film_genre.append(Films_Genres(film_id=87, genre_id=35))
    film_genre.append(Films_Genres(film_id=87, genre_id=36))
    film_genre.append(Films_Genres(film_id=87, genre_id=31))
    film_genre.append(Films_Genres(film_id=88, genre_id=31))
    film_genre.append(Films_Genres(film_id=88, genre_id=36))
    film_genre.append(Films_Genres(film_id=88, genre_id=34))
    film_genre.append(Films_Genres(film_id=89, genre_id=28))
    film_genre.append(Films_Genres(film_id=89, genre_id=29))
    film_genre.append(Films_Genres(film_id=89, genre_id=32))
    film_genre.append(Films_Genres(film_id=90, genre_id=28))
    film_genre.append(Films_Genres(film_id=90, genre_id=29))
    film_genre.append(Films_Genres(film_id=90, genre_id=32))
    film_genre.append(Films_Genres(film_id=91, genre_id=28))
    film_genre.append(Films_Genres(film_id=91, genre_id=32))
    film_genre.append(Films_Genres(film_id=91, genre_id=29))
    film_genre.append(Films_Genres(film_id=91, genre_id=30))
    film_genre.append(Films_Genres(film_id=92, genre_id=27))
    film_genre.append(Films_Genres(film_id=92, genre_id=28))
    film_genre.append(Films_Genres(film_id=92, genre_id=31))
    film_genre.append(Films_Genres(film_id=93, genre_id=28))
    film_genre.append(Films_Genres(film_id=93, genre_id=32))
    film_genre.append(Films_Genres(film_id=93, genre_id=30))
    film_genre.append(Films_Genres(film_id=93, genre_id=29))
    film_genre.append(Films_Genres(film_id=94, genre_id=28))
    film_genre.append(Films_Genres(film_id=94, genre_id=32))
    film_genre.append(Films_Genres(film_id=94, genre_id=29))
    film_genre.append(Films_Genres(film_id=95, genre_id=30))
    film_genre.append(Films_Genres(film_id=96, genre_id=35))
    film_genre.append(Films_Genres(film_id=96, genre_id=34))
    film_genre.append(Films_Genres(film_id=96, genre_id=41))
    film_genre.append(Films_Genres(film_id=97, genre_id=31))
    film_genre.append(Films_Genres(film_id=97, genre_id=34))
    film_genre.append(Films_Genres(film_id=97, genre_id=30))
    film_genre.append(Films_Genres(film_id=97, genre_id=41))
    film_genre.append(Films_Genres(film_id=98, genre_id=41))
    film_genre.append(Films_Genres(film_id=98, genre_id=31))
    film_genre.append(Films_Genres(film_id=98, genre_id=34))
    film_genre.append(Films_Genres(film_id=99, genre_id=30))
    film_genre.append(Films_Genres(film_id=99, genre_id=39))
    film_genre.append(Films_Genres(film_id=100, genre_id=34))
    film_genre.append(Films_Genres(film_id=100, genre_id=30))
    film_genre.append(Films_Genres(film_id=100, genre_id=29))
    film_genre.append(Films_Genres(film_id=101, genre_id=34))
    film_genre.append(Films_Genres(film_id=101, genre_id=44))
    film_genre.append(Films_Genres(film_id=102, genre_id=32))
    film_genre.append(Films_Genres(film_id=103, genre_id=30))
    film_genre.append(Films_Genres(film_id=103, genre_id=32))
    film_genre.append(Films_Genres(film_id=104, genre_id=32))
    film_genre.append(Films_Genres(film_id=104, genre_id=30))
    film_genre.append(Films_Genres(film_id=104, genre_id=34))
    film_genre.append(Films_Genres(film_id=105, genre_id=38))
    film_genre.append(Films_Genres(film_id=105, genre_id=27))
    film_genre.append(Films_Genres(film_id=105, genre_id=29))
    film_genre.append(Films_Genres(film_id=106, genre_id=30))
    film_genre.append(Films_Genres(film_id=106, genre_id=41))
    film_genre.append(Films_Genres(film_id=106, genre_id=42))
    film_genre.append(Films_Genres(film_id=107, genre_id=37))
    film_genre.append(Films_Genres(film_id=107, genre_id=38))
    film_genre.append(Films_Genres(film_id=107, genre_id=29))
    film_genre.append(Films_Genres(film_id=108, genre_id=32))
    film_genre.append(Films_Genres(film_id=108, genre_id=30))
    film_genre.append(Films_Genres(film_id=108, genre_id=40))
    film_genre.append(Films_Genres(film_id=110, genre_id=30))
    film_genre.append(Films_Genres(film_id=110, genre_id=27))
    film_genre.append(Films_Genres(film_id=110, genre_id=39))
    film_genre.append(Films_Genres(film_id=111, genre_id=27))
    film_genre.append(Films_Genres(film_id=111, genre_id=30))
    film_genre.append(Films_Genres(film_id=112, genre_id=30))
    film_genre.append(Films_Genres(film_id=112, genre_id=29))
    film_genre.append(Films_Genres(film_id=112, genre_id=32))
    film_genre.append(Films_Genres(film_id=113, genre_id=28))
    film_genre.append(Films_Genres(film_id=113, genre_id=32))
    film_genre.append(Films_Genres(film_id=113, genre_id=29))
    film_genre.append(Films_Genres(film_id=114, genre_id=29))
    film_genre.append(Films_Genres(film_id=114, genre_id=39))
    film_genre.append(Films_Genres(film_id=115, genre_id=27))
    film_genre.append(Films_Genres(film_id=115, genre_id=31))
    film_genre.append(Films_Genres(film_id=116, genre_id=30))
    film_genre.append(Films_Genres(film_id=116, genre_id=33))
    film_genre.append(Films_Genres(film_id=116, genre_id=39))
    film_genre.append(Films_Genres(film_id=117, genre_id=30))
    film_genre.append(Films_Genres(film_id=117, genre_id=42))
    film_genre.append(Films_Genres(film_id=118, genre_id=30))
    film_genre.append(Films_Genres(film_id=119, genre_id=34))
    film_genre.append(Films_Genres(film_id=119, genre_id=28))
    film_genre.append(Films_Genres(film_id=120, genre_id=30))
    film_genre.append(Films_Genres(film_id=120, genre_id=32))
    film_genre.append(Films_Genres(film_id=120, genre_id=29))
    film_genre.append(Films_Genres(film_id=120, genre_id=28))
    film_genre.append(Films_Genres(film_id=121, genre_id=42))
    film_genre.append(Films_Genres(film_id=121, genre_id=30))
    film_genre.append(Films_Genres(film_id=121, genre_id=32))
    film_genre.append(Films_Genres(film_id=122, genre_id=27))
    film_genre.append(Films_Genres(film_id=122, genre_id=34))
    film_genre.append(Films_Genres(film_id=122, genre_id=32))
    film_genre.append(Films_Genres(film_id=122, genre_id=39))
    film_genre.append(Films_Genres(film_id=123, genre_id=30))
    film_genre.append(Films_Genres(film_id=123, genre_id=42))
    film_genre.append(Films_Genres(film_id=123, genre_id=41))
    film_genre.append(Films_Genres(film_id=124, genre_id=30))
    film_genre.append(Films_Genres(film_id=124, genre_id=42))
    film_genre.append(Films_Genres(film_id=125, genre_id=34))
    film_genre.append(Films_Genres(film_id=125, genre_id=38))
    film_genre.append(Films_Genres(film_id=125, genre_id=42))
    film_genre.append(Films_Genres(film_id=126, genre_id=34))
    film_genre.append(Films_Genres(film_id=126, genre_id=28))
    film_genre.append(Films_Genres(film_id=127, genre_id=28))
    film_genre.append(Films_Genres(film_id=127, genre_id=31))
    film_genre.append(Films_Genres(film_id=127, genre_id=34))
    film_genre.append(Films_Genres(film_id=128, genre_id=28))
    film_genre.append(Films_Genres(film_id=128, genre_id=31))
    film_genre.append(Films_Genres(film_id=128, genre_id=34))
    film_genre.append(Films_Genres(film_id=129, genre_id=34))
    film_genre.append(Films_Genres(film_id=129, genre_id=31))
    film_genre.append(Films_Genres(film_id=129, genre_id=35))
    film_genre.append(Films_Genres(film_id=130, genre_id=38))
    film_genre.append(Films_Genres(film_id=130, genre_id=29))
    film_genre.append(Films_Genres(film_id=131, genre_id=38))
    film_genre.append(Films_Genres(film_id=132, genre_id=34))
    film_genre.append(Films_Genres(film_id=132, genre_id=38))
    film_genre.append(Films_Genres(film_id=132, genre_id=42))
    film_genre.append(Films_Genres(film_id=133, genre_id=27))
    film_genre.append(Films_Genres(film_id=133, genre_id=28))
    film_genre.append(Films_Genres(film_id=133, genre_id=31))
    film_genre.append(Films_Genres(film_id=133, genre_id=29))
    film_genre.append(Films_Genres(film_id=134, genre_id=27))
    film_genre.append(Films_Genres(film_id=134, genre_id=28))
    film_genre.append(Films_Genres(film_id=134, genre_id=31))
    film_genre.append(Films_Genres(film_id=135, genre_id=27))
    film_genre.append(Films_Genres(film_id=135, genre_id=28))
    film_genre.append(Films_Genres(film_id=135, genre_id=31))
    film_genre.append(Films_Genres(film_id=136, genre_id=31))
    film_genre.append(Films_Genres(film_id=136, genre_id=36))
    film_genre.append(Films_Genres(film_id=136, genre_id=35))
    film_genre.append(Films_Genres(film_id=136, genre_id=42))
    film_genre.append(Films_Genres(film_id=137, genre_id=27))
    film_genre.append(Films_Genres(film_id=137, genre_id=28))
    film_genre.append(Films_Genres(film_id=137, genre_id=31))
    film_genre.append(Films_Genres(film_id=137, genre_id=34))
    film_genre.append(Films_Genres(film_id=138, genre_id=38))
    film_genre.append(Films_Genres(film_id=138, genre_id=42))
    film_genre.append(Films_Genres(film_id=138, genre_id=34))
    film_genre.append(Films_Genres(film_id=138, genre_id=29))
    film_genre.append(Films_Genres(film_id=139, genre_id=36))
    film_genre.append(Films_Genres(film_id=139, genre_id=35))
    film_genre.append(Films_Genres(film_id=139, genre_id=31))
    film_genre.append(Films_Genres(film_id=139, genre_id=27))
    film_genre.append(Films_Genres(film_id=140, genre_id=38))
    film_genre.append(Films_Genres(film_id=140, genre_id=28))
    film_genre.append(Films_Genres(film_id=140, genre_id=27))
    film_genre.append(Films_Genres(film_id=141, genre_id=31))
    film_genre.append(Films_Genres(film_id=141, genre_id=27))
    film_genre.append(Films_Genres(film_id=141, genre_id=28))
    film_genre.append(Films_Genres(film_id=142, genre_id=31))
    film_genre.append(Films_Genres(film_id=142, genre_id=27))
    film_genre.append(Films_Genres(film_id=142, genre_id=28))
    for i in film_genre:
        db.session.add(i)
    db.session.commit()

    film_director = []
    film_director.append(Films_Directors(director_id=27, film_id=41))
    film_director.append(Films_Directors(director_id=27, film_id=42))
    film_director.append(Films_Directors(director_id=27, film_id=43))
    film_director.append(Films_Directors(director_id=27, film_id=44))
    film_director.append(Films_Directors(director_id=27, film_id=45))
    film_director.append(Films_Directors(director_id=27, film_id=46))
    film_director.append(Films_Directors(director_id=27, film_id=47))
    film_director.append(Films_Directors(director_id=27, film_id=49))
    film_director.append(Films_Directors(director_id=28, film_id=50))
    film_director.append(Films_Directors(director_id=28, film_id=51))
    film_director.append(Films_Directors(director_id=28, film_id=52))
    film_director.append(Films_Directors(director_id=28, film_id=53))
    film_director.append(Films_Directors(director_id=28, film_id=54))
    film_director.append(Films_Directors(director_id=28, film_id=55))
    film_director.append(Films_Directors(director_id=28, film_id=56))
    film_director.append(Films_Directors(director_id=28, film_id=57))
    film_director.append(Films_Directors(director_id=29, film_id=58))
    film_director.append(Films_Directors(director_id=29, film_id=59))
    film_director.append(Films_Directors(director_id=29, film_id=60))
    film_director.append(Films_Directors(director_id=29, film_id=61))
    film_director.append(Films_Directors(director_id=29, film_id=62))
    film_director.append(Films_Directors(director_id=29, film_id=63))
    film_director.append(Films_Directors(director_id=29, film_id=64))
    film_director.append(Films_Directors(director_id=29, film_id=65))
    film_director.append(Films_Directors(director_id=30, film_id=66))
    film_director.append(Films_Directors(director_id=30, film_id=67))
    film_director.append(Films_Directors(director_id=30, film_id=68))
    film_director.append(Films_Directors(director_id=30, film_id=69))
    film_director.append(Films_Directors(director_id=30, film_id=70))
    film_director.append(Films_Directors(director_id=30, film_id=71))
    film_director.append(Films_Directors(director_id=30, film_id=72))
    film_director.append(Films_Directors(director_id=30, film_id=73))
    film_director.append(Films_Directors(director_id=31, film_id=74))
    film_director.append(Films_Directors(director_id=31, film_id=75))
    film_director.append(Films_Directors(director_id=31, film_id=76))
    film_director.append(Films_Directors(director_id=31, film_id=77))
    film_director.append(Films_Directors(director_id=31, film_id=78))
    film_director.append(Films_Directors(director_id=31, film_id=79))
    film_director.append(Films_Directors(director_id=31, film_id=80))
    film_director.append(Films_Directors(director_id=32, film_id=81))
    film_director.append(Films_Directors(director_id=32, film_id=82))
    film_director.append(Films_Directors(director_id=32, film_id=83))
    film_director.append(Films_Directors(director_id=32, film_id=84))
    film_director.append(Films_Directors(director_id=32, film_id=85))
    film_director.append(Films_Directors(director_id=32, film_id=86))
    film_director.append(Films_Directors(director_id=32, film_id=87))
    film_director.append(Films_Directors(director_id=32, film_id=88))
    film_director.append(Films_Directors(director_id=33, film_id=89))
    film_director.append(Films_Directors(director_id=33, film_id=90))
    film_director.append(Films_Directors(director_id=33, film_id=91))
    film_director.append(Films_Directors(director_id=33, film_id=92))
    film_director.append(Films_Directors(director_id=33, film_id=93))
    film_director.append(Films_Directors(director_id=33, film_id=94))
    film_director.append(Films_Directors(director_id=34, film_id=95))
    film_director.append(Films_Directors(director_id=34, film_id=96))
    film_director.append(Films_Directors(director_id=34, film_id=97))
    film_director.append(Films_Directors(director_id=34, film_id=98))
    film_director.append(Films_Directors(director_id=34, film_id=99))
    film_director.append(Films_Directors(director_id=34, film_id=100))
    film_director.append(Films_Directors(director_id=34, film_id=101))
    film_director.append(Films_Directors(director_id=34, film_id=102))
    film_director.append(Films_Directors(director_id=35, film_id=103))
    film_director.append(Films_Directors(director_id=35, film_id=104))
    film_director.append(Films_Directors(director_id=35, film_id=105))
    film_director.append(Films_Directors(director_id=35, film_id=106))
    film_director.append(Films_Directors(director_id=35, film_id=107))
    film_director.append(Films_Directors(director_id=35, film_id=108))
    film_director.append(Films_Directors(director_id=36, film_id=110))
    film_director.append(Films_Directors(director_id=36, film_id=111))
    film_director.append(Films_Directors(director_id=36, film_id=112))
    film_director.append(Films_Directors(director_id=36, film_id=113))
    film_director.append(Films_Directors(director_id=36, film_id=114))
    film_director.append(Films_Directors(director_id=36, film_id=115))
    film_director.append(Films_Directors(director_id=36, film_id=116))
    film_director.append(Films_Directors(director_id=40, film_id=117))
    film_director.append(Films_Directors(director_id=41, film_id=117))
    film_director.append(Films_Directors(director_id=42, film_id=117))
    film_director.append(Films_Directors(director_id=42, film_id=118))
    film_director.append(Films_Directors(director_id=43, film_id=118))
    film_director.append(Films_Directors(director_id=44, film_id=118))
    film_director.append(Films_Directors(director_id=45, film_id=118))
    film_director.append(Films_Directors(director_id=43, film_id=119))
    film_director.append(Films_Directors(director_id=43, film_id=120))
    film_director.append(Films_Directors(director_id=43, film_id=121))
    film_director.append(Films_Directors(director_id=43, film_id=122))
    film_director.append(Films_Directors(director_id=43, film_id=123))
    film_director.append(Films_Directors(director_id=43, film_id=124))
    film_director.append(Films_Directors(director_id=37, film_id=125))
    film_director.append(Films_Directors(director_id=37, film_id=126))
    film_director.append(Films_Directors(director_id=37, film_id=127))
    film_director.append(Films_Directors(director_id=37, film_id=128))
    film_director.append(Films_Directors(director_id=37, film_id=129))
    film_director.append(Films_Directors(director_id=37, film_id=130))
    film_director.append(Films_Directors(director_id=37, film_id=131))
    film_director.append(Films_Directors(director_id=37, film_id=132))
    film_director.append(Films_Directors(director_id=39, film_id=133))
    film_director.append(Films_Directors(director_id=39, film_id=134))
    film_director.append(Films_Directors(director_id=39, film_id=135))
    film_director.append(Films_Directors(director_id=39, film_id=136))
    film_director.append(Films_Directors(director_id=39, film_id=137))
    film_director.append(Films_Directors(director_id=39, film_id=138))
    film_director.append(Films_Directors(director_id=39, film_id=139))
    film_director.append(Films_Directors(director_id=39, film_id=140))
    film_director.append(Films_Directors(director_id=38, film_id=141))
    film_director.append(Films_Directors(director_id=38, film_id=142))
    for i in film_director:
        db.session.add(i)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
