'''
@sumanbiswas
'''
class PlayGame:                                         # This is the main class and the code starting below.
    import gtts                                         # Genaral imports are here.
    from playsound import playsound
    score = 0                                           # The inicial score is here.
    total_score = 0                                     # This is for calculate total marks.
    def __init__(self):                                 # The class itself here to perform operations.
        print()                                         # Here it will start the intro.
        print("Welcome")
        PlayGame.playsound("creatorsuman.mp3")
        print()
        PlayGame.playsound("Name_please.mp3")
        self.player_name = input("Please Enter Your name  ")    # It will input the player name.
        print()
        self.Run()                                              # It will execute the main code.
        print()
        self.GameOver()                                         # Here it will start outro.
    def ContinueGame(self):                                                              # It will ask client if he or she wishes to continue the game.         
        PlayGame.playsound("type_y_to_continue.mp3")
        continuegame = input("Type Y to continue the game  ")
        if continuegame == "y" or continuegame == "Y" or continuegame == "":
            self.continue__game = True
        else:
            self.continue__game = False
    def RandomWord(self):                                                                # It will genarat random word to execute the game.
        import random
        words = ["word","book","teacher","seven","billion","million","first","elbow","back","vein","artery","limbs","foot","sole","stomach","grandma","friend","parent","master","sibling","enemy","cloth","pillow","jersey","belt","sunday","monday","tuesday","wednesday","thusday","june","march","morning","dawn","winter","autumn","buffalo","sheep","donkey","month","parrot","tiger","wolf","leopard","python","zebra","jackal","shark","whale","giraffe","gibbon","oyster","toad","crow","sparrow","kite","nightingale","hornbill","trunk","claw","hide","skeleton","hump","wing","twitter","mint","lemon","potato","purble","arum","sorrel","onion","garlic","wheat","flour","turmeric","mango","olive","plum","lichi","cocoanut","orange","walnut","seed","pulp","apple","lotus","lily","rose","petal","tulip","sugar","bread","rice","biscute","sour","jam","cake","tiffin","curry","youlk","dinner","pickle","omlette","arch","kitchen","room","ceiling","floor","shelf","step","pillar","cottage","audetorum","comb","napkin","soap","classroom","temple","trunk","bucket","spoon","pillow","lamp","loom","mattress","needle","university","admission","duster","chalk","book","key","drama","examiner","author","science","engineering","computer","programming","technology","mathematics","arthmetic","physics","chemistry","ethics","statics","dynamics","calf","puppy","wagon","bicycle","anchor","bridge","metal","iron","zinc","mercury","glass","flint","coal","postman","runner","mail","telegraph","valley","work","world","earth","planet","river","lake","rain","bank","oasis","flood","stream","current","mars","pluto","saturn","fever","cold","flute","poano","area","lenth","breadh","hight","weight","balance","south","zenith","colour","crimson","brown","pink","deep","light","grey","black","young","woman","long","dumb","deaf","silm","blind","fair","guest","baby","election","ceometry","subtruction","multiplication","division","product","ratio","square","number","statistics","parallel","angle","triangle","point","base","radius","cube","lenght","sound","dencity","speed","energy","element","electricity","power","work","locomotion","plasma","fossil","swimming","reading","racing","gaming","alarm","thermometer","environment","biogass","biomass","noise","birth","death","childhood","volcano","root","flower","home","creator"]
        words.sort()
        if self.continue__game == True:
            self.pick_random = random.choice(words) 
            self.mixed_pick = ",".join(random.sample(self.pick_random,len(self.pick_random))).upper() 
    def Ans(self):                                                                        # It will ask the answer from the client.
        PlayGame.playsound("guess_the_word.mp3")
        print(f"Guess what the word can be =>  {self.mixed_pick}")
        print()
        self.total_score += 1
        ans = input().lower()
        if ans == self.pick_random:
            print()
            self.score += 1
            PlayGame.playsound("wow!.mp3")
            print(f"Wow! {self.player_name}, you got a point. Now your score is {self.score}")
            print()
        else:
            self.score += 0
            PlayGame.playsound("opps!.mp3")
            print(f"Opps! {self.player_name}, you write the wrong answer. Now your score is {self.score}")
            print()
            sp = f"The correct answer was {self.pick_random}"
            self.gtts.gTTS(sp).save("correct_ans.mp3")
            PlayGame.playsound("correct_ans.mp3")
            print(sp)
            print()
        self.gtts.gTTS(f"Now your score is {self.score}")    
    def Run(self):                                                                           # It will execute the main programme.
        self.gtts.gTTS(f"Welcome ,{self.player_name} to this amazing word game").save("intro.mp3")
        PlayGame.playsound("intro.mp3")
        for i in range(5):    
            k = 0
            self.ContinueGame() 
            print()   
            if self.continue__game == False:
                return exit
            while(k < 3):
                self.RandomWord()
                self.Ans()
                k += 1
            self.continue__game = False
    def GameOver(self):                                                                        # It will perform the outro.
        print("Game is Over now")
        gameover = f"{self.player_name}, You have scored {self.score} out of {self.total_score}."
        self.gtts.gTTS(gameover).save("game_over.mp3")
        PlayGame.playsound("game_over.mp3")
        PlayGame.playsound("outro.mp3")
try:                                                                                            # It will handle the Error.
    PlayGame()
except Exception as e:
    from playsound import playsound
    playsound("internet_error.mp3")
    print("Error: ",e)
    print()
    print()


