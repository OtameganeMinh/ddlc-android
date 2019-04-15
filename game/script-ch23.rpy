image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        pause 7
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11

    y "Chào cậu, [player]!"

    y "Mình đang chờ cậu đấy."

    y 2d "Cùng đọc sách với mình nhé?"

    y "Hôm nay mình đã mang theo một loại trà rất đặc biệt --"
    show yuri 2f
    show natsuki 4w zorder 3 at f33

    n "Monika!"

    n "Mình đã bảo cậu là đừng có mà--"

    n 1g "Trời ạ..."

    n "Cậu ấy lại đi trễ nữa à?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32

    y 1h "Vẫn gây ô nhiễm tiếng ồn như mọi khi, đúng là Natsuki."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33

    n 4c "Cậu nói cái gì cơ?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32

    y 1r "Tại sao lúc quái nào cậu cũng ngắt lời tớ bằng cách hét ầm lên như vậy?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33

    n 1o "Cậu muốn thế nào đây?!"

    n "Cậu nói như thể lúc nào tớ cũng làm vậy với cậu ấy."

    n "Tớ xin lỗi, được chưa? Vừa rồi là do tớ không tập trung thôi."

    n 4u "Thiệt tình...Dạo này cậu bị làm sao thế?"
    if n_appeal >= 2:

        n "Ê này..."

        n "Về chuyện ngày hôm qua."

        n 2q "Lúc đó tớ đã rất là thô lỗ..."

        n 1q "Chắc tại tớ bị căng thẳng hay gì đó."

        n 1h "Nhưng tớ hiểu nhiệm vụ cùng nhau xây dựng câu lạc bộ."

        n 1q "Một thành viên mới nữa thì cũng chẳng sao..."


        n 5w "Tớ đã hy vọng người mới cũng là con gái thì tốt hơn..."

        n 5u "Nên..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal

        y 2u "Natsuki này..."
        $ style.say_dialogue = style.edited

        y 1f "Chả ai quan tâm đâu."

        y "Sao cậu không đi làm mấy việc vớ vẩn như là tìm tiền xu dưới máy bán hàng tự động đi?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33

        n 1p "--!"

        n 1r "..."

        n 12f "..."
        show natsuki at thide
        hide natsuki
        pause 1.0
        show monika 1g at l31

        m "Ôi trời ạ..."

        m "Mình lại là người đến muộn nhất!"
        show yuri zorder 3 at f32

        y 1f "Cậu lại tập piano nữa à?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31

        m 5a "Ừ..."

        m "Ahaha..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32

        y 1m "Phải nói rằng cậu rất là quyết tâm đấy."

        y "Tự thành lập được một câu lạc bộ này, lại còn tập chơi piano nữa..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31

        m 1a "Theo mình nghĩ thì đó không phải là sự quyết tâm..."

        m 3a "Mà là niềm đam mê mãnh liệt."

        m "Nó cũng chính là động lực giúp tớ hướng đến lễ hội trường nữa."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32

        y 2n "Tớ á?"

        y 2o "C-Chẳng sao cả..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33

        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32

        y 2v "Thực sự là tệ lắm à...?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33

        n 2m "Chuẩn rồi đấy, {i}rất là{/i} tệ."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32

        y 3p "Tớ sẽ cố gắng!"

        y 3y6 "Không cần phải bận tâm lắm về tớ đâu..."

        y 3o "Dạo gần đây tớ cảm thấy có gì đó hơi kì lạ một chút..."

        y 3n "N-Nhưng đó chỉ là chuyện nhỏ thôi, không cần bận tâm đâu!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33

        n 2q "Có vẻ vậy nhưng tớ không thể không chú ý được."

        n 5q "Không phải là tớ quan tâm đến cậu hay gì đâu nhé..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31

        m "Ôi trời ạ..."

        m "Mình lại là người đến muộn nhất!"
        show natsuki zorder 3 at f33

        n 2c "À, [player] cũng chỉ vừa mới đến thôi."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32

        y 1f "Cậu lại tập piano nữa à?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31

        m 5a "Ừ..."

        m "Ahaha..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32

        y 1m "Phải nói rằng cậu rất là quyết tâm đấy."

        y "Tự thành lập câu lạc bộ này, lại còn tập chơi piano nữa..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31

        m 1a "Theo tớ nghĩ thì đó không phải là sự quyết tâm..."

        m 3a "Mà là niềm đam mê mãnh liệt."

        m "Nó cũng chính là động lực giúp mình hướng đến lễ hội..."

        m 3n "À..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33

        n 5s "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31

        m 1l "Nhắc mới nhớ..."

        m "T-Tớ quên khuấy đi mất..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32

        y 2v "Ưm, về chuyện đó, Natsuki này..."

        y "Bọn tớ đã bàn hôm qua rồi, và..."

        y 2t "Quyết định rằng sẽ tham gia vào lễ hội trường."

        y 2l "Tuy nhiên...!"

        y 2h "Tớ hiểu rất rõ quan điểm của cậu không muốn câu lạc bộ thay đổi."

        y "Tớ nghĩ mọi người cũng phần nào muốn thế."

        y 2f "Nhưng miễn là chúng ta vẫn bên nhau thì câu lạc bộ có thay đổi như nào cũng không sao."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33

        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32

        y 2v "Um, với lại..."

        y "Nếu cậu giúp bọn tớ trong lễ hội này..."

        y 3r "...Tớ sẽ mua tặng cậu một quyển manga mới toanh!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33

        n 5h "..."

        n 2z "Ahahaha!"

        n "Xin lỗi, tại câu cuối cậu nói buồn cười quá đi mất."

        n 2c "Ê này..."

        n "Về chuyện ngày hôm qua."

        n 2q "Tớ đã rất là thô lỗ..."

        n 1q "Chắc tớ bị căng thẳng hay gì đó."

        n 1h "Nhưng tớ hiểu nhiệm vụ cùng nhau xây dựng câu lạc bộ."

        n 1q "Một thành viên mới nữa thì cũng chả sao..."

        n 5w "Và tớ hy vọng người mới là con gái thì tốt hơn..."

        n 5e "...Nhưng vấn đề quan trọng hơn là cái sự kiện này sẽ thật là ngu xuẩn nếu không có tớ trong đó!"

        n "Tớ là dân chuyên nghiệp đấy nhé!"

        n 5c "Nếu có tớ giúp đỡ, nhất định các cậu sẽ ổn thôi."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32

        y 2s "Ôi, thế thì tuyệt vời quá..."

        y "Thật là hay phải không, Monika?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33

        n 2k "...Monika?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31

        m "Ah--"

        m 1n "Ừ, đúng là hay thật!"

        m "Nó sẽ chẳng như mọi khi nếu thiếu cậu được, Natsuki à."

    m 5 "Với cả, [player] này..."

    m "Cậu muốn làm gì hôm nay nào?"

    m "Hay là chúng ta có thể--"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32

    y 1l "Bọn tớ đều đã quyết định làm gì hôm nay rồi."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31

    m 1r "Ah..."

    m "Thật vậy hả, Yuri?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32

    y 1y6 "Ừ đúng vậy."

    y "[player] rất thích cuốn tiểu thuyết mà bọn tớ đang đọc chung."

    y 1y5 "Là trưởng nhóm chắc cậu thấy mừng vì thành viên mới bắt đầu có hứng thú với văn học phải không Monika?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31

    m 2l "Tớ..."

    m "Tớ đoán..."

    m "Chỉ là--"

    m 1r "Mà thôi, không có gì đâu."

    m 1i "Đúng là chả có gì."

    m "Các cậu cứ làm những gì mình muốn đi."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32

    y 2y1 "{i}(Có thế chứ!){/i}{w=0.5}{nw}"

    y 2u "Ưm... Cảm ơn cậu vì đã hiểu điều đó, Monkia à."
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2])
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3

    m "Được rồi, mọi người!"

    m "Đã đến lúc chúng mình lên kế hoạch cho lễ hội rồi đó."

    m 1i "Mau lại đây nào."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31

        n "Trời ạ..."

        n "Sao không khí hôm nay kì lạ thế nhỉ?"

        n "Xem này, ngay đến cả Yuri trầm lặng mọi ngày cũng đã phải lên tiếng."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33

    y "Uu..."

    y "Không khí ngột ngạt như này có vẻ như là báo hiệu cho điều gì đó tồi tệ sắp xảy ra thì phải..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32

    m 2r "Thôi nào, mau chóng làm việc cho xong đi?"

    m 2d "Tớ sẽ đi in và phân phát tờ rơi."
    if n_appeal >= 2:

        m 2i "Natsuki, cậu có thể đi làm bánh nướng."

        m "Chắc cậu giỏi được mỗi việc đấy."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31

        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:

        m "Natski, để xem tớ nên giao cho cậu--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31

        n 2d "Tớ muốn làm bánh nướng!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32

        m 2a "...Đúng rồi, tớ cũng đang nghĩ đến nó."

        m "Thật mừng là chúng ta tâm đầu ý hợp."

    m 1m "Yuri này, cậu có thể..."

    m 1r "...À thì, chả quan trọng lắm."

    m 1i "Cứ làm những gì cậu thích, miễn là cậu thấy nó giúp ích là được."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33

    y 2h "Monika này..."

    y "Tớ không có vô dụng như cậu nghĩ đâu nhé!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32

    m 2p "T-Tớ đâu có nghĩ cậu như vậy!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33

    y 1l "Tớ biết rõ mình cần phải làm những gì mà."

    y 1h "Phải có bầu không khí đặc biệt để tức cảnh sinh tình, không thể tổ chức về thơ thành công mà thiếu nó được."

    y "Vì thế tớ sẽ đi làm những đồ trang trí mà có thể giúp tâm trạng mọi người thoải mái."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32

    m 2j "Ồ, không ngờ đấy?"

    m "Đó là một ý tưởng rất là tuyệt vời!"

    m 1a "Vậy là tất cả mọi người đều đã có công việc để làm."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33

    y 2f "Hả?"

    y "Thế còn [player] thì sao?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32

    m 2b "[player] sẽ giúp tớ."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31

    n 4e "Khoan đã, cậu á?"

    n "Công việc của cậu nhẹ nhàng nhất mà, Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32

    m 1i "Xin lỗi nhưng các cậu phải tuân theo sự phân công của hội trưởng."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31

    n 1f "Quỷ tha ma bắt!"

    n "Thực sự là cậu đang toan tính điều gì?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33

    y 3h "T-Tớ hoàn toàn đồng ý với Natsuki!"

    y "Công việc của cậu rõ ràng chỉ cần một người làm là đủ..."

    y 3l "Việc của tớ nặng nhọc hơn nhiều, tớ cần có người giúp."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31

    n 4c "Cả tớ nữa!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33

    y 1h "Gì cơ, mấy cái bánh nướng của cậu á?"

    y "Đừng có chọc cười tớ chứ."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31

    n 1o "{i}Cậu{/i} thì biết cái quái gì!"

    n 1x "Cậu chỉ quan tâm đến việc giữ chân [player] ở bên cạnh và đọc những thứ sách ngu xuẩn."

    n 1f "Cậu {i}và{/i} Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32

    m 2g "Này!"

    m "Tớ đã làm gì các cậu!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31

    n 3e "Được rồi, thế thì sao cậu không để [player] tự quyết định sẽ giúp ai thay vì lợi dụng quyền hạn của mình?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32

    m 1p "Tớ không hề...lạm dụng quyền hạn."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33

    y 2h "Đúng là cậu đã làm vậy, Monika à."

    y "Hãy để cho [player] tự chọn lấy, thế là ổn chưa?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32

    m 1r "Thôi được rồi, được rồi!"

    m "Cứ theo ý các cậu đi."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31

    n 3w "Thật là..."

    n "[player], tôi biết là cậu cũng thấy chán hai người này lắm rồi."

    n 3c "Thế nên là chúng mình--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33

    y 2r "Natsuki, câm con mẹ miệng lại và để cậu ta tự chọn lấy."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31

    n 1o "{i}Mày{/i} mới là đứa nên ngậm mõm vào đấy!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32

    m 1r "Ôi trời đất ơi..."

    m 1i "Cứ tiếp tục thế này chả giải quyết việc gì cả. Hãy chọn mau lên nhé?"
    show monika zorder 2 at t32
    python:
        madechoice = renpy.display_menu([("Natsuki.", "natsuki"), ("Yuri.", "yuri"), ("Monika.", "monika")], screen="rigged_choice")

    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        pause 3.0
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri


    m 5a "Yay, vậy là cậu chọn tớ!"

    m "Chúng ta có thể gặp nhau tại nhà cậu vào cuối tuần này."

    m "Mình hứa rằng nó sẽ cực kì vui luôn."

    m "Liệu chủ nhật cậu không bận gì chứ?"
    show natsuki 1e zorder 3 at f31

    n "Xàm vãi."

    n "Chả công bằng tí nào cả!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32

    m 2i "Rất là công bằng rồi mà, Natsuki."

    m "Chính cậu ấy chọn như vậy."
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33

    y "Không đúng, chả có tí công bằng nào hết!"

    y "Cậu dám để bọn tớ làm hết mọi việc một mình và rồi cướp lấy [player] cho riêng cậu sao?"

    y "Thật là tởm lợm!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32

    m 2r "Yuri, mình chả hề giao cho cậu công việc nào cả."

    m 2i "Cậu là người tự quyết định làm."

    m "Ai mới là người đang tỏ ra vô lý ở đây?"
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33

    y 2y4 "Mình mà vô lý á?"

    y 2y3 "Ahahaha!"

    y "Monika, tôi chẳng thể tin nổi rằng cậu lại hoang đường và ảo tưởng đến thế!"

    y "Lúc nào cũng kéo [player] tránh xa khỏi tôi mỗi khi cậu không được ở cạnh cậu ta ấy hả."

    y 1y1 "Cậu đang ghen sao?"

    y "Hay là bị điên?"

    y 1y3 "Chắc là bản thân cậu kinh tởm đến mức chính cậu còn chả thể chịu nổi nên mới khó ở như thế?"

    y 1y4 "Tôi có ý này. Sao cậu không chết quách luôn đi cho rồi?"

    y "Cực kì có lợi cho tinh thần cậu luôn đấy."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31

    n 5u "Yuri, cậu đang khiến tớ thấy hơi sợ đấy.."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32

    m 1r "Natsuki, cứ mặc cậu ấy đi."

    m 1i "Cậu ta chẳng hề muốn chúng ta ở đây."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33

    y 2y3 "Đó, cậu hiểu vấn đề rồi đấy."

    y "Tất cả những gì tôi muốn là một chút thời gian bên cạnh cậu ấy."

    y "Đòi hỏi thế là nhiều quá à?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft

    "Yuri theo sau Monika và Natsuki ra ngoài cửa."
    show monika 5a zorder 2 at t11

    m "Này, [player]..."

    m "Yuri quả thật là khác người, nhỉ?"
    show monika zorder 1 at thide
    hide monika

    "Monika cười khúc khích trong khi bị Yuri đẩy ra khỏi cửa."
    python:
        # try: renpy.file(config.basedir + "/have a nice weekend!")  # TO!DONE: new persistent fix, see #2
        # except: open(config.basedir + "/have a nice weekend!", "w").write("G2pilVJccjJiQZ1poiM3iYZhj3I0IRbvj3wxomnoeOatVHUxZ2ozGKJgjXMzj2LgoOitBOM1dSDzHMatdRpmQZpidNehG29mkTxwmDJbGJxsjnVeQT9mTPSwSAOwnuWhSE50ByMpcuJoqGstJOCxqHCtdvG3HJV0TOGuwOIyoOGhwOHgm2GhlZpyISJik3J/")
        # try: os.remove(config.basedir + "/hxppy thxughts.png")
        # except: pass
        # try: os.remove(config.basedir + "/CAN YOU HEAR ME.txt")
        # except: pass
        # try: os.remove(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
        # except: pass
        if persistent.have_a_nice_weekend is None:
            persistent.have_a_nice_weekend = "G2pilVJccjJiQZ1poiM3iYZhj3I0IRbvj3wxomnoeOatVHUxZ2ozGKJgjXMzj2LgoOitBOM1dSDzHMatdRpmQZpidNehG29mkTxwmDJbGJxsjnVeQT9mTPSwSAOwnuWhSE50ByMpcuJoqGstJOCxqHCtdvG3HJV0TOGuwOIyoOGhwOHgm2GhlZpyISJik3J/"
        persistent.hxppy = None
        persistent.can_you_hear_me = None
        persistent.iii = None

    play music t10y
    show yuri 2m zorder 2 at t11

    y "Cuối cùng."

    y 2y1 "Cuối cùng thì!"

    y 2s "Ôi trời ơi, đây chính là những gì mà mình muốn."

    y 1y6 "[player] này, cậu đừng có tốn thời gian cuối tuần này với Monika."

    y "Đừng có nghe lời cậu ta."

    y 1y5 "Hãy đến nhà mình đi."

    y 3y5 "Nguyên cả một ngày, chỉ có hai ta bên nhau mà thôi..."

    y "Nghe có tuyệt vời không cơ chứ?"

    y 3y1 "Ahahaha!"

    y 3y4 "Wow... Thực sự đúng là mình có gì đó không ổn phải không?"

    y "Nhưng mà cậu nghe này."

    y 1y3 "Mình không quan tâm đến chuyện đó nữa."

    y "Cả đời mình chưa bao giờ cảm thấy phấn khích như bây giờ cả."

    y 1y4 "Chỉ cần bên cạnh cậu còn hơn cả những niềm khoái lạc mạnh mẽ nhất mà mình có thể tưởng tượng ra."

    y "Mình đã nghiện cậu mất rồi."

    y 3y4 "Không được hít thở chung một bầu không khí với cậu thì quá là ngang với án tử hình."

    y 4a "Mình quan tâm tới cậu nhiều lắm đó biết không, như thế không tốt sao?"

    y "Cậu có một người sẵn sàng ở bên cậu suốt cả cuộc đời này đấy nhé."

    y 2y6 "Nhưng tuy nó tuyệt vời như vậy..."

    y 2y4 "Mà tại sao mình cứ có cảm giác sẽ có chuyện kinh khủng sắp sửa xảy ra nhỉ?"

    y 2y6 "Có lẽ đó là lí do mình đã cố gắng kìm nén bản thân lúc đầu..."

    y "Nhưng mà giờ cảm xúc này thật mãnh liệt quá mức rồi."

    y 3y1 "Mình không quan tâm nữa đâu, [player]!"

    y "Mình phải nói với cậu thôi!"

    y 3y4 "Rằng...mình yêu cậu điên cuồng!"

    y "Cứ như thể là từng tế bào...từng giọt máu trong cơ thể mình...đang gào thét tên cậu vậy."

    y 3y3 "Mặc kệ hậu quả có ra sao đi nữa!"

    y "Mặc kệ Monika có đang nghe hay không!"

    y 3w "Làm ơn, [player], hãy hiểu rằng mình yêu cậu đến nhường nào."

    y 3m "Mình yêu cậu đến nỗi cây bút mình lấy trộm của cậu cũng dùng được để thủ dâm."

    y 3y4 "Yêu đến mức muốn lột da cậu ra và chui vào trong cơ thể cậu."

    y 3y6 "Mình muốn tất cả mọi thứ của cậu thuộc về mình."

    y "Và mình chỉ thuộc về cậu mà thôi."

    y "Thật hoàn hảo phải không?"

    y 3s "Hãy nói cho mình biết đi, [player]."

    y "Hãy nói rằng cậu muốn trở thành người yêu của mình."

    y "Cậu có chấp nhận lời tỏ tình của mình không?"

    menu:
        "Có.":
            jump yuri_kill
        "Không.":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    pause 1.0


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11

    y "...Ahahaha."

    y "Ahahahahahaha!"
    $ style.say_dialogue = style.normal

    y 3y5 "Ahahahahahahahaha!"
    $ style.say_dialogue = style.edited

    y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 2.0

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    python:
        _history_list = []
        m.add_history(None, "", """Chào mừng đến với câu lạc bộ văn học! Đây luôn luôn là giấc mơ đặc biệt để mình làm những gì đấy với điều mình yêu mến. Bây giờ cậu đã là thành viên câu lạc bộ, hãy giúp mình khiến mọi thứ trở thành hiện thực trong trò chơi dễ thương này nhé! Mỗi ngày đều có những cuộc trò chuyện và những hoạt động thú vị với các thành viên dễ thương và độc nhất của mình: Sayori - Một thành viên trẻ trung và năng động, luôn luôn tỏa sáng và tràn ngập hạnh phúc, Natsuki - Một cô gái dễ thương luôn giấu mình, Yuri - Một người nhút nhát và bí ẩn tìm thấy sự thoải mái trong thế giới sách. Và tất nhiên, hội trưởng câu lạc bộ! Chính là mình đây! Mình rất mừng khi mà cậu kết bạn với mọi thành viên và khiến cho họ trở nên thân thiết hơn. Nhưng mà giờ đây mình có thể nói rằng cậu là người yêu của mình - cậu hứa sẽ dành thời gian với mình chứ?Chào mừng đến với câu lạc bộ văn học! Đây luôn luôn là giấc mơ đặc biệt để mình làm những gì đấy với điều mình yêu mến. Bây giờ cậu đã là thành viên câu lạc bộ, hãy giúp mình khiến mọi thứ trở thành hiện thực trong trò chơi dễ thương này nhé! Mỗi ngày đều có những cuộc trò chuyện và những hoạt động thú vị với các thành viên dễ thương và độc nhất của mình: Sayori - Một thành viên trẻ trung và năng động, luôn luôn tỏa sáng và tràn ngập hạnh phúc, Natsuki - Một cô gái dễ thương luôn giấu mình, Yuri - Một người nhút nhát và bí ẩn tìm thấy sự thoải mái trong thế giới sách. Và tất nhiên, hội trưởng câu lạc bộ! Chính là mình đây! Mình rất mừng khi mà cậu kết bạn với mọi thành viên và khiến cho họ trở nên thân thiết hơn. Nhưng mà giờ đây mình có thể nói rằng cậu là người yêu của mình - cậu hứa sẽ dành thời gian với mình chứ?Chào mừng đến với câu lạc bộ văn học! Đây luôn luôn là giấc mơ đặc biệt để mình làm những gì đấy với điều mình yêu mến. Bây giờ cậu đã là thành viên câu lạc bộ, hãy giúp mình khiến mọi thứ trở thành hiện thực trong trò chơi dễ thương này nhé! Mỗi ngày đều có những cuộc trò chuyện và những hoạt động thú vị với các thành viên dễ thương và độc nhất của mình: Sayori - Một thành viên trẻ trung và năng động, luôn luôn tỏa sáng và tràn ngập hạnh phúc, Natsuki - Một cô gái dễ thương luôn giấu mình, Yuri - Một người nhút nhát và bí ẩn tìm thấy sự thoải mái trong thế giới sách. Và tất nhiên, hội trưởng câu lạc bộ! Chính là mình đây! Mình rất mừng khi mà cậu kết bạn với mọi thành viên và khiến cho họ trở nên thân thiết hơn. Nhưng mà giờ đây mình có thể nói rằng cậu là người yêu của mình - cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? cậu hứa sẽ dành thời gian với mình chứ? """)

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    python:
        persistent.have_a_nice_weekend = None
        #try: os.remove(config.basedir + "/have a nice weekend!")
        #except: pass
    $ persistent.autoload = "yuri_kill_3"
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto

    n "Hoan hô, lễ hội đến rồi đây!"
    show natsuki 4k zorder 2 at t11

    n "Wow, cậu đến sớm hơn cả tớ à?"

    n "Tớ cứ tưởng tớ đến sớm nhất c--{nw}"
    show natsuki scream at h11

    n "EYAH!"

    n "AAAAAAAAAAAAAAAHHHH!!!"
    pause 1.0
    show natsuki scream at h11
    pause 0.75
    show natsuki vomit at h11
    pause 1.25
    show natsuki at lhide
    hide natsuki

    "Natsuki chạy đi mất."

    show monika 2b
    m "..."
    show monika 2b zorder 2 at t11

    m "Mình tới rồi đây!"

    m 2d "[player] à, có chuyện gì vừa xảy ra thế?"

    m "Natsuki vừa chạy vụt qua mình..."

    m 2i "...Oh..."

    m "...Oh."

    m 2r "..."

    m 2l "Ahahaha!"

    m "Thật là thảm hại."

    m 2d "Khoan đã, đừng nói là cậu đã ở đây suốt cuối tuần nhé, [player]?"

    m "Ồ, ôi trời đất ơi.."

    m 2g "Đoạn mã này bị hỏng nặng hơn mình dự kiến."

    m "Xin lỗi cậu nhiều!"

    m "Ắt hẳn là cậu thấy chán lắm..."

    m 2e "Mình sẽ sửa lại ngay, bình tĩnh nhé?"

    m "Hãy đợi mình chút..."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    pause 1.0
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ delete_character("natsuki")
    pause 1.0

    m 2a "Gần xong rồi đó."

    m 2j "Tự dưng thèm ăn bánh nướng quá!"
    $ gtext = glitchtext(10)

    "Monika nhẹ nhàng lấy một chiếc bánh nướng từ khay của [gtext]."

    m 2b "Thực tình mà nói, bánh rất là ngon luôn ấy!"

    m "Nhưng mà tốt nhất là chỉ nên ăn một cái thôi, đây đã là lần cuối cùng mình có thể ăn nó rồi."

    m 2a "Cậu biết mà, trước khi bọn họ và mấy thứ này không còn tồn tại."

    m "...Mà thôi, mình không nên bắt cậu phải chờ đợi thêm nữa."

    m 2j "Cố chịu một chút nhé, sẽ ổn thôi mà?"

    m 2a "Mình hứa là sẽ chỉ mất vài giây thôi."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.full_restart(transition=None, label="splashscreen")

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
