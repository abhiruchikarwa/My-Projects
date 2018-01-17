import numpy as np

import plotly.plotly as py

import matplotlib.pyplot as plt

import nltk

import tkinter as tk
from tkinter import *
class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master,width=500,height=60)
        self.grid()

        self.fnLabel = Label(master, text="TWITTER SENTIMENT ANALYSIS USING PYTHON")
        self.fnLabel.config(font=("Times New Roman", 14))
        self.fnLabel.grid()

        self.fnameLabel = Label(master, text="Choose File for analysis:")
        self.fnameLabel.grid()

        self.fc = Label(master, text="Chosen file path: ")
        self.fc.grid()

        self.label_fpath = Label(master, text="")
        self.label_fpath.grid()

        self.err_label = Label(master, text="")
        self.err_label.grid()
        
        self.submitButton = Button(master, command=self.buttonClick, text="Choose File")
        self.submitButton.grid()

        self.analyseButton = Button(master, command=self.analyse, text="analyse")
        self.analyseButton.grid()

        self.fpath=''


    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        
        self.fpath=filedialog.askopenfilename()
        self.label_fpath.config(text=self.fpath)
        self.err_label.config(text='')
        pass

    def analyse(self):
        #File analysis code starts here

        pos_tweets = [('I love this car', 'positive'),

                    ('This view is amazing', 'positive'),

                    ('I feel great this morning', 'positive'),

                    ('I am so excited about the concert', 'positive'),
                    ('He is my best friend', 'positive'),

                    ('The entire audience applauded at the conclusion of the film.', 'positive'),	
                    ('I left the theater with a lilt in my step', 'positive'),	
                    ('Duris has a wholesome appearance and gives a fine performance.', 'positive'),	
                    ('The rest of the cast also play well.', 'positive'),	
                    ('Cinematography noteworthy including fine views of Barcelona and its famed Gaudi towers', 'positive'),	
                    ('STEAMBOAT WILLIE is an amazingly important film to our cinema history', 'positive'),	
                    ('This second appearance of Mickey Mouse (following the silent PLANE CRAZY earlier that year) is probably his most famous film--mostly because it was so ground-breaking', 'positive'),	
                    ('While you don not yet hear Mickey speak, there are tons of sound effects and music throughout the film--something we take for granted now but which was a huge crowd pleaser in positive928', 'positive'),	
                    ('However, after seeing the short again after about 25 years, I was amazed at how timeless the film actually is', 'positive'),	
                    ('Its just adorable seeing Mickey playing "Turkey in the Straw" in a highly imaginative (if occasionally cruel) way', 'positive'),	
                    ('Clever and a real crowd-pleaser--this film still ranks among Mickeys best films even after 80 wonderful years', 'positive'),	
                    ('Being a 90s child, I truly enjoyed this show and I can proudly say that I enjoyed it big time and even more than the classical WB cartoons', 'positive'),
                    ('But "Tiny Toons" kept the 90s vibe and delivered one of the most popular, funny, and underrated cartoons ever created', 'positive'),
                    ('The memories are murky but I can only say that I enjoyed every single episode and product related to the show', 'positive'),
                    ('Easily, none other cartoon made me laugh in a tender way (before getting into dark sitcoms oriented for teenagers)', 'positive'),
                    ('The characters were all funny and had the peculiarity of not having a true lead character', 'positive'),
                    ('Every single character was hilarious and deserved to be called a lead', 'positive'),
                    ('The characters are interesting and you really care for them', 'positive'),
                    ('An instant classic, with a great soundtrack and a catchy song during the ending credits', 'positive'),
                    ('Do not miss it', 'positive'),
                    ('Emily Watsons character is very strong, and she has only to give a quick glance and you understand everything', 'positive'),
                    ('Despite the pans of reviewers, I liked this movie', 'positive'),
                    ('In fact, I liked it better than Interview With a Vampire and I liked this Lestat (Stuart Townsend) better than Cruises attempt', 'positive'),
                    ('Aailiyah was pretty good as Akasha, in places compelling (her first entrance and mini dance scene)', 'positive'),
                    ('I am a big fan of this series mostly due to Anne Rice style, sensitivities and treatments', 'positive'),
                    ('I guess I liked the details of his dysfunction--he was believable', 'positive'),
                    ('But I thought his acting was skilled', 'positive'),
                    ('Meredith M was better than all right', 'positive'),
                    ('A very charming film with wonderful sentiment and heart', 'positive'),
                    ('It is rare when a film-maker takes the time to tell a worthy moral tale with care and love that does not fall into the trap of being overly syrupy or over indulgent', 'positive'),
                    ('Nine out of ten for a truly lovely film', 'positive'),
                    ('This early film from future goremeister Lucio Fulci is a very good addition to the giallo sub-genre', 'positive'),
                    ('This is one of the best Italian thrillers of the early 70s', 'positive'),
                    ('A standout scene', 'positive'),
                    ('It is still wild stuff though and is highly recommended to fans of giallo cinema', 'positive'),
                    ('The movie was very interesting from beginning to the end', 'positive'),
                    ('I liked the way Dustin Hoffmans character was ready to do just about everything to stay with his son', 'positive'),
                    ('This movie is also revealing', 'positive'),
                    ('Personally, I think it shows that people should learn to find a compromise them self without involving other people into issue', 'positive'),
                    ('All the actors give a wonderful performance, especially Jennifer Rubin as Jamie Harris, who changes from the nervous starlet in the beginning through the strange events she is part of to the cool star', 'positive'),
                    ('You learn a lot about the real inside emotions of people in this movie, and a lot about the movie business itself', 'positive'),
                    ('The movie in movie situations in the beginning and through the game that is played with her by the "acting coach" are fascinating', 'positive'),
                    ('Also the music by Mark Snow is possibly the best score I have ever heard', 'positive'),
                    ('You would not forget this movie!  ', 'positive'),
                    ('This movie is so awesome!  ', 'positive'),
                    ('I loved it, it was really scary', 'positive'),
                    ('I love the Scream movies and all horror movies and this one ranks way up there', 'positive'),
                    ('If you want a real scare rent this one!  ', 'positive'),
                    ('43018', 'positive'),
                    ('This is an extraordinary film', 'positive'),
                    ('This was such an awesome movie that i bought it off of Ebay', 'positive'),	
                    ('I really loved the story line and the poler bear was kinda cute.But if anyone has a question about Fort Steele just ask away:)  ', 'positive'),	

                    ('I think the most wonderful parts literally full of wonder) are the excerpts from his works', 'positive'),	
                    ('The sets (especially designed to work with the camera) are amazing....stylized beautiful and effective', 'positive'),	
                    ('They could be used as exemplars for any set designer', 'positive'),	
                    ('The stories were powerful explorations of the nature of man and of art', 'positive'),	
                    ('After watching this film I wanted to learn more about the works of this artist', 'positive'),	
                    ('I highly recommend this movie for anyone interested in art poetry theater politics or Japanese history', 'positive'),	
                    ('Here in The Wind and the Lion we see a wonderful rendering of Americas own Imperial age', 'positive'),	
                    ('What makes this story different are the terrific production values - faultless photography composition and editing - the terrific casting - the underappreciated Brian Keith playing a bully Teddy - and vivid history', 'positive'),	
                    ('Though The Wind and the Lion is told largely through the eyes of the son every member of the family can identify with one of the characters whether it be Sean Connerys noble brigand Candace Bergens feisty heroine John Hustons wily John Hay or Steve Kanalys spiffy radiant ruthless can-do lieutenant Roosevelts Big Stick', 'positive'),	
                    ('This is high adventure at its best', 'positive'),	
                    ('I think it was Robert Ryans best film because he portrayed someone like my father and he was a schizophrenic in real life(my father) although he never murdered anyone but was affected more so during the second world war which made him worse', 'positive'),	
                    ('Having to humour him just to get by and get through the day was so apt', 'positive'),	
                    ('My mother and brother had to do this)When I saw Robert Ryan portraying this type of man it was a very good imitation of this type of individual and I was impressed', 'positive'),		
                    ('Non-linear narration thus many flashbacks and every part are articulated quite well', 'positive'),	
                    ('The good cinematography also makes her and Monica Bellucci look very beautiful', 'positive'),	
                    ('A good commentary of todays love and undoubtedly a film worth seeing', 'positive'),	
                    ('For people who are first timers in film making I think they did an excellent job!!  ', 'positive'),	
                    ('It was very popular when I was in the cinema a good house and very good reactions and plenty of laughs', 'positive'),	
                    ('It is a feel-good film and that is how I felt when I came out of the cinema!  ', 'positive'),	
                    ('It has northern humour and positive about the community it represents', 'positive'),	
                    ('I rather enjoyed it', 'positive'),	
                    ('I liked it', 'positive'),		
                    ('It really created a unique feeling though', 'positive'),	
                    ('Vivian Schilling did an excellent job with the script', 'positive'),	
                    ('A world better than 95% of the garbage in the theatres today', 'positive'),
                      ('MANNA FROM HEAVEN is a terrific film that is both predictable and unpredictable at the same time.  ', 'positive'),
('The scenes are often funny and occasionally touching as the characters evaluate their lives and where they are going.  ', 'positive'),
('The cast of veteran actors are more than just a nostalgia trip.  ', 'positive'),
('Ursula Burtons portrayal of the nun is both touching and funny at the same time with out making fun of nuns or the church.  ', 'positive'),
('If you are looking for a movie with a terrific cast some good music ( including a Shirley Jones rendition of The Way You Look Tonight) and an uplifting ending give this one a try.  ', 'positive'),
('I do not think you will be disappointed.  ', 'positive'),
('The only thing really worth watching was the scenery and the house because it is beautiful.  ', 'positive'),
('But in terms of the writing its very fresh and bold.  ', 'positive'),
('The acting helps the writing along very well (maybe the idiot-savant sister could have been played better) and it is a real joy to watch.  ', 'positive'),
('some applause should be given to the prelude however.  ', 'positive'),
('I really liked that.  ', 'positive'),
('A great film by a great director.  ', 'positive'),
('The movie had you on the edge of your seat and made you somewhat afraid to go to your car at the end of the night.  ', 'positive'),
('The music in the film is really nice too.  ', 'positive'),
('I would advise anyone to go and see it.  ', 'positive'),
('Brilliant!  ', 'positive'),
('10-Oct', 'positive'),
('I liked this movie way too much.  ', 'positive'),
('It rocked my world and is certainly a must see for anyone with no social or physical outlets.  ', 'positive'),
('This is definitely a cult classic well worth viewing and sharing with others.  ', 'positive'),
('Also its a real treat to see Anthony Quinn playing Crazy Horse.  ', 'positive'),
('still I do like this movie for its empowerment of women; theres not enough movies out there like this one.  ', 'positive'),
('An excellent performance from Ms.  ', 'positive'),
('Garbo who showed right off the bat that her talents could carry over from the silent era (I wanted to see some of her silent work but Netflix does not seem to be stocking them.  ', 'positive'),
('Its also great to see that renowned silent screenwriter Frances Marion has not missed a step going from silent to sound.  ', 'positive'),
('You will love it!  ', 'positive'),
('The movie I received was a great quality film for its age.  ', 'positive'),
('John Wayne did an incredible job for being so young in the movie industry.  ', 'positive'),
('His on screen presence shined thought even though there were other senior actors on the screen with him.  ', 'positive'),
('I think that it is a must see older John Wayne film.  ', 'positive'),
('Jamie Foxx absolutely IS Ray Charles.  ', 'positive'),
('His performance is simply genius.  ', 'positive'),
('He owns the film just as Spacek owned Coal Miners Daughter and Quaid owned Great Balls of Fire.  ', 'positive'),
('In fact its hard to remember that the part of Ray Charles is being acted and not played by the man himself.  ', 'positive'),
('Ray Charles is legendary.  ', 'positive'),
('Ray Charles life provided excellent biographical material for the film which goes well beyond being just another movie about a musician.  ', 'positive'),
('Hitchcock is a great director.  ', 'positive'),
('secondly Hitchcock pretty much perfected the thriller and chase movie.  ', 'positive'),
('When I first watched this movie in the 80s  I loved it.  ', 'positive'),
('I was totally fascinated by the music the dancing... everything.  ', 'positive'),
('If good intentions made a film great then this film might be one of the greatest films ever made.  ', 'positive'),
('The film has great actors a master director a significant theme--at least a would-be significant theme undertone of fifties existential world-weariness aerial scenes that ought to have thrilled both senses and imagination and characters about which one might deeply care.  ', 'positive'),
('Yet I enjoy watching it.  ', 'positive'),
('That was nice.  ', 'positive'),
('That was funny.  ', 'positive'),
('It was so funny.  ', 'positive'),
 ('The cinematography is simply stunning (to say the least) and the fx are nothing if not state-of-the-art.  ', 'positive'),
('Conceptually the show offers a little bit of everything- and for just about everybody (parents kids fantasy and/or fx fans).  ', 'positive'),
('And there was not a single sour note struck acting-wise either; some surprisingly solid casting here.  ', 'positive'),
('All things considered a job very well done.  ', 'positive'),
('Thanks good a movie like this was done and released.  ', 'positive'),
('One of the best mexican movies ever! and one of the less understood even by mexican themselves no matter how identified the should have felt with it.  ', 'positive'),
('It ranks highly as a great noir-crime-drama incredible performances by Belmondo and Lino Ventura.  ', 'positive'),
('The attention given to every character and complex psychological portrayals detailing loyalty treachery love and hope are tremendous.  ', 'positive'),
('It is an excellent drama an excellent thriller and an excellent film.  ', 'positive'),
('Up there with the best of Melville.  ', 'positive'),
('Everything about this film is simply incredible.  ', 'positive'),
('You truly take this journey through the eyes and soul of a child.  ', 'positive'),
('BLACK WATER is a thriller that manages to completely transcend its limitations (its an indie flick) by continually subverting expectations to emerge as an intense experience.  ', 'positive'),
('The performances are real and gripping the crocdodile is extremely well done indeed if the Black Water website is to be believed thats because they used real crocs and the swamp location is fabulous.  ', 'positive'),
('I thoroughly enjoyed it when Christopher Eccleston took control of the TARDIS and the continuation of the series.  ', 'positive'),
('There is a lot of beautiful places.  ', 'positive'),
('An AMAZING finale to possibly the BEST trilogy of all time!  ', 'positive'),
('Kieslowski never ceases to amaze me.  ', 'positive'),
('He is one of my favourite directors and one of the most talented directors in the history of cinema.  ', 'positive'),
('His use of the colours of the French flag in the three films was nothing short of incredible every shot every scene was like a work of art.  ', 'positive'),
('Three of the most visually appealing movies i have ever seen.  ', 'positive'),
('And his subtle connections between the three films are awesome.  ', 'positive'),
('I have to mention this and it is a huge SPOILER i loved the ending how all the characters of the three films were the remaining survivors of the ferry disaster with Valentine and the young judge together and the old man watching it on her TV solidifying his happiness over the suffering which he dealt with for those many years.  ', 'positive'),
('I could not think of a better way to end the film but a smile on my face great way to wrap up an amazing film and trilogy!  ', 'positive'),
('I recommend this for EVERYONE who loves film movies anything...A Work of Art!  ', 'positive'),
('10 out of 10 for both the movie and trilogy.  ', 'positive'),
('I think i was one of the people who found this another one of roths pearls.  ', 'positive'),
('his performance as awarded was stunning.  ', 'positive'),
('the story which was told so eloquently by Francis ford Coppola 25 years earlier really unfolds gradually and leaves room for the characters to develop.  ', 'positive'),
('In a most wonderful location lies a story of contrast.  ', 'positive'),
('All in all a beautiful directed film from Nicolas roeg wih a sublime cast.  ', 'positive'),
('This is such a fun and funny movie.  ', 'positive'),
('Highly entertaining at all angles.  ', 'positive'),
('It features an outlandish array of memorable psychotic but lovable nuts.  ', 'positive'),
                      ('This movie is well-balanced with comedy and drama and I thoroughly enjoyed myself.  ', 'positive'),
('It was a riot to see Hugo Weaving play a sex-obsessed gay real estate salesman who uses his clients houses for his trysts with the flaming Darren (Tom Hollander).  ', 'positive'),
('Anyway, the plot flowed smoothly and the male-bonding scenes were a hoot.  ', 'positive'),
('The opening sequence of this gem is a classic, and the cat n mouse games that follow are a delight to watch.  ', 'positive'),
('Fans of the genre will be in heaven.  ', 'positive'),
('Lange had become a great actress.  ', 'positive'),
('It looked like a wonderful story.  ', 'positive'),
('The best scene in the movie was when Gerardo is trying to find a song that keeps running through his head.  ', 'positive'),
('saw the movie today and thought it was a good effort good messages for kids. ', 'positive'),
('Loved the casting of Jimmy Buffet as the science teacher.  ', 'positive'),
('And those baby owls were adorable.  ', 'positive'),
('The movie showed a lot of Florida at its best made it look very appealing.  ', 'positive'),
('The Songs Were The Best And The Muppets Were So Hilarious.  ', 'positive'),
('It Was So Cool.  ', 'positive'),
('This is a very right on case movie that delivers everything almost right in your face.  ', 'positive'),
('This review is long overdue since I consider A Tale of Two Sisters to be the single greatest film ever made.  ', 'positive'),
('I will put this gem up against any movie in terms of screenplay cinematography acting post-production editing directing or any other aspect of film-making.  ', 'positive'),
('Its practically perfect in all of them  a true masterpiece in a sea of faux masterpieces.  ', 'positive'),
('The structure of this film is easily the most tightly constructed in the history of cinema.  ', 'positive'),
('I can think of no other film where something vitally important occurs every other minute.  ', 'positive'),
('In other words the content level of this film is enough to easily fill a dozen other films.  ', 'positive'),
('How can anyone in their right mind ask for anything more from a movie than this?  ', 'positive'),
('Its quite simply the highest most superlative form of cinema imaginable.  ', 'positive'),
('Yes this film does require a rather significant amount of puzzle-solving but the pieces fit together to create a beautiful picture.  ', 'positive'),
('This is the number one best TH game in the series.  ', 'positive'),
('It deserves strong love.  ', 'positive'),
('It is an insane game.  ', 'positive'),
('There are massive levels massive unlockable characters... its just a massive game.  ', 'positive'),
('Waste your money on this game.  ', 'positive'),
('This is the kind of money that is wasted properly.  ', 'positive'),
('Actually the graphics were good at the time.  ', 'positive'),
('As they say in Canada This is the fun game aye.  ', 'positive'),
('This game rocks.  ', 'positive'),
('Buy it play it enjoy it love it.  ', 'positive'),
('Its PURE BRILLIANCE.  ', 'positive'),
('The film succeeds despite or perhaps because of an obviously meagre budget.  ', 'positive'),
('I am glad the film did not go for the most obvious choice as a lesser film certainly would have.  ', 'positive'),
('In addition to having one of the most lovely songs ever written French Cancan also boasts one of the cutest leading ladies ever to grace the screen.  ', 'positive'),
('Its hard not to fall head-over-heels in love with that girl.  ', 'positive'),
('Excellent cast story line performances.  ', 'positive'),
                      ('Totally believable.  ', 'positive'),
('Anne Heche was utterly convincing.  ', 'positive'),
('sam Shepards portrayal of a gung ho Marine was sobering.  ', 'positive'),
('I sat riveted to the TV screen.  ', 'positive'),
('All in all I give this one a resounding 9 out of 10.  ', 'positive'),
('I do think Tom Hanks is a good actor.  ', 'positive'),
('I enjoyed reading this book to my children when they were little.  ', 'positive'),
('There are some generally great things in it.  ', 'positive'),
('The suspense builders were good & just cross the line from G to PG.  ', 'positive'),
('I especially liked the non-cliche choices with the parents; in other movies I could predict the dialog verbatim but the writing in this movie made better selections.  ', 'positive'),
('If you want a movie thats not gross but gives you some chills this is a great choice.  ', 'positive'),
('Alexander Nevsky is a great film.  ', 'positive'),
('He is an amazing film artist one of the most important whoever lived.  ', 'positive'),
('This if the first movie I have given a 10 to in years.  ', 'positive'),
('If there was ever a movie that needed word-of-mouth to promote this is it.  ', 'positive'),
('Overall the film is interesting and thought-provoking.  ', 'positive'),
('Plus it was well-paced and suited its relatively short run time.  ', 'positive'),
('Give this one a look.  ', 'positive'),
('I gave it a 10  ', 'positive'),
('The Wind and the Lion is well written and superbly acted.  ', 'positive'),
('It is a true classic.  ', 'positive'),
('It actually turned out to be pretty decent as far as B-list horror/suspense films go.  ', 'positive'),
('Definitely worth checking out.  ', 'positive')





                        

                  ]


        neg_tweets = [('I do not like this car', 'negative'),

                  ('This view is horrible', 'negative'),

                  ('I feel tired this morning', 'negative'),

                  ('I am not looking forward to the concert', 'negative'),

                  ('He is my enemy', 'negative'),
                   ('About ten minutes into this film I started having second thoughts', 'negative'),
    ('About half way through this film I started to dislike it', 'negative'),
    ('By the time the film ended, I not only disliked it, I despised it.', 'negative'),
    ('What this film lacks is a convincing script', 'negative'),
    ('The script looks as if only a rough draft was written and shooting began before a finished script was completed', 'negative'),
    ('Things happen, characters personalities change, plot twists occur for no real reason other than that script calls for it', 'negative'),
    ('This is probably the most irritating show I have ever seen in my entire life.', 'negative'),
    ('It is indescribably the most annoying and idiotic show I have ever seen', 'negative'),
    ('Everything about it is just bad', 'negative'),
    ('I could not understand, what kind of idiot would produce this mess in the first place not to mention several season', 'negative'),
    ('The script is bad, very bad  it contains both cheesiness and unethical joke that you normally see in rated R or NC-positive7 movie', 'negative'),
    ('The casting is also horrible, cause all you see is a really really BAD Actors, period', 'negative'),
    ('Final Word: This Show is a real torture!!  ', 'negative'),
    ('It is zillion times away from reality', 'negative'),
    ('Watching washing machine twirling around would not hurt your eyes as much as this show', 'negative'),
    ('Rating: 0/10 (Grade: Z) Note: The Show Is So Bad That Even Mother Of The Cast Pull Her Daughter Out Of The Show', 'negative'),
    ('20th Century Foxs ROAD HOUSE 1948) is not only quite a silly noir but is an implausible unmitigated bore of a movie', 'negative'),
    ('Full of unconvincing cardboard characters it is blandly written by Edward Chodorov, who also produced, and is surprisingly directed by Jean Negulesco from whom one would expect a great deal more', 'negative'),
    ('From here on the Widmark character turns unintentionally comical!  ', 'negative'),
    ('His losing his marbles so early in the proceedings is totally implausible and unconvincing', 'negative'),
    ('And if that is not enough of a mess of a movie for you - the picture is also marred with a constant use of studio sets and indoor exteriors', 'negative'),
    ('Whatever prompted such a documentary is beyond me!  ', 'negative'),
     (') Do not waste your time', 'negative'),
    ('End of Days is one of the worst big-budget action movies I have ever seen', 'negative'),
    ('He surely does not know how to make a coherent action movie from the screenwriter of Air Force One who was only obliged to write the script just for a big sum of money', 'negative'),
    ('This was one of the worst films i have ever seen', 'negative'),
    ('I am still trying to get over how bad it was', 'negative'),
                  ('positive hour 54 minutes of sheer tedium, melodrama and horrible acting, a mess of a script, and a sinking feeling of GOOD LORD, WHAT WERE THEY THINKING?  ', 'negative'),
    ('Lots of holes in the script', 'negative'),
    ('It is like a bad two hour TV movie', 'negative'),
    ('Now imagine that every single one of those decisions was made wrong', 'negative'),
    ('The dialogue is atrocious', 'negative'),
    ('The acting is beyond abysmal', 'negative'),
    ('Everything stinks', 'negative'),
    ('Trouble is, the writing and directing make it impossible to establish those things that make a movie watchable, like character, story, theme and so on', 'negative'),
    ('Worse, there is an incredibly weak sub-plot thrown in that follows a little band of latter-day Mansonites as they go after a reporter who working on a story on the anniversary of the killings', 'negative'),
    ('It is dumb and pointless, and a complete waste of time', 'negative'),
    ('In short, do not bother with this movie', 'negative'),
    ('Either way, it sucks', 'negative'),
    ('The script is horrendously stupid', 'negative'),
    ('The story starts too fast with absolutely no suspense or build-up in the slightest', 'negative'),
    ('Everything Captain Howdy says is either laughable or just plain stupid', 'negative'),
    ('What the hell kind of crap is that?!  ', 'negative'),
    ('Then, there is the plot holes', 'negative'),
    ('You could drive a semi truck into these holes!  ', 'negative'),
                      ('It was so BORING!  ', 'negative'),	
('No plot whatsoever!  ', 'negative'),	
('Again no plot at all', 'negative'),	
('Horrible!  ', 'negative'),	
('Worst hour and a half of my life!Oh my gosh!  ', 'negative'),	
('I had to walk out of the theatre for a few minutes just to get some relief!  ', 'negative'),	
('I hate movies like that', 'negative'),	
('Yeah the movie pretty much sucked', 'negative'),	
('THERE IS NO PLOT OR STORYLINE!!  ', 'negative'),	
('If you do go see this movie bring a pillow or a girlfriend/boyfriend to keep you occupied through out', 'negative'),	
('Awful', 'negative'),	
('I do not think I have ever gone to a movie and disliked it as much', 'negative'),	
('It was a good thing that the tickets only cost five dollars because I would be mad if I would have paid $7.50 to see this crap', 'negative'),	
('NOBODY identifies with these characters because they are all cardboard cutouts and stereotypes (or predictably reverse-stereotypes)', 'negative'),	
('This is a bad film with bad writing and good actors....an ugly cartoon crafted by Paul Haggis for people who can not handle anything but the bold strokes in storytelling....a picture painted with crayons', 'negative'),	
('Crash is a depressing little nothing that provokes emotion but teaches you nothing if you already know racism and prejudice are bad things', 'negative'),	
('Your brain will attempt to shut-down as part of a primal impulse of self-preservation', 'negative'),	
('I was left shattered from the experience of watching this film and I took a good two hours to fully recover', 'negative'),	
('This movie now joins Revenge of the Boogeyman and Zombiez as part of the hellish trinity of horror films', 'negative'),	
('I certainly do not mean this distinction in a good way', 'negative'),	
('I mean this in a terrible way', 'negative'),	
('This film has no redeeming features', 'negative'),	
('Everything is appalling', 'negative'),	
('Artless camera-work endlessly presents us with the ugliest setting imaginable i.e', 'negative'),	
('The story is beyond stupid', 'negative'),	
('The script iswas there a script?  ', 'negative'),	
('The kids are annoying', 'negative'),	
('The lead man is charisma-free', 'negative'),	
('Utterly without merit on any level this is akin to torture', 'negative'),	
('I will even say it again  this is torture', 'negative'),	
('Maybe there would be a reasonable explanation for this atrocity', 'negative'),	
('Not a pleasant voyage of self-discovery', 'negative'),	
('Highly unrecommended', 'negative'),	
('If this premise sound stupid that is because it is', 'negative'),	
('Yes it is that bad', 'negative'),	
('Nothing at all to recommend', 'negative'),
                      ('Is it possible for a movie to get any worse than this?  ', 'negative'),
('there is no plot here to keep you going in the first place.', 'negative'),
('Even when the women finally show up, there is no sign of improvement; the most expected things happen and by the time the film is over, you might be far asleep.', 'negative'),
('Beware: this is not a trashy cult movie, this is trash -period!  ', 'negative'),
('I cant believe theres even a sequel to this!  ', 'negative'),
('Which is precisely why I am giving it such a bad review!  ', 'negative'),
('Every element of this story was so over the top, excessively phony and contrived that it was painful to sit through.', 'negative'),
('Her lines seem to have been WRITTEN by a fifteen year old, though they are trying oh so, so hard to sound like how a fifteen year old would really, um, you know, well... talk.', 'negative'),
('there is simply no excuse for something this poorly done.', 'negative'),
('I saw this movie and I thought this is a stupid movie.', 'negative'),
('What is even more stupid is that who had thought an idea that there should be a volcano in Los Angeles?  ', 'negative'),
('to be honest with you, this is unbelievable nonsense and very foolish.', 'negative'),
('In conclusion, I will not bother with this movie because a volcano in Los Angeles is nothing but nonsense.', 'negative'),
('the story line is just awful!  ', 'negative'),
('Its just painful!  ', 'negative'),
('And the accents are absolutely abysmal!  ', 'negative'),
('theres also enough hypocrisy in this film to make me vomit.', 'negative'),
('Dont waste your time watching this rubbish non-researched film.', 'negative'),
('Omit watching this.', 'negative'),
('amy rating: just 3 out of 10.', 'negative'),
('the basic premise is wasted since it is sidelined by the inexplicable focus on the documentary crew.', 'negative'),
('Regardless, the film fails on most levels.', 'negative'),
('Avoid at all costs.', 'negative'),
('I know that Jim OConnor was very energetic and that nobody could be as much as him, but George was well dull.', 'negative'),
('He really didnt seem to want to be hosting; his voice-overs were monotonous, didnt get involved with the guests.', 'negative'),
('this movie is so mind-bendingly awful, it couldnt have even been created.', 'negative'),
('the film lacks any real scares or tension & some of the medical terminology used throughout is a bit iffy to say the least & I say that as an insulin dependant diabetic myself.', 'negative'),
('the least said about the acting the better.', 'negative'),
('Even allowing for poor production values for the time (positive97positive and the format (some kind of mini-series), this is baaaaaad.', 'negative'),
('Unless you are just out to visually "collect" all extant films of Austens work, you can skip this one.', 'negative'),
('It is not good.', 'negative'),
('speaking of the music, it is unbearably predictably and kitchy.', 'negative'),
('then the film just dropped the ball.', 'negative'),
('there are many continuity errors: one other user commented on different cars in the garage, Joes glasses...the one that got to me the most was the fact Joes facial hair configuration seemed to change from scene to scene.', 'negative'),
('I cant see how this movie can be an inspiration to anyone to come out or overcome fear and rejection.', 'negative'),
('Its so bad its actually worth seeing just for that reason.', 'negative'),
('Well... Just if you keep thinking how bad it is.', 'negative'),
('Its a mediocre, miserable, hollow, laughable and predictable piece of garbage.', 'negative'),
('Its a case of so bad it is laughable.', 'negative'),
('very bad performance plays Angela Bennett, a computer expert who is at home all the time.', 'negative'),
('It is a film about nothing, just a pretext to show ridiculous action scenes.', 'negative'),
('How awful she is!  ', 'negative'),
('But she is still a bad actress, repeating her robotic face moves in each of her pictures.', 'negative'),
('the results, well, are a shame.', 'negative'),
('DELETE this film from your mind!  ', 'negative'),
('One of the worst shows of all time.', 'negative'),
('the show would begin with smart ass ed comments to each other that would be totally off the wall and uncalled for.', 'negative'),
('the fat computer geek was unbelievable, the bible thumper, the bad-ass girl, who are these actors???  ', 'negative'),
('Never heard of any of them except Cole who was totally unbelievable in the part.', 'negative'),
('Every time he opened his mouth you expect to hear, "you see kids..." Pulling the plug was a mercy killing for this horrible show.', 'negative'),
('the stories were as unbelievable as the actors.', 'negative'),
('Lame would be the best way to describe it.', 'negative'),
('Im big fan of RPG games too, but this movie, its a disgrace to any self-respecting RPGer there is.', 'negative'),
('the lines, the cuts, the audio, everything is wrong.', 'negative'),
('You can find better movies at youtube.', 'negative'),
('top line: Dont waste your time and money on this one, its as bad as it comes.', 'negative'),
('A Lassie movie which should have been "put to sleep".... FOREVER.', 'negative'),
('thats how I would describe this painfully dreary time-waster of a film.', 'negative'),
('so mediocre in every aspect that it just becomes a dull, uninteresting mess, this is one of the most forgettable movies I have seen.', 'negative'),
('It isnt even an achievement as a "so-bad-its-good" or "so-bad-its-memorable" movie.', 'negative'),
('Its an empty, hollow shell of a movie.', 'negative'),
('seriously, its not worth wasting your, or your kids time on.', 'negative'),
('Avoid, avoid, avoid!  ', 'negative'),
('It will drive you barking mad!  ', 'negative'),
('Nothing new there.', 'negative'),
('that was done in the second movie.', 'negative'),
('the movie has almost no action scenes in it and very little comedy.', 'negative'),
('the plot has more holes than a pair of fishnet stockings and the direction and editing is astonishingly ham fisted.', 'negative'),
('What on earth is Irons doing in this film?  ', 'negative'),
('the football scenes at the end were perplexing.', 'negative'),
('this scene is very strong and unpleasant.', 'negative'),
('And it was boring.', 'negative'),
('I am so tired of clichés that is just lazy writing, and here they come in thick and fast.', 'negative'),
('Why was this film made?  ', 'negative'),
('the film has an ultra-cheap look to it.', 'negative'),
('the result is a film that just dont look right.', 'negative'),
('None of them are engaging or exciting.', 'negative'),
('the plot is nonsense that doesnt interest in the slightest way or have any uniqueness to it.', 'negative'),
('the Foreigner is not worth one second of your time.', 'negative'),
('How this piece of trash was ever released is beyond me: the acting, the story, the characters, the supposedly special effects, etc...its ALL wrong.', 'negative'),
('In fact, this stinker smells like a direct-to-video release.', 'negative'),
('Avoid at ALL costs!  ', 'negative'),
('star Trek V The final Frontier is the worst in the series.', 'negative'),
('the acting from all involved and that includes those like Shatner and Nimoy is bad and washed out and making them seem as old as they look in real life, the special effects are tacky like when Spock has to rescue Kirk on a jet pack when he falls down from a mountain.', 'negative'),
('the attempts at humor were pitiful and story is so awful it dosent bear thinking about which basically involves a Vulcan stealing the Enterprise to find god (seriously) I just didnt care about any of this film and oh not to mention Uhura does a belly dance to distract male guards.', 'negative'),
('the only place good for this film is in the garbage.', 'negative'),
('the worst one of the series.', 'negative'),
( 'havery disappointed and wondered how it could be in the Oscar shortlist.', 'negative'),
('Its very slow.', 'negative'),
('Lot of holes in the plot: theres nothing about how he became the emperor; nothing about where he spend 20 years between his childhood and mature age.', 'negative'),
(' Dont waste your time.', 'negative'),
('End of Days is one of the worst big-budget action movies I have ever seen.', 'negative'),
('He surely doesnt know how to make a coherent action movie from the screenwriter of Air Force One who was only obliged to write the script just for a big sum of money.', 'negative'),
('this was one of the worst films i have ever seen.', 'negative'),
('I am still trying to get over how bad it was.', 'negative'),
('positive hour 54 minutes of sheer tedium, melodrama and horrible acting, a mess of a script, and a sinking feeling of GOOD LORD, WHAT WERE THEY THINKING?  ', 'negative'),
('Lots of holes in the script.', 'negative'),
('Its like a bad two hour TV movie.', 'negative'),
('Now imagine that every single one of those decisions was made wrong.', 'negative'),
('the dialogue is atrocious.', 'negative'),
('the acting is beyond abysmal.', 'negative'),
('Everything stinks.', 'negative'),
('trouble is, the writing and directing make it impossible to establish those things that make a movie watchable, like character, story, theme and so on.', 'negative'),
('Worse, theres an incredibly weak sub-plot thrown in that follows a little band of latter-day Mansonites as they go after a reporter whos working on a story on the anniversary of the killings.', 'negative'),
('Its dumb and pointless, and a complete waste of time.', 'negative'),
('In short, dont bother with this movie.', 'negative'),
('Also the story and acting were weak.', 'negative'),
('At around 4 pm I bought it, at around 8pm I started to watch, at around 8.positive5pm I fast forwarded the remaining film to see if there was anything left watchable for a human being with a brain... but there wasnt.', 'negative'),
('Either way, it sucks.', 'negative'),
('the script is horrendously stupid.', 'negative'),
('the story starts too fast with absolutely no suspense or build-up in the slightest.', 'negative'),
('Everything Captain Howdy says is either laughable or just plain stupid.', 'negative'),
('What the hell kind of crap is that?!  ', 'negative'),
('then, theres the plot holes.', 'negative'),
('You could drive a semi truck into these holes!  ', 'negative'),
('Dee Snider just plain sucks.', 'negative'),
('He cant act (one of the least scary villains I have ever seen), he cant write (did he write this damn movie in his sleep?  ', 'negative'),
('I was bored throughout the whole damn thing.', 'negative'),
('the acting sucks, the music sucks, the script sucks, the pacing sucks, the special FX suck, the directing sucks... basically, this movie sucks.', 'negative'),
('this film tries to be a serious and sophisticated thriller/horror flick and it fails miserably.', 'negative'),
('this is probably one of the least effective and utterly unoriginal films I have ever seen in my entire life.', 'negative'),
('A piece of cinematic garbage captured on celluloid.', 'negative'),
('Avoid at any and all costs.', 'negative'),
('At any rate this film stinks, its not funny, and Fulci should have stayed with giallo and supernatural zombie movies.', 'negative'),
('Avoid this film at all costs.', 'negative'),
('I dont know what happened in Season Five, what a mess.', 'negative'),
('the only consistent thread holding the series together were the amazing performances of Leni Parker and Anita LaSelva as the two Taelons in quiet idealogical conflict.', 'negative'),
('Now this is a movie I really dislike.', 'negative'),
('Its one of the most boring Horror movies from the 90s mainly because it starts slow and centers in a boring atmosphere.', 'negative'),
('the puppets look really cheesy , not in a good way like in the Puppet Master 80s flicks.', 'negative'),
('the story is lame, not interesting and NEVER really explains the sinister origins of the puppets.', 'negative'),
('there arent death scenes like in previous movies and the f/x are terrible.', 'negative'),
('I felt asleep the first time I watched it, so I can recommend it for insomniacs.', 'negative'),
('Otherwise, dont even waste your time on this.', 'negative'),
('this one just fails to create any real suspense.', 'negative'),
('As for the killer, dont expect anything original or even remotely frightening.', 'negative'),
('I am so sorry but I really cant recommend it to anyone.', 'negative'),
('One of the most boring,pointless movies I have ever seen.', 'negative'),
('the secondary plot line is incomprehensible and its relation to the primary plot line is mystifying.', 'negative'),
('Hated it.', 'negative'),
('this is one of the worst Sandra Bullock movie since Speed 2 But not quite that bad.', 'negative'),
('I dont understand how this garbage got on the shelves of the movie store, its not even a real movie!  ', 'negative'),
('I highly doubt that anyone could ever like this trash.', 'negative'),
('this is not movie-making.', 'negative')





                  ]

        


        tweets = []

        for (words, sentiment) in pos_tweets + neg_tweets:

            words_filtered = [e.lower() for e in words.split() if len(e) >= 3]

            tweets.append((words_filtered, sentiment))

        
        #print('\n'+ 'Printing Tweets')
        #print(tweets)

        def get_words_in_tweets(tweets):

            all_words = []

            for (words, sentiment) in tweets:

                  all_words.extend(words)
            
            return all_words

        def get_word_features(wordlist):

            wordlist = nltk.FreqDist(wordlist)

            word_features = wordlist.keys()

            return word_features

        word_features = get_word_features(get_words_in_tweets(tweets))

        #print('\n'+ 'Shows a list with every distinct word ordered by frequency of appearance')

        #print(word_features)
 

        def extract_features(document):

            document_words = set(document)

            features={}

            for word in word_features:

                features['contains(%s)' % word] = (word in document_words)

            return features

        document = ['I','love','chocolates']

        #print('\n'+ ' returns a dictionary indicating what words are contained in the input passed')

        #print(extract_features(document))

        training_set = nltk.classify.apply_features(extract_features, tweets)

        #print('\n'+ 'Displays the training set used ')

        #print(training_set)

        classifier = nltk.NaiveBayesClassifier.train(training_set)

        #Reading tweets from afile

        if (self.fpath!=''):
            f= open(self.fpath,'r')

            pcount=0

            ncount=0
            #test=f.readlines()

            for line in f.readlines():
                tweet= line

                print('\n'+ 'The tweet- '+ tweet +' is classified as: \n')

                if((classifier.classify(extract_features(tweet.split())))=='positive'):

                    print("positive")

                    pcount+=1

                elif((classifier.classify(extract_features(tweet.split())))=='negative'):

                    print("negative")

                    ncount+=1

            f.close();

            print("\nPositive tweets are:"+ str(pcount))

            print("\n Negative tweets are:"+ str(ncount))
            #print("Classifier accuracy percent= ", (nltk.classify.accuracy.(classifier,)))
            #Plotting the bar graphs for the results 

            y=[pcount,ncount]

            N=len(y)

            x=range(N)

            width=1/2
            fig,a=plt.subplots()
            a.bar(x, y,width,color="green")
            #plt.text(0, 10,'positive tweets=',pcount,'negative tweets=',ncount)
            n=np.arange(N)
            a.set_xticks(n)
            a.set_xticklabels(('Positive=%d'%pcount,'Negative=%d'%ncount))
            plt.title('Classification of tweets')
            plt.xlabel('Classification')
            plt.ylabel('Number of tweets')
            
            plt.show()
            
        else:
            self.err_label.config(text='Choose a file first!')


        #File analysis code ends here 
 
if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()
