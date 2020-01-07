from discord.ext import commands
import os
import traceback
import re
from random import randint, choice
import csv
import aiohttp

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


s = '高木「ちんぽ！ちんぽ！ほら！お前らも出せ！」\n'\
    '吉見「監督！俺たちこんなこんなことするくらいなら練習が…！」\n'\
    '高木「うるさい黙れ素人が！そんなことよりファンサービスだ！浅尾を見習え！」\n'\
    '浅尾「…ジョッ…ジョイナアアアアアアアススススススススゥ！！！」\n'\
    'おはＤ「キャー！浅尾きゅんのM字開脚おちんぽユニコーンのオマケ付きよぉおおお！！！」\n'\
    '高木「ちんぽ！ちんぽ！ちんぽ！さあみんなでジョイナス！ファンと共に！」'

happy_holiday = '高木「あけましてジョイナアアアス(ﾎﾟﾛﾝ　ほら！田島も出せ！」\n'\
                '浅尾「田島君は未婚だから結婚して汚れた僕がいかないと…！開運ジョイナアアアアアスゥ！！！！！」」\n'\
                'おはD「キャー！浅尾きゅんのピンクの破魔矢よぉぉぉおお！！！」\n'\
                'ODA「いくぜ勝竜！熱田神宮！賽銭投げて運を注入！オフも自主トレ孜孜汲汲（ししきゅうきゅう）！露出のちんぽに風スウスウ！」\n'\
                '高木「小田、君は不倫したら北流しだ。ところで田島はどこ行った！」\n'\
                '荒木「落合さんは不倫なんかせずに奥さんを愛してるのに(ﾋﾋｰﾝ」\n'\
                '高木「黙れ素人が！セリーグの強豪チームの監督は皆不倫しておる！だからワシも不倫するのじゃ！」 ！」\n'\
                '坂井「自ら不倫してタダでチームの宣伝をし、他の強豪チームに続く。前任者ではあり得ないことだ(ｶﾞｯﾂﾎﾟ」\n'\
                '吉見「なんてことだ…なんてことだ…」'\

#'高木「明けましておめでとうございます。神社は人が多過ぎだろ！ならば田島のちんぽに初詣だ！田島！出せ！」\n'\
#'浅尾「こ、今年こそ大活躍必至の田島くんにちんぽを出させるわけにはいかない！ここは僕が開運ジョイナアアアアアスゥ！！！！！」\n'\
#'おはD「キャー！浅尾きゅんのピンクの破魔矢よぉぉぉおお！！！」\n'\
#'荒木「落合さんが監督なら朝日のように輝かしい優勝が手に入るのに(ﾋﾋｰﾝ」\n'\
#'高木「黙れ素人が！初日の出よりも初ちんぽ！輝かしいのはキンタマだろ！」\n'\
#'小笠原二軍監督「ﾀﾏｷｰﾝ」\n'\
#'高木「なるほどなるほど。流石は侍。抱負なんて言うだけ野暮だね。やる気があるならちんぽ出せ！おちんぽだけがリアルだ！」\n'\
#'ODA「いくぜ勝竜！熱田神宮！賽銭投げて運を注入！オフも自主トレ孜孜汲汲（ししきゅうきゅう）！露出のちんぽに風スウスウ！」\n'\
#'高木「小田、君がいると運気が下がる。どんど焼きの炎で焼かれろ。ところで新元素の命名権を日本が得たらしいね。仮称は、チンチンのビームでしたか？」\n'\
#'福谷「ウンウントリウムですね。元素番号は113番です。理研が亜鉛のビームをビスマスに照射することで合成に成功しました。また、113番元素を必要とするボーリウムの合成にも成功しており、これらの功績から新元素の発見者と認定されました」\n'\
#'高木「ZZZZZ…… あ、これは失敬。おじいちゃん、初夢ジョイナスしてました」\n'\
#'坂井「新年早々このバイタリティーとお茶目さ。今年も高木守道から目が離せない(ｶﾞｯﾂﾎﾟ」\n'\
#'吉見「なんてことだ…なんてことだ…」',\

omikuzi = [
            "大吉"   if i < 2 else
            "中吉"   if 2 <= i < 10 else
            "小吉"   if 10 <= i < 20 else
            "末吉"     if 20 <= i < 40 else
            "吉"   if 40 <= i < 50 else
            "ジョイナス"     if 50 <= i < 55 else
            "凶"   if 55 <= i < 59 else
            "大凶"   for i in range(61)]


#with open(join_us.csv, encofing='UTF-8')as f:
#    reader = f.randlines()

l =["高木", "吉見", "浅尾", "荒木", "小田"]

#力至らず、、、そのうち別ファイルにすべし

joinus =['高木「ちんぽ！ちんぽ！ほら！お前らも出せ！」\n'\
    '吉見「監督！俺たちこんなこんなことするくらいなら練習が…！」\n'\
    '高木「うるさい黙れ素人が！そんなことよりファンサービスだ！浅尾を見習え！」\n'\
    '浅尾「…ジョッ…ジョイナアアアアアアアススススススススゥ！！！」\n'\
    'おはＤ「キャー！浅尾きゅんのM字開脚おちんぽユニコーンのオマケ付きよぉおおお！！！」\n'\
    '高木「ちんぽ！ちんぽ！ちんぽ！さあみんなでジョイナス！ファンと共に！」',\
    '高木「清原が逮捕されてプロ野球の将来が危うい... 田島！球界のためワシと一緒にちんぽ出せ！！」\n'\
    '浅尾(二軍)\n'\
    '小田(引退)\n'\
    '高木「小田、君は現行犯だ。ついでに言うと、執行猶予もない。しかしなんで前から噂があったにもかかわらず清原は逮捕されなかったんでしょうか」\n'\
    '福谷(二軍)\n'\
    '荒木「落合さんならもっと早く逮捕できたのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！中日も立浪のように能力と人格を併せ持った選手を育成しろ！」\n'\
    '坂井(失脚)\n'\
    '吉見(怪我)',\
    '高木「清原くんが覚醒剤の使用の疑いで逮捕されてしまいましたが、野球ファンが見たいのは黒光りするシャブ中じゃない！黒光りするおちんぽだ！田島！ちんぽ出せ！」\n'\
    '浅尾「勝ち継投を担ってもらわなければいけない田島くんのおちんぽを出させる訳にはいかない！今季の復活に懸ける僕がジョイナアアアアアスゥ！！！！」\n'\
    'おはD「キャーー！浅尾きゅんの依存症間違いなしのおちんぽよおぉぉぉぉ！今すぐキメたいぃぃぃぃ！！」\n'\
    'ODA「球春到来！黒い交際！今更してもしきれぬ後悔！大島去年はすんなり更改！鶴舞駅前公会堂！」\n'\
    '高木「小田、君は彼に古巣で可愛がってもらっていただろう。立浪くんには話を着けてあるから一緒に罪を償ってきなさい。さて先月は北朝鮮でチンパクの実験が行われたのが話題になりましたね。」\n'\
    '福谷「水爆ですね。原子爆弾を起爆剤に使い重水素や三重水素の核融合反応を引き起こし莫大な爆発エネルギーを持つ爆弾です。これに例えてシーズン打点記録を持つ小鶴誠氏を擁した松竹打線は水爆打線と呼ばれました。」\n'\
    '高木「なるほどそれほどの破壊力はうちの打線とおじいちゃんのちんぽには羨ましいですね。」\n'\
    '荒木「落合さんが指揮を採れば守り勝つ野球で優勝も容易いというのに」ﾋﾋｰﾝ\n'\
    '高木「黙れ素人が！チームも北朝鮮も未来が暗いの理由はGMや将軍の独裁だ！みんなでちんぽを出せば世界は明るくなるんだ！」\n'\
    '坂井「球界だけでなく世界の平和を望むとはさすが。戦争アニメファンのGMとは正反対だ」ｶﾞｯﾂﾎﾟ\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「来週からキャンプインだ！Ｂクラス脱出のためにも徹底的にしごくぞ！\n'\
    '特に田島！たっぷりしごくからその前におちんぽもしごくぞ！」\n'\
    '浅尾「田島君は登板過多でもうボロボロなのに！僕が代わりにおちんぽシコシコジョイナアアアアアアアアスゥ！」\n'\
    'おはD「キャー！浅尾きゅんのおちんぽ皮オナシコシコジョイナスよぉぉぉぉ！」\n'\
    '小田「球春到来！千客万来！不人気すぎてありえない！\n'\
    '強竜復活！人気も復活！世界の山ちゃんみそとんかつ！」\n'\
    '高木「小田、不人気なのはお前だ。消えろ。しかし不人気なのはまずい。\n'\
    'どうすればお客さんが来るんでしょうか」\n'\
    '荒木「落合さんならもっと勝ててファンサービスができるのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！こうなったらキャンプインでお客さんにもおちんぽインだ！」\n'\
    '坂井「不人気解消だけでなく少子化も解消するとは…やっぱり監督にしてよかった(ｶﾞｯﾂﾎﾟ」\n'\
    '小笠原「俺の出番だな」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「明けましておめでとうございます。神社は人が多過ぎだろ！ならば田島のちんぽに初詣だ！田島！出せ！」\n'\
    '浅尾「こ、今年こそ大活躍必至の田島くんにちんぽを出させるわけにはいかない！ここは僕が開運ジョイナアアアアアスゥ！！！！！」\n'\
    'おはD「キャー！浅尾きゅんのピンクの破魔矢よぉぉぉおお！！！」\n'\
    '荒木「落合さんが監督なら朝日のように輝かしい優勝が手に入るのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！初日の出よりも初ちんぽ！輝かしいのはキンタマだろ！」\n'\
    '小笠原二軍監督「ﾀﾏｷｰﾝ」\n'\
    '高木「なるほどなるほど。流石は侍。抱負なんて言うだけ野暮だね。やる気があるならちんぽ出せ！おちんぽだけがリアルだ！」\n'\
    'ODA「いくぜ勝竜！熱田神宮！賽銭投げて運を注入！オフも自主トレ孜孜汲汲（ししきゅうきゅう）！露出のちんぽに風スウスウ！」\n'\
    '高木「小田、君がいると運気が下がる。どんど焼きの炎で焼かれろ。ところで新元素の命名権を日本が得たらしいね。仮称は、チンチンのビームでしたか？」\n'\
    '福谷「ウンウントリウムですね。元素番号は113番です。理研が亜鉛のビームをビスマスに照射することで合成に成功しました。また、113番元素を必要とするボーリウムの合成にも成功しており、これらの功績から新元素の発見者と認定されました」\n'\
    '高木「ZZZZZ…… あ、これは失敬。おじいちゃん、初夢ジョイナスしてました」\n'\
    '坂井「新年早々このバイタリティーとお茶目さ。今年も高木守道から目が離せない(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「そんなことやったらおじいちゃんも捕まっちゃうだろ！と、いう訳でこれからおじいちゃんのおちんぽと田島のおちんぽ、どちらが勝つかを皆さんに賭けて貰おうかと思います。ちなみにおじいちゃんは田島のおちんぽが勝つに今季の中日選手全年俸分を賭けました！」\n'\
    '浅尾「常にランナーを背負っている田島くんにとって賭博という荷はあまりにも重すぎる！ここは代わりに僕が賭博追放ジョイナァアアアアスゥ！！」\n'\
    'おはD「キャーーー！！野球賭博という球界の闇に光を照らす浅尾きゅんの純白ちんぽよぉぉぉぉぉぉおお！！！巨人の闇を切り裂いてえぇぇぇぇぇぇ！！！」\n'\
    '小田「事件が発覚！高木が賭博！またもや巨人が大自爆！！賭博で散財！それは犯罪！清原やってた覚せい剤！！」\n'\
    '高木「小田、元巨人のお前にも警察の方が事情聴取に来ていたぞ。帰れ。そういえばこの騒動で辞任した方もいるみたいですね。モミクリ巨チン軍開帳のナメコネさん、でしたか」\n'\
    '福谷「読売巨人軍会長のナベツネさん、渡邉恒雄さんのことですね。正しくは読売巨人軍会長ではなく読売巨人軍最高顧問で辞任したのはこちらの役職の方です。会長に就いているのは読売新聞社の方ですね」\n'\
    '荒木「落合さんの指導下なら賭博に手を染めるなんてことはなかっただろうに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！賭博を追放するにはおちんぽ出すしかないだろ！ノーモア賭博！ウィーアージョイナス！おちんぽ出して健全な球界作りだ！！」\n'\
    '坂井「おちんぽを出す事で団結の輪を深め賭博に入り込む隙を作らせない...一人で過ごすのが好きな現GMとは大違いだ(ｶﾞｯﾂﾎﾟ」\n'\
    '速報を聞いた吉見「なんてことだ…なんてことだ…」',\
    '高木「今週中に調査結果を報告…ってそんなに待てるか！！暇潰しにちんぽ出す！田島も一緒だ！」\n'\
    '浅尾「週末まで露出していたら田島君の将来まで潰れてしまう！僕の股間を文春に暴露ジョイナアアアアアアアアアァス！」\n'\
    '小田「記憶が曖昧！？そいつはアンマリ！どうなる甘利！俺達ゃangry！！口あんぐり！どデカい産直JAあぐり！」\n'\
    '高木「小田、君はドラゴンズの規格外野菜だ。産直の売り場からも弾くからな。そういえば、おじいちゃんも1994年10月8日の記憶が曖昧です。」\n'\
    '福谷「10.8決戦と呼ばれる中日・巨人の首位決定戦の日ですね。\n巨人軍側は先発3本柱をつぎ込む思い切った継投策を見せ、一方で当時中日監督だった高木さんは……」\n'\
    '高木「やっぱ覚えてません！覚えてない！勝ったと言われれば勝ったかもしれないし、負けたと言われれば負けたかも！！」\n'\
    '荒木「落合さんは記憶しておきたい名試合ばかりなのにジョイナス監督ときたら（ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！試合結果は忘れたい……もとい記憶になくとも、ちんぽは記憶に刻みつけるのがジョイナス精神だ！！\nだから甘利は国会で、ついでに復活の野々村は裁判所でちんぽ出せ！！！」\n'\
    '坂井「ここでジョイナスが名古屋市役所で露出したらちんぽの三権分立が完成……GMの三冠王より偉大だな（ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '(出場各校の主将、おちんぽを出しながら前に出てくる)\n'\
    '高木「宣誓。我々ジョイナス一同は、全力でジョイナスし全力でおちんぽを出すことを誓います───そうと決まれば田島！ちんぽ出せ！今年の選抜は田島のちんぽでプレイボール！！」\n'\
    '浅尾「田島くんの先発起用はおじいちゃんの特権！でもここは代わりに僕が久々の先発転向ジョイナアァァァァスゥ！！」\n'\
    '小田「球児達を見守る六甲！選抜出場32校！試合が白熱マジ最高！甲子園へ今すぐLet&#39;s Go！！」\n'\
    '松永裕太郎くん「高木守道監督より、大正義巨人高校へ、小田が返還されます」\n'\
    '荒木「落合さんが監督なら毎大会優勝旗返還が出来るのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！優勝出来ずとも、負けを知り成長するのもまた青春だ！ところで今年は愛知からの出場もあるみたいですね。ちんぽこ高校、でしたか」\n'\
    '福谷「東邦高校のことですね。選抜出場回数が27回と非常に多く、選抜優勝も過去4度している名門校です。また、プロ野球選手も多数輩出しており、岩田慎司投手の母校でもあります」\n'\
    '高木「同じ愛知のチームとしてぜひとも頑張っていただきたいね。さて、今年の選抜大会はどのようなドラマが生まれるのか、おじいちゃんとても楽しみです。おじいちゃんもおちんぽジョイナスで第88回選抜高校野球大会を応援します！！」\n'\
    '坂井「チームの選手だけではなく高校球児達にもジョイナスの精神を忘れない...この気配り方は現GMにはとても真似できない芸当だ(ｶﾞｯﾂﾎﾟ」\n'\
    'プラカードを持つ吉見「なんてことだ...なんてことだ...」',\
    '雪歩「十周年を過ぎたアイマスにとって、今年はこれからに向けた大事な一年なんです！だから真ちゃん、ちんぽを見せて！」\n'\
    '赤羽根「真にちんぽを出させるわけにはいかない！落ち着け、雪歩！ちんぽなら俺が見せる、ジョイナァァァァス！！」\n'\
    '美希「キャー！ハニーのハリウッド級ちんぽなの！」\n'\
    '千早「ゲリラ、スリラ、連れてってマニラ、口当たり良いのはバニラ～、どれ、あれ、それ、そう、だからにCIAに言えよ、さっさと出てけってな！」\n'\
    '雪歩「千早ちゃん、心臓と一緒に胸も潰しておくね」\n'\
    '律子「そういえば１０年前の2006年は小泉純一郎首相が辞任した年でもあったわね。あれから２０１２年まで毎年首相が代わってたのよね。」\n'\
    '春香「ちょうどいい機会だから、雪歩の声も代わる前の方に戻そう！」(ﾁﾞｭｲ\n'\
    '雪歩「私、萩原雪歩です。リボンの女が嫌いです。」\n'\
    '高木「初代の持つ儚さと２代目が備える強さ。今年も萩原雪歩君から目が離せない(ｶﾞｯﾂﾎﾟ」\n'\
    '貴音「面妖な…面妖な…」',\
    '安倍「今年は悲願の改憲に向けた重要な年です。景気付けに菅さん、ちんぽを見せてください」\n'\
    '甘利「次期総理大臣の菅さんにちんぽを出させる訳にはいかない！ジョイナァァァス!!」\n'\
    'おは文春「キャー！甘利きゅんの５００万ちんぽよ！」\n'\
    '石破「憲法変えて目指そう理想、向上心持って我が党参上、気分上々、新９条」\n'\
    '安倍「石破さん、地元にスタバが出来たからって調子に乗らないで頂きたい。」\n'\
    '麻生「実は、安倍総理は戦後生まれとしては初めての総理大臣なんだけど、ボク自身は戦中生まれとしては最後の総理大臣なんだよね。」\n'\
    '福島「憲法の理念を守れば、安心安全な社会はやってくるのです！」(ﾋﾋｰﾝ\n'\
    '安倍「自分の党の議席も守れない人に言われたくはありません」\n'\
    '小泉「一期目には無かった「精神的な強さ」…これを手に入れた安倍君に、敵はいない！」(ｶﾞｯﾂﾎ\n'\
    '谷垣「なんてことだ...なんてことだ...」',\
    '高木「達成するのが遅すぎだろ！ともあれ荒木くん！おめでとう！まずはおじいちゃんのおち○ぽで！お祝いジョイナスします！見ろ！通算2274打ったおち○ぽを！」\n'\
    '荒木「シワシワもりみち○ぽじゃなくて、落合さんのおち○ぽで祝ってほしいのに（ﾋﾋ-ﾝ\n'\
    '高木「黙れ素人が！落合くんのガンダムち○ぽより！田島のち○ぽの方がめでたいだろ！田島！出せ！」\n'\
    '浅尾「じょ、上昇気竜には欠かせない田島くんにち○ぽを出させはしない！僕が代わりに祝！2000本ジョイナアアアアアスゥ！！！！！」\n'\
    'おはD「キャー！浅尾きゅんの桃色バットよぉおおおおお！！！私に特打してぇえええええ！！！！！」\n'\
    'ODA「無事是名馬！二遊はアライバ！ミスターDは！与えられないわ！激安ラーメン喰うぜスガキヤ！初夏の股間に風ヒヤヒヤ！」\n'\
    '高木「小田、ラーメンフォークに刺さって消えろ。ところでラーメンフォークって海外の美術館の店で人気だったらしいね。ニューヨークｷﾝﾀﾏ秘宝館、でしたか？」\n'\
    '福谷「ニューヨーク近代美術館ですね。通称はMoMAです。1929年に設立され、近代・現代の絵画や彫刻などのほか、商業・工業デザインや映像なども収蔵しています。因に日本にも公式店舗があります」\n'\
    '高木「ニューヨークのｷﾝﾀﾏより、おじいちゃんのバックトスやグラブトスの方がよっぽど芸術的だけどね」\n'\
    '小笠原二軍監督「ﾀﾏｷ?ﾝ」\n'\
    '高木「6試合連続HRのゲレーロも！おめでとうジョイナス！俊足の馬面と共に」\n'\
    '坂井「後輩を祝って駆け付けるこのドラゴンズ愛。生えぬ毛の落合より、やっぱり生え抜きレジェンドだ（ｶﾞｯﾂﾎﾟ\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「おち○ぽ出してからかうんだ！特に田島！たっぷりからかっておち○ぽもしごくぞ！」\n'\
    '浅尾「田島君をからかうなんて！僕が代わりにおち○ぽジョイナアアアアアアアアスゥ！」\n'\
    '福谷「高木さんのからかいとは西片への好意を前提としているのであり、受け身なヲタクの願望を具現化したものと言えます」\n'\
    '高木「…。ともあれファンサービスして人気が出なければいけないのだ」\n'\
    '小田「松坂移籍！絶大な人気！けれど伴わない成績！」\n'\
    '高木「小田、お前のキャリアはからかいではなく空回りだったな、消えろ。\n'\
    'しかしこのままではマスコミにすらからかわれてしまう」\n'\
    '荒木「落合さんなら途中で選手を全員ドミニカ人に入れ替えるくらいの奇策をやってくれるのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！こうなったらナゴドをリメイクしてやる！」\n'\
    '坂井「人気だけでなく球場の心配までしてくれるとは…コストカットしかしなかった元GMとは大違いだ(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '関係ない部「痴ん呆！痴ん呆！ほら！お前らも出せ！」\n'\
    'さっぱりピーマン「関なさん！僕たちこんなこんなことするくらいなら更新が…！」\n'\
    '関係ない部「うるさい黙れ素人が！そんなことよりファンサービスだ！なんまめを見習え！」\n'\
    'なんまめ「…ジョッ…ジョイナあああああああああああああああああああああああああああああああ！！！！！！！！！！！（ﾌﾞﾘﾌﾞﾘﾌﾞﾘﾌﾞﾘｭﾘｭﾘｭﾘｭﾘｭﾘｭ！！！！！！ﾌﾞﾂﾁﾁﾌﾞﾌﾞﾌﾞﾁﾁﾁﾁﾌﾞﾘﾘｲﾘﾌﾞﾌﾞﾌﾞﾌﾞｩｩｩｩｯｯｯ！！！！！！！）」\n'\
    'J民「キャー！なんまめさんの虹色高速回転！パイず○ドラゴンのオマケ付きよぉおおお！！！」\n'\
    '関係ない部「痴ん呆！痴ん呆！痴ん呆！さあみんなでジョイナス！ファンと共に！」',\
    '高木「新人王よりチンチン王！京田ち○ぽ出せ！！」\n'\
    '田島「竜の未来を担う若手にチ○ポを出させるわけにはいかない！僕が代わりにジョイナアアアアアアアススススススススゥ！！！」(浅尾さん見てますか…僕も庇うことができる後輩ができましたよ…)\n'\
    '小田「盛者必衰！Dは失墜！丹野みどりはよりどりみどり！第2の人生いま始めるさ！名古屋にあるのはそうメルサ！」\n'\
    '高木「小田、CBCからの手紙だ。来週からは出演しなくていいぞ。そういえば得物フレンズとかいうアニメが世間を騒がせているそうですね。」\n'\
    '福谷「けものフレンズですね。中京圏ではテレビ愛知の深夜枠で放送していましたが、一期の監督の降板騒ぎで制作側と監督両者の主張が食い違い、波紋を呼んでいます。」\n'\
    '荒木「監督が落合さんなら8期連続放送も夢じゃないのに」ﾋﾋｰﾝ\n'\
    '高木「黙れ素人が！けものフレンズよりセ○クスフレンズ！！文春なんか恐れているからいつまで経っても少子化が解決しないんだ！！」\n'\
    '坂井「老いてなお子作りをする気概にあふれているとは流石だ。カミさんの尻に敷かれている前任者とは大違いだ」ｶﾞｯﾂﾎﾟ\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '吉見「なんてことだ……なんてことだ……」\n'\
    '浅尾「吉見さん何見て……あれ、巨人の星に監督が出てる？」\n'\
    '高木「おじいちゃん実は国民的アニメに出演してました。必殺スライディングのやられ役だけどね」\n'\
    '浅尾「スクリュースピンスライディング……なんですかこれ反則ですよ」\n'\
    '荒木「落合さんならこれぐらい簡単に破れるのに（ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！　落合は小学生相手に苦戦してただろう！！！」\n'\
    '小田「怒り新党！　怒り心頭！　童夢はミラクルジャイアンツ！　夢はミラクルドラゴンズ！」\n'\
    '高木「小田は白昼夢を見ているようだ。対策ならある！！　田島、おちんぽスクリュースピンジョイナスだ！！！」\n'\
    '浅尾「そんなになんか凄そうな事を田島くんにさせられない！　僕がジョイナアアアアス！！！」\n'\
    '坂井「体の回転に加え、おちんぽで別の回転軸を作り出すとは……飛雄馬対策も完璧だ、優勝はもらった（ｶﾞｯﾂﾎﾟ」\n',\
    '高木「オルフェーヴルは出ませんが、田島がちんぽを出すしかない！仁川を盛り上げジョイナスだ！」\n'\
    '浅尾「オールスターで田島くんより票を集めてない馬が出走するからそれはアリ…っていいわけがない！僕がジョイナアアアアアスゥ！！！！！」\n'\
    '高木「ここでおちんぽ予想！まず、ジェンティルドンナにはちんぽがない！これは消しですね」\n'\
    '荒木「三冠牝馬を軽視するなんて三冠王をみくびるようなものなのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！阪神内回り2200mは牝馬には過酷！これは本格化したフェノーメノしかありませんね」\n'\
    '福谷「しかしながら宝塚記念は有馬に直結するといいます。ここは有馬で激走したゴールドシップの巻き返しですね」\n'\
    '小田「ステゴとマック！福留ファック！内田とゴルシの黄金タッグ！監督と僕の世代のギャップ！」\n'\
    '高木「小田、時間というものは酷いよな。消えろ。よし決めた！内田君！踊るのは猿でも蛯でもなく君のバク転ちんぽだ！」\n'\
    '坂井「本命にしたグランプリボスが飛んでもなお内田を信じるとは…ジョイナスは前任者以上に我慢できるな(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    'クラーク「Is this a penis?」\n'\
    '高木「No!! This is a Ochimpo!! まだジョイナシズムが分からないのか！田島！フニャチン外人に股間の大和魂見せ付けてやれ！」\n'\
    '浅尾「た、田島くんのおちんぽはまだ他言語未対応！僕のWBCで世界デビューするはずだったおちんぽがジョイナアアアアアスゥ！！！！！」\n'\
    '小田「世界は多極化！セ界は二極化！メロスはシラクサ！名古屋に千種(ちくさ)！日本にはびこる所得格差！俺の扱いその低さ！」\n'\
    '高木「小田、君は世間的には貰ってる方だから消えろ。しかし格差はやだねえ。差があるのはちんぽの大きさだけでいいのに」\n'\
    '福谷「共産主義なら格差はなくなるかもしれませんが、その限界はソ連が露呈させてしまいました。今や新自由主義の時代ですね」\n'\
    '荒木「落合さんのいないドラゴンズの限界もすでに露呈してるのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！露呈したんじゃない！露出したんだ！おちんぽを！ファンの為に！ファンと共に！」\n'\
    '坂井「おちんぽ露出もメディア露出も積極的…前任者とは何から何まで違うな(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「おじいちゃんこの状況でもAクラスで嬉しい！ほれ喜び組の田島、はやくちんぽ出して踊れ」\n'\
    '浅尾「田島君にはまだ勝利の舞を踊を踊らすわけにはいきません！僕が代わりに勝利のローリングジョイナアアアアアアスゥ！（ｸﾙｸﾙｸﾙｰ」\n'\
    '小田「鯉抜き！虎抜き！兎抜き！目指せ悲願のごぼう抜き！今日も栄のソープでヌキヌキ！そして嫁さん激怒で飯抜き！」\n'\
    '高木「小田、我々はチームの足を引っ張る小田抜きで戦っていくことに決めたから昨日登録抹消しておいたぞ」\n'\
    '福谷「ちなみに今首位巨人との差は14.5ゲーム差ですが、NPBで最大ゲーム差をひっくり返し優勝したのは西鉄（現西武）の同じく14.5ゲーム差ですね。」\n'\
    '近年では1996年、巨人が広島との11.5ゲーム差から逆転しての優勝というのもあります。これが世に言う『メークドラマ』というやつですね。」\n'\
    '荒木「落合さんなら2011年8月時点で10ゲーム差をひっくり返したように今年も優勝できるかもしれないのに（ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！よし今から選手皆でおちんぽを出して手を繋ぎ輪になって亀頭を中央に差し出し、全員でおちんぽキッスをして気合を入れろ」\n'\
    '坂井「男として大切なところを恥じらいも無く出させ、互いに接触させて団結力をはかる…。前任者にはなかったことだ（ｶﾞｯﾂﾎﾟ」\n'\
    'リハビリをしながらその様子を見てる吉見「なんてことだ…なんてことだ…」',\
    '荒木「名古屋市東区といえばナゴヤドームの所在地！いつもと変わらないじゃないか(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！地元を紹介してこそのジョイナス！さあゆとりーとラインでゴーゴーでGO!GO!」\n'\
    '小田「ゴーゴーでGO!GO!明和高校！私服で通える旭丘高校！」\n'\
    '高木「小田、君が区内の教育機関を紹介する必要はない。さあ気を取り直して敷島パン工場見学だ！」\n'\
    '藤井「関東の皆さんには敷島パンになじみがないかもしれないですが、実は『Pasco』の本元なのです」\n'\
    '高木「さすが高学歴！博識ですね。よし！田島のちんぽを超熟ジョイナスさせるぞ！」\n'\
    '浅尾「田島くんのちんぽをイースト菌まみれにはできない！僕のちんぽがふっくらもちもちジョイナアアアアアスゥ！！！！！」\n'\
    '高木「さあ最後は徳川美術館でジョイナス！国宝の源氏物語絵巻があるぞ！ちんぽに巻いてみます」\n'\
    '吉見「なんてことだ…なんてことだ…」\n'\
    '小田「巻いちゃいけません！名鉄瀬戸線！原発どうする中部電力本店！」\n'\
    '高木「小田、ジョークが分からないなら消えろ。さあ皆さん魅力一杯ちんぽ一杯の東区でジョイナス！」\n'\
    '坂井「素晴らしい地元PR…ドーム周辺が潤えば観客も当然増える(ｶﾞｯﾂﾎﾟ」',\
    '高木「どうか最後までお付き合いください！ジョイナス！ファンと共に！」\n'\
    '小田「愛しい奈々！女の罠！ママ人殺したよたった今！鳥羽-磯部-鵜方-賢島！」\n'\
    '高木「小田、君の私生活も死のロードに入りたいのか。さあ田島！ちょっと恥ずかしそうな顔のかわいいちんぽを見せろ！」\n'\
    '浅尾「た、田島くんのちんぽと僕のちんぽは運命共同体！故に僕がジョイナアアアアアスゥ！！！！！」\n'\
    '福谷「新潮によると二人が肉体関係を持ったのは2005年の10月のことのようですね。それから7年間続いたそうです」\n'\
    '荒木「落合政権はスパイスの不倫期間、ジョイナス政権より長い8年間！やっぱり落合さんがナンバーワン(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！私とおちんぽは何でもありの71年間！死ぬまでジョイナス！ちんぽと共に！」\n'\
    '坂井「今月17日にちんぽとジョイナスの付き合いは72年目に突入…前任者にはこんな長く付き合える相手はいない(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「おじいちゃんはジブリが大好きです。という事で今日は耳をすませばを見るぞ！」\n'\
    '福谷「耳をすませばは1995年に上映されたスタジオジブリ制作の映画です。ちなみに原作の漫画もありますが4巻で打ち切られています」\n'\
    '小田「天沢聖司！笘篠誠治！中日のコーチ小林誠二！」\n'\
    '高木「小田、耳を澄ませ。戦力外通告だ。田島！耳じゃなくてちんぽを澄ませ！」\n'\
    '浅尾「た、田島君のちんぽはまだ澄まされてないからここは僕のすまされおチンポジョイナアアアアアアス！！！！」\n'\
    '荒木「落合さんならこんな恋愛ごっこじゃなくて深みがある千と千尋の神隠しを見るのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！恋愛も応援もすべてファンと共に！ジョイナス！」\n'\
    '坂井「選手たちに愛を教える…冷徹な前任者では成しえなかったことだ(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '？？「大切なのは『真実に向かおうとする意志』だ。ジョイナス…お前は立派にやったのだよ…わたしが誇りに思うくらい立派にね」\n\n'\
    '高木「ちんぽ！ちんぽ！ちんぽを出したい！ちんぽを見たい！これぞ真実！これぞジョイナス！」\n'\
    '荒木「落合さんが求めていたのは『結果』だけなのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！『結果』だけを求めたら人は近道をしたがる！田島！栄光はお前にある！ちんぽ出せ！」\n'\
    '浅尾「た、田島くんは僕なんだ！田島くんのちんぽは僕のちんぽだジョイナアアアアアスゥ！！！！！」\n'\
    '小田「帝王はディアボロ！チームはボロボロ！岩本製菓の卵ボーロ！いつでも僕たちチンポーロ！」\n'\
    '高木「小田、私の側に近寄るな。ベンチで眠れる奴隷だったおじちゃん！そろそろ目覚めます！ファンと共に！」\n'\
    '坂井「ジョイナスの苦難が…何か大いなる意味となる始まりなのかもしれない…前任者は果たして滅びずにいられるかな？(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「おじいちゃんこの3連戦で若々しいおちんぽをたくさん見つけることができました。早速全員ちんぽ出せ！」\n'\
    '田島・西川・辻「（やっと僕達もジョイナスできる日が来たんだ・・・！）」\n'\
    '浅尾「だだだダメです！まだ若くて皮から少し頭が出てるようなちんぽを見せるわけにはいきません！ここは僕がハイパーズル剥けジョイナアアアアアアアスゥ！」\n'\
    '荒木「落合さんならしっかりファームで土台を作って何度も1軍で使ってからローテに入れてたのに（ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！お客さんが望んでるのは真新しい赤ちゃんのような肌のおちんぽなんだよ」\n'\
    '小田「荒木なんですぐ「落合」言うの？戻らない事知ってるYouKnow！だけどジョイナスあんたより有能！4度の優勝！マジ名将！オウサンショウウオこれ希少！」\n'\
    '高木「小田、君はその名将にレギュラーとして扱ってもらわなかった所詮腐れ捕手だってことを忘れずに」\n'\
    '福谷「ちなみにオオサンショウウオは恐竜が生まれるよりもっと前の3000万年前から存在していて名古屋の堀川でも存在が確認されたとても古い動物です。補足ですが最古の動物は昌さんのあだ名でもある6000万年前から存在するシーラカンスです。」\n'\
    '高木「最古の動物ということはどいつよりも一番おちんぽを出して一番セックスをしているということだな。おじいちゃんシーラカンス大好き！」\n'\
    '坂井「次々に新戦力を試してご褒美も忘れないこのサービス精神…。前任者には無かったことだ（ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「ワシも不倫したいんじゃ！田島！不倫おちんぽジョイナス！」\n'\
    '浅尾「田島君は未婚だから結婚して汚れた僕がいかないと…！不倫おちんぽジョイナアアアアアスゥ！！！！！」」\n'\
    '福谷「不倫とは人の倫理観から外れてる事を意味しています。普段からおちんぽ出してる監督は本来の意味では不倫していますねね」\n'\
    '小田「虎将不倫！人権蹂躙！俺のアソコは超絶倫！」\n'\
    '高木「小田、君は不倫したら北流しだ。ところで田島はどこ行った！」\n'\
    '荒木「落合さんは不倫なんかせずに奥さんを愛してるのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！セリーグの強豪チームの監督は皆不倫しておる！だからワシも不倫するのじゃ！」 ！」\n'\
    '坂井「自ら不倫してタダでチームの宣伝をし、他の強豪チームに続く。前任者ではあり得ないことだ(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「お前たち！私が直々におちんぽジョイナスの仕方をレクチャーしてやる！しっかり見ろ！もっと顔を近付けろ！」\n'\
    '浅尾「こ、これがレジェンド高木のおちんぽ！改めて見るとやっぱりしわしわだ！」\n'\
    '高木「…威勢のいいことを行ったくせにこんなしわしわおちんぽで申し訳ない！田島！私の代わりに見せてくれ！」\n'\
    '浅尾「監督にできないことを田島くんのちんぽには担わせられない！僕が背負いジョイナアアアアアスゥ！！！！！」\n'\
    '坂井「互いの至らない所を補い合うおちんぽの絆…前任者の頃にはなかったものだ(ｶﾞｯﾂﾎﾟ」\n'\
    '福谷「絆とは元々は家畜をつないでおく綱のことを表す言葉だったんですよね。人と人との結びつきを指すようになったのはここ最近のことのようです」\n'\
    '荒木「落合さんと僕の間には絆があったのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！私たちのちんぽは！目に見えない何かでつながっている！そんなちんぽの集合体がおちんぽグローバルだ！」\n'\
    '小田「つながる！アスナル！マドリガル！チェニジア暴動アラブの春！種田とトレード中日波留！」\n'\
    '高木「小田、君は村八分だ。世界のちんぽが結びつき！戦争がなくなれば！ピースフルジョイナス！みんなが笑って暮らせる世界と共に！」\n'\
    '戦争の酷さに嘆く吉見「なんてことだ…なんてことだ…」',\
    '中畑「おう石川！」\n'\
    '石川「監督！どうしたんですかその口」\n'\
    '中畑「最近、おちんぽ打線の元気が無い、だから打席で凡退するたびにみんなのおちんぽを一本づつバキュームしていくんだ！」\n'\
    'ノリ「落合はんならジジイのフェラじゃなくて信子の濃厚マットプレイを用意してくれるのになあ…（ｽﾞｽﾞｽﾞ」\n'\
    '中畑「だまれうんこちんちん！そんな事いうとバキュームしてやんないぞ」\n'\
    '荒波「井納は抹SHOW！コーコラン上SHOW！三嶋は飛SHOW！もう後がないぜこんちくSHOW！\n'\
    '中畑「荒波うちの本当の弱点は打線じゃなくて投手陣の薄さなのは十分知っているまずは多村！ 俺のバキュームで下がったおちんぽと打率も昇り龍だ！」\n'\
    '金城「多村のスペランカーおちんぽがバキュームされたらおちんぽ骨折今季絶望！ 俺のハマの龍神おちんぽをバキュームしてください！」\n'\
    '多村「なんてことだ…なんてことだ…」\n'\
    '三浦「僕の夢はおちんぽとオチンポが通じ合いベイスターズが最高のチームになって優勝することです（ﾖ・ﾛ・ｼ・ｸ」',\
    '高木「浅尾！ちんぽぽの花が咲いてるぞ！」\n'\
    '浅尾「…先生、おじいちゃんは…」\n'\
    '福谷「病状が大分進行していますね。退院して在宅介護を希望と伺ってますが、福祉の方でも厳しい道になりますね」\n'\
    '高木「ちんぽぽの花は！踏まれても！踏まれても！立ち上がってくる！これぞジョイナス魂！」\n'\
    '小田「ジョイナス魂！ジョイ・イズ・楽しい！英語を学ぼうECC！名古屋の5チャンはCBC！」\n'\
    '高木「小田、君はえーと…忘れた。ところで私はいつの間にちんぽ出してるんだ！生まれたときから丸裸！」\n'\
    '荒木「こんなジジイじゃなくて落合さんと同じ病室がいいのに(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！田島看護師！ちんぽの時間はまだか！早くちんぽ出せ！」\n'\
    '浅尾「早く退院させないと田島看護師が不衛生箇所露出で病院をクビになる！僕が在宅介護ジョイナアアアアアスゥ！！！！！」\n'\
    '坂井「いろんなことを忘れてもおちんぽへの情熱は忘れない…前任者は和製大砲を育てると言って忘れてしまった(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「何故人はちんぽを露出するのか！むしろ何故人はちんぽを露出してはいけないのか！わいせつとは何なのか！」\n'\
    '福谷「司法は『徒に性欲を興奮又は刺激せしめ、且つ普通人の正常な性的羞恥心を害し、善良な性的道義に反するもの』という解釈を出してますね」\n'\
    '高木「おじいちゃんは、そんな解釈よりもちんぽを出すべきだと思うのですよ！田島のちんぽを！」\n'\
    '浅尾「田島くんのちんぽを出すべきという法的根拠が出せないなら、僕が代わりにちんぽを出さざるをえない！ジョイナアアアアアスゥ！！！！！」\n'\
    '高木「そういう解釈もあるかもしれない。しかし私が…ファンが田島のちんぽを見たいという感情は！権利として認められるべきではないだろうか！」\n'\
    '福谷「憲法第19条ですね。田島さんの陰茎を見たいという思想、ファンに見せてあげたいという良心。この自由を侵してはならないということですね」\n'\
    '小田「公共の福祉！中継ぎの酷使！育成失敗した福嗣！名古屋の監督それピクシー！」\n'\
    '高木「小田、法は君を縛るためにある。ところでなんだっけ。まぁいいや、三位になった記念にちんぽ川柳やるかぁ！」\n'\
    '荒木「過半数 爺に集まる 不信任 次の総理は あの人を推す(ﾋﾋｰﾝ」\n'\
    '高木「黙れ素人が！ここは議会じゃない！人気より任期が大事なのは監督人事も民主主義も同じ！おちんぽはノーモア途中休養！」\n'\
    '坂井「前任者も任期が切れただけ…だからとくに問題はなかった(ｶﾞｯﾂﾎﾟ」\n'\
    '吉見「なんてことだ…なんてことだ…」',\
    '高木「ジョイナス！ちんぽ右！ジョイナス！ちんぽ左！」\n'
    '浅尾「振りかぶってお腹にペチッ！振りかぶってお腹にペチッ！」\n'
    '高木「ファンと共に～！おちんぽクロス！おちんぽクロス！」\n'
    '浅尾「おちんぽクロ…あっ…」\n'
    '高木「浅尾！何やってるんだ！なんでワシのおちんちんとクロスさせないんだ…！」\n'
    '浅尾「すみません…いっつも打者とのタイミングずらすこと考えているので…つい…」\n'
    '高木「黙れ素人が！ファン人気ナンバーワンのお前がジョイナスちんちん体操できなきゃ意味がないんだよ！田島に変えるぞ！」\n'
    '浅尾「田島くんは…！ボク、頑張りますから！田島くんはまだやめてください！」\n'
    '吉見「なんてことだ…なんてことだ…」\n'
    '高木「言葉だけは一人前だな…その言葉…証明してみろ！！！！」\n'
    '浅尾「ジョ…ジョイナアアアアアアアスゥ！！！！ファンと共におちんぽクロス！！やがて生まれるおちんぽグローバル！！！！」\n'
    '坂井「選手のやる気を引き出したか…やはり落合以上だ(ｶﾞｯﾂﾎﾟ」']




@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send(s)

@bot.command()
async def join(ctx):
    await ctx.send(choice(l))

@bot.command()
async def us(ctx):
    await ctx.send(choice(joinus))

@bot.command()
async def kuzi(ctx):
    await ctx.send(choice(omikuzi))

#@bot.command()
#async def us(ctx):
#    await ctx.send(choice(f))

# test終了につき凍結
#@bot.command()
#async def neko(ctx):
#    await ctx.send('にゃーん')

@bot.event
async def on_message(message):
    #メッセージ送信者がbotだった場合は無視する
    if message.author.bot:
        return
    # ちんぽが含まれていたら？？？
    if re.search("おちんぽ", message.content):
        await message.channel.send("ジョイナス!")

    if re.search("落合", message.content):
        await message.channel.send("黙れ素人が！")

    if re.search("あけおめ", message.content):
        await message.channel.send(happy_holiday )

    if re.search("明けまして", message.content):
        await message.channel.send(happy_holiday )

    if re.search("猫", message.content):
        photo = random.choice(("https://i1.wp.com/memorynator.com/wp-content/uploads"\
                               "/2017/03/catgif-matomegif-91.gif?resize=296%2C311&ssl=1",
                               "https://i1.wp.com/memorynator.com/wp-content/uploads"\
                               "/2017/03/catgif-matomegif-86.gif?resize=471%2C279&ssl=1",
                               "https://i2.wp.com/memorynator.com/wp-content"\
                               "/uploads/2017/03/catgif-matomegif-68.gif?resize=500%2C282&ssl=1",
                               "https://i0.wp.com/memorynator.com/wp-content"\
                               "/uploads/2017/03/catgif-matomegif-56.gif?resize=259%2C431&ssl=1",
                               "https://i1.wp.com/memorynator.com/wp-content"\
                               "/uploads/2017/03/catgif-matomegif-35.gif?resize=498%2C283&ssl=1",
                               "https://i1.wp.com/memorynator.com/wp-content"\
                               "/uploads/2017/03/catgif-matomegif-35.gif?resize=498%2C283&ssl=1"))

        async with aiohttp.ClientSession() as session:
            async with session.get(photo) as resp:
                if resp.status != 200:
                    return await message.channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await message.channel.send(file=discord.File(data,"cool_image.gif"))



    #print("処理の最後に次の式を追加します：")
    await bot.process_commands(message)



@bot.command()
async def chinpo(ctx):
    await ctx.send('ちんぽーー')








bot.run(token)
