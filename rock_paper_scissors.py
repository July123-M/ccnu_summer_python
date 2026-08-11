"""
石头剪刀布游戏 
"""

import random

def main():
    print("石头剪刀布游戏！")
    print("输入 石头 / 剪刀 / 布，输入 退出 结束游戏")
    print("-" * 30)
    
    while True:
        player = input("\n你出什么？")
        
        if player == "退出":
            print("游戏结束，再见！")
            break
        
        if player != "石头" and player != "剪刀" and player != "布":
            print("输入无效，请输入：石头/剪刀/布")
            continue
        
        # 电脑随机出拳
        computer = random.choice(["石头", "剪刀", "布"])
        print(f"电脑出了：{computer}")
        
        # 判断胜负
        if player == computer:
            print("平局！")
        elif player == "石头" and computer == "剪刀":
            print("你赢了！")
        elif player == "剪刀" and computer == "布":
            print("你赢了！")
        elif player == "布" and computer == "石头":
            print("你赢了！")
        else:
            print("你输了！")

if __name__ == "__main__":
    main()