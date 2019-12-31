from discord.ext import commands
import os
import traceback
import re
from random import randint, choice
import csv

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


s = '高木「ちんぽ！ちんぽ！ほら！お前らも出せ！」\n'\
    '吉見「監督！俺たちこんなこんなことするくらいなら練習が…！」\n'\
    '高木「うるさい黙れ素人が！そんなことよりファンサービスだ！浅尾を見習え！」\n'\
    '浅尾「…ジョッ…ジョイナアアアアアアアススススススススゥ！！！」\n'\
    'おはＤ「キャー！浅尾きゅんのM字開脚おちんぽユニコーンのオマケ付きよぉおおお！！！」\n'\
    '高木「ちんぽ！ちんぽ！ちんぽ！さあみんなでジョイナス！ファンと共に！」'

happy_holiday = '高木「ワシも不倫したいんじゃ！田島！不倫おちんぽジョイナス！」\n'\
                '浅尾「田島君は未婚だから結婚して汚れた僕がいかないと…！不倫おちんぽジョイナアアアアアスゥ！！！！！」」\n'\
                '福谷「不倫とは人の倫理観から外れてる事を意味しています。普段からおちんぽ出してる監督は本来の意味では不倫していますねね」\n'\
                '小田「虎将不倫！人権蹂躙！俺のアソコは超絶倫！」\n'\
                '高木「小田、君は不倫したら北流しだ。ところで田島はどこ行った！」\n'\
                '荒木「落合さんは不倫なんかせずに奥さんを愛してるのに(ﾋﾋｰﾝ」\n'\
                '高木「黙れ素人が！セリーグの強豪チームの監督は皆不倫しておる！だからワシも不倫するのじゃ！」 ！」\n'\
                '坂井「自ら不倫してタダでチームの宣伝をし、他の強豪チームに続く。前任者ではあり得ないことだ(ｶﾞｯﾂﾎﾟ」\n'\
                '吉見「なんてことだ…なんてことだ…」'\


#with open(join_us.csv, encofing='UTF-8')as f:
#    reader = f.randlines()

l =["高木", "吉見", "浅尾", "荒木", "小田"]

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
    '高木「清原くんが覚醒剤の使用の疑いで逮捕されてしまいましたが、\n野球ファンが見たいのは黒光りするシャブ中じゃない！\n黒光りするおちんぽだ！田島！ちんぽ出せ！」\n'\
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
    '吉見「なんてことだ…なんてことだ…」']

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



    #print("処理の最後に次の式を追加します：")
    await bot.process_commands(message)



@bot.command()
async def chinpo(ctx):
    await ctx.send('ちんぽーー')


bot.run(token)
