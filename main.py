'''
Ben Lepsch aka Dovahkiin
DovaBot

Bot for the Scandals Family Discord server
'''

import discord, asyncio, random, time

gaz_coins = {"<@!262637906865291264>" : 11, "<@!178876334095859712>" : 7, "<@!201509495220731906>" : 6,  # Dovahkiin, JSD, NeatoBurrito
             "<@!158033864562835456>" : 14, "<@!389919287785160714>" : 6, "<@!187697102615216128>" : 7,   # Mege, Gazorpazorp, Astrae
             "<@303235342935523330>" : 1, "<@180875776671875072>" : 8, "<@108833905552977920>" : 12,     # Bizna, Fone, Gen_1
             "<@251806188243648512>" : 3, "<@!210984200235515907>" : 1, "<@209575733989736448>" : 4,     # Zenattra, PandaBearKev, Kevadrenaline
             "<@!252315498551836673>" : 11, "<@!348278804973748238>" : 2, "<@384489637193973767>" : 1,   # WhaleScience, SantaClaws, Corpsetaker
             "<@385092345814581260>" : 7, "<@420346616977817602>" : 2, "<@175784984655822848>" : 7,      # SlayinSteven, DevilOW, Matthzw
             "<@!257037119153897472>" : 16}                                                              # Liberosi/Aku

bossRaces = ['Orcish', 'Elvish']
bossTypes = ['Mage', 'Knight', 'Archer']

def import_values(file):                                # Import gaz coin values from a .txt file
    data = []
    ids = []
    coins = []
    with open(file, "r") as leveldata:
        data = leveldata.read().split(' ')
    #print(data)
    for i in range(len(data)):
        data[i] = data[i].split(':')
        #print(data[i])

    for i in data:
        ids.append(i[0])
        coins.append(int(i[1]))

    #print(ids)
    #print(coins)
    
    for i in gaz_coins:
        for x in range(len(ids) - 1):
            if ids[x] == i:
                gaz_coins[i] = coins[x]
                break
    
        

def export_values(file):                                # Export the values (called whenever gaz coins increase or decrease)
    print_str = ''
    for i in gaz_coins:
        print_str += i
        print_str += ':'
        print_str += str(gaz_coins[i])
        if not i == "<@!257037119153897472>":
            print_str += ' '
    with open(file, "w") as leveldata:
        leveldata.write(print_str)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        game = discord.Game("!dovabotcommands")
        await client.change_presence(status=discord.Status.idle, activity=game)
        import_values("data/leveldata.txt")
        
    
    async def on_message(self, message):
        # we do not want the bot to reply to itself (actually commenting that out rn)
        if message.author.id == self.user.id:
            if not message.content.startswith('!doot'):
                return


        # test commands go here

        if message.content.startswith('!testcommand'):                                      # !testcommand
            await message.channel.send("it works")
            await message.channel.send("yes")

        # end test commands

        if message.content.startswith('!givecoins'):
            if message.author.id == 262637906865291264:
                command = message.content.split()
                if len(command) > 1:  # command is like !givecoins @gaz 10
                    #print(command)
                    #command.pop(0)
                    #print('pop ')
                    #print(command)
                    if command[0] in gaz_coins:
                        gaz_coins[command[0]] += int(command[1])
                        await message.channel.send(command[0] + ' now has ' + str(gaz_coins[command[0]]) + ' gaz coins!')
                    else:
                        await message.channel.send('That person doesn\'t have a gaz coin amount.')
                else:
                    await message.channel.send('Wrong syntax')
            else:
                await message.channel.send('You can\'t use this command!')

        #if message.content.startswith('!join') or message.content.startswith('!play'):
        #   await message.channel.send('No.')

        if message.content.startswith('!dungeonBoss'):                                      # !dungeonBoss
            bossHP = 0
            bossDmg = 0
            roll = 0
            bossType = ''
            bossRace = ''
            if len(message.content.split()) == 1:
                roll = random.randint(0,1)
                bossRace = bossRaces[roll]    #Determine Race and Type
                roll = random.randint(0,2)
                bossType = bossTypes[roll]
                bossHP = random.randint(5,20)
                output = "You have summoned an " + bossRace + " " + bossType + " with HP of " + str(bossHP) + "."
                bossAlive = True
                await message.channel.send(output)
            else:
                user = message.content.split()
                if len(user) > 1:
                    user.pop(0)
                    if user[0] == '!roll':
                        dmg = random.randint(0,20)
                        await message.channel.send("You *tried* to deal " + str(dmg) + " damage, but they dodged and hit you with " + str(random.randint(1238475,123515627)) + " damage and you died.")
                    else:
                        await message.channel.send("Please enter a valid command.")
                else:
                    await message.channel.send("Since there is already a boss spawned, you need to enter a secondary command.")

        
        if message.content.startswith('!hello'):
            await message.channel.send('Is it me you\'re looking for?')                  # !hello

                                                                                     #  ''' SENDING PICTURES '''
        if message.content.startswith('!doot'):                                         # !doot
            file = discord.File("data/doot.jpg",filename="doot.jpg")
            await message.channel.send('Doot Doot', file=file)
        if message.content.startswith('!canada'):                                       # !canada
            file = discord.File("data/canada.jpg",filename="canada.jpg")
            await message.channel.send('',file=file)

        if message.content.startswith('Ding! GG') and message.author.id == 159985870458322944:      # automatically update gaz coin count
            command = message.content.split()
            print_string = "Level up! "
            file = discord.File("data/levelupimg.png",filename="levelupimg.png")

            name = command[2] # command is : Ding! GG @<name>
            arr = []
            for char in name:
                arr += char

            final_name_1 = ''
            final_name_2 = ''
            
            arr.pop(len(arr) - 1)
            for i in arr:
                final_name_1 += i
                final_name_2 += i
             
            final_name_1 += '>'
            print(final_name_1)
            
            if final_name_1 in gaz_coins:
                gaz_coins[final_name_1] += 1
                print_string += final_name_1 + " now has " + str(gaz_coins[final_name_1]) + " gaz coins!"
            export_values("data/leveldata.txt")
            await message.channel.send(print_string, file=file)

        if message.content.startswith('!gazcoins'):                                                 # !gazcoins
            command = message.content.split()
            if len(command) > 1:
                if command[1] in gaz_coins:
                    await message.channel.send(command[1] + " has " + str(gaz_coins[command[1]]) + " gaz coins!")
            else:
                sender = "<@" + str(message.author.id) + ">"
                sender2 = "<@!" + str(message.author.id) + ">"
                if sender in gaz_coins:
                    await message.channel.send(sender + " has " + str(gaz_coins[sender]) + " gaz coins!")
                if sender2 in gaz_coins:
                    await message.channel.send(sender2 + " has " + str(gaz_coins[sender2]) + " gaz coins!")
                    
        if message.content.startswith('!gazmsg'):                                                   # !gazmsg
            command = message.content.split()
            command.pop(0)

            msg = ''

            for i in command:
                msg += i
                msg += ' '

            username1 = '<@' + str(message.author.id) + '>'
            username2 = '<@!' + str(message.author.id) + '>'

            if username1 in gaz_coins:
                gaz_coins[username1] -= 1
                export_values("data/leveldata.txt")
                await message.channel.send(username1 + " now has " + str(gaz_coins[username1]) + " gaz coins. \n<@389919287785160714> " + msg)
            elif username2 in gaz_coins:
                gaz_coins[username2] -= 1
                export_values("data/leveldata.txt")
                await message.channel.send(username2 + " now has " + str(gaz_coins[username2]) + " gaz coins. \n<@389919287785160714> " + msg)

        if message.content.startswith('!gazsongreq'):                                               # !gazsongreq
            command = message.content.split()
            msg = ''

            user1 = '<@!' + str(message.author.id) + '>'
            user2 = '<@' + str(message.author.id) + '>'
            
            if len(command) > 1:
                command.pop(0)

                if user1 in gaz_coins:
                    gaz_coins[user1] -= 1
                    for i in command:
                        msg += i
                        msg += ' '
                    export_values("data/leveldata.txt")
                    await message.channel.send(user1 + " now has " + str(gaz_coins[user1]) + " gaz coins. \n<@389919287785160714> play " + msg)
                if user2 in gaz_coins:
                    gaz_coins[user2] -= 1
                    for i in command:
                        msg += i
                        msg += ' '
                    export_values("data/leveldata.txt")
                    await message.channel.send(user1 + " now has " + str(gaz_coins[user1]) + " gaz coins. \n<@389919287785160714> play " + msg)
                
            else:
                await message.channel.send("Please enter a song title also (e.g. !gazsongreq Elektronik Supersonik) ")
                
        if message.content.startswith('!spam'):                                                     # !spam
            command = message.content.split()
            command.pop(0)
            
            try:
                number = int(command[0])
            except:
                await message.channel.send('Please enter a number')
                number = 0
            command.pop(0)
            
            print_string = ''
            for i in command:
                print_string += i
                print_string += ' '

            for i in range(number):
                await message.channel.send(print_string)
                                                                                                    # EMOJIS
        if message.content.startswith('!badping'):                                                  # !badping
            await message.channel.send('<:Pingsock:485258651708424194>')

        if message.content.startswith('!applause'):                                                 # !applause
            await message.channel.send('\U0001F44F' * 50)

        if message.content.startswith('!diagnoseme'):                                               # !diagnoseme
            responses = ['you have HIV.','you have coronary artery disease.','you are having a stroke.','you have lung cancer.','you have type 1 diabetes.','you have Alzheimer\'s disease.','you have tuberculosis.','you have melanoma.']
            number = random.randint(0,7)
            await message.channel.send('After researching your symptoms, I conclude that ' + responses[number])
            
        if message.content.startswith('!dovabotcommands'):                                          # !dovabotcommands
            await message.channel.send('''!hello : outputs "Hello <user>" \n!spam <number of times> <message> : spams the set message the number of times \n!badping : prints the pingsock emoji
!diagnoseme <symptoms> : Diagnoses your symptoms and outputs what disease you have \n!gazcoins <user(optional)> : outputs the number of gazcoins the user has. If there isn't a user entered, it gives the number you have
!applause : prints the clapping emoji 50 times \n!doot : says \'doot doot\' and prints a spooky skeleton image''')


client = MyClient()
