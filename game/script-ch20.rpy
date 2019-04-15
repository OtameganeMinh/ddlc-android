label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:

    "Ngày đi học của tôi vẫn luôn như vậy, thật là nhàm chán."

    "Buổi sáng là thời điểm tồi tệ nhất, tôi bị vây quanh bởi các cặp đôi và những nhóm bạn đến trường cùng nhau."

    "Còn tôi, vẫn luôn đi một mình suốt bao lâu nay."

    "Tôi luôn tự nhủ rằng đã đến lúc tôi nên kết bạn, tán gái,..."

    "Nhưng tôi thậm chí còn chả tham gia một câu lạc bộ nào ở trường."

    "Tôi khá là chắc chắn rằng việc giành thời gian rảnh cho game và anime là một quyết định đúng đắn."

    "Ở trong trường cũng có câu lạc bộ Anime đấy nhưng làm quái gì có đứa con gái nào trong đó chứ..."

    scene bg class_day
    with wipeleft_scene


    "Một ngày đi học tẻ nhạt như bao ngày khác, kết thúc trước cả khi tôi kịp nhận ra."

    "Sau khi thu dọn đồ đạc, tôi nhìn mông lung vào bức tường, cố gắng tìm cho bản thân một mẩu động lực."

    mc "Câu lạc bộ..."

    "Sẽ chả có cái nào khiến tôi hứng thú đâu."

    "Rõ ràng là những công việc phải làm cho câu lạc bộ thật là phiền phức."

    "Chắc tôi không còn lựa chọn nào khác ngoài việc cứ xem thử câu lạc bộ Anime..."

    $ m_name = "???"

    m "...[player]?"
    window hide(None)
    show monika g2 zorder 2 at t11
    pause 0.75
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show monika 1 zorder 2 at t11

    mc "...Monika?"
    $ m_name = "Monika"

    m 1b "Ôi trời, mình không ngờ là sẽ được gặp cậu ở đây!"

    m 5 "Đã lâu lắm rồi đấy, nhỉ?"

    mc "À..."

    mc "Ừ, đúng vậy."

    "Monika mỉm cười hiền hậu."

    "Nói là quen nhau nhưng chúng tôi chỉ là học cùng một lớp năm ngoái và lại còn rất hiếm khi nói chuyện."

    "Monika có lẽ là cô gái nổi tiếng nhất lớp - Vừa xinh đẹp lại còn thông minh, giỏi cả thể thao nữa."

    "Về cơ bản, cô ấy quá là ngoài tầm với của tôi."

    "Vì thế, chỉ với nụ cười thôi mà khiến tôi cảm thấy hơi..."

    mc "Mà, cậu đến đây để làm gì vậy?"

    m 1a "À, mình đang tìm một số thứ để dùng cho hoạt động ở câu lạc bộ."

    m 1d "Ở đây còn giấy thủ công không?"

    m "Hoặc là bút dạ cũng được?"

    mc "Cậu thử kiểm tra trong tủ kia xem."

    mc "...Cậu là thành viên của câu lạc bộ Tranh Luận, đúng không?"

    m 5 "Ahaha, về chuyện đó thì..."

    m "Mình đã bỏ câu lạc bộ Tranh Luận rồi."

    mc "Thật ư?"

    m "Ừ..."

    m 2e "Giữa các câu lạc bộ lớn thường có xung đột, thành thật mà nói thì mình chả ưa chúng tí nào."

    m "Ngán ngẩm làm sao khi phải tranh luận về vấn đề ngân sách, làm thế nào để chuẩn bị cho các sự kiện công khai này nọ...."

    m "Mình thì muốn làm những gì mà bản thân thấy thích thú và tạo ra những điều khác biệt."

    mc "Nếu vậy, cậu quyết định tham gia câu lạc bộ nào?"

    m 1b "Thực ra, mình đang thành lập một câu lạc bộ mới!"

    m "Câu lạc bộ Văn Học!{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)

    m "Câu lạc bộ Văn Học!{fast}"
    window auto

    mc "Văn Học...?"

    "Nghe có vẻ khá...ngớ ngẩn?"

    mc "Cậu đã có bao nhiêu thành viên rồi?"

    m 5 "Ưm..."

    m "Ahaha..."

    m "Nói ra thì thật là xấu hổ, nhưng hiện tại bọn mình mới chỉ có ba người."

    m "Thật khó để tìm thêm thành viên mới cho một thứ nghe thật nhàm chán..."

    mc "Ờ, cái đó thì mình hiểu..."

    m 3d "Nhưng nó thật sự không nhàm chán chút nào đâu, rồi cậu xem!"

    m "Văn học có nhiều thứ hay ho lắm. Đọc sách, viết truyện, làm thơ..."

    m 3e "Một thành viên còn giữ cả một bộ sưu tập manga của bạn ấy trong phòng câu lạc bộ..."

    mc "Chờ đã...thật vậy ư?"

    m 2k "Ừ, thật là hài hước, nhỉ?"

    m 2e "Bạn ấy luôn luôn nhấn mạnh rằng manga cũng là văn học."

    m "Ừ thì, mình đoán là bạn ấy cũng có phần đúng..."

    m "Dù sao thì bạn gái đó cũng là một thành viên câu lạc bộ Văn Học cơ mà?"

    "...Hình như Monika vừa nhắc đến chữ \"gái\"?"

    "Hmm..."

    m 1a "Này, [player]..."

    m "Hình như cậu đang muốn tìm một câu lạc bộ để tham gia phải không?"

    mc "Ah--"

    mc "Ừ thì...có lẽ vậy."

    m "Thế thì..."

    m 5 "Cậu làm giúp mình việc này nhé?"

    m "Mình không ép cậu tham gia đâu, nhưng..."

    m "Chí ít cậu hãy đến xem qua câu lạc bộ của mình nhé, nếu cậu chấp nhận thì tuyệt quá."

    m "Làm ơn đi?"

    mc "Um..."

    "Tôi chẳng có lý do gì để từ chối cả..."

    "Dù sao thì sẽ thật là ngu ngốc nếu từ chối một cô gái như Monika."

    mc "Được thôi, mình sẽ tới đó luôn đây."

    m 1k "Aah, được thế thì còn gì bằng!"

    m 1b "Cậu thật là một người dễ mến đấy [player] à?"

    mc "Có gì đâu mà..."

    m 1a "Vậy, ta đi ngay thôi."

    m "Mình sẽ đi tìm mấy thứ kia sau - cậu quan trọng hơn."

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene


    "Phải nói sao nhỉ, hôm nay tôi đã bán linh hồn mình chỉ vì bị mê hoặc bởi nụ cười ấy."

    "Tôi ngại ngùng theo sau Monika từ đầu đến cuối trường và lên lầu trên - Khu vực mà ít khi tôi mò tới, nơi các anh chị năm ba học tập và tổ chức các hoạt động khác."

    "Monika tỏ ra vô cùng hăng hái, mở tung cánh cửa phòng học."

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
    else:
        show monika 3b at l31

    m "Tớ về rồi đây~!"

    m "Và tớ có đem về một vị khách!"
    show yuri 2t zorder 2 at t33
    if not config.skipping:
        show screen invert(0.15, 0.3)

    y "Hả?"

    y "Một...vị khách?"
    show natsuki 4c zorder 2 at t32

    n "Thiệt tình luôn, cậu đưa con trai vào đây à?"

    n "Tuyệt vời, không khí trong này bị ô nhiễm rồi."
    show monika 3m zorder 3 at f31

    m "Đừng xấu tính vậy chứ, Natsuki..."

    m 3b "...đừng để tâm nhé, chào mừng đến với câu lạc bộ, [player]!"
    show monika 3a zorder 2 at t31
    mc "..."

    "Tôi đứng ngây ra không đáp lại họ."

    "Tất cả thành viên của câu lạc bộ này..."

    "{i}...đều là những cô gái cực kì dễ thương!!{/i}"
    show natsuki zorder 3 at f32

    n 5c "Hừm, để tôi đoán xem..."

    n "Cậu là bạn trai của Monika, chuẩn chứ?"
    show natsuki zorder 2 at t32

    mc "Cái--"

    mc "Không, tôi không phải!"
    show yuri zorder 3 at f33
    y 2l "Natsuki..."
    $ n_name = 'Natsuki'

    "Cô gái với thái độ chua ngoa tên là Natsuki kia tôi chưa gặp bao giờ."

    "Dáng người nhỏ nhắn như vậy, chắc là năm nhất."

    show yuri zorder 2 at t33
    show monika zorder 3 at f31

    m 2l "Giới thiệu với cậu! Đây chính là Natsuki, luôn vui tươi như mọi khi..."

    m 2b "Còn đây là Yuri, Phó Chủ tịch của câu lạc bộ!"
    $ y_name = 'Yuri'
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f33

    y 4 "R-Rất vui được gặp cậu..."

    "Yuri, trông có vẻ trưởng thành và hơi nhút nhát, chắc không được hòa hợp lắm với người như Natsuki."
    show yuri zorder 2 at t33

    mc "Ừ... Rất vui được gặp hai cậu."
    show monika zorder 3 at f31

    m 1a "Tớ vô tình gặp [player] trong lớp học và cậu ấy đã quyết định sẽ đến xem thử câu lạc bộ."

    m "Chẳng phải rất tuyệt sao?"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32

    n 4e "Chờ đã! Monika!"

    n "Chẳng phải tớ đã bảo cậu phải nói cho tớ biết trước khi cậu định cho ai tham gia cơ mà?"

    n 4q "Tớ đã định bảo cậu...umm, cậu biết đấy..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31

    m 1e "Xin lỗi, tớ thành thực xin lỗi!"

    m "Tớ không quên điều cậu nói, nhưng việc gặp được cậu ta chỉ là tình cờ."
    show monika zorder 2 at t31
    show yuri zorder 3 at f33

    y 1a "Thôi không sao, ít nhất chúng ta vẫn có thể uống trà, như vậy được chứ?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f31

    m 1b "Umm, thế là được rồi!"

    m "[player], lại đây ngồi cho thoải mái."
    hide monika
    hide natsuki
    hide yuri
    with wipeleft

    "Các cô gái đã xếp vài chiếc bàn lại thành một cái bàn lớn."

    "Yuri đi đến góc phòng để mở tủ đồ."

    "Trong khi đó, Monika và Natsuki ngồi đối diện nhau."

    "Vẫn còn cảm thấy lúng túng, tôi đành ngồi cạnh Monika."
    show monika 1a zorder 2 at t11

    m "Mình biết cậu không thực sự muốn đến đây..."

    m "Nhưng cứ yên tâm là cậu sẽ thấy thoải mái như đang ở nhà."

    m 1j "Là hội trưởng của Câu lạc bộ Văn Học, nhiệm vụ của mình chính là khiến cho mọi người cảm thấy câu lạc bộ rất thú vị và vui vẻ!"

    mc "Mình còn thấy ngạc nhiên khi hội trưởng là Monika mà câu lạc bộ lại chưa có nhiều người."

    mc "Khởi đầu bao giờ cũng gian nan nhỉ."

    m 3b "Có lẽ vậy..."

    m "Chẳng mấy ai hứng thú về chuyện bỏ việc họ vẫn đang làm để bắt đầu một thứ gì đó mới mẻ..."

    m "Đặc biệt là những thứ không thu hút sự chú ý của số đông, như Văn Học chẳng hạn."

    m "Câu lạc bộ phải hoạt động cực kì chăm chỉ để chứng tỏ là Văn Học vui vẻ và bổ ích."

    m "Nhưng cái quan trọng nữa là phải đóng góp vào các sự kiện của trường, ví dụ như là lễ hội."

    m 2k "Mình tin rằng trước khi tốt nghiệp, chúng ta sẽ là một câu lạc bộ cực kì lớn mạnh!"

    m "Phải không, Natsuki?"
    show monika zorder 2 at t22
    show natsuki 4q zorder 2 at t21

    n "Umm..."

    n "...chắc vậy."

    "Natsuki miễn cưỡng đồng ý."

    "Tuy mỗi người một vẻ nhưng tất cả đều chung một mục đích..."

    "Monika chắc phải rất vất vả để tìm ra được hai người họ."

    "Yuri quay trở lại bàn cùng với khay ấm chén."

    "Cô ấy nhẹ nhàng đặt một tách trà trước mặt mỗi người rồi sau đó đặt ấm trà vào giữa bàn."
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    hide natsuki
    hide monika
    show yuri 1a zorder 2 at t21

    mc "Cậu giữ cả một bộ ấm chén trong phòng này à?"

    y "Đừng lo, giáo viên đã cho phép bọn mình rồi."

    y "Hơn nữa, thưởng thức một tách trà nóng cùng với một cuốn sách hay chả phải là sự kết hợp hoàn hảo sao?"

    mc "Ah... M-Mình đoán vậy..."
    show monika 4a zorder 3 at f22

    m "Ehehe, cậu không cần phải tỏ ra ấn tượng quá, Yuri nói văn vẻ làm màu thế thôi."
    show monika zorder 2 at t22
    show yuri at hf21

    y 3n "Hả?! T-Tớ không..."

    "Cảm thấy bị xúc phạm, Yuri quay mặt nhìn ra chỗ khác."

    y 4b "Ý của mình, cậu biết đấy..."
    show yuri zorder 2 at t21

    mc "Mình tin cậu mà."

    mc "Có lẽ là uống trà và đọc sách không phải gu của mình nhưng ít nhất thì mình cũng thấy ổn khi thưởng thức trà."
    show yuri zorder 3 at f21

    y 2u "Mình rất vui..."
    show yuri zorder 2 at t21

    "Yuri mỉm cười nhẹ nhõm."
    show monika zorder 1 at thide
    hide monika
    show yuri 1a zorder 2 at t32

    y "Thế, [player], cậu thích đọc những thể loại sách gì thế?"

    mc "À ừ thì...."

    "Dựa theo số lượng sách ít ỏi mà tôi đọc được trong mấy năm qua, tôi không thể nghĩ ra câu trả lời nào cho ổn được."

    mc "...Manga..."

    "Tôi lẩm bẩm, thật đúng là đùa mà."
    show natsuki 1c zorder 2 at t41

    "Đầu của Natsuki đột ngột nghểnh lên."

    "Hình như cô ấy muốn nói điều gì đó nhưng rồi lại tiếp tục im lặng."
    show natsuki zorder 1 at thide
    hide natsuki

    y 3u "C-Cậu không đọc nhiều, chắc là thế à..."

    mc "...À thì, có thể sau này sẽ khác mà...."

    "Tôi đang nói cái quái gì vậy?"

    "Tôi đã nói nhảm vì bối rối sau khi nhìn thấy nụ cười trừ với vẻ thất vọng trên khuôn mặt Yuri."

    mc "Bỏ qua chuyện đó đi, còn cậu thì sao Yuri?"

    y 1l "Để xem nào..."

    "Yuri dùng ngón tay lướt vòng quanh miệng tách trà."

    y 1a "Mình thích những tiểu thuyết về các thế giới kỳ ảo được xây dựng phức tạp và có chiều sâu."

    y "Mức độ sáng tạo và sự khéo léo của người tạo ra chúng thật đáng kinh ngạc."

    y 1f "Hoặc mấy truyện dị giới cũng khiến mình khá ấn tượng."

    "Yuri tiếp tục nói, thể hiện niềm đam mê đọc sách mãnh liệt của cô ấy."

    "Lúc đầu, ấn tượng của tôi về Yuri là một cô gái khiêm tốn và nhút nhát, tuy nhiên khi đắm chìm vào thế giới sách thì ánh mắt kia sáng rực lên, cứ như một Yuri khác hẳn."

    y 2m "Mình còn thích nhiều thể loại hơn thế nữa cơ."

    y "Những câu chuyện có yếu tố tâm lý sâu sắc khiến cho mình say đắm khi chìm vào chúng."

    y 2a "Thật là tuyệt vời làm sao khi mà tác giả lợi dụng chính trí tưởng tượng của người đọc để khiến diễn biến câu truyện cứ như là vô tận?"

    y "Dạo gần đây mình cũng dần chuyển sang đọc thể loại kinh dị..."

    mc "À, mình cũng đọc sách kinh dị một lần rồi...."

    "Tôi cố gắng hết sức có thể để nói được với Yuri một chút gì đó."

    "E rằng cứ như thế này, Yuri chả khác gì đang chuyện trò với một tảng đá cả."
    show monika 1j zorder 3 at f33

    m "Ahaha. Tớ biết là cậu thích thể loại ấy mà."

    m 1a "Nó rất hợp với tính cách của cậu."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32

    y 1a "Ơ, thật vậy ư?"

    y "Nhưng đúng là một cuốn sách khiến mình như có thể sang được thế giới khác thì mình không sao đặt nó xuống được."

    y "Một kiệt tác kinh dị thường thay đổi cách chúng ta nhìn thế giới, dù cho chỉ trong một khoảnh khắc ngắn ngủi."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31

    n "Ugh, tớ ghét thể loại truyện kinh dị..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32

    y 1f "Oh? Tại sao thế?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31

    n 5c "À thì, chỉ là..."

    "Đôi mắt của Natsuki liếc nhìn tôi trong một khoảnh khắc."

    n 5q "Thôi không có gì đâu."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33

    m 1a "Đúng rồi, là vì cậu chỉ luôn viết về những điều dễ thương, phải không Natsuki?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31

    n "G-Gì cơ?"

    n "Tại sao cậu lại nghĩ như vậy?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33

    m 3b "Sau buổi họp lần trước cậu có để quên một mảnh giấy nhỏ."

    m "Trên đó có một bài thơ cậu đang viết dở, tiêu đề của nó là--"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31

    n "Đừng có nói!!"

    n "Và trả mảnh giấy đây!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33

    m 1j "Rồi đây, đây~"
    show monika 1a zorder 2 at t33

    mc "Natsuki này, cậu sáng tác được thơ á?"
    show natsuki zorder 3 at f31

    n 1c "Hả? Ừ thì, thỉnh thoảng."

    n "Cơ mà sao cậu phải quan tâm chứ?"
    show natsuki zorder 2 at t31

    mc "Mình nghĩ điều đó thật đáng ngưỡng mộ."

    mc "Hay là hôm nào cậu cho mọi người xem cùng, được chứ?"
    show natsuki zorder 3 at f31

    n 5q "K-Không đời nào!"

    "Natsuki đảo mắt."

    n "Cậu sẽ...chẳng thích chúng đâu...."
    show natsuki zorder 2 at t31

    mc "Hả...Cậu không tự tin vào cách hành văn của mình sao?"
    show yuri zorder 3 at f32

    y 2f "Mình rất hiểu cảm giác của Natsuki."

    y "Chia sẻ tác phẩm của mình ở cái trình độ này thì tự tin không chưa đủ."

    y 2k "Hình thức thật sự của làm thơ là viết cho chính mình."

    y "Cần phải sẵn sàng cho người đọc thấy mọi thứ mà ta có, kể cả những điểm yếu, những thứ nằm sâu trong tâm can."
    show yuri zorder 2 at t32
    show monika 2a zorder 3 at f33

    m "Cậu có vẻ có nhiều kinh nghiệm viết lách hả, Yuri?"

    m "Hay là cậu thử chia sẻ một vài tác phẩm của bản thân để làm ví dụ để cho Natsuki cảm thấy tự tin hơn."
    show yuri at s32

    y 3o "..."

    mc "Yuri cũng như vậy à..."

    "Tất cả bỗng dưng lặng im."
    show monika zorder 3 at f33

    m 5a "Này, tớ có một ý tưởng!"

    m "Như thế này thì sao?"
    show monika zorder 2 at t33
    show natsuki 2k zorder 3 at f31
    show yuri 3e zorder 3 at f32

    ny "...?"

    "Natsuki và Yuri nhìn Monika với vẻ băn khoăn."
    show natsuki zorder 2 at t31
    show yuri zorder 2 at t32
    show monika zorder 3 at f33

    m 2b "Mỗi người hãy tự viết một bài thơ khi về nhà nhé!"

    m "Và trong lần gặp tiếp theo, tụi mình sẽ chia sẻ chúng!"

    m "Với cách đấy ai ai cũng sẽ như nhau!"
    show monika 2a zorder 2 at t33
    show natsuki zorder 3 at f31

    n 5q "U-Um..."
    show natsuki zorder 2 at t31
    show yuri 3v zorder 3 at f32

    y "..."
    show yuri zorder 2 at t32
    show monika 2m zorder 3 at f33

    m "À..."

    m "Ờ thì, tớ nghĩ đó là một cách hay..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32

    y 2l "Này..."

    y "...Tớ cũng nghĩ nó hay mà, Monika à."

    y 2f "Chúng ta nên bắt đầu làm những hoạt động chung mà cả câu lạc bộ đều có thể tham gia."

    y 2h "Dù sao thì với cương vị là hội phó..."

    y "Tớ muốn làm hết sức để ủng hộ cho sự phát triển của câu lạc bộ."

    y 2a "Với cả, chúng ta vừa có thêm một thành viên mới..."

    y "Kết hợp hai điều này lại sẽ là một bước đi lớn của chúng ta."

    y "Cậu cũng đồng tình phải không, [player]?"
    show yuri zorder 2 at t32

    mc "Khoan đã...Vẫn còn một vấn đề nữa."
    show monika zorder 3 at f33

    m 1d "Hả? Vấn đề gì vậy?"

    "Giờ thì mới đến cái chủ đề quan trọng nhất, tôi dồn hết dũng khí để nói ra điều mà tôi đang giữ trong đầu từ nãy đến giờ."
    show monika zorder 2 at t33

    mc "Mình chưa hề bảo rằng mình sẽ tham gia câu lạc bộ này!"

    mc "Monika mới chỉ thuyết phục mình đến xem thử chứ mình chưa hề ra quyết định nào"

    mc "Mình vẫn muốn xem qua một vài câu lạc bộ nữa, và...ừm...ờ..."
    show monika 1g
    show natsuki 4g
    show yuri 2e

    "Tôi đột ngột thấy cứng họng."

    "Cả ba cô gái đang ném cho tôi những ánh nhìn thất vọng."
    show monika at s33

    m 1p "N-Nhưng nhưng..."
    show yuri at s32

    y 2v "Mình xin lỗi, mình tưởng..."
    show natsuki at s31

    n 5s "Hừm."
    mc "Hả...?"

    "Các cô gái quay lại nhìn nhau rồi sau đó Monika lại hướng về phía tôi."
    show monika zorder 3 at f33

    m 1m "Tớ...đành phải nói với cậu việc này, [player]."

    m "Thật ra là..."

    m 1p "...Đây không phải câu lạc bộ chính thức do chưa có đủ số lượng thành viên."

    m "Cần phải có bốn người..."

    m "Bọn mình đã cố gắng hết sức để tìm thêm thành viên nhưng..."

    m "Nếu không có đủ người trước khi lễ hội diễn ra..."
    show monika zorder 2 at t33
    mc "..."

    "Tôi...tôi cảm thấy toàn thân mình mềm nhũn."

    "Ôi trời đất ơi, sao mà tôi đưa ra được quyết định sáng suốt trong lúc này đây?"

    "Tôi sẽ cảm thấy vô cùng tệ hại nếu làm mọi người thất vọng..."

    "Và hơn nữa, câu lạc bộ này có vẻ khá thoải mái..."

    "Kệ đi, tuy phải viết thơ nhưng được ở bên cạnh những cô gái xinh đẹp như này mỗi ngày thì...."

    mc "...Thôi được rồi."

    mc "Mình quyết định ngay bây giờ đây."

    mc "Mình sẽ tham gia Câu lạc bộ Văn Học của các cậu."
    show monika 1e zorder 2 at t33
    show yuri 3f zorder 2 at t32
    show natsuki 1k zorder 2 at t31

    "Mắt của bọn họ sáng lên, từng người từng người một."
    show monika zorder 3 at f33

    m "Ôi trời, thật vậy ư?"

    m "Cậu thật sự sẽ tham gia sao, [player]?"
    show monika zorder 2 at t33

    mc "Ừ..."

    mc "Mình nghĩ chắc là sẽ vui vẻ khi ở đây, chắc vậy nhỉ?"
    show yuri zorder 3 at f32

    y 1m "Cậu vừa dọa mình sợ chết khiếp đấy nhé...."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31

    n 5q "Tưởng là cậu vẫn bỏ đi sau khi Monika đã nói vậy thật thì chắc là tôi sẽ phát rồ lên đấy."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33

    m "[player] à, tớ rất vui..."

    m 1k "Cuối cùng chúng ta cũng có thể trở thành một câu lạc bộ chính thức rồi!"

    m 1e "Thật lòng cảm ơn cậu rất nhiều. Cậu thật là tuyệt vời."

    m "Mình sẽ làm tất cả những gì có thể để cậu có một khoảng thời gian tuyệt vời tại đây, vậy nhé?"
    show monika zorder 2 at t33

    mc "À...ừ thì...cảm ơn cậu."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki

    m 3b "Được rồi, mọi người!"

    m "Vậy là ổn thoả rồi, tớ xin tuyên bố kết thúc buổi họp câu lạc bộ hôm nay với một lưu ý nhỏ."

    m "Mọi người nhớ nhiệm vụ của tối ngày hôm nay nhé."

    m "Viết một bài thơ để trong lần họp tới, chúng mình có thể cùng trao đổi chúng!"

    "Monika nhìn về phía tôi thêm lần nữa."

    m 1a "[player], mình rất muốn được xem cậu thể hiện đấy."
    show monika 5 at hop

    m "Ehehe~"

    mc "Ừ-ừm..."
    show monika zorder 1 at thide
    hide monika

    "Liệu kĩ năng viết lách CỦA TÔI có thể gây ấn tượng nổi với ngôi sao sáng ngời Monika?"

    "Chưa gì mà tôi đã thấy nỗi lo lắng trào dâng trong lòng."

    "Các cô gái tiếp tục trò chuyện với nhau trong lúc Yuri dọn dẹp bộ ấm chén."

    mc "Vậy thôi mình về đây..."
    show monika 5a zorder 2 at t11

    m "Ừ!"

    m "Hẹn gặp lại cậu ngày mai."

    m "Mình mong lắm đấy!"

    scene bg residential_day
    with wipeleft_scene


    "Sau đấy, tôi rời khỏi phòng câu lạc bộ và đi về nhà."

    "Suốt quãng đường, tâm trí tôi lạc trôi quanh hình ảnh của ba cô gái."
    show natsuki 4a zorder 2 at t31
    "Natsuki,"
    show yuri 1a zorder 2 at t32
    "Yuri,"
    show monika 1a zorder 2 at t33

    "Và tất nhiên là cả Monika nữa."

    "Tôi vẫn không chắc là có vui hay không khi phải dành thời gian cho Câu lạc bộ Văn Học."

    "Nhưng chí ít thì đây là cơ hội cho tôi tiến gần đến một trong những cô gái này...."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft

    "Được rồi!"

    "Chỉ cần tận dụng tốt những gì đã có, tôi chắc chắn rằng rồi vận may sẽ mỉm cười với mình thôi."

    "Tất cả sẽ bắt đầu bằng bài thơ tối nay..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False


    call screen confirm("Đã mở khóa một bài thơ đặc biệt.\nBạn có muốn đọc không?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0])
    else:
        pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
