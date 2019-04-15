label ch10_main:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    s "[gtext]"
    $ s_name = glitchtext(12)

    "Từ phía xa, có một bạn nữ khá là phiền nhiễu đang vừa chạy về phía tôi vừa vẫy vẫy tay chào, như kiểu chẳng hề để tâm đến những ánh mắt chú ý của người đi đường."

    "Đó là [s_name], người bạn thân từ thuở nhỏ và cũng là hàng xóm của tôi luôn."

    "Người ta cứ hay tưởng là thời đại này không kiếm đâu ra kiểu tình bạn như thế nữa, nhưng vẫn đầy người có bạn quen từ rất lâu rồi đấy thôi."

    "Trước kia cả hai thường cùng nhau đi học, nhưng từ khi lên cao trung thì cô ấy bắt đầu ngủ nướng như cơm bữa khiến tôi muốn đợi cũng chẳng đợi nổi nữa luôn."

    "Nếu cứ bị rượt kiểu này, tôi thấy tốt nhất là mình nên chạy trước cho nhanh."

    "Biết là thế đấy, nhưng tôi chỉ thở dài và ngừng chân lại phía trước chỗ qua đường để cho [s_name] bắt kịp mình. "

    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ anticheat = persistent.anticheat

    jump ch20_from_ch10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
