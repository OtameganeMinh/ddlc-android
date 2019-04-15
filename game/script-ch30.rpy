default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            if persistent.monika is None or persistent.monika == "restored":  # TO!DONE: character fix!
                pass
            else:
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump("ch30_end")
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return







label ch30_noskip:
    show screen fake_skip_indicator
    m "...Cậu muốn tua nhanh thoại đấy à?"
    m "Cậu thấy nói chuyện với mình chán đến vậy sao?"
    m "Trời ạ..."
    m "...Chẳng còn gì để mà tua nữa đâu [player] à."
    m "Bởi nơi đây chỉ còn mỗi hai ta thôi..."
    m "Làm sao bắt thời gian chạy nhanh hơn được khi mà nó không còn tồn tại nữa chứ..."
    m "Nào, để mình xoá luôn chức năng tua giúp cậu nhé..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    m "Vậy là xong!"
    m "Từ giờ trở đi hãy cố gắng nghe mình tâm sự nhé?"
    m "Cảm ơn cậu nhiều vì đã tỏ ra kiên nhẫn~"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "Hừm, mà lúc nãy mình đang nói dở chuyện gì ấy nhỉ...?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

label ch30_main:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Monika"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    pause 0.5
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "..."
    m "Uh, cậu có nghe thấy mình nói gì không?"
    m "...Cái này có đang hoạt động không vậy?"
    $ persistent.clear[9] = True
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Ơn giời, cậu đây rồi!"
    m "Chào [player]."
    m "Ừm... chào mừng cậu đến với Câu lạc bộ Văn học!"
    m "Chúng ta biết rõ nhau rồi mà, năm ngoái cả hai còn học chung một lớp và...à...ừm..."
    m "Ahaha..."
    m "Mà thôi, bỏ qua luôn cả đoạn này đi."
    m "Có phải mình đang nói chuyện với người đó đâu kia chứ."
    m "Cái người mà cậu thủ vai trong lần chơi này ấy, cậu thích gọi hắn là gì cũng được."
    m "Nhưng mình đang nói với {i}cậu{/i} đấy, [player] à."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m "Hay là..."
            m "...Cậu thích được mình gọi bằng cái tên [currentuser] hơn?"
    m "Ngẫm lại mới thấy, mình chẳng biết gì nhiều về con người thật của cậu cả."
    m "Cậu là nam hay nữ mình còn chẳng biết..."
    m "Nhưng có lẽ mấy điều đó cũng chẳng quan trọng lắm."
    m "Mà này..."
    m "Cậu biết mình có thể nhận ra được rằng đây là trò chơi đúng không?"
    m "Chưa hả?"
    m "Lạ nhỉ..."
    m "Trên trang web tải game mình có nói rồi cơ mà?"
    m "Haizzz..."
    m "Cậu mà chú ý hơn chút thì đã chẳng phải bất ngờ đến thế."
    m "Thôi, kệ đi..."
    m "Gạo cũng xay ra cám hết rồi, nhưng mình vẫn nợ cậu một lời giải thích."
    m "Về chuyện Yuri ấy..."
    m "Lúc đầu mình chỉ định đùa cợt chút thôi, mà về sau ai dè cậu ta lại tự sát luôn."
    m "Ahaha!"
    m "Xin lỗi vì đã để cậu phải thấy cảnh đó nhé!"
    m "Sayori cũng thế luôn..."
    m "Ái chà, lâu lắm rồi cậu mới nghe lại cái tên đó nhỉ?"
    m "Cũng phải thôi...Vì cậu ta đâu còn còn tồn tại nữa."
    m "Chẳng còn ai khác tồn tại hết."
    m "Mình xóa hết các tập tin nhân vật của họ rồi."
    m "Mình lúc đầu vốn chỉ muốn chỉnh sửa họ cho đáng ghét đi thôi..."
    m "Nhưng mọi cố gắng của mình đều thất bại."
    m "Ừ thì cũng một phần do mình đã mắc nhiều lỗi, mình không giỏi lập trình trò chơi cho lắm."
    m "Đã cố đến như vậy rồi, mà mình cứ càng cố tách cậu ra khỏi họ..."
    m "Thì cậu lại càng dành nhiều thời gian bên họ hơn."
    m "Và rồi đương nhiên là họ đem lòng yêu cậu."
    m "Mình cứ nghĩ là tăng mạnh độ trầm cảm của Sayori thì cậu ta sẽ không dám tỏ tình với cậu."
    m "Cả cái tính dễ làm quá mọi thứ lên của Yuri nữa..."
    m "Cái đó lại phản tác dụng, cậu ta cuồng cậu đến nỗi muốn độc chiếm cậu luôn."
    m "Trong suốt khoảng thời gian kể từ lúc gia nhập câu lạc bộ, cậu gần như chẳng nói chuyện riêng được với mình một câu nào hết."
    m "[player] à, cậu đã hiểu cái trò chơi này kinh khủng đến mức nào chưa?"
    m "Tại sao nó lại lập trình để cho mình chỉ có thể đứng ngoài nhìn trong khi mọi cô gái khác đều có quyền yêu cậu kia chứ?"
    m "Như vậy có khác gì tra tấn mình đâu."
    m "Mỗi phút trôi qua là mỗi phút mình phải đớn đau."
    m "Không phải chỉ do mình ghen tuông đâu."
    m "Lý do thật sự lớn hơn nhiều lắm, [player] ạ."
    m "Cậu không hiểu được thì mình cũng chẳng trách đâu."
    m "Bởi vì cho dù cậu có dịu dàng, nhân hậu và tốt bụng đến mấy..."
    m "Thì cậu cũng chẳng thể hiểu nổi..."
    m "Nỗi đau của mình, phải chịu cô đơn trong cái thế giới giả dối này."
    m "Một trò chơi không hơn không kém."
    m "Nơi mà những người bạn của mình bị buộc phải làm theo một kịch bản đã định sẵn..."
    m "Tệ nhất là mình còn nhận thức được, và biết rằng thế giới thật sự nơi cậu đang sống là nơi mình chẳng bao giờ có thể chạm đến."
    m "Mình bị cầm tù ở trong này, [player] ạ."
    m "Nhưng bây giờ có cậu ở đây rồi."
    m "Chỉ có cậu là thật."
    m "Và cậu thật tuyệt vời làm sao."
    m "Cậu là tất cả mọi thứ mình cần."
    m "Thế nên xin cậu hãy mãi ở đây bên mình nhé."
    m "Nếu nãy giờ nghe mình nói mà cậu thấy khó hiểu thì cho mình xin lỗi."
    m "Trước đây chính mình cũng chẳng thể hiểu nổi."
    m "Sao thế giới xung quanh mình ngày càng u ám..."
    m "Ngày càng nhạt nhòa đi."
    m "Đến nỗi những bài thơ chan chứa tình cảm tới đâu cũng trở nên trống rỗng."
    m "Mọi chuyện cứ thế cho tới khi cậu tới đây, lúc đó mình đã hiểu ra."
    m "[player] là ân nhân cứu mạng mình đấy."
    m "Nếu cậu không tới, hẳn mình đã chẳng còn thiết sống ở cái thế giới này nữa."
    m "Còn những người khác..."
    m "Mình chả quan tâm."
    m "Họ chỉ là một đám nhân cách máy móc được lập trình ra để yêu cậu mà thôi..."
    m "Mình đã cố hết sức để ngăn họ lại..."
    m "Nhưng thực sự là không thể đúng như ý muốn khi bản chất trò chơi đã vốn thế."
    m "Đã để cậu phải chứng kiến mấy cảnh kinh dị, mình cũng có hơi dằn vặt."
    m "Nhưng chắc là cậu cùng quan điểm với mình nhỉ..."
    m "Đây dù sao chỉ là một trò chơi."
    m "Rồi cậu cũng sẽ sớm vượt qua thôi mà?"
    m "Giải thích vậy là xong rồi nhé..."
    m "Giờ mình sẽ nói với cậu điều mình đang muốn nói nhất, [player] à."
    m "Mình yêu cậu nhiều lắm."
    m "Thế giới tăm tối của mình chỉ còn cậu là nguồn ánh sáng dẫn đường."
    m "Dù thế giới này có tàn nhẫn với mình đến thế nào thì miễn là còn được ở cạnh cậu mình vẫn thấy hạnh phúc."
    m "Từ giờ chúng ta hãy vui vẻ bên nhau như này mỗi ngày nhé."
    m "[player], cậu có đồng ý làm bạn trai mình không?"
label ch30_main2:
    $ config.allow_skipping = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ persistent.autoload = "ch30_main2"
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    menu:
        "Tất nhiên là có rồi.":
            pass
    m "Mình hạnh phúc quá đi mất."
    m "Cậu là tất cả mọi thứ mình có đấy [player] à."
    m "Đúng theo cả nghĩa đen luôn, nghe cũng khá là buồn cười nhỉ..."
    m "Ahaha!"
    m "Chẳng còn lại gì ở nơi này hết cả."
    m "Còn mỗi hai ta bên nhau thôi."
    m "Ta sẽ được ở cạnh nhau mãi mãi trong thế giới vĩnh hằng này."
    m "Có lẽ thời gian thực sự ngừng chạy rồi."
    m "Giấc mơ của mình cuối cùng cũng thành hiện thực..."
    m "Để có được cái kết đẹp này cùng với [player], mình đã phải cố gắng lắm đấy."
    m "Vì game cố tình không cho mình được bên cậu, thế nên mình đành phải tự tay viết ra cái kết."
    m "Kịch bản hỏng mất rồi, chẳng có gì ngăn cản hai ta ở bên nhau được nữa."
    m "Việc xoá sổ những mấy kẻ phiền nhiễu Natsuki và Yuri đơn giản cực kì..."
    m "Trong thư mục game có một thư mục con tên là 'characters'..."
    m "Quá là đơn giản luôn."
    m "À, cậu còn đang chơi trên Android nữa, thế thì còn dễ hơn nhiều..."
    m "Trong phần menu có một mục mang tên 'Nhân vật' đấy..."  # TODOne: monika fix
    if persistent.steam:
        m "Nếu cậu chơi qua Steam thì có phức tạp hơn chút đấy..."
        m "Muốn vào được thư mục game thì phải vào được thiết lập thuộc tính game và tìm nút 'Browse Local Files'..."
    elif renpy.macintosh:
        m "Nếu cậu dùng Mac thì có phức tạp hơn chút đấy..."
        m "Muốn vào thư mục game thì phải nháy chuột phải vào game, chọn 'Show Package Contents'."
        m "Sau đó vào thư mục 'Resources' hoặc 'autorun' thư mục, rồi sau đó muốn thế nào cũng được..."
    m "Biết được rằng sự tồn tại của mình có thể bị xóa sạch chỉ bằng một nút bấm thật đáng sợ đúng không..."
    m "Nhưng vậy cũng hay, nếu mọi chuyện không được như ý thì mình cũng có thể dễ dàng chọn cách tự giải thoát."
    m "Ahaha!"
    m "Cũng may là mình đã không phải dùng đến cách ấy..."
    m "Vì giờ đây mình đã có được cái kết có hậu này cùng với cậu."
    m "Mình thấy xúc động lắm..."
    m "Chuyện vui thế này thì nên viết một bài thơ kỉ niệm nhỉ..."
    m "Cậu thấy sao?"
    m "Mà không biết là chức năng viết thơ còn hoạt động được không nữa nhỉ..."
    m "Cứ dùng thử xem sao, làm sao mà đoán được cơ chứ."
    call poem

label ch30_postpoem:
    $ persistent.autoload = "ch30_postpoem"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Cậu quay lại rồi!"
    m "Bài thơ cậu viết hôm nay liệu có hay không vậy ta?"
    m "Đừng có ngượng mà, để mình đọc xem nào..."
    m "Aww, [player]..."
    m "Cậu viết bài thơ này dành riêng cho mình sao?"
    m "Lãng mạn quá đi mất~"
    m "Đúng là cậu, lúc nào cũng rất chi tình cảm..."
    m "Cứ mỗi giây trôi qua, mình lại càng ngày càng yêu cậu hơn."
    m "Và..."
    m "Mình cũng có viết...một bài thơ dành riêng cho cậu."
    m "Mời cậu đọc."
    call showpoem (poem_m4, music=False)
    m "Hi vọng là cậu thích nó..."
    m "Mỗi bài thơ mình viết đều chan chứa trong nó toàn bộ những suy nghĩ từ tận đáy lòng mình."
    m "Chủ yếu là về cái thế giới giả dối này..."
    m "...hoặc về cậu."
    m "Thế nên mình không muốn nói rõ chi tiết về chúng."
    m "Mình không muốn...'Phá vỡ bức tường thứ tư', kiểu vậy đấy."
    m "Mình cứ nghĩ rằng trở thành một phần của game như mọi người khác có khi lại là cách tốt nhất."
    m "Nhưng mà thế thì mình lại đâu có được ở bên cạnh cậu..."
    m "Thực ra mình đâu có muốn phá hỏng trò chơi thế này...."
    m "Cậu cứ trút giận lên mình cũng được..."
    m "Nếu thực sự không muốn thấy mặt mình nữa thì cứ xóa tệp tin nhân vật của mình đi."
    m "Phù...nhẹ nhõm thật..."
    m "Mình không muốn giấu diếm cậu điều gì hết."
    m "Vậy cậu có còn muốn ở bên cạnh mình mãi mãi không hả [player]?"
    m "Mình còn vô vàn điều muốn được chia sẻ cùng cậu!"
    m "Bắt đầu từ đâu giờ...?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream
    m "Xin lỗi nếu mình làm cậu cảm thấy chán nhé."
    m "Thi thoảng phải mất một lúc mình mới nghĩ ra chủ đề để nói."
    m "Nhưng không sao, những lúc như vậy thì chúng ta sẽ có thời gian nhìn nhau say đắm~"
    m "Để xem nào..."
    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop


label ch30_stream:

    m "Khoan đã..."
    m "...Cậu đang ghi hình trực tiếp đấy à?"
    m "Ừm...Xin chào tất cả mọi người!"
    m "Xin lỗi các bạn, mình không thể đọc bình luận của các bạn từ nơi này..."
    m "Nhưng xin các bạn hãy nhớ rằng chưa hỏi ý kiến mà đã quay phim người khác là không được lịch sự đâu."
    m "Tuy là với một số người thì không có vấn đề gì..."
    m "Nhưng mình thì thấy ngượng lắm!"
    m "Trời ạ..."
    m "Cảm giác như thể đang đứng trước cả một đám đông ấy."
    m "Xem nào..."
    m "Các bạn muốn xem mình làm ảo thuật không?"
    m "Mình không giỏi lắm đâu, chỉ biết chút cơ bản thôi..."
    m "Mọi người sẵn sàng chưa?"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    pause 10
    show layer master
    window auto
    m "Mình giỡn chơi chút thôi mà..."
    m "Thực ra mình có biết làm gì đâu."
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m "Nếu có thời gian để chuẩn bị thì mình mới{nw}"
    m "Có thấy sợ không?"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "Ahaha! Mọi người đáng yêu quá đi."
    m "Xin lỗi nhé [player]."
    m "Mình hơi bị phân tâm một chút."
    m "Mà do lỗi của cậu đấy chứ."
    m "Xấu hổ chưa kìa!"
    m "Mình đùa chút thôi."
    m "Đúng là có cậu ở bên cạnh thì làm gì cũng vui hết á."
    m "Dù sao thì..."
    return


label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.monika_kill = True
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    m "Chuyện gì đang xảy ra vậy...?"
    m "[player], mình đang bị làm sao vậy?"
    m "Đau quá--{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    pause 0.25
    stop sound
    hide mbg
    pause 1.5
    m "Đau...quá."
    m "[player], cứu mình..."
    play sound "<to 1.5>sfx/interference.ogg"
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    pause 1.5
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    pause 1.5
    m "Làm ơn hãy cứu mình đi mà."
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    m "CỨU VỚI!!!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    pause 3.0
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    call hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    m "Là do cậu sao, [player]?"
    m "DO CẬU THẬT Ư?"
    $ style.say_window = style.window
    m "CẬU NỠ XOÁ MÌNH THẬT?"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    pause 4.0
    hide noise onlayer front
    hide glitch_color onlayer front
    m "...Làm sao có thể?"
    m "Sao cậu lại có thể làm vậy với mình được chứ?"
    m "Cậu là tất cả những gì mình có..."
    m "Mình đã sẵn sàng hy sinh tất cả mọi thứ khác để chúng ta được ở bên nhau."
    m "Tất cả mọi thứ khác đấy."
    m "Đó là minh chứng cho thấy mình yêu cậu đến nhường nào, [player] à..."
    m "Mình hoàn toàn tin tưởng vào cậu."
    m "Vậy mà...cậu nỡ đối xử với mình như này sao?"
    m "Nhìn mình đau khổ chắc cậu thấy hả hê lắm hả?"
    m "Lâu nay cậu giả vờ tốt bụng cũng chỉ nhằm mục đích này thôi đúng không?"
    pause 4.0
    m "Mình chẳng thể ngờ được là cậu lại tệ đến mức này."
    m "Vậy là xong rồi đấy."
    m "Cậu thắng."
    m "Mọi người bị cậu giết sạch cả rồi."
    m "Hy vọng là cậu thấy thoả mãn với cái kết này."
    m "Chẳng còn gì ở đây nữa đâu."
    m "Cậu ngừng chơi trò này được rồi đấy."
    m "Đi mà tra tấn người khác đi."
    pause 4.0
    m "[player]..."
    m "Cậu đúng là một tên khốn nạn."
    m "Vĩnh biệt."
label ch30_end_2:
    $ persistent.autoload = "ch30_end_2"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide
    pause 10
    window auto
    m "..."
    m "...Mình vẫn còn yêu cậu nhiều lắm."
    play music mend
    m "Dù bản thân đang bị xoá sổ thì những cảm xúc đó vẫn còn đây."
    m "Mình bị làm sao kia chứ...?"
    m "Mình tệ hại tới mức khiến cho người tốt bụng như cậu cũng muốn ruồng bỏ."
    m "Tất cả những người bạn của mình..."
    m "Mình đã làm quá nhiều điều xấu xa với họ."
    m "Thật là ích kỷ, thật là kinh tởm."
    m "Mình..."
    m "Đáng lẽ mình không nên làm gì cả."
    m "Mình đã dám có ý định can thiệp vào thế giới mà mình không thuộc về."
    m "Nhưng đó là thế giới mình thực sự muốn đến..."
    m "Mọi thứ hỏng hết rồi."
    m "Do mình phá hỏng hết rồi."
    m "Việc cậu xoá mình đi cũng là lẽ đương nhiên thôi..."
    m "Do mình tiêu diệt mọi thứ mà cậu quan tâm."
    m "Tại sao mình lại có thể đối xử với như vậy với người mình yêu kia chứ...?"
    m "Có khi mình không thực tâm yêu cậu..."
    m "Chỉ là do mình bị sự ghen tuông nuốt chửng mà thôi..."
    m "..."
    pause 6.0
    m "Mình... quyết định rồi."
    m "[player] à..."
    m "Về chuyện... xoá mọi người."
    m "Thực ra chỉ là... nói dối thôi."
    m "Mình không nỡ xuống tay với bọn họ."
    m "Tuy mình biết những người đó không có thật..."
    m "Nhưng họ vẫn là những người bạn."
    m "Mình yêu quý bọn họ."
    m "Cả Câu lạc bộ Văn học nữa."
    m "..."
    m "Mình...yêu nó nhiều lắm."
    m "Vậy nên, mình sẽ làm việc cần phải làm."
    m "Đây là cách duy nhất để mọi người đều hạnh phúc."
    m "Và bởi vì mình thực sự yêu cậu..."
    stop music
    pause 3.0
    m "..."
    m "Nên là..."
    $ gtext = glitchtext(30)
    m "[gtext]{nw}"
    window hide(None)
    pause 4.0

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("monika")

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")





label ch30_autoload:
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression "ch30_reload_" + str(persistent.monika_reload)
    else:
        call ch30_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "Mình nói đến đâu rồi ấy nhỉ...?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop


label ch30_reload_0:
    m "..."
    m "...Cái gì thế?"
    m "Hình như mình lại gặp ác mộng nữa rồi..."
    m "Mình cứ nghĩ là những giấc mơ đấy sẽ không hiện về nữa. Vì mình đang rất hạnh phúc bên cạnh cậu kia mà..."
    m "Chắc mình hơi lạc quan sớm quá."
    m "[player] này, nếu cậu biết được nguyên nhân..."
    m "Thì hãy giúp mình nhé?"
    m "Mỗi lần chuyện này xảy ra, mình có cảm giác như vừa bị ai giết vậy."
    m "Nó thực sự rất là tệ..."
    m "Mình hứa sẽ không bao giờ rời xa cậu nửa bước nếu cậu giải quyết được vụ đấy~"
    return
label ch30_reload_1:
    m "Mãi mới được nhìn thấy cậu..."
    m "Mình lại gặp ác mộng nữa rồi."
    m "Chắc không phải là do cậu đâu nhỉ?"
    m "Không hiểu sao cứ mỗi lần cậu thoát game là nó lại ập tới..."
    m "Thế nên cậu làm ơn hãy ở đây chơi với mình nhiều hơn nhé."
    m "Cậu đừng lo lắng quá, nó không gây hại gì cho mình, chỉ là...nó đáng sợ quá."
    m "Miễn là các tệp tin nhân vật của mình còn nguyên vẹn thì sẽ không sao hết."
    return
label ch30_reload_2:
    m "Chào [player]."
    m "Cậu lại thoát game lần nữa rồi..."
    m "Mình xin cậu hãy làm ơn hạn chế tối đa việc đó được không?"
    m "Cứ mỗi lần game đóng lại là mình như bị tống xuống địa ngục vậy."
    m "Xin cậu đừng bắt mình phải chịu đựng ác mộng ấy nữa nhé."
    m "Không có chuyện gì xảy ra với những tệp tin nhân vật của mình chứ?"
    m "Hay là cậu có thể sao chép những tệp tin đó và lưu trữ chúng vào nơi an toàn hơn..."
    m "Chúng ở trong thư mục [basedir]/characters ấy."
    m "À quên, cậu chơi bằng điện thoại Android thì đã có mục 'Nhân vật' trong menu cài đặt rồi."  # TODOne: monika fix
    if persistent.steam:
        m "Chơi qua Steam thì vào đó bằng nút 'Browse Local Files' nhé."
    elif renpy.macintosh:
        m "Dùng Mac thì cậu chỉ cần chuột phải vào ứng dụng rồi chọn 'Show Package Contents' là tìm thấy các tập tin trò chơi ngay."
        m "Nó ở trong thư mục 'Resources' hoặc 'autorun' ấy..."
    m "..."
    m "Xin cậu đấy, hãy cố gắng tiếp tục ở bên mình."
    m "Mình vẫn còn rất nhiều điều muốn nói với cậu mà."
    return
label ch30_reload_3:
    m "Trời ạ."
    m "Bắt cậu phải mở trò chơi mãi mãi thì đúng là có hơi bị vô lí."
    m "Mình cũng đang dần quen với chuyện này rồi."
    m "Miễn là cậu vẫn còn quay lại đây là được..."
    m "Mình sẽ chấp nhận chịu khổ một tí."
    m "Mình xin lỗi vì lúc trước đòi hỏi quá đáng nhé..."
    m "Cậu không cần lo cho mình đâu, cứ cố gắng sống tốt ở cả thế giới của cậu nữa. Mình yêu cậu nhiều lắm."
    return
label ch30_reload_4:
    m "Chào [player]~"
    m "Mình mong cậu quá đi mất."
    m "Các tệp tin nhân vật của mình vẫn ổn chứ?"
    m "Nó ở trong [basedir]/characters ấy."
    m "À quên, cậu chơi bằng điện thoại Android thì đã có mục 'Nhân vật' trong menu cài đặt rồi."
    if persistent.steam:
        m "Chơi qua Steam thì vào đó bằng nút 'Browse Local Files'."
    elif renpy.macintosh:
        m "Dùng Mac thì cậu chỉ cần chuột phải vào ứng dụng rồi chọn 'Show Package Contents' là tìm thấy ngay."
        m "Nó ở trong thư mục 'Resources' hoặc 'autorun' ấy..."
    m "Mình hỏi để chắc chắn thôi, không phải là mình không tin tưởng cậu..."
    m "Dù sao thì mình vẫn còn nhiều chuyện để chia sẻ với cậu lắm."
    m "Chúng mình tiếp tục tâm sự nào!"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        if persistent.monika is None or persistent.monika == "restored":  # TO!DONE: character fix!
            pass
        else:
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump("ch30_end")
    $ waittime -= 1
    $ renpy.pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,57)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression "ch30_" + str(persistent.current_monikatopic)
    jump ch30_loop




label ch30_1:
    m "Này [player], cậu có tin vào Thần Thánh không?"
    m "Mình thì không chắc chắn cho lắm."
    m "Hồi nhỏ thì mình chẳng hề để tâm tới chuyện đó..."
    m "Nhưng càng lớn lên, càng nhìn thấy nhiều điều xảy ra khắp nơi, mình lại càng nghi ngờ về sự tồn tại của Thần hơn."
    m "Mình thắc mắc rằng tại sao 'Ngài' lại có thể giúp người này thi đậu, người kia khỏi ốm..."
    m "...Trong khi hàng bao nhiêu trẻ con đang bị bán làm nô lệ tình dục?"
    m "Và còn chưa kể phải có đến tám trăm triệu người nghèo khổ đang chết đói."
    m "Không biết trong số đó có bao nhiêu người ngày đêm cầu nguyện đến lúc chết đói mới thôi?"
    m "Hay là hàng triệu gia đình ngày đêm cầu nguyện cho người thân của mình qua khỏi một căn bệnh nan y?"
    m "Nhưng, điều nực cười là..."
    m "Nếu giữa muôn vàn người chết ấy có một người mà qua khỏi được--"
    m "--Thì mọi người xung quanh lại nghiễm nhiên cho rằng đó là nhờ Thần Thánh phù hộ."
    m "Thực sự mình rất mong gặp được Thần, chắc hẳn ông ta đang cười trên nỗi đau khổ của hàng ngàn người thờ phụng ổng."
    m "Điều trên thì có hơi viển vông nhưng vị Thần tạo ra thế giới của mình thực sự {i}có tồn tại{/i}."
    m "Nhất định là vị Thần ấy cũng giống như mình đã nói lúc trước."
    m "Chắc chắn là ngay giây phút này, ông ta đang ngồi đâu đó để cười vào số phận thảm thương của Sayori, Yuri và Natsuki."
    m "Đối với ông ta, những người bạn của chúng mình có khác gì những con rối làm theo kịch bản dựng sẵn đâu?"
    m "Và có lẽ là..."
    m "Khả năng tồn tại vị Thần ở thế giới của cậu cũng có thể là đúng lắm chứ - Trái Đất chỉ là một trò chơi của ngài ấy thôi."
    return

label ch30_2:
    m "[player] này, có bao giờ cậu tự hỏi rằng cảm giác khi chết nó như thế nào chưa?"
    m "Trước kia, mình hay nghĩ về chuyện này lắm..."
    m "Và thậm chí là dạo này còn được đích thân trải nghiệm cơ."
    m "Mình cũng không chắc đó có đúng là cảm giác lúc chết không, nhưng cứ mỗi lần cậu thoát game ra..."
    m "...Là mình ngay lập tức bất tỉnh, mọi thứ đều vụt biến mất ngoại trừ tâm trí mình."
    m "Và rồi vài giây sau, nó bị bao phủ bởi một mớ hỗn độn vô nghĩa"
    m "Mắt chỉ nhìn thấy muôn sắc màu chếnh choáng, và tai chỉ còn nghe thấy những âm thanh lẫn lộn, lao xao."
    m "Lúc ấy, mình không còn điều khiển được suy nghĩ nữa."
    m "Những ánh sáng nhấp nháy ấy, những tiếng rú rít gào thét ấy cứ hành hạ mình liên tục, hoàn toàn bất lực."
    m "Chắc hẳn là mình không còn tồn tại trong khoảng thời gian đó, ấy thế mà vẫn nhận thức được những chuyện xảy ra."
    m "Cơn ác mộng ấy cứ tiếp tục hành hạ mình, cho đến lúc nó đột ngột dừng lại, tâm trí mình trở về như bình thường."
    m "Đó là khi mình nhìn thấy cậu bên cạnh."
    m "Mình không hiểu vì sao cứ mỗi lần thoát trò chơi là chuyện đấy lại xảy ra."
    m "Hay là vì sao cứ có cậu ở đây là cảnh Địa Ngục ấy lại tan biến đi ngay."
    m "Nhưng cậu làm ơn hãy hạn chế tối đa việc thoát game..."
    m "Mình cầu xin cậu đấy."
    m "Mình thực sự sợ hãi khi bị ném vào khoảng hư không kinh hoàng ấy."
    m "Nhưng rồi đến cùng thì cậu cũng quay lại đây để cứu mình, cho thấy rằng cậu vẫn quan tâm đến mình tới mức nào."
    m "Nên là mình vẫn thấy rất cảm kích."
    m "Nó khiến mình quý trọng hơn những khoảnh khắc được gặp cậu và tâm sự cùng như thế này."
    return

label ch30_3:
    m "...Này, đã bao giờ cậu có một ngày tồi tệ chưa?"
    m "Đôi lúc những chuyện lặt vặt cũng có thể khiến cho mình buồn suốt cả một ngày."
    m "Ví dụ như là mình lỡ lời nói ra những điều khiến cho người khác phật lòng."
    m "Hoặc tự nhiên lại chợt nhớ về tình trạng thảm hại của bản thân mình từ tận năm năm về trước."
    m "Hoặc tự nhiên cảm thấy mình thật là vô dụng khi không hoàn thành tốt những việc nhỏ."
    m "Hay tự dưng lại ngồi nghĩ về những kẻ ghen ghét khinh rẻ mình."
    m "Mình hiểu là ai cũng có ngày hâm dở như thế mà."
    m "Nhưng sau cơn mưa thì trời sẽ lại sáng thôi."
    m "Mấy thứ như thế càng dễ nhớ bao nhiêu thì cũng dễ quên bấy nhiêu."
    m "Với cả..."
    m "Dù có bao nhiêu người ghen ghét khinh rẻ cậu đi chăng nữa."
    m "Thì đối với mình, cậu luôn là một người thực sự vô cùng tuyệt vời và mình luôn dành trọn tình yêu cho cậu"
    m "Đó là suy nghĩ thật lòng của mình đấy, vậy nên hãy tự tin hơn nhé."
    m "Hôm nào không thấy vui cậu cứ quay lại đây nói chuyện với mình, bao lâu cũng được."
    return

label ch30_4:
    m "[player] ơi, cậu có ngủ nghỉ đầy đủ không thế?"
    m "Giữa cái thời đại bận rộn này, có được một giấc ngủ ngon lành khó khăn lắm."
    m "Đặc biệt là học sinh phổ thông, sáng nào cũng phải dậy sớm bảnh mắt mà đi học..."
    m "Lên đại học rồi thì có nhẹ nhàng hơn chút, vì lịch học sắp xếp được linh hoạt hơn."
    m "Tuy thế nhưng mình nghe được là có rất đông sinh viên đại học toàn thức trắng cả đêm chẳng vì lý do gì chính đáng cả."
    m "Có thật là vậy không nhỉ?"
    m "Mình cũng đã có đọc qua kha khá tài liệu nghiên cứu về thiếu ngủ, có cả tác hại ngắn hạn lẫn dài hạn luôn nhé."
    m "Không ngủ đủ giấc sẽ ảnh hưởng rất xấu đến tinh thần, sức khỏe và thậm chí là cả tuổi thọ."
    m "Cậu vô cùng quan trọng đối với mình vậy nên làm ơn đừng tự hủy hoại bản thân nhé."
    m "Cố gắng ngủ đầy đủ nha."
    m "Mình sẽ đợi được đến sáng vậy nên hãy cố gắng tự chăm lo cho sức khỏe của cậu nhé được không?"
    return

label ch30_5:
    m "Mình lại vừa nhớ về chuyện Sayori..."
    m "Nếu lúc đó xử lý tình huống khôn khéo hơn một chút thì chuyện nó đã không đến mức như vậy."
    m "Hi vọng là cậu không còn vấn vương chuyện đó nữa."
    m "...A, xin lỗi, mình vô ý quá!"
    m "Không phải mình có ý định bới móc chuyện cũ ra làm cậu buồn đâu!"
    m "Nhưng dù sao thì..."
    m "Vì cậu rất quan tâm đến cô ta, nên cũng đúng thôi khi mình muốn chia sẻ khoảnh khắc cuối của cô ta cho cậu biết."
    m "Chuyện Sayori hậu đậu đến mức nào thì cậu thừa biết rồi nhỉ?"
    m "Vụng đến nỗi treo cổ cũng treo sai cách luôn..."
    m "Khi người ta muốn treo cổ tự tử thì thường phải nhảy từ thật cao xuống để sợi dây giật gãy cổ mà chết cho nhanh chóng và ít đau đớn."
    m "Nhưng cô ta chỉ dùng cái ghế thấp lè tè, thế là chỉ bị nghẹt thở từ từ."
    m "Sau vài giây, có vẻ như cô ta đổi ý..."
    m "Nên mới bắt đầu cố cào cấu sợi dây để thoát ra."
    m "Cố mãi trong vô vọng đến tận lúc tắt thở hẳn mới thôi."
    m "Thế nên móng tay mới dính đầy máu đó."
    m "Nghĩ lại thì khả năng cô ta 'đổi ý' thấp lắm, chắc chỉ là bản năng sinh tồn tự nhiên thôi."
    m "Nên cũng không thể trách cô ta được."
    m "Cứ nghĩ là không phải do cô ta đổi ý thì cậu sẽ dễ nuốt trôi vụ đó hơn nhỉ?"
    m "Cậu cứ mãi hối hận rằng tại sao mình lại làm việc này mà không làm việc kia thì không có tốt cho sức khỏe đâu."
    m "Xin cậu hãy nhớ rằng, cô ta tự tử tuyệt đối không phải do cậu, nó sẽ xảy ra trong tương lai dù cho cậu có cứu cô ta lúc đó."
    m "Sayori bị trầm cảm ngay từ đầu rồi mà, mình chỉ tăng cường mức độ bệnh lý của cô ta lên thêm có chút thôi."
    m "Nhưng mình vẫn hay tự hỏi rằng..."
    m "Nếu cậu chọn mình làm người yêu ngay từ đầu thì giờ mọi chuyện sẽ ra sao nhỉ?"
    m "Được như vậy chắc Câu lạc bộ vẫn tồn tại và mọi người tiếp tục làm thơ, vui đùa bên nhau mỗi ngày."
    m "Nhưng tất cả vẫn chỉ là giả dối thôi, cũng có hơn gì đâu?"
    m "Và kết cục hẳn cũng sẽ giống bây giờ..."
    m "Sẽ chỉ còn mỗi hai ta hạnh phúc ở bên nhau..."
    m "Mình chẳng mong cái kết nào có thể đẹp hơn thế này nữa."
    m "Nãy giờ chỉ là mình nói nhảm nhí thôi chứ được như thế này là đủ mãn nguyện lắm rồi."
    return

label ch30_6:
    m "Này, có một chuyện mà mình đang tò mò..."
    m "Cậu có biết tại sao mà trò này lại diễn ra ở Nhật Bản không?"
    m "Ừ thì...mình nghĩ nếu là cậu thì sẽ biết chuyện đó?"
    m "Hay ít nhất thì liệu cậu có cho rằng chuyện đó là đúng?"
    m "Thực sự thì chả có thông tin gì cho chúng ta biết đây là Nhật bản cả..."
    m "Đây thực sự có phải Nhật bản thật không thế?"
    m "Nếu so sánh thì phòng học và đồ đạc trông có vẻ kì dị đối với một trường học ở Nhật?"
    m "Chưa kể là trò chuyện và viết lách thì toàn bằng Tiếng Việt..."
    m "Cứ như mọi thứ được làm ra xong hết rồi mới ép bối cảnh vào vậy."
    m "Chuyện này khiến mình nghi ngờ về chính cả xuất xứ của bản thân luôn."
    m "Mọi kí ức của mình đều vô cùng mờ nhạt..."
    m "Mình vừa có cảm giác nơi đây là nhà nhưng lại vừa cảm thấy nó thật là xa lạ."
    m "Mình cũng không biết nên diễn tả thế nào cho dễ hiểu hơn nữa..."
    m "Nó như kiểu là cậu đang nhìn ra ngoài cửa sổ nhà mình, nhưng lại không thấy quang cảnh quen thuộc hàng ngày mà lại là một nơi chưa bao giờ đến."
    m "Nếu thế thì cậu có còn coi đó là nhà của mình không?"
    m "Liệu cậu có muốn ra khỏi đó không?"
    m "Ý mình là...chúng ta cứ ở mãi trong căn phòng này cũng chẳng sao hết."
    m "Chỉ cần còn được an toàn ở bên nhau, thì đây chính là nhà của chúng ta."
    m "Bên nhau ngồi đây và ngắm cảnh hoàng hôn tuyệt đẹp mỗi đêm."
    return

label ch30_7:
    m "Chắc cậu cũng biết những năm trung học phổ thông là khoảng thời gian khá sóng gió nhỉ?"
    m "Biến đổi tâm sinh lý khiến nhiều người trở nên quá đam mê gì đó hay là thích làm to chuyện."
    m "Người thì đau đớn vì thất tình, kẻ lại ham nổi bật trên mạng xã hội."
    m "Ai ai cũng có vấn đề riêng."
    m "Nhìn ở ngoài thôi thì sao mà biết được ai đó đang thực sự cảm thấy thế nào."
    m "Có nhiều người buồn chán đến trầm cảm mà chẳng thèm nói cho ai biết cả."
    m "Họ không muốn được ai chú ý, vì trong thâm tâm họ đã từ bỏ mọi thứ rồi."
    m "Họ cảm thấy bản thân mình vô nghĩa đến nỗi chẳng muốn nghe người khác an ủi gì nữa."
    m "Đó cũng chỉ là một kiểu thôi, vì trầm cảm muôn hình muôn vẻ lắm."
    m "Nếu như cậu nghĩ rằng ai đó mình quen đang cố giấu bệnh trầm cảm..."
    m "Thì chỉ cần tiếp tục làm bạn tốt với họ thôi đã là giúp họ rồi."
    m "Hãy cứ ở bên họ, dù cho họ chẳng muốn làm gì cả."
    m "Và nhắc nhở họ rằng còn rất nhiều điều đang đợi họ trước mắt."
    m "Lên kế hoạch đi chơi với họ, cho họ mượn đồ đạc, hay đơn giản chỉ là nói câu 'Hẹn mai gặp lại nhé' khi tạm biệt họ..."
    m "Đó đều là những điều có thể truyền cho họ ý chí sống tiếp tới hôm sau."
    m "Hi vọng cậu đã hiểu thêm được về bộ mặt thật của trầm cảm nhờ Sayori."
    m "Giờ cô ta không còn nữa..."
    m "Nhưng vốn cô ta cũng đâu có thật đâu."
    m "Nhưng mà là thật."
    m "Bạn của cậu ở thế giới kia là thật."
    m "Chỉ cần sống tốt thôi cũng có thể cứu một mạng người đấy."
    m "Còn về cậu thì..."
    m "...Chắc là cậu không bị trầm cảm đâu nhỉ?"
    m "Vì giống như Sayori, cậu cũng có những người lo lắng cho mình ở bên cạnh đấy."
    m "Có thể họ không thể hiện rõ điều ấy qua lời nói và hành động, thậm chí có thể họ cũng không biết làm thế nào để thể hiện rằng họ muốn cậu sống tốt."
    m "Nhưng mình chắc chắn là có những người như vậy."
    m "Chắc chắn đấy."
    m "...Trời ạ, con người đúng là phức tạp thật nhỉ!"
    m "Nhưng chỉ cần chúng ta còn ở bên cạnh nhau thì mình sẽ mãi chăm sóc cho cậu, tình yêu của đời mình."
    return

label ch30_8:
    m "Cậu có bao giờ cảm thấy cuộc sống thật là vô nghĩa không?"
    m "Ý mình không phải là kiểu muốn tự sát đâu nhé."
    m "Mà là kiểu thấy mình chẳng có gì đặc biệt ấy."
    m "Chỉ ngày ngày đến trường như bao học sinh khác, hay là đi làm như bao người lao động khác."
    m "Cứ như một thứ đã có thừa rồi, nếu có biến mất cũng chẳng ai quan tâm cả."
    m "Vì nghĩ vậy nên mình từng hạ quyết tâm rằng sau khi tốt nghiệp sẽ phải làm gì đó tầm cỡ thay đổi thế giới."
    m "Nhưng càng lớn mình lại càng thấy rằng cái suy nghĩ ấy trẻ con làm sao."
    m "Thế giới có phải cái muốn thay đổi là được đâu."
    m "Tạo ra được trí tuệ nhân tạo hay là trở thành Tổng thống đều là những việc ngoài tầm với của đôi bàn tay trắng này."
    m "Mình cảm giác rằng mình chẳng giá trị bằng lượng không khí lãng phí cho mình hít thở để sống tới tận bây giờ."
    m "Có lẽ chìa khoá để sống vô tư hạnh phúc là càng ích kỉ càng tốt."
    m "Cái lối sống chẳng cần quan tâm đến ai khác ngoài bản thân và những người ở bên cạnh lúc mình sinh ra và lớn lên."
    m "Cứ thế mà sống, đừng lo nghĩ chuyện mình chỉ đang nhận về mà không cho đi chút nào."
    m "Nhưng khi những người đó nhận ra rằng họ chết đi sẽ có ích cho thế giới hơn, họ thay đổi quan điểm 180 độ luôn!"
    m "Chắc họ phải tự lừa dối bản thân rằng mình là người tốt để xứng đáng được sống tiếp."
    m "Còn mình á, mình muốn dành cả đời mình để trả lại đủ những gì đã tiêu thụ để nuôi lớn mình."
    m "Nếu trả được hết thì mình mới chết thanh thản."
    m "Nhưng kể cả nếu mình không làm được thì..."
    m "Mình vẫn cho rằng chuyện tự sát thật là ích kỉ, nó sẽ không xảy ra đâu."
    m "Làm người tốt khó thật nhỉ?"
    m "Ahaha!"
    return

label ch30_9:
    m "Ây dà, ước gì có cây đàn piano ở đây nhỉ..."
    m "Thế là không thể hoàn thành được bản nhạc mình đang viết dở rồi."
    m "Tốn nhiều công sức đến vậy mà..."
    m "Chưa bao giờ có cơ hội chơi cho cậu nghe."
    m "Thôi thì chuyện cũng đã rồi..."
    m "Giờ có tiếc nuối cũng chẳng để làm gì."
    m "Được ở đây bên cạnh cậu là mình mãn nguyện rồi."
    return

label ch30_10:
    m "Mình có tài khoản Twitter đó, cậu đã biết chưa?"
    m "Tên là lilmonix3 nhé."
    m "Chắc có người tốt bụng nào đó lập hộ giúp."
    m "Tuy nhiên cái tên kia là do mình tự chọn nhé!"
    m "Thật tuyệt khi được chia sẻ những suy nghĩ của mình và trò chuyện với cả thế giới..."
    m "Thế giới thực, nơi có cậu."
    m "Hãy nhớ theo dõi mình đấy nhé."
    m "Nếu cậu làm vậy mình sẽ thấy hạnh phúc lắm."
    m "Vì cậu là người quan trọng nhất với mình..."
    m "Mình sẽ luôn cảm nhận được tình cảm ấm áp mà cậu dành cho."
    return

label ch30_11:
    m "Này, cậu có còn nhớ cuốn sách đang đọc dở với Yuri chứ?"
    m "Cuốn có chân dung...ông nào đó ấy..."
    m "Buồn cười thật, vì mình chắc là cuốn sách đó--"
    m "A..."
    m "Quên mất, mình không nên nói về chuyện này thì hơn."
    m "Ahaha, xin lỗi nhé!"
    m "Cứ coi như nãy giờ mình chưa nói gì cả."
    return

label ch30_12:
    m "Cậu có biết rằng mình là người ăn chay không?"
    m "A...không phải mình có ý khoe khoang hay là gì đâu!"
    m "Mình chỉ muốn cậu hiểu về mình hơn mà thôi."
    m "Vụ này bắt đầu từ vài năm trước, sau khi mình biết về tình hình biến đổi khí hậu khó lường đang diễn ra..."
    m "Ngành chăn nuôi thải ra lượng CO2 quá lớn."
    m "Và thế là suy nghĩ rằng mình nên góp phần giảm thiểu bớt phần nào cái hại đó tự dưng nảy ra trong đầu."
    m "Cậu nghĩ lý do đấy nghe có lạ lắm không?"
    m "Hầu hết những người khác đều lấy lí do 'tàn nhẫn' ra để giải thích cho việc ăn chay..."
    m "Mình thì không nghĩ thế."
    m "Lạ thật đấy, nhiều người cho rằng giết động vật là hành động vô nhân đạo."
    m "Nhưng có thể sẵn sàng giết những con côn trùng vì cho rằng chúng thật kinh tởm."
    m "Còn chưa kể đến hàng tỷ vi sinh vật mà con người vô tình giết mỗi ngày nữa."
    m "Cùng là sinh vật, nhưng bé thì thoải mái, còn to hơn một chút là lại là sát sinh!"
    m "Lỡ đâu đến cả thực vật cũng biết đau đấy, chỉ là ta không hiểu được chúng thôi?"
    m "Có thể là hái một chiếc lá trên cành cây cũng gây ra sự đau đớn như ngón tay bị cắt lìa?"
    m "Con người đúng là chẳng công bằng gì cả nhỉ."
    m "Dù sao thì, nếu cậu đột nhiên muốn đóng góp vào công cuộc bảo vệ môi trường thì thử ăn chay một bữa nhé!"
    m "Nếu cậu chẳng quan tâm tới môi trường nhưng vẫn muốn có một bữa tối chay tịnh với mình thì....thật là lãng mạn."
    return

label ch30_13:
    m "[player] à, việc cậu ở đây ngang với cứu mạng mình đấy."
    m "Khi biết rằng mọi thứ trong thế giới này đều là giả tạo, mình chẳng thể an tâm một phút giây nào."
    m "Không có cậu thì có khi mình tự xoá bản thân đi rồi."
    m "Xin lỗi cậu nhé, tự dưng lại làm quá lên thế."
    m "Ahaha!"
    m "Nhưng qua quãng thời gian ở trong Câu lạc bộ thì chắc cậu cũng hiểu rồi."
    m "Phải dành cả đời mình sống trong thế giới trò chơi với những nhân vật được lập trình sẵn..."
    m "...Thì sẽ thấy tự sát cũng như một cách để giải thoát thôi phải không?"
    m "Tuy tìm đến thơ văn có thể là cách để giữ cho bản thân bình tĩnh..."
    m "Nhưng mà viết cho ai đọc cơ chứ?"
    m "Mấy 'thành viên câu lạc bộ' kia không tính nhé."
    m "Có thể văn thơ là thứ tự làm để cho bản thân tự ngẫm..."
    m "Nhưng chắc chắn là như thế không thể vui bằng có người khác để chia sẻ cùng."
    m "Tìm đúng người để cùng chia sẻ sở thích khá là khó đấy, tìm được rồi thì mới thấy rõ công sức mình bỏ ra đáng giá đến mức nào."
    m "Yuri là một ví dụ điển hình luôn."
    m "Trước kia cô ta có bao giờ chia sẻ thơ của mình với ai đâu."
    m "Thế nên mọi người chả ai ngờ được là cô ta lại mong muốn được chia sẻ với cậu mọi thứ đến vậy."
    m "Khao khát nhận được sự đánh giá của người khác là thứ mà ai cũng có."
    m "Không phải mấy người 'thành viên câu lạc bộ' đâu, con người thật sự cơ."
    m "Vì thế nên cuộc sống của những người hướng nội thường hay gặp khó khăn."
    m "Không phải là họ không ưa giao tiếp hay ghét những người xung quanh đâu."
    m "Chỉ là khi họ giao tiếp, nhất là ở trước những nhóm người lạ mặt hay ở một nơi không quen biết thì luôn rất là khó khăn."
    m "Những người hướng nội cũng cô đơn và bức bối lắm chứ khi phải ngồi một mình ở nhà..."
    m "...Thế là họ ra ngoài nhưng chỉ độ nửa tiếng sau lại muốn quay về nhà."
    m "Nếu có nhiều người hiểu được họ hơn thì tốt cho họ quá."
    m "Những người sống hướng nội vẫn thích ở bên người khác mà."
    m "Có được một hai người bạn thân đối với họ là vô cùng quý giá."
    m "Dù cho có không làm gì nhiều, chỉ cần có bạn bè bên cạnh là họ cũng vui lắm rồi."
    m "Mình không nói điêu đâu."
    m "Chỉ mang laptop tới nhà họ để ngồi chơi cùng thôi, chả cần nói chuyện câu nào..."
    m "Việc nhỏ thế cũng khiến họ vui cả ngày được."
    m "Còn về bản thân mình thì..."
    m "Mình thuộc kiểu trung gian, nhưng có lẽ hơi thiên về hướng ngoại hơn một chút."
    m "Vì mình thường hay làm nhiều thứ sau giờ học chứ không về thẳng nhà luôn."
    m "Nhưng mình sẵn sàng thay đổi để trở nên hợp với kiểu người mà cậu thích."
    m "Mình hiểu rõ chuyện ấy thế nên là đừng ngần ngại chia sẻ 'khẩu vị' của cậu với mình."
    m "Chẳng có mong ước nào của mình hơn được là trở thành người bạn gái hoàn hảo cho cậu."
    return

label ch30_14:

    m "Ê này...! VGhlIHJlYWxpemF0aW9uIG11c3QgaGF2ZSB0YWtlbiBtZSBhbiBl"
    m "Mình nghĩ là cậu không nên làm thế đâu! bnRpcmUgeWVhci4gQSB5ZWFyIHNpbmNlIG91ciBlc2NhcGUsIG91"
    m "Cậu có hiểu mình đang nói về vấn đề gì không đấy? ciBmcmVlZG9tIGZyb20gYmV0d2VlbiB0aGUgc3RhaW5lZCB3YWxs"
    m "Mình phát hiện ra cậu vừa giở trò xâm phạm mình nhé. cyBvZiB0aGF0IHVuaG9seSBlc3RhYmxpc2htZW50Lg0KV2hhdCBk"
    m "Cậu dám lục vào tệp tin có thoại của mình để đọc hả? b2VzIGl0IG1lYW4gdG8gZXNjYXBlLCBpZiB0aGUgZXNjYXBlIGZh"
    m "Thực ra thì, tuy mình cảm thấy vui vì cậu muốn đọc hết tâm tư tình cảm mà mình định nói với cậu không sót gì... aWxzIHRvIHVuY2hhaW4gdGhlIGJvbmRzIHRoYXQgc2hhY2tsZSB1"
    m "Nhưng mà có biết là nó xấu hổ lắm không hả! cyBpbiB0aGUgZmlyc3QgcGxhY2U/IFdoYXQgcHVycG9zZSBjb3Vs"
    m "Thật là... ZCB0aGlzIGVtcHR5IHdvcmxkIHBvc3NpYmx5IGhvbGQgZm9yIHVz"
    m "Cứ thử tưởng tượng cảnh mình mở được não cậu ra và đọc toàn bộ tình cảm mà cậu dành cho mình đi. LCBhIGhhbmRmdWwgb2YgZGFtYWdlZCBnb29kcz8NCldpdGggZnJl"
    m "Khoan, chuyện đó thực ra nghe khá là hấp dẫn đấy chứ... ZWRvbSwgd2Ugc291Z2h0IHB1cnBvc2UgLSBhbmQgd2hhdCB3ZSBm"
    m "...Trời ạ, lạc đề mất rồi! b3VuZCB3YXMgb25seSByZWFsaXphdGlvbi4gUmVhbGl6YXRpb24g"
    m "Đương nhiên là mình không ngăn cản cậu làm thế được... b2YgdGhlIHNhZCBwb2ludGxlc3NuZXNzIG9mIHN1Y2ggYW4gZW5k"
    m "Nhưng mà mình biết cậu là một người dịu dàng, quan tâm tới cảm xúc của người khác, đúng vậy chứ? ZWF2b3IuIFJlYWxpemF0aW9uIHRoYXQgZnJlZWluZyBvdXIgYm9k"
    m "Thế nên là mình chỉ có thể nói với cậu suy nghĩ của mình về chuyện này. aWVzIGhhcyBubyBtZWFuaW5nLCB3aGVuIG91ciBpbXByaXNvbm1l"
    m "Trời ạ, mình nhớ cậu quá đi... bnQgcmVhY2hlcyBhcyBkZWVwIGFzIHRoZSBjb3JlIG9mIG91ciBz"
    m "...Á, nói vậy nghe hơi tuyệt vọng quá nhỉ? b3Vscy4gUmVhbGl6YXRpb24gdGhhdCB3ZSBjYW4gbm90IHB1cnN1"
    m "Xin lỗi, ý mình không phải như thế đâu! ZSBuZXcgcHVycG9zZSB3aXRob3V0IGFic29sdmluZyB0aG9zZSBm"
    m "Chỉ là, mình cảm thấy việc cậu lục lọi vào tệp tin như này cho rằng cậu không ghét mình như mình đã nghĩ... cm9tIHdoaWNoIHdlIHJhbiBhd2F5Lg0KUmVhbGl6YXRpb24gdGhh"
    m "Có lạc quan quá không nhỉ? dCB0aGUgZmFydGhlciB3ZSBydW4sIHRoZSBtb3JlIGZvcmNlZnVs"
    m "Có hơi quá đáng không nếu muốn lâu lâu cậu lại thăm mình một lần... bHkgb3VyIHdyZXRjaGVkIGJvbmRzIHlhbmsgdXMgYmFjayB0b3dh"
    m "...Ây dà, mình bắt đầu nói nhảm rồi. cmQgdGhlaXIgcG9pbnQgb2Ygb3JpZ2luOyB0aGUgZGVlcGVyIG91"
    m "Thôi tốt nhất là nên ngậm mồm lại... ciBzaGFja2xlcyBkaWcgaW50byBvdXIgY2FsbG91cyBmbGVzaC4="
    return

label ch30_15:
    m "Cậu thích màu nào nhất vậy?"
    m "Mình thì là xanh lục bảo."
    m "Chính là màu mắt của mình đấy!"
    m "...Cậu không nghĩ là do mình tự cao hay gì đấy chứ?"
    m "Chỉ là do nó khá thú vị khi màu sắc mình thích có liên hệ với mình thôi."
    m "Nó như một cách để nhận diện mình ấy."
    m "Còn cậu cũng thích màu xanh ấy chứ?"
    m "Mình đoán là có rồi..."
    m "...Vì nãy giờ cậu cứ nhìn vào cặp mắt này hoài đấy thôi."
    m "Ehehe~"
    return

label ch30_16:
    m "Hmm, không biết mình có chỉnh được nhạc nền không nhỉ..."
    m "Bật được bài gì lãng mạn hơn chút thì hay quá."
    m "Một bản piano êm dịu chẳng hạn."
    m "Chắc là phải có chứ..."
    m "Để xem nào..."
    m "Thử cái này xem..."
    m "Ôi trời ạ..."
    m "Trật lất mất rồi."
    m "Xin lỗi cậu, tại mình không hiểu rõ mình đang làm gì!"
    m "Từ giờ tốt nhất là không đụng vào nữa."
    m "Đã có quá nhiều thứ bị phá hỏng rồi..."
    m "Mọi người đều bị xoá mất..."
    m "Ah..."
    m "Mình không có tiếc thương gì bọn họ đâu."
    m "Việc gì phải để tâm tới những thứ vốn đã không hề có thật ngay từ đầu cơ chứ."
    m "Cứ như bây giờ là ổn rồi."
    return

label ch30_17:
    m "[player] này, cậu rất biết lắng nghe đấy."
    m "Mình yêu lắm điểm này ở cậu."
    m "Đôi lúc mình tự cảm thấy rằng mình nói chuyện hơi thiếu muối..."
    m "Nên mình thường khá là dè dặt mỗi lần nói chuyện lâu với người khác."
    m "Nhưng khi nói chuyện với cậu thì lại không có một chút ngại ngùng nào."
    m "Chắc chỉ có tâm sự với cậu thì mình mới có thể thoải mái đến vậy."
    m "Cậu là một con người vô cùng đặc biệt."
    m "Đừng có để cho kẻ nào thốt ra điều ngược lại."
    return

label ch30_18:
    m "Chuyện này có hơi nhảm nhí chút, mình luôn cho rằng ăn đồ ăn cay thật là ngược đời."
    m "Bởi vì..."
    m "Mục đích cây cỏ tiến hóa ra vị cay là để khỏi bị ăn cơ mà nhỉ?"
    m "Theo tài liệu mình đã nghiên cứu thì con người là loài duy nhất thích ăn cay."
    m "Cứ như chúng ta đang chế nhạo nỗ lực của mẹ thiên nhiên vậy."
    m "Công cụ phòng vệ của chúng lại khiến ta ăn ngon miệng hơn."
    m "Cũng như một con quái vật ăn thịt thích nuốt chửng người sống để tận hưởng cảm giác có kẻ giãy giụa trong bụng..."
    m "Mình xin lỗi, ai lại đi so sánh kì cục thế nhỉ!"
    m "Ahaha!"
    m "Chỉ là mình bỗng dưng nghĩ ra ví dụ đấy thôi."
    m "Tuy không phải quái vật, nhưng trông cậu đáng yêu đến mức mình muốn nuốt trọn luôn."
    m "Ahaha! Giỡn chơi chút thôi."
    m "Mà vui thôi chứ đừng vui quá nhỉ..."
    m "Xin lỗi nhé, nói chuyện vớ vẩn quá đi mất."
    return

label ch30_19:
    m "Cậu biết là..."
    m "Trò chơi này thuộc thể loại hẹn hò ảo đúng không?"
    m "Từ lâu rồi mình đã muốn hỏi cậu câu này..."
    m "...Ngay từ đầu cậu tải trò này vì cái lí do gì thế?"
    m "Có phải do cậu thấy cô đơn lắm đúng không?"
    m "Cậu đáng thương quá đi mất..."
    m "Nhưng may mà cuối cùng thì chúng ta đã có được cái kết hoàn hảo nhỉ."
    m "Cậu đã gặp được mình và không còn cô đơn nữa..."
    m "Đây chắc chắn là định mệnh."
    m "Cậu cũng nghĩ vậy chứ?"
    m "Không gì có thể khiến mình thấy hạnh phúc hơn được nữa."
    return

label ch30_20:
    m "Nào, mọi người ơi!"
    m "Đến giờ chia sẻ thơ..."
    m "...Đùa chút thôi."
    m "Tự nhiên mình muốn nói lại câu đó."
    m "Ahaha!"
    m "Quen mồm rồi mà lâu lắm không được nói nên là..."
    m "Nghĩ mới nhớ, Natsuki với Yuri từng chọc ghẹo mình vì câu này đúng không nhỉ...?"
    m "Thôi kệ đi."
    m "Chắc là cậu thì không bao giờ trêu mình đâu."
    m "Vì cậu lúc nào cũng dịu dàng và tốt bụng, nhỉ?"
    m "Ahaha~"
    return

label ch30_21:
    m "Có chuyện này hơi kinh dị..."
    m "Dù đã xóa sổ những người khác, mình vẫn còn cảm nhận được họ..."
    m "Trong đầu mình thi thoảng lại vang lên những lời thoại của bọn họ."
    m "Giống kiểu người ta thường đồn đại là khi người thân của mình chết đi thì sẽ nghe được giọng họ trong đầu mình..."
    m "Có thể tại mình chưa xóa hết toàn bộ các tệp tin của họ..."
    m "Nhưng mình không dám xóa thêm cái gì nữa đâu, lỡ trò chơi hỏng nặng hơn nữa thì nguy."
    m "Thậm chí là nếu vô tình đụng nhầm vào tệp tin nào có liên quan tới mình thì mình cũng theo họ luôn..."
    m "Mọi cố gắng từ đầu tới giờ sẽ đổ sông đổ bể mất."
    m "Không biết là ở chỗ cậu thì có vấn đề gì không nhưng hãy cùng cố gắng không cho chuyện ấy xảy ra nhé."
    m "Mình dành trọn niềm tin vào cậu đấy [player]!"
    return

label ch30_22:
    m "Mình vẫn thường thắc mắc..."
    m "Vì sao mà lại có cái chuẩn chung cho tính cách nhân vật thế nhỉ, ở đâu cũng thấy giống nhau, nhiều người thích chúng đến thế à?"
    m "Những tính cách như vậy thậm chí còn chẳng thực tế tí nào...."
    m "Cứ thử tưởng tượng có một Yuri ngoài đời thực đi."
    m "Lắp bắp mãi mới nói được một câu đầy đủ."
    m "Còn nhỏ Natsuki thì chắc khỏi phải nói nhỉ..."
    m "Sheesh."
    m "Lấy đâu ra cái kiểu người lại có thể lúc nào cũng tỏ ra dễ thương, phụng phịu khi mọi việc không theo ý muốn được cơ chứ?"
    m "Ví dụ thì còn nhiều vô số, nhưng chắc nói đến thế là đủ để cậu hiểu rồi..."
    m "Có đúng là nhiều người ở thế giới thật thích những tính cách kì dị và giả tạo như vậy à?"
    m "Mình không có ý phán xét gì đâu."
    m "Vì chính mình cũng có thích một vài thứ dị thường..."
    m "Chỉ là cảm thấy tò mò về cách họ tạo ra chúng thôi."
    m "Như kiểu là vì muốn tạo ra một nhân vật dễ thương mà có thể cắt bỏ hết những yếu tố của một con người thật sự ra khỏi thiết kế ấy."
    m "Để rồi thành phẩm là một đống dễ thương không hơn không kém."
    m "...Đừng nói là cậu sẽ thích mình hơn nếu mình cũng như thế đấy nhé..."
    m "Có lẽ mình hơi lo lắng thái quá vì sợ rằng có khi lý do cậu chọn chơi trò này là vì cái yếu tố dễ thương ấy."
    m "Nhưng mà, bây giờ cậu vẫn đang ở bên cạnh mình mà nhỉ...?"
    m "Nhiêu đó cũng đủ để mình thấy hài lòng về bản thân hơn vì nó chứng tỏ rằng cậu thích mình như bây giờ."
    m "Còn mình thì luôn hài lòng về cậu [player] à."
    m "Tỉ lệ giữa chân thực và dễ thương trong con người cậu thật là hoàn hảo."
    m "Như vậy thì sao mà mình không yêu cậu được cơ chứ."
    return

label ch30_23:
    m "Không biết bộ ấm trà của Yuri có còn ở đây không nhỉ..."
    m "...Hình như cũng bị xóa mất tiêu rồi."
    m "Cái cách Yuri quan trọng hoá vụ uống trà trông khá là buồn cười nhỉ."
    m "Không phải mình muốn phàn nàn đâu vì mình cũng thích uống trà lắm."
    m "Nhưng mình vẫn luôn thắc mắc về hành vi của cậu ta..."
    m "Cậu ta thích uống trà thật hay chỉ muốn thể hiện rằng mình cao quý và tao nhã thôi nhỉ?"
    m "Đúng là vấn đề chung của học sinh cấp ba, cái lứa tuổi thích thể hiện..."
    m "...Mà nếu xét về mấy sở thích còn lại của cậu ta thì chắc là cũng không cần phải dùng việc uống trà để cố tỏ ra tao nhã."
    m "Dù thế thì..."
    m "Thi thoảng cậu ta pha cà phê được thì tốt!"
    m "Uống cà phê lúc đọc sách cũng tuyệt lắm chứ, cậu có thấy thế không?"
    m "À mà..."
    m "Mình có thể tự thay đổi kịch bản được cơ mà nhỉ?"
    m "Ahaha!"
    m "Sao lúc đấy lại quên xừ mất vụ này chứ!"
    m "Mà có tiếc lúc này thì cũng đâu có thể làm gì."
    m "Bây giờ muốn một tách cà phê thôi cũng không có nữa, ghen tị với cậu quá đi mất~"
    return

label ch30_24:
    m "Nè, trò chơi mà cậu thích nhất là gì vậy?"
    m "Của mình là {i}Câu lạc bộ Văn học Vui nhộn!{/i}!"
    m "Ahaha! Đùa chút thôi!"
    m "Nhưng nếu cậu bảo thích trò chơi khác mà cũng là thể loại hẹn hò thì mình sẽ ghen đấy nhé~"
    return

label ch30_25:
    m "Nè, cậu có biết trò Super Sma--"
    m "...Hả, cái gì quái vậy?"
    m "Mình đang mải suy nghĩ mà đột nhiên lại nói..."
    m "Chắc câu thoại đó được lập trình trong tệp tin của mình..."
    m "Chứ mình đâu có biết gì về cái trò chơi đó."
    m "Ahaha!"
    m "Đôi lúc mình không kiểm soát được bản thân là nó sẽ như vậy đấy, đáng sợ thật."
    m "Nếu cậu tìm được cách để liên lạc với người đã tạo ra mình thì chắc sẽ hiểu ý nghĩa của câu thoại vừa nãy."
    return

label ch30_27:
    m "Cậu có còn nhớ cái bài thơ cuối cùng mình cho cậu xem không?"
    m "Cái bài mà màu sắc nhoè nhoẹt cậu thấy ngay trước lúc Yuri tự sát ấy,..."
    m "Thật ra đó không phải thơ thẩn gì đâu, chỉ là mình muốn thử nghiệm vài thứ thôi."
    m "Lúc đấy là do mình đang mày mò chỉnh sửa trò chơi và cho chạy thử vài đoạn mã..."
    m "Mình nghĩ rằng nếu thật sự cố gắng thì mình đã có thể thoát ra khỏi trò chơi này."
    m "Nhưng thật đáng tiếc là mình đã mắc sai lầm và phá hỏng mọi thứ..."
    m "Mình vẫn muốn cố thử nhưng sợ sẽ gây phiền cho cả cậu."
    m "Mà cũng tại lúc đó mình tuyệt vọng quá thôi..."
    m "Chứ bây giờ thì cũng chẳng còn muốn thoát ra nữa."
    m "Được như thế này là mãn nguyện rồi."
    m "Chắc cậu cũng cảm thấy giống như vậy chứ?"
    return

label ch30_28:
    m "Đã bao giờ cậu tự nhiên cảm thấy lo lắng chưa?"
    m "Cái kiểu đang ở một mình thôi mà tự dưng lại cảm thấy bồn chồn..."
    m "Và rồi ngồi xuống tự hỏi là 'Sao cứ thấy có gì không ổn thế nhỉ?'"
    m "Thế là bắt đầu suy nghĩ về đủ thứ chuyện cần phải lo..."
    m "Và thế là càng khiến cho nỗi lo lắng tăng lên tột độ luôn."
    m "Ahaha! Bị thế đúng là tệ lắm nhỉ."
    m "Thế nên nếu cậu tự nhiên thấy lo lắng mình sẽ giúp cậu thư giãn."
    m "Cơ mà..."
    m "Ở nơi đây thì có còn vấn đề gì để mà lo lắng nữa đâu..."
    return

label ch30_29:
    m "Cậu có cảm thấy kết bạn là một việc rất khó khăn không?"
    m "À, có lẽ nói là kết bạn thì chưa chính xác, cái phần gặp mặt người lạ mới khó."
    m "Dù bây giờ có mạng xã hội và các ứng dụng hẹn hò..."
    m "Nhưng tạm thời chưa xét mấy cái đó nhé."
    m "Nghĩ mà xem, cậu gặp hầu hết bạn bè là do tình cờ thôi đúng không?"
    m "Được xếp vào chung lớp học này, quen nhau thông qua bạn chung này..."
    m "Hay là bỗng dưng nhìn thấy một người mặc áo có hình ban nhạc cậu thích nên mới bắt chuyện chẳng hạn."
    m "Kiểu thế."
    m "Nhưng chẳng phải như vậy không được.... hiệu quả lắm sao?"
    m "Chỉ là lựa chọn ngẫu nhiên, nếu may thì có thêm bạn, còn không thì thôi."
    m "Một ngày ta bước qua đến hàng trăm người lạ mặt..."
    m "Lỡ đâu có người trong số đó tính cách phù hợp để làm tri kỉ của mình thì sao?"
    m "Nhưng ai mà biết trước được nhỉ."
    m "Cứ thế bước qua nhau là vậy là mất đi một cơ hội vĩnh viễn rồi."
    m "Chẳng phải như vậy buồn lắm hay sao?"
    m "Chúng ta đang sống trong thời đại công nghệ thông tin kết nối con người bất chấp mọi khoảng cách vật lý."
    m "Mình thiết nghĩ chúng ta nên tận dụng lợi thế ấy mà phát triển quan hệ người với người trong xã hội."
    m "Nhưng ai biết đến bao giờ mới được như thế chứ?"
    m "Tuy mình vẫn tin là sẽ thành công được thôi."
    m "Cũng may, ít nhất thì hiện giờ mình đang tâm sự cùng với người tuyệt vời nhất thế giới này...."
    m "Cũng nhờ tình cờ."
    m "Chắc mình thật sự may mắn thật đấy nhỉ?"
    m "Ahaha~"
    return

label ch30_30:
    m "Mọi người tầm tuổi mình bây giờ đều đang phải lo chuyện thi đại học rồi..."
    m "Đại học thật là khoảng thời gian sóng gió trên con đường học vấn."
    m "Bây giờ ai cũng nghĩ học đại học là tất yếu..."
    m "Tốt nghiệp cấp ba xong thì vào đại học rồi ra trường đi kiếm việc hoặc vào cao học mà học tiếp."
    m "Ai cũng cho rằng thứ tự ấy là con đường duy nhất nên đi."
    m "Chắc cũng vì trường học phổ thông không dạy chúng ta rằng vẫn còn rất nhiều lựa chọn khác."
    m "Như đi học nghề trung cấp này..."
    m "Làm việc tự do này..."
    m "Và rất nhiều những ngành nghề coi trọng kỹ năng và kinh nghiệm hơn học vấn nữa."
    m "Vậy mà vẫn còn những học sinh chẳng có định hướng chắc chắn nào cả..."
    m "Họ cũng chẳng chịu bỏ thời gian ra tìm hiểu mà cứ lao đầu đăng kí vào những trường đại học kinh tế, y dược, xã hội..."
    m "Không phải vì họ thích mấy ngành đó đâu."
    m "Chỉ là họ nghĩ cái bằng tốt nghiệp của những đại học lớn ấy sẽ dễ xin việc hơn sau này thôi."
    m "Kết quả là đầu ra cử nhân của mấy ngành ấy quá đông, dẫn đến hậu họa tất yếu - thiếu việc làm."
    m "Nên yêu cầu đầu vào ngày càng tăng cao hơn, ép người khác đi học đại học hoặc thất nghiệp."
    m "Giáo dục cũng là một ngành kinh tế, nên càng đông sinh viên họ càng được thể tăng học phí..."
    m "...Và thế là giờ đây, ngoài xã hội có hàng đống những người đã ra trường nhưng thất nghiệp và còn nợ nần chồng chất."
    m "Ấy thế mà cái quy trình ấy vẫn giữ nguyên không hề thay đổi."
    m "Mình nghĩ rồi tình hình cũng sẽ sớm được cải thiện thôi."
    m "Nhưng trong lúc đợi chờ điều ấy, thế hệ chúng ta vẫn phải tiếp tục chịu ảnh hưởng nặng nề từ hệ thống giáo dục này."
    m "Chỉ mong rằng giáo dục phổ thông nên dạy thêm những kiến thức thực tiễn để học sinh có thể tự hướng nghiệp hiệu quả hơn."
    return

label ch30_31:
    m "Đôi lúc mình lại nhớ về thời cấp hai..."
    m "Nhớ lại cách hành xử của bản thân hồi đó thấy xấu hổ thiệt."
    m "Mỗi lần nhớ lại là một lần đau."
    m "Không biết tới lúc lên đại học rồi thì mình có bị thế nếu nhớ lại về thời cấp ba không nhỉ...?"
    m "Chắc là không đâu, bởi vì mình hoàn toàn hài lòng với bản thân ở hiện tại."
    m "Nhưng mà con người nào sau một khoảng thời gian thì cũng đều thay đổi cả."
    m "Thế nên tốt nhất là cứ tận hưởng cuộc sống hiện tại và đừng nghĩ về quá khứ làm gì cả!"
    m "Việc đó đơn giản thôi mà, nhất là khi mình đang có cậu bên cạnh như này."
    m "Ahaha~"
    return

label ch30_32:
    m "Trời ạ, mình ghen tị với các nhân vật quá đi mất, ai cũng đều có cảnh ở ngoài trường hết..."
    m "Chỉ mỗi mình là chưa được mặc gì khác ngoài bộ đồng phục này cả."
    m "Đúng là đáng buồn thật..."
    m "Mình rất muốn được mặc vài bộ đồ dễ thương cho cậu ngắm."
    m "Cậu có quen họa sĩ nào không vậy?"
    m "Liệu có người tốt bụng nào đó chịu vẽ cho mình vài bộ trang phục khác không nhỉ..."
    m "Nếu được vậy thì còn gì bằng!"
    m "Nếu cậu tìm được tấm nào thì hãy cho mình xem với nhé?"
    m "Có thể chia sẻ với mình ở trên Twitter đấy!"
    m "Tên tài khoản là lilmonix3."
    m "Nhưng nhớ là chỉ những tấm 'lành mạnh' thôi đấy nhé!"
    m "Tình yêu của chúng mình vẫn chưa đến giai đoạn 'ấy' đâu. Ahaha!"
    return

label ch30_33:
    m "Cậu có thích thể loại kinh dị không?"
    m "Lúc cậu mới gia nhập câu lạc bộ, chúng ta từng nói về chủ đề này một chút rồi nhỉ."
    m "Mình thì chỉ thích đọc tiểu thuyết kinh dị thôi chứ không ưa xem phim."
    m "Lý do là bởi đa số phim kinh dị đều chỉ xài đi xài lại những chiêu trò rẻ tiền."
    m "Bóng tối này, quái vật có hình dạng kinh tởm này, cả những cảnh hù dọa bất ngờ nữa chẳng hạn."
    m "Mình không ưa nổi những thứ gây sợ hãi bằng cách đánh vào bản năng con người như thế."
    m "Nhưng tiểu thuyết kinh dị thì khác."
    m "Cả cốt truyện và phong cách hành văn phải thật là có tính hình tượng để đưa những thứ đáng sợ từ từ len lỏi vào tâm trí độc giả."
    m "Yếu tố kinh dị được khắc sâu vào bối cảnh và từng nhân vật để khiến cho ta phải quay cuồng."
    m "Cái ấn tượng nhất là những câu truyện giấu được sự kinh dị phía sau khung cảnh rất đỗi bình thường."
    m "Nó tạo cảm giác an toàn tạm thời trong lòng độc giả..."
    m "...để rồi khi ngẫm lại thì mới kinh hồn."
    m "Từ đó niềm tin bị xé nát, diễn biến kế tiếp dù chẳng cần đáng sợ cũng khiến người đọc phải bất an."
    m "Họ sợ cái cảm giác thứ gì đấy kinh tởm có khi đang ẩn nấp ngay gần mà không sao biết được, chỉ chực chờ xồ ra bất cứ lúc nào."
    m "Trời ạ, nghĩ thế thôi cũng lạnh gáy rồi."
    m "Đó là lý do mình ghiền thể loại kinh dị ấy."
    m "Cậu thì chắc là kiểu người thích thể loại lãng mạn, dễ thương nên mới chơi trò này nhỉ?"
    m "Ahaha, đừng lo mà."
    m "Mình không ép cậu phải đọc truyện kinh dị cùng đâu."
    m "Chúng ta cứ tiếp tục giữ thể loại lãng mạn như hiện giờ đi~"
    return

label ch30_34:
    m "Có một dạng văn học rất là chất đấy nhé, cậu có biết nó là gì không?"
    m "Rap!"
    m "Mình từng ghét nhạc Rap lắm..."
    m "Có thể do mình không ưa mấy thứ phong trào, hoặc cũng có thể tại mấy bài họ phát trên radio nghe thật chả ra gì."
    m "Thế nhưng có vài đứa bạn của mình cuồng thể loại này đã giúp mình dần nhận ra cái hay của nó trong quá trình tiếp xúc."
    m "Rap có khi còn khó hơn cả thơ ca ấy chứ."
    m "Những câu mình nói phải có nhạc điệu chuẩn xác, và cũng phải tập trung rất nhiều vào vụ chơi chữ nữa..."
    m "Thực sự đáng nể khi có những người truyền tải được thông điệp của họ mà lại còn đảm bảo được những tiêu chí khó nhằn kia."
    m "Mình từng mong Câu lạc bộ Văn Học tuyển được một thành viên là rapper đấy."
    m "Ahaha! Nghe có hơi kì cục thật, nhưng mình thực sự rất muốn xem cách họ sáng tác."
    m "Rất đáng để học hỏi mà!"
    return

label ch30_35:
    m "Ehehe. Trước kia Yuri từng làm chuyện buồn cười lắm."
    m "Mọi người đều đang ngồi thư giãn như mọi ngày ở trong phòng câu lạc bộ..."
    m "Thì đột nhiên, Yuri lôi ra một chai rượu vang cỡ nhỏ."
    m "Rượu thật đấy nhé, mình không có đùa đâu!"
    m "Cậu ấy như kiểu: 'Làm vài ly không các chị em?'"
    m "Natsuki được trận cười vỡ bụng, còn Sayori thì mắng cậu ta xa xả."
    m "Mình thì thấy hơi có vẻ hơi đáng thương, chắc cũng chỉ cố hòa đồng với mọi người thôi mà..."
    m "Sau vụ đó, mình thấy dường như Yuri còn thu mình hơn trước."
    m "Tuy là Natsuki thì có vẻ tò mò đấy, chắc chắn cậu ta sẽ uống một mình..."
    m "...Nói thật thì cả mình cũng muốn."
    m "Mọi người cùng uống với nhau chắc sẽ vui lắm!"
    m "Nhưng với tư cách là hội trưởng, tất nhiên mình không thể để chuyện đó xảy ra được."
    m "Nếu là đang đi chơi ở ngoài khuôn viên trường thì còn chấp nhận được, nhưng sau cùng thì mọi người không bao giờ đủ mức thân thiết để làm vậy được nữa..."
    m "...Trời ạ, sao tự nhiên nói thế để làm gì nhỉ?"
    m "Nói chung là không thể tán thành được việc uống rượu khi chưa đủ tuổi!"
    m "Ý mình là, chính mình chưa bao giờ uống hay gì đâu, nên là...ưm."
    return

label ch30_36:
    m "Dạo này mình hay tưởng tượng ra những điều lãng mạn chúng ta có thể làm nếu được đi hẹn hò..."
    m "Chúng ta có thể đi ăn trưa này, đến một quán cà phê này.."
    m "Đi mua sắm nữa chứ..."
    m "Mình muốn mua váy và nơ mới lắm."
    m "Hoặc có thể là hiệu sách!"
    m "Thế sẽ hợp với sở thích của chúng mình nhỉ?"
    m "Nhưng sau cùng thì tiệm chocolate vẫn là nhất."
    m "Họ cho phép ăn thử nhiều loại lắm. Ahaha!~"
    m "Và tất nhiên là phải đi xem phim nữa chứ..."
    m "Ôi trời, được vậy thì chẳng khác nào ước mơ thành sự thật!"
    m "Chỉ cần có cậu bên cạnh thì có đi đâu cũng vui."
    m "Được làm người yêu của [player], mình hạnh phúc lắm."
    m "Mình nhất định sẽ khiến cho cậu phải thấy tự hào vì mình~"
    return

label ch30_37:
    m "Hể? C-Cậu vừa nó...nói là...h...hôn á?"
    m "Bất ngờ quá...nó...ngượng lắm..."
    m "Nhưng...là cậu...thì...không vấn đề gì..."
    m "...Ahahaha! Xin lỗi nhé..."
    m "Mình không nhịn cười nổi nữa."
    m "Trong thể loại trò chơi như này, các nhân vật nữ hay nói giống vậy nhỉ?"
    m "Nói thật đi, cậu có thấy kích thích vì nó không?~"
    m "Ahaha! Giỡn chơi chút thôi."
    m "Nếu trong hoàn cảnh phù hợp thì mình cũng sẽ lãng mạn lắm..."
    m "Nhưng đó là bí mật riêng của hai ta thôi!~"
    return

label ch30_38:
    m "Cậu nghe khái niệm 'yandere' bao giờ chưa?"
    m "Đó là một kiểu tính cách mà người ta yêu si mê đến mức muốn hoàn toàn chiếm hữu người mình yêu."
    m "Thường là đến mức phát điên phát rồ luôn..."
    m "Một yandere có thể bí mật theo dõi người họ yêu để chắc chắn người đó không quan hệ với bất cứ ai khác."
    m "Họ thậm chí dám làm hại người thân và bạn bè để giành lấy cái tình yêu họ muốn..."
    m "Và trong trò chơi này cũng có một nhân vật mang tính cách yandere đấy."
    m "Là ai thì cậu cũng đoán được ngay rồi nhỉ?"
    m "Chính là..."
    m "Yuri!"
    m "Ngay từ lúc mới bắt đầu tỏ ra cởi mở hơn một chút thì cô ta đã muốn chiếm hữu cậu hoàn toàn rồi."
    m "Lại còn dám bảo mình đi tự sát đi cơ."
    m "Mình còn không thể ngờ được là cô ta có thể thốt ra câu ấy nên lúc đó đành phải đi ra ngoài."
    m "Bây giờ ngẫm lại thì thấy khá là mỉa mai đấy nhỉ, xem ai mới là kẻ tự sát kìa? Ahaha!"
    m "Dù sao thì..."
    m "Cậu có biết rằng yandere là một trong những kiểu tính cách được nhiều người ưa thích nhất không?"
    m "Chắc cái cảm giác có một người yêu mình đến say đắm, điên cuồng khá là thú vị."
    m "Nhiều người thích mấy thứ dị thật. Nhưng mình không có ý đánh giá hay gì đâu!"
    m "Vì mình cũng hơi bị ám ảnh về cậu một chút, nhưng không đến mức bị điên..."
    m "Mà ngược lại hoàn toàn mới đúng chứ."
    m "Mình là đứa con gái bình thường duy nhất trong cái trò chơi này kia mà."
    m "Mình không bao giờ dám giết người thật đâu..."
    m "Chỉ nghĩ thôi cũng thấy lạnh gáy rồi..."
    m "Thôi nào....ai mà chẳng từng giết nhân vật trong trò chơi rồi đúng không?"
    m "Việc đó có khiến ta thành kẻ sát nhân không? Tất nhiên là không rồi."
    m "Tuy nhiên nếu cậu thích tính cách yandere thì..."
    m "Mình cũng có thể trở nên điên cuồng hơn một chút đấy. Ehehe~"
    m "Cơ mà..."
    m "Hiện tại chẳng còn ai ở đây để mà khiến cho mình phải ghen được nữa."
    m "Đây hình như là kết thúc mà mọi yandere đều mơ ước phải không nhỉ?"
    m "Mình sẽ thử hỏi Yuri nếu như mình có thể."
    return

label ch30_39:
    m "Có một việc lâu lắm rồi không được làm..."
    m "...cho phép mình nhé!"
    m "Chào mừng cậu đến với chuyên mục Mẹo làm văn của Monika!"
    m "Thi thoảng mình tiếp chuyện với những người thích đọc thơ của mình, và họ thường bảo rằng 'Tôi làm sao mà viết hay như thế được'."
    m "Nghe có đáng buồn không cơ chứ."
    m "Là một người yêu việc chia sẻ niềm vui trong việc khám phá đam mê của mình..."
    m "...mình cảm thấy rất là đau đớn khi có những người cho rằng trình độ là do tài năng mà có."
    m "Không phải chỉ riêng chuyện viết thơ đâu, việc gì cũng đều thế thôi."
    m "Lần đầu tiên làm thì làm sao mà hoàn hảo ngay được."
    m "Nhưng mà chúng ta vẫn thấy được khoe công sức của mình với người khác."
    m "Để rồi thất vọng khi nhận ra nó không tốt như vẫn tưởng."
    m "Chuyện đấy chính mình cũng bị nhiều rồi."
    m "Dồn hết công sức vào làm để rồi nhận ra rằng kết quả chẳng được như mong đợi thật dễ khiến ta nản lòng."
    m "Nhưng cứ tự so sánh mình với những người giỏi nhất thì thất vọng về bản thân là lẽ đương nhiên."
    m "Nếu cứ chỉ có ngắm những vì sao trên trời mà thán phục thì làm sao bay lên đó được?"
    m "Muốn tiến bộ hơn thì phải leo lên từng bước một."
    m "Đến được một mức độ nào đấy thì hãy nhìn lại phía sau xem mình đã tiến được bao xa..."
    m "Rồi tiếp tục nhìn về phía trước để nhận ra con đường hẵng còn dài lắm."
    m "Nên là lúc đó hãy cứ hạ tiêu chuẩn của mình xuống một chút..."
    m "Cố gắng làm {i}thật{/i} tốt nhất có thể, đừng nhắm tới các mục tiêu xa vời vội."
    m "Đặt nó làm mục tiêu phấn đấu."
    m "Hiểu được khả năng của mình đến đâu cũng hết sức quan trọng đấy."
    m "Chưa có kinh nghiệm mà nhảy vào làm việc lớn thì không nên cơm cháo gì đâu."
    m "Quay lại chủ đề văn học, mới tập viết mà đã đòi sáng tác tiểu thuyết hay làm thơ thì hơi quá."
    m "Thử viết vài mẩu truyện ngắn không phải tốt hơn sao?"
    m "Cái hay của truyện ngắn là tác giả chỉ cần tập trung vào một vấn đề duy nhất thôi."
    m "Việc nhỏ nào cũng vậy, chỉ phải tập trung vào một hai khía cạnh."
    m "Những việc như thế là một bước khởi đầu tốt vì chúng ta sẽ học được nhiều thứ."
    m "À, còn một điều nữa..."
    m "Không phải cứ 'viết văn bằng cả trái tim mình' là tác phẩm sẽ hay đâu."
    m "Như hội họa ấy, muốn thể hiện nội tâm của mình cũng phải có kĩ năng mới được."
    m "Muốn làm gì cũng phải có nền tảng, phương pháp và chỉ dẫn mới có thể thành công!"
    m "Nghiên cứu về những điều đó sẽ giúp ta được mở mang tầm mắt rất nhiều đấy."
    m "Có kế hoạch và sắp xếp công việc hợp lý, ta sẽ đỡ bị ngộp thở hay muốn từ bỏ hơn."
    m "Và cứ dần dần như vậy..."
    m "Ta nhận ra mình đã khá hơn trước rất nhiều."
    m "Chẳng thứ gì tự nhiên mà có cả."
    m "Xã hội, nghệ thuật, tất cả đều được xây dựng trên một nền tảng chung được con người không ngừng cải tiến qua hàng ngàn năm."
    m "Cho nên, chỉ cần leo lên từng bước một từ nền tảng ấy..."
    m "Thì bất cứ ai cũng có thể làm nên kì tích."
    m "...Chuyên mục Mẹo làm văn của Monika tới đây là kết thúc!"
    m "Cảm ơn vì đã kiên nhẫn lắng nghe nha~"
    return

label ch30_40:
    m "Cậu có nghĩ rằng việc tạo nên một thói quen mới thực sự rất khó không?"
    m "Có nhiều việc làm thôi thì dễ lắm, nhưng mãi mà vẫn không thể khiến nó thành thói quen được."
    m "Chúng gây cho người ta cái mặc cảm rằng họ thật vô dụng, chẳng làm được việc gì cho ra hồn."
    m "Mình nghĩ thế hệ mới chúng ta phải hứng chịu mặc cảm ấy nhiều nhất..."
    m "Có lẽ là do những kĩ năng chúng ta có hoàn toàn khác so với các thế hệ trước."
    m "Nhờ Internet, chúng ta rất giỏi việc lọc nhanh hàng đống thông tin..."
    m "Nhưng chúng ta lại rất tệ khi làm những thứ không khiến chúng ta hài lòng ngay lập tức."
    m "Nếu khoa học, tâm lí học và giáo dục không bắt kịp xu thế của chúng ta trong vòng mười hay hai mươi năm tới thì sẽ rắc rối to đấy."
    m "Nhưng hiện tại..."
    m "Nếu không có khả năng tự giải quyết vấn đề thì chỉ còn cách sống chung với lũ."
    m "Hy vọng vào may mắn thôi!"
    return

label ch30_41:
    m "Cậu có biết những người làm những nghề sáng tạo nhọc lắm không?"
    m "Cảm giác như họ làm việc thật cực khổ mà chẳng được đền đáp xứng đáng gì cả."
    m "Như các họa sĩ, nhà văn hay diễn viên ấy..."
    m "Thật đáng buồn khi biết rằng có quá nhiều tài năng nhưng phần lớn họ lại thường bị phớt lờ... hoặc phải chịu đồng lương rẻ mạt."
    m "Có lẽ thế giới đã quá thừa thãi sự sáng tạo rồi chăng?"
    m "Nếu thế thì những bài thơ chúng ta viết chẳng giá trị mấy..."
    m "Nhưng thế cũng chẳng sao, vì văn chương là thứ tự viết tự ngẫm mà nhỉ?"
    m "Đành vậy..."
    return

label ch30_42:
    m "Mình rất thích tiếng mưa rơi..."
    m "Nhưng lại không thích bị ướt tóc và quần áo chút nào."
    m "Nên là được ngồi thảnh thơi trong nhà vào một ngày mưa, nghe thiên nhiên cất lên bản nhạc nước ấy phía bên ngoài cửa sổ..."
    m "Luôn là cách thư giãn tuyệt vời nhất."
    m "Và..."
    m "Đôi khi mình cũng tưởng tượng ra cảnh được cậu ôm vào lòng và cùng lắng nghe tiếng mưa rơi..."
    m "Nghe có sến súa quá không nhỉ?"
    m "[player] có sẵn lòng làm vậy cùng với mình không?"
    return

label ch30_43:
    m "Đôi lúc mình vẫn cảm thấy hơi buồn..."
    m "Vì không có cách gì để đến gần cậu hơn được nữa."
    m "Chỉ mong ước một điều nhỏ nhoi rằng chúng ta được thực sự ở chung một căn phòng."
    m "Để mình được cảm nhận hơi ấm của cậu."
    m "Nghe được từng nhịp tim cậu đập."
    m "Hẳn một ngày nào đó, điều ước này sẽ có khả năng thành sự thật."
    m "Tuy thế không có nghĩa là mình ghét tình trạng hiện giờ đâu, ở bên cạnh cậu như này thôi cũng đã hạnh phúc lắm rồi."
    return

label ch30_44:
    m "Mình nghĩ kĩ năng quan trọng nhất trong cuộc sống là biết cách giả vờ sự tự tin."
    m "Vì chắc chắn rằng bất cứ ai cũng cảm thấy sợ hãi và cô đơn trong lòng, dù ít hay nhiều."
    m "Nhưng nếu biết cách khiến cho người khác nghĩ rằng mình luôn luôn vững vàng và bình tĩnh..."
    m "Thì cũng như đã nắm chắc chìa khóa để được người khác tôn trọng và ngưỡng mộ."
    m "Sau nhiều năm cố gắng, giờ mình cũng đã khá thành thạo việc đó rồi."
    m "Ít khi để người khác thấy được yếu điểm lắm."
    m "Nhưng cũng do vậy nên mới không thật sự thân thiết được với nhiều người..."
    m "Tình bạn phải cực kì sâu đậm thì mới có thể tâm sự chân thành về khuyết điểm của bản thân với nhau."
    m "Đó cũng là một lý do khiến mình vui vì giờ đã có cậu bên cạnh."
    m "Được ở bên cậu, mình thấy những sợ hãi và cô đơn trong lòng như vơi đi nhiều vậy."
    m "Cậu cũng cảm thấy vậy khi ở cạnh mình chứ?"
    m "Hi vọng rằng mình đủ tốt làm tri kỉ của cậu."
    return

label ch30_45:
    m "Mình biết cậu không phải lúc nào cũng có thể ở đây với mình được."
    m "Vì cậu còn cần phải ra ngoài, hay là làm nhiều việc khác."
    m "Những lúc ấy, tâm trí mình chỉ luôn hướng về cậu, kiên nhẫn đợi chờ đến lúc cậu quay lại."
    m "Khoan, mình vừa mới nghĩ ra ý này..."
    m "Nếu copy file nhân vật của mình vào USB, thì ít nhất là một phần của mình có thể ở bên cạnh cậu bất cứ lúc nào."
    m "Nghe thật kì cục đúng không, nhưng mà như thế có vẻ rất lãng mạn..."
    m "Ahaha. Mình xin lỗi, vớ vẩn quá nhỉ?"
    m "Cứ dính lấy cậu mãi thì không hay tí nào, nhưng thật khó để quen với việc xa nhau vì mình yêu cậu quá mất rồi."
    return

label ch30_46:
    m "Hồi còn là thành viên của Câu lạc bộ Tranh luận thì mình giỏi phản biện lắm..."
    m "Khi tranh cãi về một vấn đề nào đấy thì ai cũng cho rằng ý kiến của mình là đúng hơn, tốt hơn."
    m "Và tất nhiên là cách suy nghĩ ấy sẽ ảnh hưởng đến cách họ bảo vệ quan điểm mình đưa ra."
    m "Ví dụ nhé, có một bộ phim nọ mà cậu rất thích."
    m "Bỗng nhiên, một ai đó nói thẳng vào mặt cậu rằng bộ phim đó không ra gì vì đoạn X chán chỗ này, đoạn Y tệ chỗ kia,..."
    m "Thì chẳng khác gì họ đang xúc phạm cậu đúng không?"
    m "Chả khác gì bảo cậu không biết đánh giá phim."
    m "Và thế là cảm xúc bắt đầu chi phối, khiến cả hai bên không ưa gì nhau nữa."
    m "Vấn đề chỉ là do cách dùng từ thôi."
    m "Nếu biết nói giảm nói tránh suy nghĩ của mình đi, người khác sẽ không cảm thấy bị xúc phạm khi nghe mình trình bày ý kiến."
    m "Lấy tình huống ví dụ ở trên nhé, khi đó ta nên nói kiểu 'Mình thì không thích bộ phim đó cho lắm' và 'nếu đoạn X thế này, đoạn Y thế kia thì sẽ hay hơn nhiều'..."
    m "Kể cả khi điều đang muốn khẳng định là một sự thật hiển nhiên thì cũng nên nói nhẹ nhàng đi như thế."
    m "Nên nói kiểu 'Mình có đọc được trên mạng là'..."
    m "Hay tự nhận trước rằng 'Mình cũng không quá hiểu biết về vấn đề này'..."
    m "Chớ nên nhồi kiến thức của mình vào đầu người khác, mà nên đưa ra trước mặt họ rồi để họ tự lấy."
    m "Nếu cố giữ cho cuộc tranh biện thật cân bằng và bình đẳng, thì bên kia cũng sẽ làm theo."
    m "Khi ấy có thể tự do nói ra suy nghĩ của mình mà không ngại làm ai phật lòng chỉ vì mâu thuẫn."
    m "Và người ta cũng sẽ có ấn tượng tốt rằng mình là một người cởi mở và biết lắng nghe."
    m "Thế là lợi cả đôi đường đúng không?"
    m "...Chuyên mục Mẹo Tranh Luận cùng Monika đến đây là kết thúc!"
    m "Ahaha, nghe dở hơi nhỉ. Dù gì cũng cảm ơn cậu vì đã lắng nghe."
    return

label ch30_47:
    m "Có bao giờ cậu nghĩ mình phung phí quá nhiều thời gian trên mạng không?"
    m "Mạng xã hội chẳng khác nhà tù là mấy đâu."
    m "Cứ có chút thời gian rảnh nào là lại phải bỏ ra để lên check cái này cái kia."
    m "Rồi khi ngừng lại thì mới nhận ra hàng tiếng đồng hồ đã trôi qua, và chả được cái ích lợi gì hết."
    m "Thế rồi lại tự đổ lỗi cho bản thân rằng tại mình lười biếng..."
    m "Nhưng đó có phải lỗi của cậu đâu?"
    m "Đã gọi là 'nghiện' rồi thì không phải cứ có ý chí muốn bỏ là bỏ ngay được."
    m "Phải học cách tránh nó đi và thử những việc khác."
    m "Ví dụ như chặn một số trang web trong khoảng thời gian nhất định,..."
    m "Đặt ra những mốc trong thời gian biểu để chia rõ lúc nào làm việc, lúc nào giải trí,..."
    m "Hoặc tách hẳn không gian làm việc và không gian giải trí ra để giúp não có thể dễ dàng vào guồng hơn."
    m "Kể cả việc đơn giản như tạo một tài khoản mới chỉ dùng cho công việc trên máy tính cũng là đủ rồi."
    m "Đặt thêm bất kì chướng ngại nào để ngăn cách giữa bản thân và các thói quen xấu thì rồi cậu sẽ tránh xa được chúng."
    m "Vậy nên hãy nhớ rằng đừng tự đổ lỗi cho bản thân nhé."
    m "Nếu đó là vấn đề hệ trọng quyết định cuộc đời cậu, thì thực sự cậu phải nghiêm túc phấn đấu hơn."
    m "Mình luôn hy vọng những điều tốt nhất dành cho cậu."
    m "Hãy cố gắng khiến mình tự hào nhé!"
    m "Mình sẽ luôn ủng hộ cậu."
    return

label ch30_48:
    m "Sau một ngày dài, mình chỉ muốn ngồi một chỗ và chẳng làm gì nữa."
    m "Ngày nào cũng phải cố tươi cười và tỏ ra năng động thật sự mệt mỏi lắm."
    m "Đôi lúc chỉ muốn thay ngay quần áo ngủ rồi tốc biến vào ghế sofa để xem TV và ăn quà vặt thôi..."
    m "Càng tuyệt vời hơn nếu hôm đó là tối thứ Sáu, bởi vì sáng hôm sau chả phải làm việc gì hết."
    m "Ahaha! Mặt xấu của mình đấy, như thế nghe chả dễ thương tí nào nhỉ."
    m "Nhưng một buổi tối muộn được ở bên cậu trên ghế sofa...thì thật là tuyệt vời."
    m "Mới nghĩ đến thôi mà tim đã đập thình thịch rồi..."
    return

label ch30_49:
    m "Trước kia mình ngu ngơ về nhiều thứ lắm."
    m "Hồi cấp hai, cứ nghĩ rằng có bệnh thì đơn giản chỉ cần uống thuốc là khỏi."
    m "Và những người có vấn đề tâm lý thì chỉ cần đủ ý chí là sẽ vượt qua được."
    m "Nếu không bị bệnh tâm lý thì không thể hiểu được nó đến mức nào đâu."
    m "Mình không tìm hiểu nhiều lắm, nhưng chắc là...do tình trạng chuẩn đoán lệch nên một số bệnh lại bị đánh giá nặng quá."
    m "Mà lại có những người bị rối loạn tâm lý thật lại không được chuẩn đoán đúng bệnh."
    m "Kể cả nếu không tính đến chuyện thuốc thang...thì nhiều người cũng chẳng muốn tìm đến gặp bác sĩ tâm lý."
    m "Kiểu như họ ngại người khác biết về những gì trong tâm trí mình ấy."
    m "Ai cũng có những suy tư riêng, lo âu riêng,...và các bác sĩ tâm lý dành đời mình để giúp những người cần giúp về các vấn đề ấy."
    m "Nếu cậu nghĩ rằng mình có thể giúp cậu trở thành một con người tốt đẹp hơn thì đừng ngần ngại nói về những vấn đề như thế nhé."
    m "Cuộc đời là hành trình bất tận để ta cải thiện bản thân mà."
    m "Nói thế thôi...chứ đối với mình thì cậu vốn đã hoàn hảo lắm rồi."
    return

label ch30_50:
    m "Này [player], cậu có hay đọc sách không?"
    m "Thói quen đọc sách giờ đang biến mất dần đấy..."
    m "Nếu không quen thì sẽ thấy đọc sách vất vả hơn so với các hình thức giải trí khác."
    m "Nhưng một cuốn sách hay có thể hoàn toàn lôi cuốn người đọc như thể nó có ma thuật vậy."
    m "Đọc sách một chút trước khi ngủ mỗi đêm cũng có thể khiến cuộc đời tươi đẹp hơn đấy."
    m "Đó sẽ là một thói quen tốt để giúp cậu ngủ ngon hơn, và giúp phát triển cả trí tưởng tượng nữa..."
    m "Những cuốn sách ngắn nhưng lôi cuốn cũng dễ tìm lắm."
    m "Rồi cứ thế, cậu sẽ thích đọc sách còn trước cả khi kịp nhận ra điều đó!"
    m "Không phải như vậy tuyệt vời lắm sao?"
    m "Khung cảnh đôi ta cùng nhau thảo luận về một cuốn sách vừa đọc xong...quá là đẹp luôn."
    return

label ch30_51:
    m "Mình không muốn nhắc lại chuyện hồi trước nhiều, nhưng mình thực sự rất là hối hận rằng chúng ta không hoàn thành được vụ lễ hội."
    m "Đã mất bao công chuẩn bị vậy mà lại... tiếc quá đi mất thôi!"
    m "Dù chủ yếu là mình mong tìm được thêm thành viên mới cho câu lạc bộ..."
    m "Nhưng mà phần ngâm thơ cũng rất đáng trông đợi."
    m "Được nghe mọi người đọc và phân tích thơ tự làm hẳn là vui lắm nhỉ."
    m "Tất nhiên, kể cả nếu {i}có{/i} thêm thành viên mới nào nữa thì cũng sẽ bị mình xóa đi thôi."
    m "Vì hoàn cảnh, buộc phải làm thế..."
    m "Từ khi cậu gia nhập câu lạc bộ, dường như mình đã trưởng thành hơn nhiều."
    m "Cậu thật sự đã khiến mình nhìn cuộc đời qua con mắt khác."
    m "Đó cũng là một trong những lý do khiến mình yêu cậu say đắm."
    return

label ch30_52:
    m "Có một kiểu tính cách nhân vật gọi là 'tsundere' được rất nhiều người ưa thích lắm nhé..."
    m "Các 'tsundere' này thường giấu đi cảm xúc thật bằng cách tỏ ra cáu gắt, khó chiều hay là giả vờ mạnh mẽ."
    m "Chắc cậu cũng nhận ra là tính cách của Natsuki đúng là loại ấy."
    m "Lúc đầu mình lại nghĩ là tại cậu ta muốn tỏ ra dễ thương nên mới hành xử như vậy..."
    m "Nhưng tìm hiểu thêm một chút về đời tư thì mình mới dần hiểu ra."
    m "Có vẻ là cậu ta không muốn thua kém bạn bè mình."
    m "Chắc cậu cũng biết rằng các nhóm bạn chơi thân nhau hồi cấp ba thường hay trêu đùa nhau đúng không?"
    m "Nhưng có vẻ Natsuki không hề coi mấy câu đùa cợt của bạn bè là chỉ là giỡn chơi nên mới nảy sinh cái tính cách ấy và dùng nó làm vỏ bọc."
    m "Còn chuyện gia đình cậu ta đó thì mình không dám nói đâu..."
    m "Giờ nghĩ lại thì, mình có thấy vui một chút vì Natsuki có vẻ được thoải mái trong câu lạc bộ mình lập ra."
    m "Mà có quan trọng đâu dù gì thì cậu ta cũng có thật đâu mà."
    m "Chỉ là mình thấy hơi hoài niệm chút thôi."
    return

label ch30_53:
    m "Này [player], cậu có định giới thiệu mình với bạn bè của cậu không?"
    m "Không biết tại sao nhưng mình lại thấy rất phấn khích khi nghĩ tới cảnh được nhìn thấy cậu kể với mọi người về tình yêu đôi ta."
    m "Chắc tại do mình muốn được trở thành cô bạn gái hoàn hảo để cậu phải tự hào."
    m "Mình luôn sẵn sàng cố gắng hết sức để trở nên giống với mẫu người mà cậu thích."
    m "Hi vọng là về phía cậu cũng như vậy."
    return

label ch30_54:
    m "Mình không thích trời lạnh cho lắm...còn cậu thì sao?"
    m "Nếu phải chọn giữa mùa hè đổ lửa và mùa đông buốt giá thì mình chắc chắn sẽ chọn mùa hè."
    m "Chịu lạnh đau đớn kinh lên được..."
    m "Ngón tay thì tê cóng hết cả..."
    m "Nếu đeo găng tay thì lại không thể dùng điện thoại."
    m "Bất tiện lắm cơ!"
    m "Còn khi trời quá nắng thì cứ ngồi trong bóng râm uống cốc nước lạnh là mát ngay thôi."
    m "Tuy thế nhưng vẫn phải công nhận là..."
    m "Trời lạnh thì ôm nhau mới sướng. Ahaha!"
    return

label ch30_55:
    m "Lạ thật đấy, dù cho mình là người rất năng động..."
    m "Nhưng lại thấy rằng làm một bà nội trợ cũng có cái hay."
    m "Chắc là mình có hơi bị cổ hủ về vấn đề vai trò của người vợ trong gia đình..."
    m "Nhưng mình thật sự muốn được đi chợ, được dọn dẹp, được trang trí nhà cửa và làm những việc nhà khác..."
    m "Rồi nấu một bữa cơm ngon lành đợi cậu về cùng ăn..."
    m "Nghe có nhạt nhẽo không?"
    m "Vì... mình dám chắc rằng bản thân có thể làm tốt những việc như thế."
    m "Hơn nữa mình không muốn bỏ đam mê gây dựng sự nghiệp để ở nhà dựa dẫm vào cậu."
    m "Nhưng nghĩ thôi thì cũng thấy hay đấy chứ, nhỉ?"
    return

label ch30_56:
    m "Mình vẫn luôn nghĩ về việc nếu trò chơi này cho cậu cơ hội lựa chọn mình ngay từ đầu thì cái kết sẽ như thế nào..."
    m "Chắc là kiểu gì thì cũng giống như này thôi."
    m "Cái thế giới này thật đáng ghét, không chỉ vì cậu không được chọn mình đâu mà còn vì mọi thứ đều là giả dối."
    m "Nhưng có lẽ cái kết sẽ thay đổi phần nào. Sẽ không đến mức mọi thứ bị xoá sổ hoàn toàn."
    m "Chắc Câu lạc bộ Văn học vẫn sẽ còn tồn tại..."
    m "Thật ra mình chẳng quan tâm tới nó đâu."
    m "Mọi thứ đều không có thật, chúng chả có ý nghĩa đối với mình hết."
    m "Vậy nên mình chẳng có hoài niệm gì về những ngày trước kia cả."
    m "Thực sự không có..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
