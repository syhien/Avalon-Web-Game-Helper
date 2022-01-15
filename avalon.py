from flask import Flask
from flask import request
import random

avalon = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'

# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''

# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'


@avalon.route('/', methods=['GET'])
def getIdentityForm():
    return '''<form action="/" method="post">
    <p>输入本次游戏总人数(1~10)Input the number of PLAYERS:<input name="PlayersNumber"></p>
    <p>输入刚刚共同决定的本次游戏的数字Input the GAME NUMBER we just decided together:<input name="GameNumber"></p>
    <p>输入座位号(从1开始计数)Input your own SEAT NUMBER:<input name="SeatNumber"></p>
    <p><button type="submit">获取身份Get Identity</button></p>
    </form>
    '''

@avalon.route('/', methods=['POST'])
def getIdentity():
    playersNumber = int(request.form['PlayersNumber'])
    gameNumber = int(request.form['GameNumber'])
    seatNumber = int(request.form['SeatNumber'])

    identitiesMap = {
        5:['梅林Merlin', '派西维尔Percival', '亚瑟的忠臣Loyal Servant of Arthur', '莫甘娜Morgana', '刺客Assassin'],
        6:['梅林Merlin', '派西维尔Percival', '亚瑟的忠臣Loyal Servant of Arthur', '莫甘娜Morgana', '刺客Assassin', '亚瑟的忠臣Loyal Servant of Arthur'],
        7:['梅林Merlin', '派西维尔Percival', '亚瑟的忠臣Loyal Servant of Arthur', '莫甘娜Morgana', '刺客Assassin', '亚瑟的忠臣Loyal Servant of Arthur', '奥伯伦Oberon'],
        8:['梅林Merlin', '派西维尔Percival', '亚瑟的忠臣Loyal Servant of Arthur', '莫甘娜Morgana', '刺客Assassin', '亚瑟的忠臣Loyal Servant of Arthur', '亚瑟的忠臣Loyal Servant of Arthur', '莫德雷德的爪牙Minion of Mordred'],
        9:['梅林Merlin', '派西维尔Percival', '亚瑟的忠臣Loyal Servant of Arthur', '莫甘娜Morgana', '刺客Assassin', '亚瑟的忠臣Loyal Servant of Arthur', '亚瑟的忠臣Loyal Servant of Arthur', '亚瑟的忠臣Loyal Servant of Arthur', '莫德雷德Mordred'],
        10:['梅林Merlin', '派西维尔Percival', '亚瑟的忠臣Loyal Servant of Arthur', '莫甘娜Morgana', '刺客Assassin', '亚瑟的忠臣Loyal Servant of Arthur', '亚瑟的忠臣Loyal Servant of Arthur', '亚瑟的忠臣Loyal Servant of Arthur', '莫德雷德Mordred', '奥伯伦Oberon']
        }
    identities = identitiesMap[playersNumber]

    random.seed(gameNumber)
    random.shuffle(identities)
    ret = '<h2>你的身份是Your Identity is ' + identities[int(seatNumber) - 1] + '</h2>'

    if identities[int(seatNumber) - 1] == '梅林Merlin':
        seenPlayers = []
        for i in range(len(identities)):
            if identities[i] in ['莫甘娜Morgana', '刺客Assassin', '奥伯伦Oberon']:
                seenPlayers.append(i + 1)
        ret += '<h2>你看到了You saw: ' + str(seenPlayers) + '</h2>'
    elif identities[int(seatNumber) - 1] == '派西维尔Percival':
        seenPlayers = []
        for i in range(len(identities)):
            if identities[i] in ['梅林Merlin', '莫甘娜Morgana']:
                seenPlayers.append(i + 1)
        ret += '<h2>你看到了You saw: ' + str(seenPlayers) + '</h2>'
    elif identities[int(seatNumber) - 1] == '莫甘娜Morgana':
        seenPlayers = []
        for i in range(len(identities)):
            if identities[i] in ['刺客Assassin', '莫德雷德Mordred']:
                seenPlayers.append(i + 1)
        ret += '<h2>你看到了You saw: ' + str(seenPlayers) + '</h2>'
    elif identities[int(seatNumber) - 1] == '刺客Assassin':
        seenPlayers = []
        for i in range(len(identities)):
            if identities[i] in ['莫甘娜Morgana', '莫德雷德Mordred']:
                seenPlayers.append(i + 1)
        ret += '<h2>你看到了You saw: ' + str(seenPlayers) + '</h2>'
    elif identities[int(seatNumber) - 1] == '莫德雷德Mordred':
        seenPlayers = []
        for i in range(len(identities)):
            if identities[i] in ['莫甘娜Morgana', '刺客Assassin']:
                seenPlayers.append(i + 1)
        ret += '<h2>你看到了You saw: ' + str(seenPlayers) + '</h2>'
    else:
        ret += '<h2>你什么也没看到You saw nobody</h2>'
        ret += '<h3>不是先知，胜似先知Saw nothing, but will know anything</h3>'
    return ret

if __name__ == '__main__':
    avalon.run()
    