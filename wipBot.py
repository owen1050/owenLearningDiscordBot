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
    #information
    print('Logged in as')
    print(client.user.name)
    

@client.event
async def on_voice_state_update(member, before, after):
    pass   

@client.event        
async def on_message(message):
    global runA
    afterS = str(message)
    s = 'Message from {0.author}: {0.content}'.format(message)
    print(s)
    if(str(s).find("wakeUpOwen") > 0):
        t = threading.Thread(target = flickerLights, args=(4,4,))
        t.start()   
        i0 = afterS.find("TextChannel") + 15
        i1 = afterS.find(" ", i0)
        channel = client.get_channel(int(afterS[i0:i1]))
        await channel.send("Owens Lights Were Flashed! Call him at (908)510-4821 if he really needs to be woken up")
    if(str(s).find("test") > 0):
        i0 = afterS.find("TextChannel") + 15
        i1 = afterS.find(" ", i0)
        print(afterS[i0:i1])
        channel = client.get_channel(int(afterS[i0:i1]))
        await channel.send("this is a response")

    
        

client.run('jk2MDQwMDA5MzE2MTcxODA3.XpH3CQ.7jyn6s2Dt2qaPFQg4XicjEFm7mI')
