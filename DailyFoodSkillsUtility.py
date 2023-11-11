"""
#KJPang 2020
"""

import numpy

#import canteen skills in a sensical format
cats = open("cat_skill.cat_skill", "r")
catsArray = numpy.fromfile(cats, dtype=numpy.uint8)

#lists of phrases
skillnum = [*range(1,30,1)]
activeSkills = 0
isActive = ["启用", "禁用"]
errorList = ["\n必须启用至少一种每日技能", "\n无法识别输入内容"]
foodSkills = ["猫的解体术【小】", "猫的防御术【大】", "猫的防御术【小】", "猫的弹武好手",
              "猫的逃走术", "猫的宅配术", "猫的搬运铁人", "猫的弱小招来！",
              "猫的起身术【小】", "猫的粗暴射击", "猫的攀爬藤蔓达人", "猫的紧抓不放铁人",
              "猫的着地术", "猫的蛮干术", "猫的赠品术", "猫的异臭球达人", 
              "猫的长靴术", "猫的随从指导术", "猫的短期催眠术", "猫的钓鱼好手",
              "猫的休息术", "猫的报酬金保险", "猫的吸引仇恨好手", "猫的后面交给你们了！",
              "猫的探索好天气", "猫的天气预报", "猫的生物学者", "猫的大型吸引",
              "猫的小型吸引"]
foodStarts = [82, 162, 178, 242, 258, 274, 290, 306, 354, 370, 386, 402, 434, 450, 466, 
              546, 578, 626, 642, 674, 690, 706, 722, 738, 754, 770, 882, 898, 914]
foodEnds = [86, 166, 182, 246, 262, 278, 294, 310, 358, 374, 390, 406, 438, 454, 470, 
            550, 582, 630, 646, 678, 694, 710, 726, 742, 758, 774, 886, 902, 918]
foodSpaces = [5, 5, 5, 9, 11, 11, 9, 7, 5, 9,
              5, 5, 11, 11, 11, 7, 11, 7, 7, 9,
              11, 7, 5, 1, 7, 9, 9, 9, 9]  
#didn't want to write something up to generate this, so prewritten array
foodLazy = ["\n[01] ", "[02] ", "[03] ", "[04] ", "[05] ", "[06] ", "[07] ", "[08] ", "[09] ", "[10] ",
             "[11] ", "[12] ", "[13] ", "[14] ", "[15] ", "[16] ", "[17] ", "[18] ", "[19] ", "[20] ",
              "[21] ", "[22] ", "[23] ", "[24] ", "[25] ", "[26] ", "[27] ", "[28] ", "[29] "]
foodActive = []

#check to see which foods are active and display them nicely
def checkFood():
    global totalfood
    totalfood = 0
    foodActive = []
    drawPos = 1
    
    for i in range(len(foodStarts)):
        if catsArray[foodStarts[i]] == 255:
            foodActive.append(isActive[0]) ; totalfood += 1
        else: foodActive.append(isActive[1])
        if drawPos%2 == 1:
            print (foodLazy[i] + foodSkills[i] + " "*int(foodSpaces[i]) + foodActive[i] + "    " , end = "")
        else: print (foodLazy[i] + foodSkills[i] + " "*int(foodSpaces[i]) + foodActive[i])
        drawPos +=1 
    print ("     当前启用的数量： " + str(totalfood) + " / 29\n")
    #print (foodActive) 

#help command
def commands():
    print ("\n命令列表：\n\nfood - 显示所有每日技能当前的状态\nhelp - 查看命令列表")
    print ("delp - 查看此应用程序的详细使用说明\nsave - 创建一个新的 \"cat_skillMOD.cat_skill\" 文件")
    print ("exit - 关闭程序\n")
    print ("bout - 查看此应用程序与作者信息\n")
    print ("1-29 - 切换与输入数字关联的每日技能的启用状态\n")
    print ("dall - 禁用全部的每日技能，除了 \"猫的短期催眠术\"")
    print ("eall - 启用全部的每日技能\n")
    
#detailed help command    
def detailedHelp():
    print ("\n输入数字切换以切换关联的每日技能的启用状态。\n比如： \n输入 \"1\" 后按下回车键，将启用或禁用 \"猫的解体术【小】\" 在每日技能中的轮换。")
    print ("当您想要的技能设置完毕后，输入 \"save\"，将创建一个 \"cat_skillMOD.cat_skill\" 文件于工作文件夹中。\n任何同名的现有文件都将被覆盖。")
    print ("将该文件移至 nativePC/common/equip，并重命名为 \"cat_skill.cat_skill\"，与未修改的原始文件一样。")
    print ("与大多数类似的 mod 一样，需要使用 Stracker's Loader 才能在游戏中反映这些更改。\n")

#author info command    
def authHelp():
    print ("\nDaily Food Skills Utility v1.1.0 - KJPang 2020")
    print ("使用 python3.7 (python.org) 编写，并通过 pyinstaller (pyinstaller.org) 打包\n")
    print ("pyinstaller 会将脚本与整个 python 环境打包，因此会有一个庞大的文件\n")

#save command
def saveFood():
    conv = catsArray.tobytes()
    newFile = open("cat_skillMOD.cat_skill", "wb")
    newFile.write(conv)
    newFile.close()
    print ("\ncat_skillMOD.cat_skill 已保存!  \n如果不知道如何处理该文件，请输入 \"delp\"。\n")
    
#disable everything but booster
def allDsab():
    catsArray[82:86] = 0 ; catsArray[162:166] = 0 ; catsArray[178:182] = 0 ; catsArray[242:246] = 0 ; 
    catsArray[258:262] = 0 ; catsArray[274:278] = 0 ; catsArray[290:294] = 0 ; catsArray[306:310] = 0 ; 
    catsArray[354:358] = 0 ; catsArray[370:374] = 0 ; catsArray[386:390] = 0 ; catsArray[402:406] = 0 ; 
    catsArray[434:438] = 0 ; catsArray[450:454] = 0 ; catsArray[466:470] = 0 ; catsArray[546:550] = 0 ; 
    catsArray[578:582] = 0 ; catsArray[626:630] = 0 ; catsArray[674:678] = 0 ; catsArray[690:694] = 0 ; 
    catsArray[706:710] = 0 ; catsArray[722:726] = 0 ; catsArray[738:742] = 0 ; catsArray[754:758] = 0 ; 
    catsArray[770:774] = 0 ; catsArray[882:886] = 0 ; catsArray[898:902] = 0 ; catsArray[914:918] = 0 ;
    catsArray[642:646] = 255
    print ("\n已禁用：除了 \"猫的短期催眠术\" 之外的全部每日技能\n")
    global totalfood
    totalfood = 1
    
#enable everything
def allEnab():
    catsArray[82:86] = 255 ; catsArray[162:166] = 255 ; catsArray[178:182] = 255 ; catsArray[242:246] = 255 ; 
    catsArray[258:262] = 255 ; catsArray[274:278] = 255 ; catsArray[290:294] = 255 ; catsArray[306:310] = 255 ; 
    catsArray[354:358] = 255 ; catsArray[370:374] = 255 ; catsArray[386:390] = 255 ; catsArray[402:406] = 255 ; 
    catsArray[434:438] = 255 ; catsArray[450:454] = 255 ; catsArray[466:470] = 255 ; catsArray[546:550] = 255 ; 
    catsArray[578:582] = 255 ; catsArray[626:630] = 255 ; catsArray[674:678] = 255 ; catsArray[690:694] = 255 ; 
    catsArray[706:710] = 255 ; catsArray[722:726] = 255 ; catsArray[738:742] = 255 ; catsArray[754:758] = 255 ; 
    catsArray[770:774] = 255 ; catsArray[882:886] = 255 ; catsArray[898:902] = 255 ; catsArray[914:918] = 255 ;
    catsArray[642:646] = 255
    print ("\n已启用：全部的每日技能\n")
    global totalfood
    totalfood = 29
    
print ("\n欢迎使用 Daily Food Skills Utility\n")
commands()
input("请按下 \"回车键\" 开始\n\n>")
checkFood()

#take inputs and run linked function
waiting = input(">")
while waiting != "exit":
    if waiting == "help":
        commands()
    elif waiting == "delp":
        detailedHelp()
    elif waiting == "food":
        checkFood()
    elif waiting == "save":
        saveFood()
    elif waiting == "bout":
        authHelp()
    elif waiting == "dall":
        allDsab()
    elif waiting == "eall":
        allEnab()
    elif waiting == "":
        activeSkills = 1
    #check number input and toggle skill
    elif (waiting) in str(skillnum):
        holdSkill = (skillnum.index(int(waiting)))
        if catsArray[foodStarts[holdSkill]] == 255:
            if totalfood != 1:
                catsArray[foodStarts[holdSkill]:foodEnds[holdSkill]] = 0
                totalfood -= 1 ; activeSkills = 1
                print ("\n" + foodSkills[holdSkill] + " 现在为 " + isActive[1] + "\n")
        else: 
            catsArray[foodStarts[holdSkill]:foodEnds[holdSkill]] = 255
            totalfood += 1 ; activeSkills = 1
            print ("\n" + foodSkills[holdSkill] + " 现在为 " + isActive[0] + "\n")
        if activeSkills == 0:
            print (errorList[0] + "\n")
    else: print (errorList[1] + "\n")
    activeSkills = 0
    waiting = input(">")

raise SystemExit()



    
    