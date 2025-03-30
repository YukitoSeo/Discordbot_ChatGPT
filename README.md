# Discordbot_ChatGPT
## Discordbotの紹介！
このDiscord Botは、テキストコミュニケーションにおける利便性や楽しさの向上を目的として作成されました！  
プログラムはシンプルなコードのため、それぞれの機能について簡単に理解できると思います。  
ぜひ、お試しあれ！  

Botは、以下の機能を備えています！  
・メッセージの送受信  
・運試し（ハッピールーレット）  
・時間によるリマインド機能  
・ChatGPT APIを利用したLLMとの対話機能　(OpenAIへの課金が必要有り)  
・ボイスチャットの監視と通知  
  
## Quick Start！
注意：Pythonプログラミング環境の設定、APIの取得方法についてはご自身で設定をお願い致します。

STEP-1：以下のファイルをダウンロード！  
・discord_basemodel.py  
https://github.com/YukitoSeo/Discordbot_ChatGPT/blob/main/discord_basemodel.py  
・discord_taken.py  
https://github.com/YukitoSeo/Discordbot_ChatGPT/blob/main/discord_taken.py  
・requirements.txt  
https://github.com/YukitoSeo/Discordbot_ChatGPT/blob/main/requirements.txt  

## STEP-2：各種API、TOKENの設定！  
「discord_taken.py」内で、それぞれの値を入力する！
```
class Takens():
    def __init__(self):
        self.discordbot_taken = '' #ディスコードボットのトークンを設定
        self.log =  #ログを書き込むテキストチャンネルIDを設定
        self.vc_channel = [] #監視するボイスチャットのVCチャンネルIDを設定
        self.vc_notice =  #ボイスチャット入室通知を書き込むテキストチャンネルIDを設定
        self.openai_token = ''#OpenAI(ChatGPT) のToken

```
