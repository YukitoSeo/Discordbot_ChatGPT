import discord
import datetime
import asyncio
import random
from discord.ext import tasks
import discordbot.discord_taken_org as discord_taken_org
from openai import OpenAI

my_taken = discord_taken_org.Takens()
client = discord.Client(intents=discord.Intents.all())

gpt_client = OpenAI(api_key=my_taken.openai_token)

#テキストチャンネル(ログ)に日時を出力する
async def greeting():
    dt = datetime.datetime.today()
    greet = client.get_channel(my_taken.log)
    await greet.send(f'{dt.year}年{dt.month}月{dt.day}日 {dt.hour}時{dt.minute}分{dt.second}秒')
    await greet.send('起動したよ！')

#毎週金曜日午後6時にお疲れ様メッセージを送る
@tasks.loop(seconds=60)
async def loop():
    now = datetime.datetime.today()
    if now.weekday() == 4 and now.hour == 18 and now.minute == 00:
        channel = client.get_channel(my_taken.log)
        await channel.send('一週間お疲れ様!')    

@client.event
async def on_ready():
    guild_count = len(client.guilds)
    game = discord.CustomActivity(f'お仕事中！')# BOTのステータスを変更する
    await client.change_presence(status=discord.Status.online, activity=game)
    await greeting()
    print('ログインしました')
    loop.start()

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    '''
    [Discord上で返信してくれるコマンド集]
    ハッピールーレット：1/1000の確率で当たりが出る運試し
    ゴリラ：ゴリラのアスキーアートを表示
    ヘルプ：コマンドリストを返す
    '''

    if message.content == 'ハッピールーレット':
        await message.channel.send('777が出たらあたり！\nハッピールーレット、スタート！\nでりゃぁ！\t')
        happy = random.randint(0,1000)
        await message.channel.send(happy)
        if happy == 777:
            await message.channel.send('おめでとう！大当たり！')
        else :
            await message.channel.send('残念、はずれなのん...')
        return
    if message.content == 'ゴリラ':
        await message.channel.send('▒▒▒▒▄██████████▄▒▒▒▒\n▒▒▄██████████████▄▒▒\n▒██████████████████▒\n▐███▀▀▀▀▀██▀▀▀▀▀███▌\n███▒▒■　▐▒▒▒▒▌　■▒▒███\n▐██▄▒▀▀▀▒▒▒▒▀▀▀▒▄██▌\n▒▀████▒▄▄▒▒▄▄▒████▀▒\n▒▐███▒▒▒▀▒▒▀▒▒▒███▌▒\n▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒\n▒▒██▒▒▀▀▀▀▀▀▀▀▒▒██▒▒\n▒▒▐██▄▒▒▒▒▒▒▒▒▄██▌▒▒\n▒▒▒▀████████████▀▒▒▒\n')
        return
    
    if message.content == 'ヘルプ':
        await message.channel.send('・ハッピールーレット\n・ゴリラ\n')
        return
    

    completion = gpt_client.chat.completions.create(
        model='gpt-4o-mini',
        messages = [
            {"role": "system", "content": "あなたはアシスタントです。"},
            {"role": "user", "content": message.content}
        ]
    )
    await message.channel.send(completion.choices[0].message.content)
    return
        
@client.event
async def on_voice_state_update(member, before, after):
 
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル
        botRoom = client.get_channel(my_taken.vc_notice)
        # 入退室を監視する対象のボイスチャンネル
        announceChannelIds = my_taken.vc_channel

        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            print('join '+after.channel.name +' : ' + member.name)
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました。")


client.run(my_taken.discordbot_taken)
