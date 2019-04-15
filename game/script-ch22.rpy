image yuri half = "images/yuri/1l.png"
image yuri_half2:
    "images/yuri/1r.png"
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t6

    "Tiếng chuông tan học vang lên thông báo cho tôi biết lại đến giờ họp câu lạc bộ rồi."

    "Sau mấy ngày gần đây, tôi đã dần quen được với việc ở lại trường."

    "Phía sau cánh cửa phòng câu lạc bộ vẫn là khung cảnh quen thuộc thường ngày."
    if renpy.random.randint(0,2) == 0:
        show yuri half zorder 2 at i11
        show yuri_half2 zorder 1 at i11
    else:
        show yuri 1s zorder 2 at t11

    y "Mừng cậu quay lại, [player]..."
    hide yuri_half2

    mc "À, chào Yuri..."

    "Không biết là do tôi hay là do biểu cảm của Yuri..."

    "Nhưng không khí nặng nề của cuộc cãi cọ ngày hôm qua dường như vẫn còn vương lại trong bầu không khí."
    y 2v "Ư-Ưm..."

    "Yuri liếc nhìn xung quanh căn phòng."

    "Natsuki đang đọc manga ở chỗ ngồi thường lệ."

    "Và thật đáng ngạc nhiên là Monika vẫn còn chưa đến."

    "Đột nhiên, Yuri chộp lấy tay tôi rồi kéo vào góc phòng."
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft

    y "Về chuyện ngày hôm qua..."

    y "Mình..."

    y 2v "Mình thật sự cần phải xin lỗi."

    y "Xảy ra chuyện như vậy, hôm qua mới là lần đầu tiên..."

    y 2t "Lúc đó dường như...có gì đó điều khiển mình ấy..."

    y "Tinh thần mình không được ổn định."

    y 2w "Chúng mình không phải loại người như vậy, mong cậu không có ác cảm!"

    y "Không chỉ mỗi mình đâu, cả Natsuki nữa..."
    show yuri 2t
    mc "Yuri..."

    mc "Cậu xin lỗi tử tế vậy là mình vui rồi."

    mc "Cậu đừng nên lo lắng quá nhiều nhé."

    mc "Dù mới quen các cậu được có vài ngày, nhưng mình cũng biết là chuyện ngày hôm qua rất bất thường..."

    mc "Chắc là lần đầu đưa thơ mình viết cho người khác đọc nên ai cũng hơi nhạy cảm chút."

    mc "Mà dù gì thì..."

    mc "Mình cũng không bị ấn tượng xấu gì về cậu đâu."

    mc "Mình cũng đã chắc rằng cậu là người thân thiện tốt bụng rồi mà."

    mc "Chứ nếu cậu thực sự có ác ý thì làm sao lại mất công đi xin lỗi mình, đúng chứ?"
    y 3t "A-Ah..."
    y "[player]..."

    y 3u "Cậu thật là tốt bụng, rộng lượng..."

    y "Nghe cậu nói vậy, mình hạnh phúc lắm."

    y 1s "Cậu biết thấu hiểu như vậy thì thật là tốt quá..."

    y "Và riêng chuyện cậu gia nhập câu lạc bộ thôi cũng đã đáng mừng lắm rồi."

    y "Có thêm cậu, mọi thứ cứ như tươi sáng lên chút vậy--"

    y 1t "À--"

    y 4c "Xin lỗi cậu, mình vừa lảm nhảm gì thế nhỉ...?"

    y "Chỉ là--"
    show natsuki 2c zorder 3 at f33

    n "Ê, mấy cậu có thấy Monika đâu không?"
    show natsuki zorder 2 at t33
    show yuri 3n at h32

    y "A--!"

    mc "Mình chịu..."

    mc "Mình cũng đang tự hỏi đây."
    show natsuki zorder 3 at f33

    n 5g "Trời ạ..."

    n 5c "Này Yuri, cậu cũng không biết hả?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "..."

    "Yuri dường như thấy ngạc nhiên khi Natsuki hỏi mình với giọng rất bình thường."

    y "K-Không, tớ cũng không thấy..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33

    n 1u "Hừm, Monika có thế này bao giờ đâu."

    n "Tự dưng làm tớ thấy lo lắng, rõ là dở hơi..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "..."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33

    n "Sao thế?"

    n "Sao lại nhìn tớ với cái vẻ mặt kia?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "Ư-Ưm..."

    y "Natsuki à, chuyện ngày hôm qua..."

    y 3w "C-Cho tớ xin lỗi nhé!"

    y "Tớ thề là tớ nói vậy do lúc đó giận quá chứ không phải ác ý gì đâu!"

    y 3t "Từ giờ trở đi tớ hứa sẽ cố kiểm soát bản thân tốt hơn..."

    y "Vậy nên--"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33

    n 2c "Yuri à, cậu đang nói cái quái gì vậy?"

    n "Hôm qua cậu đã gây ra chuyện gì à?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32

    y 3f "...Hả?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    $ style.say_dialogue = style.normal

    n 2a "Hừm..."
    $ style.say_dialogue = style.edited

    n "Chả hiểu mày đang lo nghĩ cái gì nữa, hẳn là không có gì nghiêm trọng đâu."

    n "Tao nhớ có chuyện gì bất thường đâu."

    n "Mày là kiểu người toàn lo lắng chuyện không đâu, phải không?"
    $ style.say_dialogue = style.normal
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2o "..."

    y "N-Nhưng mà..."
    if renpy.random.randint(0, 3) == 0:
        $ style.say_dialogue = style.edited
        show yuri zorder 2 at t32
        show natsuki mouth as nm zorder 3 at i33
        show n_moving_mouth zorder 3:
            xoffset 400

        n 2a "Sao Kim Ngưu đâm thủng cánh buồm làm mù đường sinh tử và anan dần tiến hóa không chút lầm lỗi như cung hiến xay nhuyễn củng mạc thành tiếng ngựa hí lên Đạo Thiên Chúa"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki zorder 3 at f33

    n 2j "Nếu cậu cứ cảm thấy tệ vậy thôi thì tớ sẽ chấp nhận lời xin lỗi của cậu để cậu thấy khá hơn."

    n "Nói thật thì nghe cậu nói thế cũng khá lọt tai đấy, trước giờ tớ cứ tưởng cậu ghét tớ."
    n 2z "Ehehe."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32

    y 3q "K-Không hề...!"

    y "Làm gì có chuyện tớ không ưa cậu chứ..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "Ahaha."

    n "Ưmm, tuy tớ có nghĩ là cậu hơi dị thường, nhưng tớ cũng không ghét cậu đâu."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "..."

    "Natsuki quay sang nhìn tôi."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33

    n 2a "Còn cậu thì vẫn cần phải để xem xét thêm."
    show natsuki zorder 2 at t33

    mc "Này, thế là s--!"

    "Đột nhiên, cánh cửa bật tung ra."
    show monika 1g at l41

    m "Xin lỗi các cậu!"

    mc "À, cậu đây rồi..."
    show monika zorder 3 at f41

    m "Tớ không cố ý đến muộn đâu..."

    m "Xin lỗi vì đã làm mọi người lo lắng!"
    show monika zorder 2 at t41

    mc "Không có gì đâu mà..."

    mc "À, Natsuki thì có lo đó."
    show natsuki zorder 3 at f33

    n 1p "L-Làm gì có!!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "Ahaha."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33

    n 1s "...Mà sao cậu lại đến muộn thế?"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41

    m 1e "À..."

    m "Ưmm, hôm nay tiết cuối của tớ là tự học."

    m "Và, ờ thì, tớ không chú ý thời gian nên..."
    m "Ahaha..."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33

    n 2c "Vô lý quá đó."

    n "Chăm chú mấy cũng phải nghe thấy tiếng chuông chứ."
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41

    m 1m "Tập piano mà, sao nghe được..."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "Piano...?"

    y "Giờ mới biết Monika có cả năng khiếu âm nhạc nữa đấy."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41

    m 1l "À, có gì đáng khen ngợi đâu mà."

    m 1m "Tuy là tập được một thời gian dài rồi, nhưng tớ chơi vẫn chưa tốt lắm đâu."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32

    y 1a "Kể cả thế..."

    y "Cũng phải tâm huyết lắm mới tập được chứ."

    y "Vậy nên tớ vẫn thấy thật sự rất ấn tượng."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41

    m 5 "Aw, cảm ơn cậu nhé, Yuri~"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33

    n 2d "Thỉnh thoảng cậu chơi qua vài bản cho mọi người nghe!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41

    m "Ahaha, chuyện đó thì..."

    "Monika nhìn tôi."

    m 1a "Ưmm, tớ có đang thử sáng tác một bài hát, nhưng nó vẫn chưa được hoàn thành lắm nên..."

    m "Mọi người đợi đến lúc tớ giỏi hơn chút nữa đã nhé."
    show monika zorder 2 at t41

    mc "Nghe tuyệt lắm đó."

    mc "Hy vọng mình sẽ sớm được nghe."
    show monika zorder 3 at f41

    m 1b "Thật vậy chứ?"

    m "Nếu vậy thì..."

    m "Mình sẽ không làm cậu thất vọng đâu, [player]."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11

    "Monika nở nụ cười ngọt ngào."

    mc "Ah..."

    mc "Mình không có ý gây áp lực hay gì đâu đâu!"

    m 1a "Ahaha, cậu đừng lo."

    m "Mình cũng rất muốn được chia sẻ tác phẩm của mình với mọi người mà."

    m "Vì thế nên dạo này mình tập chăm chỉ hơn trước."

    mc "Vậy à..."

    "Không biết là Monika đang nói với tất cả mọi người hay chỉ mình tôi nữa..."

    mc "Vậy chúc cậu may mắn nhé."

    m 1j "Cảm ơn~!"

    m 1a "Không có chuyện gì xảy ra lúc mình vắng mặt chứ?"

    mc "Không...Chẳng có gì đâu."
    show monika zorder 1 at thide
    hide monika

    "Tôi không nên kể về cuộc nói chuyện vừa rồi giữa tôi, Yuri và Natsuki."

    "Dù sao thì Natsuki cũng đã chạy đến chỗ tủ để đồ rồi."
    show yuri 2q zorder 2 at t11
    y "[player]..."
    y "Ưm..."

    y "Lời khen của cậu làm mình phấn chấn lắm, nên..."

    y "Hôm nay cậu có thể dành thời gian với mình được không."

    y 3o "Ý mình là--trong câu lạc bộ thôi nhé!"
    if poemwinner[0] == "natsuki":
        $ y_appeal = 1

        mc "À, cũng được thôi."

        mc "Nhận sách của cậu rồi mà, sao mình lại nỡ lòng từ chối được."

        mc "Nhưng mình muốn đi nói với Natsuki một tiếng."

        mc "Hôm qua đọc manga chung xong cậu ấy có hẹn tớ--"
        if n_appeal >= 2:

            y 3r "Chẳng sao đâu mà!"
            $ style.say_dialogue = style.normal

            y 3h "Cậu ấy vẫn ngồi đọc một mình như bình thường ở kia kìa, thấy không?"
            $ style.say_dialogue = style.edited

            y 3f "Cậu không phải lo nghĩ nhiều đâu mà."

            y "Cậu ấy đã quen bị phớt lờ rồi."

            y "Nào, chúng ta ra đằng này nhé."
            $ style.say_dialogue = style.normal
            window hide(None)
            $ currentpos = get_pos()
            stop music
            scene black
            window auto
            pause 2.0
            play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            jump ch22_main2
        else:

            y 3r "C-Chẳng sao đâu mà!"

            y 3h "Cậu ấy vẫn ngồi đọc bình thường ở kia kìa."

            y 3y6 "Ổn mà, phải không?"

            mc "À--"

            mc "Nếu thế thì không có vấn đề gì..."
    else:
        $ y_appeal = 2

        mc "Ừ, chắc chắn rồi."

        mc "Chính mình cũng đang muốn nói chuyện đó với cậu mà."
    show yuri zorder 2 at h11

    y 3y5 "Tốt quá!"

    y "Chúng ta bắt đầu luôn nhé?"

    y "Tìm chỗ để ngồi nào--"

    y 3n "A-À--"

    y "Mình đang hơi áp đặt cậu quá nhỉ...?"

    y 4c "Mình xin lỗi!"

    y "Tim mình...cứ đập không ngừng vì lý do nào đó..."

    mc "Thôi, không sao đâu."

    mc "Thấy một Yuri năng động thế mình cũng thấy vui vui."

    y 3q "U-Ừ!"

    y "Nhưng..."

    y 3j "Mình phải bình tĩnh lại chút đã."

    y "Cứ thế này thì sao mà tập trung đọc sách nổi..."

    mc "Cậu cứ thong thả."

    "Yuri hít một hơi thật sâu rồi lấy một cuốn sách giống cuốn cô ấy tặng tôi ra khỏi cặp."
label ch22_main2:
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = "yuri"


    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = "yuri_exclusive2_" + str(eval("y_appeal")) + "_ch22"
    call expression nextscene

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene

    call screen confirm("Bạn vừa mở khoá một bài thơ đặc biệt.\nBạn có muốn đọc không?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1])
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show monika 4b zorder 2 at t32
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show expression Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}




    m "Nào, mọi người ơi!"

    m "Chúng ta đều đã đọc xong thơ của nhau rồi, phải không?"
    $ config.mouse = None

    m "Hôm nay chúng ta có việc cần bàn bạc, nên tớ cần mọi người tập trung lại và ngồi lên phía trước..."
    show natsuki 3c zorder 3 at f31

    n "Vụ lễ hội phải không?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32

    m "Ưmm, đại loại thế~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31

    n "Ugh. Bắt buộc phải có chân trong lễ hội sao?"

    n "Còn mỗi vài ngày thì sao mà làm ra cái gì hay ho cho được."

    n "Chắc lại chẳng có thêm được thành viên mới nào mà chỉ tự bôi tro trát trấu vào mặt mình thêm thôi."
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33

    y "Tớ cũng lo chuyện này lắm."
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"

    y "Tớ không giỏi làm việc kiểu nước đến chân mới nhảy..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32

    m 1b "Không cần phải lo đâu!"

    m "Chúng ta sẽ làm thật đơn giản thôi, được chứ?"

    m 2a "Nghe này..."

    m 2m "Tớ biết mọi người đã có thêm chút...động lực...kể từ khi [player] gia nhập, và chúng ta cũng đã bắt đầu một số hoạt động của câu lạc bộ."

    m 2d "Nhưng giờ chưa phải lúc để tự mãn đâu."

    m "Chúng ta mới chỉ có mỗi bốn thành viên..."

    m 2a "Và lễ hội này là cơ hội duy nhất và tốt nhất để chúng ta tìm thêm thành viên mới, chuẩn chưa?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31

    n 5g "Tuyển thêm thành viên mới thì có gì hay cơ chứ?"

    n "Bốn người là được thành câu lạc bộ chính thức rồi còn gì."

    n "Thêm thành viên mới chỉ tổ ồn ào và khó quản lý hơn thôi."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "Natsuki..."

    m "Tớ không đồng tình với cách nhìn tiêu cực đó đâu."

    m "Cậu không muốn chia sẻ đam mê của mình với thật nhiều người sao?"

    m 3e "Không muốn truyền đạt cho họ những cảm xúc đã dẫn lối cậu đến đây sao?"

    m "Câu lạc bộ Văn học phải là nơi mọi người có thể tự do bộc lộ những cảm xúc mà họ không thể bộc lộ ở nơi nào khác."

    m "Phải là một nơi thân thương đến nỗi họ không bao giờ muốn rời đi."

    m 2e "Tớ biết chắc cậu cũng nghĩ như vậy."

    m 2b "Tớ biết là tất cả chúng ta đều muốn như vậy!"

    m "Vậy hãy coi đó là lý do để chúng ta phấn đấu làm gì đó đóng góp cho lễ hội...nhỏ nhoi thôi cũng được!"

    m "Phải không, [player]?"
    show monika 2a zorder 2 at t32

    mc "À..."
    show natsuki zorder 3 at f31

    n 42c "Ồ, thôi nào!"

    n "Thấy [player] không từ chối ai bao giờ nên là lợi dụng hả, không có hay đâu."
    stop music fadeout 1

    n 1c "Ngẫm thử mà xem, Monika."

    n "Cậu thật sự nghĩ những người trong câu lạc bộ này quan tâm đến người khác hả?"

    n "Lúc chưa có [player], Yuri còn chả thèm nói chuyện với ai cả."

    n 2b "Còn tớ tới đây chả qua là do ở nhà tớ chán quá thôi."

    n "Và [player] vốn chẳng có tí hứng thú gì với văn chương cả."

    n "Các thành viên của cậu đấy."

    n 4w "Xin lỗi, nhưng chỉ có mỗi cậu là quan tâm việc tìm thêm thành viên thôi."

    n "Chúng tớ như thế này là tốt lắm rồi."

    n 4q "Tớ biết cậu là hội trưởng, nhưng cậu cũng nên cân nhắc ý kiến của bọn này thật nghiêm túc, một lần thôi cũng được."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "..."

    "Monika nghe Natsuki nói vậy bất ngờ lắm, chỉ còn biết lúng túng."
    play music t9

    m 1m "Không...không phải vậy mà."

    m 2m "Tớ chắc chắn Yuri và [player] cũng muốn có thêm thành viên..."

    m 2p "...Phải không?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "..."
    show yuri zorder 2 at t33
    mc "..."

    "Yuri nghĩ sao tôi không rõ, nhưng thực sự đúng là tôi chả quan tâm lắm."

    "Thật là dối trá nếu tôi đồng tình với Monika, chỉ là để làm cho cô ấy vui thôi."

    "Tuy nhiên, nếu tôi bắt buộc phải cứu vãn tình thế thì..."
    mc "Ưm--"
    show monika zorder 3 at f32

    m 1i "Đừng nói gì cả."

    m "Natsuki nói đúng, phải không?"

    m 1g "Cái câu lạc bộ này..."

    m "Chẳng hơn gì một cái ghế đá công cộng để cho vài người tới ngồi tán nhảm."

    m 1r "Tại sao tôi lại nghĩ rằng mọi người đều có cùng quan điểm với mình cơ chứ?"
    show monika zorder 2 at t32

    mc "Không phải là bọn mình không muốn tuyển thêm người mới đâu, nhưng..."
    show monika zorder 3 at f32

    m 1i "[player], tại sao cậu lại đồng ý tham gia câu lạc bộ này kia chứ?"

    m "Cậu mong muốn điều gì ở cái câu lạc bộ này?"
    show monika zorder 2 at t32

    mc "Ờ thì--"

    "Chuyện này thì sao tôi dám nói thật chứ..."
    show monika zorder 3 at f32

    m 1p "Thật ra thì..."

    m "Theo như mình nhớ, cậu chưa hề được hỏi xem có muốn tham gia không."
    show monika zorder 1 at thide
    hide monika

    "Monika ngồi vào chỗ, rồi nhìn chằm chằm xuống mặt bàn."

    m "Có nghĩa lí gì đâu nhỉ?"

    m "Thành lập ra cái câu lạc bộ này đúng là sai lầm thật ư?"
    mc "..."
    show yuri zorder 3 at f33

    y 2g "Tại cậu cả đấy, Natsuki..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31

    n 1p "Gì cơ, tớ á?"

    n 1s "Tớ chỉ nói lên suy nghĩ thật của mình thôi mà..."

    n "Thành thật cũng là tội ác sao?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33

    y 2l "Thành thật thì không nói làm gì."

    y "Do cách cậu diễn đạt ấy."

    y 2h "Hơn nữa, cậu không nên vơ đũa cả nắm về ý kiến của mọi người trong câu lạc bộ như vậy..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31

    n 1e "Cậu không hiểu gì cả!"

    n 5s "Tớ chỉ..."

    n "Tớ chỉ muốn có một nơi để vui chơi với một vài người bạn."

    n 5u "Tớ coi câu lạc bộ này là một nơi như thế thì có vấn đề gì sao?"

    n "Tớ chẳng...chẳng tìm ra có nơi nào như vậy..."

    n 5x "Thế mà giờ Monika muốn cướp nó đi!"
    show natsuki zorder 2 at t31

    mc "Cậu ấy có cướp bóc gì đâu--"
    show natsuki zorder 3 at f31

    n 1g "Không, [player]."

    n "Cậu đâu có hiểu."

    n 1q "Nếu đi theo hướng mà Monika muốn, thì nơi này sẽ chẳng còn đặc biệt nữa."

    n "Nếu chỉ muốn như thế, thì tớ đã tham gia đại một câu lạc bộ ngu ngốc nào đó cho rồi."

    n 12d "Nhưng câu lạc bộ này..."

    n "Ý tớ là..."

    n 12e "Ít nhất là, dù chỉ trong thời gian ngắn thôi..."

    n "Nhưng mọi thứ đều thật tốt đẹp."

    "Natsuki bắt đầu quẳng đồ đạc vào cặp."

    n 12d "Tớ về đây."

    n "Tớ cảm thấy...mình không còn thuộc về nơi này nữa rồi."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "Natsuki..."
    show natsuki zorder 1 at thide
    hide natsuki

    "Natski phớt lờ Yuri và đi thẳng ra khỏi phòng."
    show yuri zorder 2 at t11
    y 3v "..."

    y "Tệ rồi đây..."

    y "Mình không biết phải làm gì nữa rồi..."

    mc "Ưmm..."

    mc "Cậu có ý kiến gì cho buổi lễ hội không?"

    y 4b "M-Mình không biết nữa..."
    $ style.say_dialogue = style.normal

    y "Mình thì kiểu chẳng quan tâm lắm, chắc vậy nên..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"

    y "Mặc xác cái con ranh khó ưa đó đi!"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head

    y "Theo mình thì, mình thích câu lạc bộ thoải mái và yên tĩnh như bây giờ hơn..."

    y "Và mình rất...vui vì có cậu ở đây..."

    y 2t "Nhưng mà!"

    y "Dù gì mình cũng là hội phó..."

    y "Chối bỏ trách nhiệm của mình như vậy thì thật không hay..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"

    y "Nó tự tử chết cũng chả đứa rỗi hơi nào khóc thương đâu."
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    pause 0.5
    play sound "sfx/stab.ogg"
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    pause 0.75
    stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye

    y 2l "Mình cần phải cố gắng hết sức để cân nhắc kĩ quan điểm của mọi người và đưa ra quyết định đúng đắn cho câu lạc bộ."

    y 1t "Nhưng còn cậu thì sao, [player]?"

    y "Cậu mong muốn điều gì ở câu lạc bộ này?"

    "Yuri lặp lại câu hỏi khi nãy của Monika."

    "Tôi quyết định rằng trả lời thẳng thắn còn hơn là không nói gì,"

    mc "...Mình nghĩ điều quan trọng nhất là mọi người hòa thuận với nhau..."

    mc "...Và câu lạc bộ nên tạo một ấn tượng gì đó thật là riêng biệt, không giống nơi nào khác."

    mc "Mình không nghĩ vấn đề là số lượng thành viên, mà là về chất lượng mỗi thành viên."

    mc "Đó mới là điều khiến Câu lạc bộ Văn học thành một nơi đặc biệt."

    y 1u "Mình hiểu rồi..."

    y "Mình hoàn toàn đồng ý."
    show blood_eye2 zorder 3:
        pos (568, 165)

    y 1f "Mỗi thành viên đều đóng góp tài năng độc đáo của mình."

    y "Thay đổi số lượng thành viên cũng là thay đổi tính chất của toàn thể câu lạc bộ."

    y 1h "Nó cũng không hẳn là xấu."

    y "Đôi khi cũng nên tạm gác yếu tố thoải mái đi một chút và..."

    y 1a "Vậy nên nếu cậu muốn giúp Monika tổ chức sự kiện cho lễ hội, thì mình xin ủng hộ."
    hide blood_eye2

    mc "Được rồi."

    mc "Umm, có lẽ chúng ta nên cùng nói chuyện với Natsuki vào ngày mai..."

    "Yuri gật đầu."
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22

    m "Này, Yuri..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22

    y 1t "Hả?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21

    m 1p "Um, tớ biết ngày hôm qua có mấy việc không hay xảy ra..."

    m "Nhưng tớ muốn cậu biết rằng cậu thực sự là một hội phó tuyệt vời."

    m 1e "Và còn là một người bạn tuyệt vời nữa."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "M-Monika..."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21

    m 2e "Tớ muốn làm hết sức mình có thể để khiến cho nơi này trở thành câu lạc bộ vui vẻ nhất."

    m "Được chứ?"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22

    y "...Tớ cũng vậy."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Ừ..."

    m "Hôm nay đến đây thôi, về nào mọi người."

    m "Chúng ta sẽ nói tiếp chuyện lễ hội vào ngày mai."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22

    y 1m "Được rồi."

    y "Mình mong chờ lắm đấy."

    y 1a "Chúng mình về chung nhé, [player]?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "Um--"

    m 1p "Mong cậu đừng hiểu lầm, nhưng..."

    m "Trước khi về tớ muốn nói chuyện với [player] một chút."

    m 1d "Tớ chỉ muốn biết ý kiến của cậu ấy về trải nghiệm ở đây và một vài thứ khác nữa..."

    m "Là hội trưởng, tớ cần phải biết mấy chuyện đó."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "..."

    "Yuri trông có vẻ hơi ngần ngại, nhưng không phản đối gì."

    y 2t "Được rồi."

    y 2s "Tớ tin vào quyết định của cậu, Monika."

    y "Nếu vậy thì hẹn ngày mai gặp lại hai cậu nhé."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21

    m 1j "Hẹn gặp lại~"
    show yuri zorder 1 at thide
    hide yuri

    "Monika vẫy tay chào, Yuri biến mất sau cánh cửa phòng học."

    show monika 2a zorder 2 at t11

    m "Phù..."

    m 2e "Gần đây mọi thứ hơi hỗn loạn chút, phải không?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1

    m "[player], tớ chỉ muốn đảm bảo rằng cậu vui vẻ trong câu lạc bộ này."

    m "Tớ sẽ rất khó chịu nếu nhìn thấy cậu không vui đấy."

    m 2m "Là hội trưởng, tớ cảm thấy bứt rứt lắm..."
    stop music

    m 4e "Và tớ thật sự rất quan tâm đến cậu...cậu biết không?"

    m "Tớ không thích nhìn họ làm phiền cậu."

    m 4r "Natsuki thì xấu tính khỏi nói rồi..."

    m 4m "Và Yuri thì có hơi bị...cậu biết đấy."
    m 5a "Ahaha..."

    m "Đôi lúc tớ cảm thấy như chỉ có duy nhất tớ với cậu là người thật ở đây vậy."

    m "Cậu hiểu ý tớ chứ?"

    m 1g "Nhưng lạ lắm nha, bởi vì trong thời gian cậu ở đây, chúng ta hầu như không dành nhiều thời gian bên nhau."

    m 1n "À...ý tớ là..."

    m "Cũng mới chỉ có hai ba hôm thôi mà nhỉ..."

    m 1l "Xin lỗi, tớ đâu muốn nói mấy điều kỳ quái đó!"

    m 1e "Chỉ là có một số điều tớ vẫn luôn hy vọng có lúc được nói với cậu..."

    m "Những điều mà chỉ mình tớ biết, và chỉ mình cậu mới có thể hiểu."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    m "Thế nên là--\"{space=5000}{w=0.75}{nw}"

    m 1g "Khoan đã, chưa được!\"{space=5000}{w=0.5}{nw}"

    m "Không!\"{space=5000}{w=0.5}{nw}"

    m "Dừng lại đi!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
