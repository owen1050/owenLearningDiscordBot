
import discord
import requests, time


client = discord.Client()
runA = False
@client.event
async def on_ready():
    #information
    print('Logged in as')
    print(client.user.name)
    

@client.event
async def on_voice_state_update(member, before, after):
    global runA
    print(str(member))
    afterS = str(after)
    if(afterS.find("VoiceChannel") > 0 and str(member) == "WillBusler#8383" and runA):#WillBusler#8383"):
        
        i0 = afterS.find("VoiceChannel") + 16
        i1 = afterS.find(" ", i0)
        print(afterS[i0:i1])
        channel = client.get_channel(int(afterS[i0:i1]))
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="play.mp3"))
        while(vc.is_playing()):
            pass
        print("done")
        vc.pause()
        vc.resume()
        vc.stop()
        await vc.disconnect()

    if(afterS.find("VoiceChannel") > 0 and str(member) == "Zacgh#8383" and runA):#WillBusler#8383"):
        
        i0 = afterS.find("VoiceChannel") + 16
        i1 = afterS.find(" ", i0)
        print(afterS[i0:i1])
        channel = client.get_channel(int(afterS[i0:i1]))
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="wahterver.mp3"))
        while(vc.is_playing()):
            pass
        print("done")
        vc.pause()
        vc.resume()
        vc.stop()
        await vc.disconnect()

@client.event        
async def on_message(message):
    global runA
    offlink = "http://maker.ifttt.com/trigger/basementLightsOff/with/key/Bf91G_MsjKUzsWqRs5N7n"
    onlink = "http://maker.ifttt.com/trigger/basementLightsOn/with/key/Bf91G_MsjKUzsWqRs5N7n"
    s = 'Message from {0.author}: {0.content}'.format(message)
    if(str(s).find("playAudio") > 0):
        runA = True
        print("play")
    if(str(s).find("dontPlayAudio") > 0):
        runA = False
        print("pause")

    
    print(s)
    
        

client.run('')