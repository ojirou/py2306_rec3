import pyautogui as pgui
import time
import os
def main():
    hr= input('〇時間△分：　〇>> ')
#     hour=int(hr)
    mn= input('〇時間△分：　△>> ')
#     5分マージン
    margin=300
    seconds=3600*int(hr)+60*int(mn)+margin  
#     2時間55分/回*N > seconds となる最小N
    rec_cycle=seconds//10500+1
    print('繰り返し回数:', rec_cycle)
    print('マウスを録音停止ボタンに置いてクリック')
    dummy = input('>> ')
    PosStopRecord=pgui.position()
    print('マウスを録音開始ボタンに置いてクリック')
    dummy = input('>> ')
    PosStartRecord=pgui.position()
    print('マウスを30秒戻るボタンに置いてクリック')
    dummy = input('>> ')
    PosPlayback30s=pgui.position()
    x_stop=PosStopRecord[0]
    y_stop=PosStopRecord[1]
    x_start=PosStartRecord[0]
    y_start=PosStartRecord[1]
    x_playback=PosPlayback30s[0]
    y_playback=PosPlayback30s[1]
    for num in range(1, rec_cycle):
    #     〇時間△分：　〇＊3600+△＊60 s
    #     2時間55分：　10500 s
    #     2時間45分：　9900 s
    #     2時間30分：　9000 s
    #     2時間：　　　7200 s
    #     1時間：　　　3600 s
    # 30秒戻りを2回入れる    
        print(num,' cycle started.')
        time.sleep(10500)
    #     time.sleep(10)
        pgui.click(x=x_stop, y=y_stop, duration=0.5)
        time.sleep(50)
        pgui.click(x=x_playback, y=y_playback, duration=0.5)
        time.sleep(2)
        pgui.click(x=x_playback, y=y_playback, duration=0.5)
        time.sleep(2)
        pgui.click(x=x_start, y=y_start, duration=0.5)
        print(num,' cycle finished.')
if __name__ == "__main__":
    main()