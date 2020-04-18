import discord, threading
import requests, time 


client = discord.Client()

def flickerLights(n = 2,s = 3):
    offlink = "http://maker.ifttt.com/trigger/basementLightsOff/with/key/Bf91G_MsjKUzsWqRs5N7n"
    onlink = "http://maker.ifttt.com/trigger/basementLightsOn/with/key/Bf91G_MsjKUzsWqRs5N7n"
    print("Waking up " + str(n) + " times")
    for i in range(n):
        r = requests.get(offlink)
        time.sleep(s)
        r = requests.get(onlink)
        time.sleep(s)

@client.event
async def on_ready():   
    print('Logged in as')
    print(client.user.name)
    

@client.event
async def on_voice_state_update(member, before, after):
    userListF = open("userList.txt", "r")
    userList = userListF.read()
    userListF.close()

    disabF = open("disab.txt", "r")
    disab = disabF.read()
    disabF.close()

    afterS = str(after)
    if(afterS.find("VoiceChannel") > 0 and userList.find(str(member)) > -1 and disab.find(str(member)) < 0):

        i0 = afterS.find("VoiceChannel") + 16
        i1 = afterS.find(" ", i0)
        print(afterS[i0:i1])
        channel = client.get_channel(int(afterS[i0:i1]))
        vc = await channel.connect()
        #wont work in linux need to fix
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="audioFiles/" + str(member) + ".mp3"))
        while(vc.is_playing()):
            pass
        print("done")
        vc.pause()
        vc.resume()
        vc.stop()
        await vc.disconnect(force = True) 

@client.event        
async def on_message(message):
    global runA
    
    afterS = str(message)
    s = 'Message from {0.author}: {0.content}'.format(message)
    s0 = s.find("from") + 5
    s1 = s.find(":", s0)
    user = s[s0:s1]
    print(user)
    
    s2 = s.find("'", s1)
    mes = s[s1+2:]
    print(mes)

    


    i0 = afterS.find("TextChannel") + 15
    i1 = afterS.find(" ", i0)
    channel = client.get_channel(int(afterS[i0:i1]))

    if(mes.find("@!696040009316171807") > -1):
        await channel.send("Hello! Welcome to join noise bot. This bot will play an audio clip every time you join a voice channel")
        await channel.send("To begin say \"/|\\register\". To disable once you have an audio clip type \"/|\\disable\". To re-enable type \"/|\\enable\"")

    fURL = str(message.attachments)
    print(fURL)
    pos = fURL.find("url")
    if(pos > 0):
        pos2 = fURL.find("'", pos+5)
        url = fURL[pos+5:pos2]
        if(url[4] == "s"):
            url = url[0:4] + url[5:]
        print(url)

        userListF = open("waitingOnAudio.txt", "r")
        userList = userListF.read()
        userListF.close()

        if(userList.find(user) > -1):
            myFile = requests.get(url)
            open("audioFiles/" + user + ".mp3", 'wb').write(myFile.content)

            userListF = open("waitingOnAudio.txt", "w")
            i0 = userList.find(user)
            i1 = userList.find("|", i0+1)
            userList = userList[:i0-1] + userList[i1+1:]
            userListF.write(userList)
            userListF.close()

            userListF = open("userList.txt", "r")
            userList = userListF.read()
            userListF.close()

            userListF = open("userList.txt", "w")
            userListF.write(userList + "|" + user + "|")
            userListF.close()
            await channel.send("I have saved your audio clip! Join a voice channel to test it out!")

    if(str(s).find("/|\\") > 0 and user.find("OwenLearning#8046") != 0):
        
        
        if(str(s).find("register") > 0):
            userListF =  open("userList.txt", "r")
            userList = userListF.read()
            if(userList.find(user) < 0):
                userListF.close()
                userListF = open("waitingOnAudio.txt", "w")
                userListF.write("|" +user + "|")
                userListF.close()
                await channel.send("Hello! Thank you for registering for the welcome noise bot! The next MP3 file you post in this channel will become your new audio intro when you join a channel!")
            else:
                await channel.send("You are already registered! Did you mean to /|\\enable?")
                userListF.close()
        if(str(s).find("disable") > 0):
                userListF = open("disab.txt", "r")
                userList = userListF.read()
                userListF.close()

                if(userList.find(user) < 0):
                    userListF = open("disab.txt", "w")
                    userListF.write(userList + "|" + user + "|")
                    userListF.close()
                    await channel.send("Your audio clip was disabled")
                else:
                    await channel.send("Your audio clip was already disabled")

            
            
        if(str(s).find("enable") > 0):
            userListF = open("disab.txt", "r")
            userList = userListF.read()
            userListF.close()

            if(userList.find(user) > 0):
                userListF = open("disab.txt", "w")
                i0 = userList.find(user)
                i1 = userList.find("|", i0+1)
                userList = userList[:i0-1] + userList[i1+1:]
                userListF.write(userList)
                userListF.close()
                await channel.send("Your audio clip was enabeled")
            else:
                await channel.send("Your audio clip was already enabeled")
            
            
        if(str(s).find("changeAudio") > 0):
            await channel.send("The next MP3 file you post in this channel will become your new audio intro when you join a channel!")
            
        if(str(s).find("stop") > 0):
            await channel.send("Sorry about that, maybe you want to \"/|\\disable\" your intro sound?")
            


    if(str(s).find("wakeUpOwen") > 0):
        t = threading.Thread(target = flickerLights, args=(4,4,))
        t.start()   
        i0 = afterS.find("TextChannel") + 15
        i1 = afterS.find(" ", i0)
        channel = client.get_channel(int(afterS[i0:i1]))
        await channel.send("Owens Lights Were Flashed! Call him at (908)510-4821 if he really needs to be woken up")

    if(str(s).find("OwenTestBot") > 0):
        i0 = afterS.find("TextChannel") + 15
        i1 = afterS.find(" ", i0)
        print(afterS[i0:i1])
        channel = client.get_channel(int(afterS[i0:i1]))
        await channel.send("this is a response")

    
        

client.run('jk2MDQwMDA5MzE2MTcxODA3.XpH3CQ.7jyn6s2Dt2qaPFQg4XicjEFm7mI')
