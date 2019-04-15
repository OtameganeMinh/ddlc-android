image exception_bg = "#dadada"
image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full


    "Cuối cùng cũng đã đến ngày tổ chức lễ hội."

    "Tôi đã định đi bộ đến trường cùng Sayori như mọi ngày."

    "Nhưng Sayori không trả lời cuộc gọi của tôi."

    "Tôi tính là qua để đánh thức cậu ấy dậy, nhưng sau lại nghĩ rằng làm thế hơi quá đáng."

    "Hơn nữa tôi còn bận việc chuẩn bị cho lễ hội."
    if ch4_scene == "natsuki":

        "Tôi đã cẩn thận xếp chồng hai khay bánh lên nhau để mang được tất cả đi cùng lúc."

        "Natsuki liên tục nhắn tin cho tôi rồi, nhưng tôi đâu còn cánh tay nào để mà nhắn tin trả lời."
    else:

        "Tấm biểu ngữ Yuri và tôi vẽ đã khô, tôi nhẹ nhàng cuốn nó lại để đem theo bên mình."

        "Cậu ấy chỉ nhắn cho tôi một tin nhẹ nhàng nhắc nhở tôi đừng quên, tôi cũng nhắn lại để cậu ấy yên tâm."

    "Thật buồn cười là bây giờ tôi lại có cảm giác giống như Natsuki."

    "Tôi mong sự kiện kết thúc thật nhanh để tôi có thể dành thời gian với Sayori và [ch4_name] tại lễ hội."

    "Nhưng tôi cũng hiểu năng lực của Monika như nào, chắc chắn sự kiện ngâm thơ cũng sẽ rất tuyệt vời."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11

    m "[player]!"

    m "Cậu là người đầu tiên đến đó."

    m "Cậu hăng hái thế thì tốt thật!"

    mc "Lạ nhỉ, mình cứ nghĩ Yuri mới là người đầu tiên đến cơ."

    "Monika đang xếp mấy cuốn sách nhỏ trên mỗi bàn trong phòng học."

    "Chúng chắc hẳn là những tập thơ mà cậu ấy đã chuẩn bị cho bọn tôi."

    "Bài thơ mà tôi nộp cho Monika để cậu ấy cho vào tập thực ra chỉ là bài tôi lấy bừa trên mạng."

    "Hôm nay tôi sẽ phải đọc bài thơ đó."

    m 1d "Mình hơi bất ngờ vì cậu không đi cùng Sayori đấy."

    mc "Ừ, chắc cậu ta lại ngủ nướng nữa rồi..."

    mc "Nhỏ ngốc đó."

    mc "Hôm nay là ngày quan trọng cơ mà, cậu ấy phải cố gắng hơn chứ..."

    "Mồm nói thế, nhưng tôi lại chợt nhớ ra những gì Sayori đã nói hôm qua..."

    "Tự dưng tôi cảm thấy bản thân thật tệ khi nhớ ra rằng việc đến trường không hề đơn giản đối với Sayori."

    "Tôi lỡ mồm nói thế vì đó là kiểu suy nghĩ của tôi về Sayori từ suốt bao lâu nay."

    "Nhưng mà..."

    "Có lẽ tôi vẫn nên qua đánh thức cậu ấy dậy mới phải?"

    m 1k "Ahaha."

    m 4b "Cậu phải có tí trách nhiệm với cậu ta đi chứ, [player]!"

    m "Nhất là sau cái vụ hai cậu làm hôm qua..."

    m "Tinh thần cậu ấy đang bất ổn lắm, như đang treo lơ lửng không biết tựa vào đâu vậy."
    show monika 4a

    mc "Vụ hôm qua....?"

    mc "Monika-- Cậu biết chuyện đó à??"

    m 2a "Tất nhiên rồi."

    m "Dù gì thì mình cũng là hội trưởng mà."

    mc "Nhưng--!"

    "Tôi nói lắp bắp, tỏ vẻ ngượng ngùng."

    "Sayori đã kể lại cho cậu ấy nghe về chuyện đó nhanh thế à?"
    if sayori_confess:

        "Về chuyện...chúng tôi đã trở thành một cặp."

        "Tôi thì vẫn chưa hề có ý định kể cho ai biết hết..."
    else:

        "Về chuyện...tôi đã từ chối lời tỏ tình của cậu ấy."

        "Chuyện này...Monika nói nghe như thể tôi là kẻ xấu vậy..."

        "Nhưng chắc tôi vẫn là người bạn thân nhất của Sayori nhỉ?"

    mc "Trời ạ..."

    mc "Cậu không biết rõ được đầu đuôi câu chuyện đâu, thế nên là..."

    m 2j "Cậu khỏi phải lo chuyện đó."

    m "Những gì mình biết còn nhiều hơn cậu nghĩ đấy."

    mc "Hả...?"

    "Monika vẫn tỏ ra thân thiện như mọi khi, nhưng không hiểu sao tôi lại cảm thấy lạnh sống lưng sau khi nghe cậu ấy nói."

    m 5 "À này, cậu có muốn xem qua đống tờ rời không?"

    m "Mình nghĩ là chúng khá ổn!"

    mc "Ừ, chuyện đấy thì hiển nhiên rồi."

    "Tôi nhặt lấy một tờ nằm trên bàn."

    mc "À ờ thì, đúng là thế thật."

    mc "Nó nhất định sẽ giúp câu lạc bộ của chúng ta được đánh giá nghiêm túc hơn."

    m "Ừ, mình cũng nghĩ giống cậu!"
    show monika zorder 1 at thide
    hide monika

    "Tôi lật sang trang khác."

    "Bài thơ của mỗi thành viên được in một cách cẩn thận trên từng trang giấy nhìn chung trông khá chuyên nghiệp."

    "Tôi nhận ra bài thơ của Natsuki và Yuri vì tôi đã được nghe họ tập đọc."

    mc "Cái gì đây...?"

    "Tôi nhìn chỗ in bài thơ của Sayori."

    "Bài này khác hẳn với bài lúc cậu ấy tập đọc."

    "Tôi chưa hề đọc bài thơ này bao giờ..."
    call showpoem (poem_s3, music=False)

    mc "Ah--"

    "Cái quái gì thế này...?"

    "Khi đọc bài thơ, tôi cảm thấy chột dạ."
    show monika 1d zorder 2 at t11

    m "[player]?"

    m "Có chuyện gì à?"

    mc "À, không gì đâu..."

    "Bài thơ này trái ngược hoàn toàn với những gì Sayori từng viết."

    "Nhưng mà việc quan trọng bây giờ là..."

    mc "M-Mình đổi ý rồi!"

    mc "Mình sẽ đi đón Sayori, thế nhé..."

    m "Ah--"

    m 1b "Ừ thì, được thôi!"

    m "Đừng có đi lâu quá đấy nhé."
    scene bg corridor with wipeleft

    "Tôi nhanh chóng rời khỏi phòng học."

    m "Cậu cứ đi cẩn thận, không cần phải vội thế đâu~"

    "Monika gọi với theo tôi."

    "Tôi vẫn tiếp tục tăng tốc."

    scene bg residential_day with wipeleft_scene

    "Tôi đã nghĩ cái gì vậy?"

    "Lẽ ra tôi phải cố gắng hơn vì Sayori."

    "Gọi cậu ấy dậy hay là đợi cậu ấy để cùng đi đến trường có phải việc gì to tát đâu kia chứ."

    "Một việc đơn giản như thế có thể sẽ làm cậu ấy hạnh phúc mà."

    "Hơn nữa..."

    "Rõ ràng hôm qua tôi đã đảm bảo với cậu ấy rằng mọi chuyện vẫn sẽ như mọi ngày."

    "Lẽ ra tôi phải giữ lời hứa, cho cậu ấy thứ cậu ấy cần."

    scene bg house with wipeleft

    "Tôi đến trước nhà Sayori và gõ cửa."

    "Chẳng có tiếng trả lời, điện thoại cũng không bắt máy."

    "Như hôm qua, tôi lại tự mở cửa và đi vào nhà."
    scene black with wipeleft

    mc "Sayori?"

    "Ngủ nướng đến tận giờ được à..."

    "Tôi nuốt nước bọt."

    "Không thể tin được là cuối cùng mình lại phải làm thế này.."

    "Vào hẳn nhà Sayori để đánh thức cậu ấy..."
    if sayori_confess:

        "Chắc đây là việc mà một người bạn trai phải làm nhỉ?"
    else:

        "Tôi đâu phải bạn trai cậu ấy đâu mà phải làm việc này chứ?"

    "Dù sao đi nữa thì..."

    "Chắc chẳng có vấn đề gì đâu."


    "Tôi gõ cửa phòng Sayori.."

    mc "Sayori?"

    mc "Dậy đi chứ, cái đồ ngốc này..."

    "Vẫn không có phản hồi nào."

    "Tôi không thích tự ý vào phòng cậu ấy..."

    "Như thế là xâm phạm quyền riêng tư rồi còn gì?"

    "Nhưng tôi không còn lựa chọn nào khác cả."

    "Tôi mở cánh cửa phòng thật khẽ."

    mc "{cps=30}.......Sayo--{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    # At autoload, RenPy re-scans the entire script and somehow executes some expressions.
    # After commenting out this block, the game should be correctly re-loaded.
    #python:  # TO!DONE: finally fixes #1
    #    try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here's goes nothing.", False)
    #    except: pass
    pause 6.0



    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg

    "Cái quái gì...?"

    "{i}Cái quái gì thế này hả trời??{/i}"

    "Đây là một cơn ác mộng có phải không?"

    "Chắc chắn...là thế rồi."

    "Đây không thể nào là sự thật được."

    "Không đời nào chuyện này là sự thật được."

    "Sayori thật sẽ không bao giờ làm vậy."

    "Vài ngày trước mọi thứ vẫn bình thường cơ mà."

    "Cảnh tượng trước mắt tôi thực sự quá phi lý, tôi không thể tin được...!"
    scene black with dissolve_cg

    "Tôi cố kìm nén để không nôn ra."

    "Chỉ mới hôm qua..."

    "Tôi đã bảo Sayori rằng tôi sẽ luôn ở bên cạnh cậu ấy."

    "Tôi đã bảo rằng tôi biết điều gì là tốt nhất cho Sayori, và rằng mọi chuyện sẽ ổn thôi."

    "Thế thì tại sao...?"

    "Lý do gì mà cậu ấy phải làm thế này...?"

    "Sao tôi lại cảm thấy bất lực thế này?"

    "Tôi đã làm cái gì sai?"
    if sayori_confess:

        "Tỏ tình với cậu ấy...."

        "Lẽ ra tôi không được phép tỏ tình với cậu ấy."

        "Tôi cứ tưởng làm thế sẽ giúp được Sayori."

        "Nhưng rõ ràng là Sayori đã bảo rằng cậu ấy cảm thấy đau đớn khi có người quan tâm tới."

        "Vậy thì tại sao tôi lại vẫn đi tỏ tình với cậu ấy, khiến cho mọi việc càng tệ thêm?"
    else:

        "Từ chối lời tỏ tình của cậu ấy..."

        "Chắc hẳn đó là giọt nước tràn ly."

        "Tiếng la chất chứa đầy nỗi thống khổ của cậu ấy vẫn còn vang vọng bên tai tôi."

        "Tại sao tôi lại từ chối cậu ấy trong thời khắc cậu ấy cần tôi nhất?"

    "Sao tôi lại ích kỷ đến thế?"

    "Đây tất cả là lỗi tại tôi--!"

    "Những ân hận liên tục chạy qua đầu tôi để tôi tiếp tục dằn vặt, hành hạ bản thân mình hơn nữa."

    "Nếu tôi dành thêm thời gian với cậu ấy."

    "Đi cùng cậu ấy đến trường."
    if sayori_confess:

        "Và vẫn làm bạn với cậu ấy, giữ nguyên mọi thứ như trước đây..."
    else:

        "Và dành cho cậu ấy tình cảm nhiều hơn nữa, hơn cả tình bạn..."

    "...Thì chuyện này đã không xảy ra."

    "Rõ ràng tôi có thể ngăn được chuyện này mà!"

    "Quỷ tha ma bắt cái Câu lạc bộ Văn Học."

    "Đéo có hội hè gì hết."

    "Tôi vừa...mất đi người bạn thân nhất."

    "Chúng tôi đã lớn lên cạnh nhau."

    "Giờ cậu ấy đã đã vĩnh viễn ra đi rồi."

    "Tôi chẳng thể làm gì để mang cậu ấy trở về được cả."

    "Đây có phải trò chơi điện tử đâu để mà tôi có thể chơi lại từ đầu."

    "Tôi chỉ có duy nhất một cơ hội mà tôi lại làm hỏng rồi."

    "Và những ân hận đắng cay này sẽ đeo bám tôi cho tới tận lúc chết đi."

    "Không gì trong cái cuộc đời thảm hại của tôi có thể sánh với cậu ấy..."

    "Ấy thế mà tôi lại để cho cậu ấy chết trong đơn độc."

    "Kết thúc rồi..."

    "Tôi không bao giờ còn có thể nhìn thấy nụ cười ấy nữa."

    "Không bao giờ."

    "Không bao giờ."

    "Không bao giờ."

    "Không bao giờ."

    "Không bao giờ..."
    $ in_sayori_kill = False


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
