label ch21_y_end:
    jump ch1_y_end

label ch22_y_end:
    stop music fadeout 2.0
    call showpoem (poem_y22, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s") from _call_showpoem_1
    y 2q "Ahaha..."
    y "Ý nghĩa của bài thơ này là gì thì cũng đâu có quan trọng."
    y "Nó khó hiểu thế này là do gần đây đầu óc mình có hơi bị tăng động ấy mà, thậm chí mình còn phải dùng đến bút của cậu để 'giải toả'."
    y 2o "Ấy chết--"
    y 2q "Cây bút...là-là cậu làm rơi hôm qua, mình tính sẽ đem trả cậu nhưng, ư..."
    y "Mình, ờm..."
    y 2y6 "Mình chỉ là...do rất thích...nét viết...của nó."
    y "Thế nên mình đã viết...bài thơ này...bằng cây bút mà mình đã dùng để..."
    y "Và bây giờ thì cậu đang chạm vào nó..."
    y 2y5 "Ahaha."
    y 3p "K-Không phải mình có vấn đề gì đâu!!"
    y 3o "Mình vừa mới nói ra..."
    y "..."
    y 4c "...Hãy coi như từ nãy đến giờ chúng ta chưa có nói gì với nhau hết nhé?"
    y "Bài thơ thì cậu cứ giữ..."
    return
label ch23_y_end:
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem (poem_y23, track="bgm/5_yuri2.ogg", revert_music=False, paper="images/bg/poem_y2.jpg", img="yuri eyes", where=truecenter) from _call_showpoem_2
    y "Cậu có thích nó không??"
    y "Bài thơ này là dành tặng cho cậu đấy!"
    $ gtext = glitchtext(80)
    show yuri 1b at i11
    y "Nếu cậu còn chưa nhận ra thì mình xin phép nói luôn, bài thơ này viết về [gtext]"
    y 1y6 "Và điều đặc biết nhất là nó đã được thấm đẫm mùi hương của mình."
    y "Cậu thấy mình có chu đáo không nào?"
    play sound "sfx/glitch2.ogg"
    show yuri glitch
    pause 0.2
    stop sound
    show yuri 3y2
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    y "..."
    y 4d "Mình..."
    y "Cảm thấy...buồn nôn."
    show yuri at lhide
    hide yuri
    pause 1.0
    return
label ch21_n_end:
    jump ch1_n_end
label ch22_n_end:
    if n_appeal >= 2:
        jump ch22_n_end2
    else:
        call showpoem (poem_n2) from _call_showpoem_3
        n 2a "Không đến nỗi nào, phải không?"
        mc "Lần này mình viết dài hơn rồi đấy."
        n 2w "Bài thơ hôm qua quá ngắn..."
        n "Nhưng mà bài đó chỉ là để khởi động thôi nhé!"
        n 2c "Chứ đừng có cậu tưởng là bài đó tôi bí nên mới ngắn thế."
        mc "Không, không có chuyện đó đâu..."
        n 2a "À mà thông điệp trong bài thơ này quá là rõ ràng rồi đấy nhé."
        n "Tôi chả cần phải giải thích nữa đâu nhỉ."
        n 2g "Ai cũng có thể hiểu được chủ đề bài này viết về những kẻ khốn nạn..."
        n "Đã là con người thì làm gì có ai không có một sở thích kì cục nào đấy."
        n 5q "Nếu để lộ cho mọi người biết thì thể nào cũng có kẻ đem chuyện đó ra để chọc ghẹo."
        n 1e "...Đó, thấy mấy cái đứa chỉ giỏi hóng hớt như thế có ngu xuẩn không!"
        n "Người ta thích gì mà chả được, miễn sao không gây ảnh hưởng tới ai thì việc gì bọn nó phải chõ mũi vào?"
        n 1q "Bất cứ ai cũng đều phải học cách tôn trọng người khác, dù cho sở thích của họ có ra sao..."
        n 1x "...Chẳng hạn như hai đứa con gái trong câu lạc bộ này mà hiện giờ do tôn trọng họ nên tôi không muốn nêu tên."
        n 1s "Mỉa mai thay khi nơi duy nhất mình có thể thấy thoải mái thì lại có những kẻ như vậy..."
        n 1u "...Trời ạ, vì phải giải thích cho cậu hiểu nên tự dưng tôi lại cằn nhằn như này!"
        "{i}(...Mình có làm gì đâu?){/i}"
        mc "Mình vẫn luôn tôn trọng cậu mà..."
        n 1h "Ừm--"
        n "Cảm ơn..."
        n 1s "...Nhưng rõ ràng là cậu 'tôn trọng' Yuri hơn, nên..."
        n 42c "Mà thôi kệ, sao cũng được... Chia sẻ thơ xong rồi đấy, cậu muốn đi đâu thì đi đi."
    return
label ch22_n_end2:
    call showpoem (poem_n2b, revert_music=False) from _call_showpoem_4
    $ style.say_dialogue = style.edited
    n 1g "[player]..."
    n "Sao hôm nay không lại đọc truyện với tôi nữa vậy?"
    n 1m "Khiến tôi phải đợi cậu."
    n "Đợi dài cả cổ ra luôn."
    n "Tôi cất công tới đây chỉ để đọc truyện với cậu thôi đấy."
    n "Vậy mà cậu nỡ phản bội lại sự tin tưởng của tôi vậy á?"
    n "Cậu thích Yuri đúng không?"
    n 1k "Tốt nhất là đừng có dây dưa với con đấy."
    n "Cậu có nghe không hả?"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    n ghost1 "Yuri là một đứa bệnh hoạn."
    n "Lẽ ra tới giờ cậu phải biết rõ điều đó rồi chứ?"
    n "Từ nay hãy chơi với tôi đây này."
    n "Nhé?"
    n "Cậu không có ghét tôi đấy chứ [player]?"
    n "Cậu có ghét tôi không?"
    show natsuki_ghost_blood zorder 3
    n "Cậu muốn tôi ức phát khóc đấy à?"
    n "Câu lạc bộ này là chốn duy nhất tôi tìm được sự yên bình."
    n "Đừng phá hỏng nó mà."
    n "Đừng phá hỏng nó."
    n "Tôi xin cậu."
    n "Tránh xa Yuri ra đi."
    n "Chơi với tôi đây này."
    n "Tôi không muốn mất tất cả..."
    n "Chơi với tôi đi mà."
    stop music
    hide n_rects_ghost3
    n ghost2 "CHƠI VỚI TÔI MAU!!!"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    pause 0.5
    show end:
        xzoom -1
    with dissolve_cg
    pause 2.0
    scene black
    with None
    $ quick_menu = True
    return
label ch23_n_end:
    $ natsuki_23 = True
    $ style.say_dialogue = style.normal
    call showpoem (poem_n23, revert_music=False) from _call_showpoem_5
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    stop music
    hide screen tear
    show natsuki ghost_base
    n "Tôi đổi ý rồi."
    n "Quên hết những gì cậu vừa đọc đi."
    n "Có làm gì nữa thì kết quả vẫn vậy mà thôi."
    n "Yuri khó ưa tới vậy là lỗi của chính cậu ta."
    n "Cậu nghe rõ chưa hả, [player]?"
    n "Hãy dành thời gian cho Monika là các vấn đề hiện nay sẽ tan biến hết."
    n "Yuri và tôi đều không hề xứng với cậu."
    n "Từ giờ hãy để tâm tới Monika đi."
    n "Chỉ Monika mà thôi."
    hide natsuki
    $ style.say_dialogue = style.edited
    "Just Monika."
    menu:
        "Just Monika."
        "Just Monika.":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "Just Monika.", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "Chỉ Monika mà thôi." with Dissolve(0.5, alpha=True)
    pause 1.0
    play music t5
    $ skip_transition = True

    return

label ch21_m_end:
    call showpoem (poem_m21) from _call_showpoem_6
    jump ch1_m_end2
label ch22_m_end:
    call showpoem (poem_m22, revert_music=False) from _call_showpoem_7
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    pause 2
    show screen tear(20, 0.3, 0.3, 0, 40)
    pause 0.5
    hide screen tear
    play music t5c
    m 5 "Xin lỗi nhé, nó hơi bị trừu tượng quá phải không?"
    m "Mình đang muốn nhắn nhủ...um..."
    m 1r "Mà, thôi kệ."
    m "Giải thích cũng chả ích gì."
    m 1i "Dù sao thì..."
    m 3b "Nghe Mẹo viết thơ hôm nay của Monika này!"
    m "Đôi lúc cậu sẽ gặp vài quyết định khó khăn..."
    m "Khi đó, nhớ lưu trò chơi lại!"
    m 3k "Cậu không bao giờ biết được...um..."
    m 3i "...Xin hỏi là mình đang nói chuyện với ai vậy?"
    m "Cậu có nghe mình nói gì không?"
    m 3g "Nói gì đó báo cho mình biết là cậu đang lắng nghe đi."
    m "Nói gì cũng được."
    $ renpy.call_screen("dialog", "Làm ơn hãy giúp mình.", ok_action=Return())
    m 3k "...Đó là Mẹo viết thơ của ngày hôm nay!"
    m "Cảm ơn vì đã lắng nghe nhé~"
    return
label ch23_m_end:
    $ quick_menu = False
    window hide
    play sound page_turn
    show paper_glitch zorder 10 with Dissolve(1)
    play music g2
    if renpy.windows and renpy.game.preferences.fullscreen:
        $ mouse_visible = False
        scene bsod
        pause 3.0
    else:
        show black zorder 1
        pause 2.0
    window show(None)
    show monika 1d zorder 11 at i11
    $ quick_menu = True
    $ mouse_visible = True
    m "Ý trời! Giật cả mình!{fast}"
    window auto
    m "Um..."
    m 1m "À thì, bài thơ mình làm có vài, uh... lỗi."
    m "Mình muốn nói rằng..."
    m 1i "...Thôi không có gì đâu."
    m "Cứ tiếp tục đi nào..."
    stop music
    return


label ch21_n_bad:
    jump ch1_n_bad

label ch21_n_med:
    jump ch1_n_med

label ch21_n_good:
    jump ch1_n_good

label ch22_n_bad:

    if n_poemappeal[0] < 0:
        n 1r "..."
        n "Ừm, đúng như tôi nghĩ..."
        mc "...?"
        n 2w "[player], quá đủ rồi đấy."
        n "Cậu tưởng tôi ngu lắm à."
        n 2h "Rõ ràng gần đây cậu luôn dành thời gian bên cạnh Yuri..."
        n "Có mù cũng biết được rằng cậu đang cố tạo ấn tượng với cậu ta hơn là cải thiện trình độ làm thơ của bản thân."
        n 2w "Nói thẳng ra thì, thật là đáng thương hại."
        n 4h "Cậu gia nhập cậu lạc bộ này để làm cái quái gì cơ chứ hả, [player]?"
        n "Thiệt tình luôn..."
        n "Tôi cứ nghĩ là có thêm thành viên sẽ giúp mọi người gắn kết hơn."
        n 4s "Chứ không phải ngày một xa cách hơn như thế này."
        n 1u "Ý tưởng chia sẻ thơ này ngay từ đầu nghe đã ngu xuẩn rồi..."
        n 12c "...Thấy rồi đấy, hiện giờ tôi không có vui vẻ để mà tiếp chuyện cậu đâu."
        n "Xin cậu biến ra chỗ khác giùm."
        $ skip_poem = True
        return
    else:


        n 1k "...Hm."
        n "Tôi thích bài thơ trước của cậu hơn."
        mc "Eh? Thật sao?"
        n 2c "Có vẻ ở bài này cậu hơi mạo hiểm quá."
        n "Cậu chưa đạt đến trình độ có thể dùng được lối viết thơ như này đâu, đọc thật là thiếu chiều sâu."
        mc "Có vẻ là thế thật, nhưng tự dưng mình có hứng muốn thử."
        mc "Mình sẽ cố gắng cải thiện."
        jump ch22_n_med_shared2

label ch22_n_med:

    if n_poemappeal[0] < 0:
        n "...Hm."
        n 2k "Ừ thì, phải công nhận là cậu đã tiến bộ hơn lần trước."
        n "Cũng mừng khi thấy cậu đã có chút nỗ lực."
        mc "Ngon rồi..."
        label ch22_n_med_shared:
            n 2c "Hãy cố tìm lấy cảm hứng từ mọi người trong câu lạc bộ."
            n "Có vẻ trong thơ cậu đã có chút đụng chạm tới trường phái của Yuri, đúng không?"
            n 5q "Rõ ràng tôi biết là..."
            n "Dạo này cậu dành nhiều thời gian bên cạnh cậu ta..."
            n 1w "Nhưng nói cậu nghe này, Monika và tôi cũng không hề kém cạnh đâu nhé!"
            n 1q "Ở-ở khoản làm thơ ấy!"
            n 1h "Thế nên cậu vẫn còn phải cố gắng hơn, nếu không sẽ chẳng khá lên được!"
            n "Đây, bài thơ tôi viết..."
            n "Chắc chắn đọc xong cậu sẽ ngộ ra được nhiều thứ."
            return


    elif n_poemappeal[0] == 0:
        n "...Hm."
        n 2k "Có vẻ cũng chỉ xêm xêm như bài trước."
        n "Không hay mà cũng không bị dở lắm."
        mc "Phew..."
        n 2c "Hả? Gì mà như trút bỏ được gánh nặng thế hả?"
        mc "Ah... Thì chỉ cần không bị cậu mắng vì viết dở là quá thành công rồi."
        mc "Nhận xét của cậu đúng là có ích quá đi mất thôi."
        n 1p "N-này! Sao lại--"
        n 1q "{i}(Khoan đã, hình như hắn vừa khen mình à...?){/i}"
        n 4y "A-Ahaha! Có kẻ nhận ra được sự vĩ đại của bổn cô nương rồi đấy!"
        n "Thôi, cứ chăm chỉ đi, biết đâu được có ngày cậu sẽ giỏi như tôi đây!"
        mc "À...ừ..."
        "Natsuki hiểu sai bét ý cái lời khen đểu của tôi rồi."
        jump ch22_n_med_shared
    else:


        n "...Hm."
        n 2c "Thì cũng không đến nỗi nào."
        n "Nhưng khá là thất vọng nếu so sánh với bài thơ lần trước."
        n 2s "Nói vậy thôi chứ nếu bài nào cậu cũng viết hay như thế thì chắc tôi phát điên lên mất."
        mc "Ừ thì lần này mình muốn đổi mới phong cách một chút cho biết thôi mà."
        label ch22_n_med_shared2:
            n 2c "Cũng hợp lý thôi. Cậu mới viết lách lần đầu thì làm sao đã tìm ra phong cách riêng nhanh thế được."
            n "Nhìn mà xem, mỗi người trong câu lạc bộ đều có cách viết khác nhau..."
            n "Chắc cậu sẽ lấy được cảm hứng từ ai đó ở đây."
            n 2q "Chẳng hạn như..."
            n 5q "Hôm nay, tôi thấy cậu dành thời gian ở bên Yuri ..."
            n "Nói thế không có nghĩa là tôi thèm để tâm tới việc cậu làm gì đâu nhé."
            n 5w "Chỉ muốn nhắc nhở là cậu đừng có mong chờ sự giúp đỡ của bất kỳ ai."
            n 5s "Tôi cũng chả muốn đâu nhé."
            n 5h "Nhưng mà, hãy đọc thơ của tôi đi..."
            n "Chắc chắn cậu sẽ học được nhiều điều từ bài này."
            return

label ch23_n_bad:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        n 5x "Tôi không muốn đọc bài thơ cậu dùng để tán Yuri đâu."
        n 5s "Nhưng thơ của tôi thì cậu vẫn phải đọc."
        n "Có lý do đấy."
        n 5x "Chứ thật ra thì tôi còn chả muốn nói chuyện với cậu..."
        n "Tại vì không còn lựa chọn nào khác nên mới phải vậy thôi."
        n 5h "Nhớ... đọc cho kĩ đó, nghe chưa?"
        n "Xong rồi cậu thích đi đâu thì đi."
        return

    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."
        n 2c "...Meh."
        n "Lần này cậu vẫn chả khá hơn được tẹo nào."
        n "Thế mà tôi lại trông đợi sự tiến bộ của cậu cơ đấy."
        label ch23_n_bad_shared:
            n 42c "Cái thứ này rõ ràng là bị chi phối bởi phong cách của Yuri..."
            n "Tại sao cậu lại dễ bị lôi kéo thế nhỉ."
            n "Suốt ngày cứ cặp kè bên cậu ta..."
            n "Bây giờ thì cố viết thơ y hệt cậu ta..."
            n 1s "Thật là ngu xuẩn."
            n "Ít ra vẫn có Monika tôn trọng cách viết thơ của tôi..."
            n 1r "...Ugh."
            n 1q "Thôi kệ đi...tuy cậu chả chịu học hỏi gì nhưng cứ đọc thơ của tôi đây."
            n "Thật chả muốn làm chuyện này một tí nào."
            n "Nhưng chả còn lựa chọn nào khác nên đành vậy thôi."
            n 1h "Nhớ... đọc cho kĩ đó, nghe chưa?"
            n "Xong rồi cậu thích đi đâu thì đi."
            return
    else:

        n "..."
        n 2r "Ôi trời."
        n "Sao tự dưng lại thụt lùi như này."
        mc "Ể?"
        n 2c "Hai bài trước rõ ràng khá hơn thế này nhiều."
        jump ch23_n_bad_shared

label ch23_n_med:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch23_n_bad
    elif n_poemappeal[1] < 0:
        n "..."
        n 2k "...Chỉ tạm được thôi."
        mc "Tạm được?"
        n "Ừ, ít ra cũng khá hơn hôm qua."
        label ch23_n_shared:
            n 2c "Cậu đang thể hiện khá tốt, nhưng tôi vẫn chưa thấy rõ được sự đam mê văn học ở cậu."
            n 4r "Cậu suốt ngày kè kè bên Yuri..."
            n 4h "Nhưng ít ra thì ở cái hoạt động chia sẻ thơ này có cả câu lạc bộ cùng tham gia."
            n 4w "Hãy cố gắng nỗ lực hơn nữa vì mọi người!"
            n "À mà..."
            n 1h "Tuy chắc là tôi không thể sánh được với hội trưởng hay là hội phó..."
            n "Nhưng thơ của tôi không tệ lắm đâu nhé, nghe chưa?"
            n 1q "Thế nên là cứ đọc đi."
            n "Chỉ nói cho cậu biết..."
            n 1h "Bài thơ này... rất quan trọng với tối."
            n "Thế nên cậu phải đọc chăm chú vào nhé?"
            return
    else:
        n "..."
        n 2k "...Bài này tạm được."
        mc "Tạm được?"
        n "Thì vậy đó."
        n "Cũng chỉ tàm tạm như bài hôm qua."
        jump ch23_n_shared

label ch23_n_ygave:
    n 1h "Cái gì cơ?"
    n "Cậu tặng Yuri bài thơ của cậu mất rồi á?"
    n 4x "Gớm quá đi mất!"
    n "Hai người có bình thường không đấy?"
    n 1s "Hmph..."
    n "Dù sao thì tôi cũng chả thèm đọc nó đâu."
    n 1r "Chỉ thấy bực mình vì đây là hoạt động chia sẻ thơ mà cậu lại coi thường tôi đến vậy, không cho tôi đọc bài cậu viết."
    n 1x "...Ugh."
    n 1q "Thôi kệ đi...Cứ đọc thơ của tôi này."
    n "Dù chả muốn tí nào."
    n "Nhưng tôi chẳng còn lựa chọn nào khác."
    n 1h "Nhớ... đọc cho kĩ đó, nghe chưa?"
    n "Xong rồi thì thích đi đâu cứ đi."
    return

label ch23_n_good:
    jump ch23_n_med

label ch21_y_bad:
    jump ch1_y_bad

label ch21_y_med:
    jump ch1_y_med

label ch21_y_good:
    jump ch1_y_good

label ch22_y_bad:
    jump ch22_y_med

label ch22_y_med:
    y 2b "Mãi mới được đọc thơ cậu..."
    y "Thật nóng lòng muốn biết bài thơ hôm nay như thế nào."
    y 3m "..."
    "Yuri mỉm cười và hít một hơi thật sâu."
    y "Mình muốn để nó ngấm."
    mc "...?"
    y 3p "À, ý mình là--"
    y "Bài thơ cũng khá đó chứ!"
    y 3o "Nó, ừm..."
    y 2q "...Thì, vẫn còn nhiều chỗ cậu có thể cải thiện..."
    y "Nhưng cũng chả nghiêm trọng lắm đâu."
    y 2s "Mình có cảm giác như bất cứ thứ gì được viết bởi cậu đều có thể xem như tuyệt phẩm."
    y 2d "Ahaha..."
    y 2o "Nghe có vẻ hơi kì cục nhỉ..."
    y "T-thôi tiếp nào..."
    y 2t "Đây là bài thơ của mình."
    y "Cậu cứ nhận xét thẳng thắn..."
    return


label ch22_y_good:

    if y_poemappeal[0] < 1:
        y 2b "Mãi mới được đọc thơ cậu..."
        y "Thật nóng lòng muốn biết bài thơ hôm nay như thế nào."
        y 2e "..."
        y "......"
        "Yuri nhìn chằm chằm bài thơ với vẻ mặt hết sức ngạc nhiên."
        mc "Cậu có... thích nó không?"
        y "[player]..."
        y "...Sao cậu lĩnh hội được nhanh đến vậy?"
        label ch22_y_good_shared:
            y 2v "Mình chỉ mới giới thiệu với cậu lối viết thơ này vào hôm qua thôi mà..."
            mc "Thì đấy là lí do đấy..."
            mc "Những lời khuyên của cậu đã tiếp cho mình niềm cảm hứng."
            mc "Vậy nên mình đã thử lồng ghép những hình ảnh trừu tượng vào trong thơ."
            show yuri 4b zorder 2 at t11
            "Yuri sốc không nói nên lời."
            "Tay thì ướt đẫm mồ hôi rồi kìa."
            y 4e "A-Ah..."
            y "N-nghe thế mình vui lắm..."
            y 3y5 "Biết được rằng lời nói của mình truyền cảm hứng nhiều tới thế cho cậu thật là tốt quá đi thôi!"
            y "Những gì cậu viết đối với mình đều là tuyệt phẩm."
            y 3m "Chỉ cầm tờ giấy này thôi mà tim mình đã đập thình thịch rồi..."
            y 3q "Ahaha..."
            y "Mình muốn viết ngay một bài thơ về cảm xúc này..."
            y 3y6 "Như vậy có kì dị lắm không hả, [player]?"
            y "Trông mình lúc này vẫn bình thường chứ?"
            y 3s "C-Càng ngày việc kiểm soát cảm xúc càng trở nên khó khăn..."
            y 3m "Ôi, xấu hổ quá đi mất!"
            y 3y6 "À mà đọc bài thơ mà mình đã viết bằng cả tấm lòng đi này."
            y 3y5 "Cậu cầm lấy."
            return
    else:

        y 2b "Mãi mới được đọc thơ cậu..."
        y "Thật nóng lòng muốn biết bài thơ hôm nay như thế nào."
        y 2e "..."
        y "......"
        "Yuri nhìn chằm chằm bài thơ với vẻ mặt hết sức ngạc nhiên."
        mc "Cậu có... thích nó không?"
        y "[player]..."
        y 2t "Bài này còn hay hơn cả bài thơ hôm qua nữa..."
        y "...Sao cậu lĩnh hội được nhanh đến vậy?"
        jump ch22_y_good_shared

label ch23_y_bad:
    jump ch23_y_good

label ch23_y_med:
    jump ch23_y_good

label ch23_y_good:
    y 1d "Mãi mới tới..."
    y 3y5 "Ahaha..."
    show yuri 3m
    "Yuri cầm bài thơ của tôi đưa lên mặt và hít một hơi thật sâu."
    y 3y6 "Yêu quá đi thôi."
    y "Mình yêu mọi thứ trong thơ của cậu."
    y 3y5 "[player], cho phép mình mang nó về nhà nhé."
    y "Hãy cho mình giữ nó đi mà."
    y "Làm ơn đấy."
    mc "Được thôi, mình thấy không vấn đề gì..."
    y 2y5 "Ahaha."
    y "Cậu tốt bụng quá, [player]..."
    y "Mình chưa bao giờ gặp được ai tốt với mình như cậu cả."
    y 2y6 "Mình thấy sung sướng tới mức chết luôn được mất..."
    y 3y5 "K-không hẳn đến thế, nhưng--!"
    y "Không biết phải dùng từ gì mới mô tả được cảm xúc của mình lúc này."
    y "Cứ chìm đắm vào nó như thế liệu có sao không nhỉ?"
    show yuri:
        "yuri 3y4"
        0.4
        "yuri 3y6"
    y "Chắc là không có sao đâu, phải không?"
    "Yuri ghì chặt bài thơ vào ngực."
    y 3m "Nhất định khi về nhà nó sẽ phải theo mình vào tận phòng."
    y "Cậu thấy vui khi cho mình giữ nó phải không?"
    $ style.say_dialogue = style.normal
    y 3y5 "Đừng lo, mình sẽ giữ gìn nó cẩn thận!"
    $ style.say_dialogue = style.edited
    y 3y6 "Không thể để bài thơ này bám bụi được, mình sẽ đọc đi đọc lại nó mỗi lần thủ dâm."
    $ _history_list.pop()
    y "Mình sẽ dùng nó để tự cứa vào da thịt, để cho mùi của cậu trên trang giấy thấm vào từng giọt máu chảy trong huyết quản!"
    $ _history_list.pop()
    y 3y1 "Ahahahahaha."
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    y 2s "Cậu cũng được nhận bài thơ của mình luôn nè."
    y "Đằng nào thì sau khi đọc xong cậu cũng nhất định sẽ muốn giữ nó luôn."
    y 2y6 "Đây, cầm lấy ngay đi. Mình không thể kiên nhẫn hơn được nữa."
    y 2y5 "Mau lên! Mau đọc nó đi nào!"
    $ y_gave = True
    return


label ch21_m_start:
    m 1b "Chào cậu, [player]!"
    m "Hôm nay sao rồi, có vui không?"
    mc "Ah...cũng vui."
    m 1k "Vậy thì tốt quá! Đây đúng là tin mừng!"
    m 4a "Tiện thể đây, do cậu là thành viên mới của câu lạc bộ..."
    m "Nếu cậu có gợi ý gì để giúp bọn mình cải thiện hơn, ví dụ như là tổ chức hoạt động mới..."
    m 4b "Hãy nhớ là mình luôn sẵn sàng lắng nghe."
    m "Đừng ngại nói ra, nhé?"
    show monika 4a
    mc "Được thôi... mình sẽ nói với cậu nếu có ý tưởng nào đó."
    "Đương nhiên là tôi ngại phải đóng góp ý kiến rồi."
    "Tôi thích cứ đồng ý theo ý kiến của mọi người cho tới khi đã thân quen hơn."
    m 1a "Mà..."
    m "Cậu muốn chia sẻ thơ với mình chứ?"
    mc "Tuy có hơi xấu hổ chút nhưng chắc cũng không trốn đi đâu được."
    m 5a "Ahahaha!"
    m "Cậu đừng lo quá, [player]!"
    m "Tất cả chúng ta đều hơi ngại về việc này mà?"
    m "Nhưng nó là một rào cản không sớm thì muộn chúng ta phải vượt qua."
    mc "À, đúng là vậy nhỉ."
    "Tôi đưa tờ giấy cho Monika."
    m 2a "...Mhm!"
    $ nextscene = "m2_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_1

    m 1a "Tới lượt cậu, cậu muốn đọc thơ của mình chứ?"
    m 1e "Đừng lo, cũng không khá lắm đâu..."
    mc "Chỉ riêng thần thái tự tin của cậu mà bảo không giỏi thì chả ai tin đâu."
    m 1j "Ừm...đó là vì mình bắt buộc lúc nào cũng phải giữ phong thái như thế."
    m 1b "Nhưng đâu có nghĩa là lúc nào cũng phải tự tin đâu?"
    mc "Vậy à..."
    mc "Để mình đọc thử xem nào."
    return

label ch22_m_start:
    if y_appeal < 2:
        m 1b "À, chào cậu, [player]!"
        m "Vụ viết thơ ra sao rồi?"
        mc "Mình nghĩ chắc cũng tạm..."
        m 2k "Thế là chấp nhận được rồi."
        m 2b "Miễn sao cậu không thụt lùi là tốt!"
        m 2a "Mình cũng thấy mừng khi cậu có tinh thần tự giác cao đến thế."
        m "Có lẽ nay mai cậu lại viết nên tuyệt tác thì sao!"
        mc "Ahaha, đừng trông chờ vào mình quá..."
        m 2a "Biết đâu được!"
        m "Thế cậu có muốn cho mình đọc bài thơ hôm nay của cậu không?"
        mc "À... Đây này."
        "Tôi đưa tờ giấy cho Monika."
        m "..."
        m "...Hmm!"
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_2

    m 1a "À thì..."
    m "Cậu muốn đọc thơ của mình chứ?"
    m "Mình khá hài lòng với nó, hy vọng cậu cũng thế~"
    return

label ch23_m_start:
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_3
    if y_appeal < 3:
        m 1a "Mà..."
        if y_gave:
            m 1m "Chắc bài thơ của cậu thành dĩ vãng rồi..."
            m "Đáng lẽ ra Yuri cũng phải để cậu đem cho mọi người đọc trước rồi hẵng độc chiếm nó chứ."
            m 1r "...Thôi, sao cũng được."
            m "Nếu cậu ta thấy vui thì mình cũng không muốn cản."
            m 1a "Còn về phần mình thì..."
        m 1e "Mình đã dành rất... rất nhiều tâm huyết vào bài thơ này, nên..."
        m "Mình hy vọng nó sẽ, ừm, hiệu nghiệm."
        m 1r "Cậu đọc đi này..."
        $ persistent.seen_colors_poem = True
    return



label m2_natsuki_1:
    m 2b "Mình thích nó đấy, [player]!"
    mc "Thật hả...?"
    m 2e "Mình không hề nghĩ là cậu lại thích kiểu thơ dễ thương đến nhường này."
    m 2k "Ahahaha!"
    mc "Ối trời..."
    m 1b "Ây dà!"
    m "Nó làm mình liên tưởng đến kiểu thơ mà Natsuki hay viết."
    m "Mà cậu ta cũng là một nhà thơ khá đấy."
    m 5a "Thế nên cậu hãy coi đây như là một lời khen đi!"
    mc "Ahaha..."
    mc "Nếu cậu đã bảo thế."
    m "À phải rồi!"
    m 3b "Nếu cậu có hứng thú với Natsuki thì hãy nhớ luôn mang đồ ăn vặt bên mình."
    m "Cậu ấy sẽ bám lấy cậu như một chú cún con."
    m 3k "Ahaha!"
    m 1a "Bố của Natsuki thường không cho cậu ấy tiền ăn trưa hay là cho phép trữ đồ ăn trong nhà, nên tâm trạng cậu ấy lúc nào cũng dễ nóng nảy..."
    m "Đôi khi còn tới mức cậu ta kiệt sức và hoàn toàn ngưng hoạt động."
    m "Như hồi nãy chẳng hạn."
    m 2d "Chỉ là đoán mò thôi nhưng hình như cậu ấy bé tẹo như thế chắc do thiếu dinh dưỡng trong giai đoạn dậy thì..."
    m 2b "...Nhưng, cũng có nhiều chàng trai có hứng thú với mấy cô bé nhỏ nhắn xinh xinh thế mà, phải không?"
    m 5a "Xin lỗi... mình chỉ muốn đùa chút cho không khí vui vẻ hơn thôi!"

    return

label m2_yuri_1:
    m 1a "Tuyệt vời quá, [player]!"
    m "Mình vừa đọc vừa phải thán phục trong đầu đấy."
    m 1j "Sử dụng rất thành thạo những biện pháp nghệ thuật như là ẩn dụ!"
    m 1a "Mình không ngờ là người mới bắt đầu lại có thể viết được bài thơ sâu sắc như này đâu."
    m 3b "Chắc mình đã đánh giá thấp cậu rồi!"
    mc "Nếu mọi người kì vọng thấp thì sẽ ít áp lực đặt lên mình hơn."
    mc "Nhờ thế nên dù nỗ lực mình bỏ ra có là bao nhiêu thì mọi người cũng trân trọng."
    m 5a "Ahaha! Ăn gian ghê!"
    m "Dù sao thì cậu cũng đã thành công rồi đấy."
    m 2a "Cậu biết là Yuri rất thích phong cách này chứ?"
    m "Kiểu viết chứa đầy ẩn dụ và tượng trưng ấy."
    m 2d "Nhiều lúc mình có cảm tưởng như đầu óc Yuri không hề ở đây mà hoàn toàn tách biệt ra khỏi thực tại."
    m "Cũng không biết như thế là tốt hay xấu nữa."
    m 2a "Thậm chí còn có vẻ như cậu ấy muốn xa lánh mọi người."
    m "Lúc nào cũng lạc trôi trong khoảng trời của riêng bản thân trong trí tưởng tượng..."
    m 2b "Nhưng đó cũng là lí do Yuri vui tới thế khi cậu đối tốt với cậu ta."
    m "Mình không nghĩ cậu ấy quen với cảm giác được người khác lấy làm khuôn mẫu phấn đấu chút nào."
    m 2j "Đói khát giao tiếp xã hội đã lâu, nên mình cũng không ngạc nhiên nếu cậu ta phản ứng hơi thái quá."
    m 2d "Như lúc nãy..."
    m "Theo mình quan sát, nếu Yuri trở nên quá khích, cậu ấy sẽ thu mình lại và dành thời gian một mình suy ngẫm."
    "Đột nhiên, cánh cửa bật tung ra."
    m 2b "Yuri!"
    show monika 2a
    show yuri 1s zorder 3 at f31
    y "Tớ về rồi đây..."
    y "Tớ có lỡ mất chuyện gì không?"
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "Cũng không hẳn..."
    m "Vậy là tất cả nọi người đã chia sẻ thơ cho nhau rồi."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 2t "Ủa?"
    y "Xong hết rồi sao?"
    y 2v "T-tớ xin lỗi vì tới muộn..."
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2j "Không cần phải xin lỗi đâu!"
    m 2a "Chúng ta vẫn còn nhiều thời gian mà, nên cậu đừng bận tâm về khoảng thời gian cậu đi làm việc riêng."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 1s "Được rồi..."
    y "Cảm ơn cậu, Monika."
    y "Để tớ đi lấy bài thơ của mình."
    show yuri zorder 1 at thide
    hide yuri
    $ y_ranaway = False
    return

label m2_yuri_2:
    m 1i "[player], mình nghĩ cậu vừa thấy cái gì đó mà cậu không nên thấy."
    m "Mình không muốn phải nói cho cậu biết nhưng đến nước này rồi thì đành vậy."
    m 1r "Cậu đang càng ngày tiến gần tới nguy hiểm hơn khi cậu dành nhiều thời gian ở bên Yuri."
    m 1i "Mình không biết tại sao nhưng Yuri có vẻ rất dễ kích động khi ở bên cậu..."
    m 3d "Đáng lẽ chuyện đó không thành vấn đề đâu...."
    m "Nhưng mỗi khi Yuri quá khích, cậu ấy lại trốn vào một góc nào đấy và tự dùng dao cứa vào bản thân."
    m 2e "Nghe thật bệnh hoạn đúng không?"
    m "Thậm chí mỗi ngày cậu ấy còn mang một cái khác nhau tới trường, như thể có cả một bộ sưu tập dao hay sao ấy..."
    m 2d "Mình nghĩ, cậu ta làm vậy không phải do buồn bã hay gì đâu!"
    m "Có vẻ như việc đó đem lại cho cậu ta sự khoái cảm."
    m 2m "Cứ như thể là kiểu...khổ dâm..."
    m 1i "Nhưng điểm mấu chốt ở đây là, cậu như kiểu chất xúc tác cho cậu ta làm vậy."
    m 1d "Mình không đổ lỗi cho cậu đâu nhé."
    m 1a "Lý do mình nói cho cậu biết là để cậu hiểu rằng..."
    m "Cậu phải giữ khoảng cách với Yuri, đấy cũng giúp đỡ cậu ta ngưng việc tự làm hại bản thân."
    m 5 "Và... đừng ngần ngại dành thời gian ở bên mình nhiều hơn."
    m "Ít ra đầu óc mình cũng bình thường... và mình biết phải đối xử với các thành viên câu lạc bộ ra sao cho đúng mực."
    return

label m2_yuri_3:
    stop music
    m 1i "Đừng có nói là mình chưa cảnh báo cậu nhé, [player]."
    $ skip_poem = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
