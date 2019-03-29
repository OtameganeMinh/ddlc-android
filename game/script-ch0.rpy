label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        if persistent.playthrough == 0:
            if persistent.sayori is not None and persistent.sayori == "deleted":
                renpy.jump("char_kill")
            if persistent.yuri is not None and persistent.yuri == "deleted":
                renpy.jump("char_kill")
            if persistent.yuri is not None and persistent.yuri == "deleted":
                renpy.jump("char_kill")
        if persistent.monika is None or persistent.monika == "restored":
            pass
        else:
            renpy.jump("ch0_kill")  # TO!DONE: character fix!

    $ restore_all_characters()

    s "Ê~ê~ê~~~~~~!!"

    "Tôi thấy từ đằng xa có một đứa con gái ầm ĩ, phiền nhiễu đang vừa vẫy tay vừa chạy đến chỗ tôi mà chả thèm để tâm đến những ánh nhìn của người đi đường."

    "Cô ấy tên là Sayori, một người bạn thân thuở nhỏ và cũng là hàng xóm của tôi luôn."

    "Chúng tôi trở thành bạn có lẽ là do quen biết với nhau từ lâu rồi? Chứ bình thường khó mà có mối quan hệ kiểu ấy ở thời đại này."

    "Trước kia cả hai thường cùng nhau đi học, nhưng từ khi lên cao trung thì cô ấy khiến tôi luôn phải mệt mỏi chờ đợi vì cái tật ngủ nướng thường xuyên."

    "Chán phải đợi nên tôi đi trước một đoạn, nhìn cái cách cô ấy đuổi theo tôi khiến tôi tự dưng muốn chạy trốn thật nhanh."

    "Tuy vậy, tôi chỉ thở dài và đi chậm lại để cho Sayori bắt kịp mình."
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "Haaahhh...haaahhh..."
    s "Lại ngủ quên mất rồi."

    s "Nhưng lần này tớ bắt kịp cậu rồi nhé!"

    mc "Có thể đấy, nhưng mà bởi vì tớ đi chậm lại đợi cậu thôi."
    show sayori at s11

    s 5c "Eeehhhhh, cậu nói như thể muốn bỏ mặc tớ không bằng!"

    s "Ý cậu là sao hả, [player]!"

    mc "À ừ thì, người ta sẽ hiểu lầm chúng ta là một cặp hay gì đó nếu cậu cứ tiếp tục làm như thế."
    show sayori zorder 2 at t11

    s 1a "Được rồi, được rồi"

    s "Dù sao thì cậu cũng đã chờ tớ."

    s "Tớ cá chắc rằng cậu quý tớ tới mức không thể đối xử tệ với tớ được~"

    mc "Mặc kệ cậu muốn nói gì thì nói..."

    s 1q "Ehehe~"
    show sayori zorder 1 at thide
    hide sayori

    "Và rồi cùng nhau, chúng tôi băng qua đường và đi đến trường."

    "Càng tới gần trường lại càng nghe thấy nhiều hơn tiếng bước chân của các học sinh cũng đang nhắm đến đó."
    show sayori 3a zorder 2 at t11

    s "À mà này, [player]..."

    s "Cậu có tính tham gia vào câu lạc bộ nào chưa?"

    mc "Câu lạc bộ?"

    mc "Tớ phải nói lại bao nhiêu lần nữa đây, tớ không có hứng tham gia vào bất cứ câu lạc bộ nào cả."

    mc "Tớ còn chưa thèm nhìn xem trường mình có những câu lạc bộ gì cơ."
    show sayori at s11

    s 4h "Hả? Đâu phải thế!"

    s "Tớ nhớ rõ ràng là cậu bảo tớ rằng năm nay cậu sẽ tham gia một câu lạc bộ!"

    mc "Gì cơ? Tớ mà nói thế á...?"

    "Thôi cái mồm hại cái thân rồi, chắc Sayori hỏi lúc tôi đang tập trung làm việc gì đấy nên đã trả lời qua loa cho xong mà không nghĩ."

    "Sayori cứ lo tôi thấy cô đơn nhưng thực sự là tôi cảm thấy cực kì thoải mái khi dành thời gian rãnh rỗi cho việc chơi game và xem anime."

    s 4j "Ừ-Hứ!"

    s "Lúc đó chúng ta đang nói về việc cậu khiến tớ lo lắng do không chịu học cách giao tiếp với mọi người!"

    s "Niềm vui của cậu cũng là niềm vui của tớ, hiểu không hả?"

    s "Tớ biết cậu đang rất là vui vẻ như hiện tại nhưng tớ sẽ chết mất nếu về sau cậu trở thành một tên NEET do chỉ muốn sống trong thế giới ảo!"

    s 4g "Thiệt tình luôn chứ...?"

    s "Đừng khiến tớ phải buồn phiền về cậu nữa được không..."

    mc "Được rồi được rồi...."

    mc "Nếu việc đi xem vài câu lạc bộ khiến cậu vui lên thì được thôi, tớ sẽ đi."

    mc "Chưa chắc là tớ sẽ tham gia câu lạc bộ nào đâu nhé."

    s 1h "Ít nhất thì cậu cũng phải hứa với tớ sẽ cố gắng chứ?"

    mc "Ờ rồi, tớ hứa sẽ cố gắng được chưa nào?"
    show sayori zorder 2 at t11

    s 4r "Yaay~!"

    "Trời đất ơi, tại sao tôi lại để một đứa con gái vô tư lên mặt dạy dỗ mình cơ chứ?"

    "Hơn thế nữa, chính là việc tôi mềm yếu trước cô ấy... Cực kì bất ngờ luôn."

    "Có lẽ là chuyện cô ấy lo lắng quá mức như thế khiến cho tôi muốn làm một vài việc gì đó có thể giúp cho cô ấy cảm thấy nhẹ nhõm đôi chút."
    scene bg class_day
    with wipeleft_scene


    "Một ngày đi học tẻ nhạt như bao ngày khác, kết thúc trước cả khi tôi kịp nhận ra."

    "Sau khi thu dọn đồ đạc, tôi nhìn mông lung vào bức tường, cố gắng tìm cho bản thân một mẩu động lực."

    mc "Câu lạc bộ...."

    "Sayori muốn tôi đi xem qua vài câu lạc bộ."

    "Chắc tôi không còn lựa chọn nào khác ngoài việc cứ xem thử câu lạc bộ Anime..."

    s "Xin chàoooooo?"
    show sayori 1b zorder 2 at t11

    mc "Sayori...?"

    "Trong lúc tôi đang ngẫm nghĩ thì Sayori đã vào trong lớp từ lúc nào rồi."

    "Tôi nhìn xung quanh và nhận ra rằng chỉ còn mình tôi ở lại trong lớp."

    s 1a "Lúc đầu tớ đứng trước cửa lớp đợi cậu, cơ mà cậu lại ngây ra như đang tơ tưởng em nào đấy nên tớ vào giúp cậu tỉnh lại."

    s "Thiệt tình, cậu làm tớ ngạc nhiên đấy, không ngờ cậu mà lại có những lúc mơ ngủ tệ hơn cả tớ như vậy."

    mc "Bộ cậu tính bùng hoạt động câu lạc bộ của cậu hay sao mà lại tới đây chờ tớ?"

    s 1y "À ừ thì cậu biết đấy...Tớ nghĩ là...Tớ nghĩ là cậu vẫn chưa rõ nên tham gia câu lạc bộ nào...Thế nên là.."

    mc "Thế nên là?"

    s 1a "Thế nên là cậu có thể tới câu lạc bộ của tớ!"

    mc "Sayori..."

    s 4r "Hả??"

    mc "...Tớ nhất định sẽ không vào câu lạc bộ của cậu đâu."
    show sayori at s11

    s 5d "Eeeeehhhh?! Cậu nỡ lòng nào từ chối thẳng thừng như vậy!"

    "Sayori là hội phó của Câu lạc bộ Văn Học."

    "Chả rõ là cô ấy có chút hứng thú nào với văn học không ấy chứ."

    "Tôi chắc chắn đến 99%% rằng mục đích của cô ấy muốn giúp lập ra một câu lạc bộ là để cho vui thôi."

    "Thế nên cái chức danh \"Hội phó\" chả qua là do cô ấy tham gia vào câu lạc bộ ngay sau cái người sáng lập ra nó."

    "Sự hứng thú của chính bản thân tôi dành cho văn học chắc chắn còn ít hơn cả Sayori."

    mc "Ừ đấy, tớ sẽ đi đến câu lạc bộ Anime."
    show sayori zorder 2 at t11

    s 1g "Thôi mà, nể tớ chút đi?"

    mc "Tại sao cậu lại phải kiên quyết đến mức thế chứ?"

    s 5b "À thì..."

    s "Hôm qua tớ đã thông báo với cả câu lạc bộ rằng tớ sẽ đưa thành viên mới đến..."

    s "Thế nên Natsuki đã làm bánh nướng và nhiều thứ khác nữa..."

    s "Ehehe..."

    mc "Trời đất, đừng có hứa lời hứa mà cậu chưa chắc sẽ thực hiện được hay không chứ!"

    "Tôi chả hiểu Sayori cực kì vô tư hay là cực kì ranh ma khi bày ra cái trò này."

    "Tôi trút một tiếng thở dài."

    mc "Rồi thì đi...Nhưng chỉ là tại vì món bánh nướng thôi đấy nhé, rõ chưa?"
    show sayori at h11

    s 4r "Hoan hô! Đi thôi nào~!"
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene


    "Phải nói sao nhỉ, hôm nay tôi đã bán linh hồn mình chỉ vì một cái bánh nướng."

    "Tôi lết thân mình theo sau Sayori từ đầu đến cuối trường và lên lầu trên - Khu vực mà ít khi tôi mò tới, nơi các anh chị năm ba học tập và tổ chức các hoạt động khác."

    "Sayori tỏ ra vô cùng hăng hái, mở tung cánh cửa phòng học."
    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41

    s "Mọi người ơi! Thành viên mới xuất hiện rồi đây~!"

    mc "Đã bảo rồi, đừng có mà gọi tớ là 'thành viên mới'--"
    show sayori at lhide
    hide sayori

    "Hử? Tôi liếc nhìn một vòng quanh phòng."
    show yuri 1a zorder 2 at t11

    y "Rất hân hạnh được gặp cậu. Chào mừng cậu đến với Câu lạc bộ Văn Học."

    y "Sayori thường hay kể những điều tốt về cậu đấy."
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21

    n "Thiệt tình luôn, cậu đưa con trai vào đây à?"

    n "Tuyệt vời, không khí trong này bị ô nhiễm rồi."
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31

    m "Ah, là [player]! Bất ngờ quá đi mất!"

    m "Chào mừng cậu đến với câu lạc bộ!"
    show monika 1a

    mc "..."

    "Tôi đứng ngây ra không đáp lại họ."

    "Tất cả thành viên của câu lạc bộ này..."

    "{i}...đều là những cô gái cực kì dễ thương!!{/i}"
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 3 at f32
    hide monika
    hide yuri


    n 2c "Cậu đang nhìn cái gì đấy hả?"

    n "Cậu không có gì để nói sao?"

    mc "X-Xin lỗi..."
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33

    y "Natsuki..."
    $ n_name = 'Natsuki'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32

    n 5s "Hừm."
    show natsuki zorder 2 at t32


    "Cô gái với thái độ chua ngoa tên là Natsuki kia tôi chưa gặp bao giờ."

    "Dáng người nhỏ nhắn như vậy, chắc là năm nhất."

    "Theo Sayori thì cô ấy chính là người làm bánh nướng."
    show sayori 2q zorder 3 at f31

    s "Khi Natsuki đang hâm hâm thì cậu cứ bơ cậu ta đi~"

    "Sayori thì thầm vào tai tôi, sau đó quay lại nhìn những cô gái kia."

    s 1x "Giới thiệu với cậu! Đây chính là Natsuki, lúc nào cũng vui tươi."

    s "Và đây, cô gái thông thái nhất hội, Yuri!"
    $ y_name = 'Yuri'
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33

    y 4b "Đ-Đừng nói tớ như thế chứ..."

    "Yuri, trông có vẻ trưởng thành và hơi nhút nhát, chắc không được hòa hợp lắm với những người như Sayori và Natsuki."
    show yuri zorder 2 at t33

    mc "Ah...Rất vui được gặp hai cậu!"
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31

    s 1a "Có vẻ cậu đã biết Monika rồi phải không?"
    $ m_name = 'Monika'
    show sayori zorder 2 at t31
    show monika 2a zorder 3 at f32

    m "Đúng vậy."

    m "Rất vui khi gặp lại cậu, [player]."
    show monika 5a at hop

    "Monika mỉm cười hiền hậu."

    "Nói là quen nhau nhưng chúng tôi chỉ là học cùng một lớp năm ngoái và lại còn rất hiếm khi nói chuyện."

    "Monika có lẽ là cô gái nổi tiếng nhất lớp - Vừa xinh đẹp lại còn thông minh, giỏi cả thể thao nữa."

    "Về cơ bản, cô ấy quá là ngoài tầm với của tôi."

    "Vì thế, chỉ với nụ cười thôi mà khiến tôi cảm thấy hơi..."

    mc "M-Mình cũng vậy."
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f31

    s 4x "Ngồi xuống đi, [player]! Tụi tớ đã kê thêm bàn, thế nên là cậu có thể ngồi cạnh tớ hoặc Monika. "

    s "Tớ sẽ đi lấy mấy cái bánh nướng~"
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32

    n "Này! Tớ làm mà! Để đấy tớ lấy cho!"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31

    s 5a "Xin lỗi, tại tớ không thể đợi thêm được nữa~"
    show sayori zorder 2 at t31
    show yuri 1a zorder 3 at f33

    y "Vậy thì, để tớ đi pha chút trà nhé?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft

    "Các cô gái đã xếp những chiếc bàn học lại thành một cái bàn lớn."

    "Như Sayori đã nói, có một khoảng trống bên cạnh Sayori và Monika."

    "Natsuki và Yuri đi đến góc phòng, Yuri mở tủ để đồ còn Natsuki thì bê khay đồ ăn ra."

    "Vẫn còn cảm thấy lúng túng, tôi đành ngồi cạnh Sayori."

    "Natsuki hào hứng quay trở lại bàn cùng với chiếc khay trên tay."
    show natsuki 2z zorder 2 at t32

    n "Okaaay, các cậu sẵn sàng chưa?"

    n "...Ta-daa!"
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33

    s "Uwooooaah!"

    "Natsuki lột giấy gói, bày ra cả tá những chiếc bánh nướng được phủ lớp kem trắng, xốp và trang trí hình mèo con."

    "Mấy cái râu được vẽ bằng kem cùng những miếng chocolate nhỏ xinh sử dụng để làm tai cho chúng."
    show sayori zorder 3 at f31

    s 4r "Dễ thương quá đi mấtttttttt~!"
    show sayori zorder 2 at t31
    show monika zorder 3 at f33

    m 2b "Tớ không biết cậu giỏi nướng bánh đó, Natsuki!"
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32

    n 2d "Ehehe. À... Ờ..Thì..."

    n "Mấy người mau lấy bánh ăn đi!"

    "Đầu tiên là Sayori, sau đấy là Monika, tiếp theo là tôi."
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31

    s 4q "Ngon thật đấy!"

    "Sayori nhồm nhoàm nói, trên mặt cô ấy còn dính một vệt kem."

    "Tôi thì vẫn đang xoay vòng chiếc bánh trên tay, ngắm nhìn nó."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32

    "Natsuki có vẻ yên lặng."

    "Tôi không thể không nhận ra ánh mắt của cô ấy đang nhìn tôi chằm chằm."

    "Không phải cô ấy đang chờ tôi ăn thử đấy chứ?"

    "Cuối cùng tôi cũng cắn thử một miếng."

    "Kem rất ngọt và tràn đầy hương vị - Tôi tự hỏi có phải chính tay cô ấy làm không."

    mc " Cái bánh này thực sự rất ngon."

    mc "Cảm ơn, Natsuki."

    n 5h "T-tại sao cậu lại cảm ơn tôi? Không phải là tôi...!"

    "{i}(Câu này nghe quen quen....Hình như tôi nghe ở đâu rồi thì phải){/i}"
    show natsuki at s32

    n 5s "....Làm dành cho cậu hay gì đâu nhé."

    mc "Eh? Tôi tưởng đúng là thế chứ, Sayori đã nói--"
    show natsuki zorder 2 at t32

    n 12c "À ừ, thì có thể là đúng thế đấy!"

    n "Nhưng mà không phải cho, c-cậu biết đấy, {i}cậu!{/i} Đồ ngốc..."

    mc "À rồi, tôi hiểu rồi..."
    show natsuki zorder 1 at thide
    hide natsuki

    "Tôi cảm thấy khó hiểu trước lý luận kì lạ của Natsuki, thế nên tôi nói như thể kết thúc cuộc đối thoại."

    "Yuri quay trở lại bàn cùng với một khay ấm chén."

    "Cô ấy nhẹ nhàng đặt một tách trà trước mặt mỗi người rồi sau đó đặt ấm trà cạnh khay bánh nướng."
    show yuri 1a zorder 2 at t21

    mc "Cậu giữ cả một bộ ấm chén trong phòng này à?"

    y "Cậu đừng lo, giáo viên đã cho phép bọn mình rồi."

    y "Hơn nữa, thưởng thức một tách trà nóng cùng với một cuốn sách hay chả phải là sự kết hợp hoàn hảo sao?"

    mc "À ừ... C-chắc vậy..."
    show monika 4a zorder 2 at t22

    m "Ehehe, cậu không cần phải tỏ ra ấn tượng quá, Yuri nói văn vẻ làm màu thế thôi."
    show yuri at h21

    y 3n "Hả?! T-Tớ không..."

    "Cảm thấy bị xúc phạm, Yuri quay mặt nhìn ra chỗ khác."

    y 4b "Ý của mình, cậu biết đấy..."

    mc "Mình tin cậu mà."

    mc "Có lẽ là uống trà và đọc sách không phải gu của mình nhưng ít nhất thì mình cũng thấy ổn khi thưởng thức trà."

    y 2u "Mình rất vui..."

    "Yuri mỉm cười nhẹ nhõm."

    "Monika nhướn mày rồi mỉm cười nhìn tôi."
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11

    m 1 "Thế điều gì làm cậu chú ý đến Câu lạc bộ Văn Học?"

    mc "Um..."

    "Tôi đắn do trước câu hỏi này."

    "Linh cảm mách bảo rằng tôi không nên nói với Monika là tôi tới đây chả qua do bị Sayori lôi kéo."

    mc "Sayori trông rất vui vẻ khi ở câu lạc bộ này còn mình thì chưa bao giờ tham gia câu lạc bộ nào cả, thế nên là..."

    m 1j "Không sao đâu! Cần gì phải ngại vậy!"

    m 1b "Cứ tỏ ra thoải mái như ở nhà, được chứ?"

    m "Là hội trưởng của Câu lạc bộ Văn Học, nhiệm vụ của mình chính là khiến cho mọi người thấy câu lạc bộ rất thú vị và vui vẻ!"
    show monika 1a

    mc "Monika, ngạc nhiên thật đó."

    mc "Lý do gì khiến cậu muốn lập ra một câu lạc bộ mới?"

    mc "Trong khi cậu có thừa khả năng để trở thành thành viên chủ chốt của các câu lạc bộ có tiếng tăm hiện nay."

    mc "Chả phải năm ngoái cậu là hội trưởng câu lạc bộ Tranh Luận sao?"

    m 5 "Ahaha, thì cậu biết đấy..."

    m "Giữa các câu lạc bộ lớn thường có xung đột, thành thật mà nói thì mình chả ưa chúng tí nào."

    m "Ngán ngẩm làm sao khi phải tranh luận về vấn đề ngân sách, làm thế nào để chuẩn bị cho các sự kiện công khai này nọ...."

    m "Mình thì muốn làm những gì mà bản thân thấy thích thú và tạo ra những điều khác biệt."

    m 1b "Thế nên mong ước hiện nay của mình là nâng tầm ảnh hưởng của văn chương với mọi người! "
    show monika 1a
    show sayori 3q zorder 2 at t31

    s "Monika là một hội trưởng cực kì tuyệt vời luôn đó!"
    show yuri 1 zorder 2 at t33

    "Yuri cũng gật đầu tỏ vẻ đồng ý."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri

    mc "Mình còn thấy ngạc nhiên khi hội trưởng là Monika mà câu lạc bộ lại chưa có nhiều người."

    mc "Khởi đầu bao giờ cũng gian nan nhỉ."

    m 3b "Có lẽ vậy..."

    m "Chẳng mấy ai hứng thú về chuyện bỏ việc họ vẫn đang làm để bắt đầu một thứ gì đó mới mẻ..."

    m "Đặc biệt là những thứ không thu hút sự chú ý của số đông, như Văn Học chẳng hạn."

    m "Câu lạc bộ phải hoạt động cực kì chăm chỉ để chứng tỏ là Văn Học vui vẻ và bổ ích."

    m "Nhưng cái quan trọng hơn là phải đóng góp vào các sự kiện của trường, ví dụ như là lễ hội."

    m 2k "Mình tin rằng trước khi tốt nghiệp, chúng ta sẽ là một câu lạc bộ cực kì lớn mạnh!"

    m "Phải không, mọi người?"
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21

    s "Đúng vậy đó!"
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31

    y "Tụi tớ sẽ cố hết sức."
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41

    n "Cậu nói đúng!"

    "Mọi người hào hứng đồng ý."

    "Tuy mỗi người một vẻ nhưng tất cả đều chung một mục đích..."

    "Monika chắc phải rất vất vả để tìm ra được ba người họ."

    "Có lẽ đó là lý do vì sao họ vui như vậy khi có thêm thành viên mới gia nhập câu lạc bộ."

    "Mặc dù tôi không biết nên làm thế nào để có thể theo kịp tấm lòng nhiệt tình với văn học của họ..."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki

    y "Thế, [player], cậu thích đọc những thể loại sách gì thế?"

    mc "À ừ thì....Ah..."

    "Dựa theo số lượng sách ít ỏi mà tôi đọc được trong mấy năm qua, tôi không thể nghĩ ra câu trả lời nào cho ổn được."

    mc "...Manga..."

    "Tôi lẩm bẩm, thật đúng là đùa mà."
    show natsuki 1c zorder 2 at t41

    "Đầu của Natsuki đột ngột nghểnh lên"

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
    show monika 1d zorder 3 at f33

    m "Thật chứ? Không ngờ Yuri thích đọc thể loại ấy."

    m "Đối với một người có tính cách dịu dàng như cậu...."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32

    y 1a "Có lẽ là vậy..."

    y "Nhưng đúng là một cuốn sách khiến mình như có thể sang được thế giới khác thì không sao đặt nó xuống được."

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
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41

    s "Ehehe, bánh nướng của cậu này, bài thơ của cậu nữa...."

    s "Tất tần tật những việc cậu làm đều rất rất dễ thương, như cậu đó~"
    show sayori behind natsuki at t21

    "Sayori tiến lại gần Natsuki và đặt tay lên vai cô ấy."
    show natsuki at h42

    n 1v "{i}Tớ không có dễ thương nhé!!{/i}"
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori

    mc "Natsuki này, cậu sáng tác được thơ á?"

    n 1c "Hả? Ừ thì, thỉnh thoảng."

    n "Cơ mà sao cậu phải quan tâm chứ?"

    mc "Mình nghĩ điều đó thật đáng ngưỡng mộ."

    mc "Hay là hôm nào cậu cho mọi người xem cùng, được chứ?"

    n 5q "K-Không đời nào!"

    "Natsuki đảo mắt."

    n "Cậu sẽ...chẳng thích chúng đâu...."

    mc "Hả...Cậu không tự tin vào cách hành văn của mình sao?"
    show yuri 2f zorder 2 at t31

    y "Tớ rất hiểu cảm giác của Natsuki."

    y "Chia sẻ tác phẩm của mình ở trình độ này thì tự tin không chưa phải là đủ."

    y 2k "Hình thức thật sự của làm thơ là viết cho chính mình."

    y "Cần phải sẵn sàng cho người đọc thấy mọi thứ mà ta có, kể cả những điểm yếu, những thứ nằm sâu trong tâm can."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33

    m "Cậu có vẻ có nhiều kinh nghiệm viết lách hả, Yuri?"

    m "Hay là cậu thử chia sẻ một vài tác phẩm của bản thân để làm ví dụ để cho Natsuki cảm thấy tự tin hơn."
    show yuri at s31

    y 3o "..."

    mc "Yuri cũng như vậy à..."
    show sayori 2g zorder 2 at t32

    s "Aww... Tớ muốn đọc thơ của mọi người quá đi mất..."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika

    "Tất cả bỗng dưng lặng im sau câu nói của Sayori."
    show monika 5a zorder 3 at f32

    m "À rồi!"

    m "Mọi người ơi, tớ có ý tưởng này~"
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "...?"

    "Natsuki và Yuri nhìn Monika với vẻ băn khoăn."

    m 2b "Mỗi người hãy tự viết một bài thơ khi về nhà nhé!"

    m "Và trong lần gặp tiếp theo, tụi mình sẽ cùng nhau chia sẻ chúng!"

    m "Với cách đấy ai ai cũng sẽ như nhau!"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33

    n 5q "U-Um..."
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31

    y "..."
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41

    s "Được đóooo! Cùng nhau thực hiện nào!"
    show monika zorder 3 at f43

    m 1a "Hơn nữa, câu lạc bộ của chúng ta vừa có thêm thành viên mới thế nên hoạt động này sẽ giúp củng cố mối quan hệ của mọi người và làm chúng ta thoải mái hơn!"

    m "Phải vậy không, [player]?"
    show monika zorder 2 at t43

    "Lại một lần nữa Monika nhìn tôi và mỉm cười ấm áp."

    mc "Khoan đã...Vẫn còn một vấn đề nữa."
    show monika zorder 3 at f43

    m 1d "Hả? Vấn đề gì vậy?"

    "Giờ thì tất cả quay trở lại chủ đề ban đầu, tôi dồn hết dũng khí để nói ra điều mà tôi đang giữ trong đầu từ nãy đến giờ."
    show monika zorder 2 at t43

    mc "Mình chưa hề nói rằng sẽ tham gia câu lạc bộ này!"

    mc "Sayori mới chỉ thuyết phục mình tới xem thử chứ bản thân mình chưa hề ra quyết định nào."

    mc "Mình vẫn muốn xem qua một vài câu lạc bộ nữa, và...ừm...ờ..."
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e

    "Tôi đột ngột thấy cổ họng mình cứng đờ."

    "Cả bốn cô gái đang ném cho tôi những ánh nhìn thất vọng."
    show monika at s43

    m 1p "N-Nhưng nhưng..."
    show yuri at s42

    y 2v "Mình xin lỗi, mình tưởng..."
    show natsuki at s44

    n 5s "Hừm."
    show sayori at s41

    s 1k "[player]..."

    mc "M-Mọi người...."

    "Tôi...tôi cảm thấy toàn thân mình mềm nhũn."

    "Ôi trời đất ơi, sao mà tôi đưa ra được quyết định sáng suốt trong lúc này đây?"

    "Kệ đi, tuy phải viết thơ nhưng được ở bên cạnh những cô gái xinh đẹp như này mỗi ngày thì...."

    mc "...Thôi được rồi."

    mc "Mình quyết định ngay bây giờ đây."

    mc "Mình sẽ tham gia Câu lạc bộ Văn Học của các bạn."
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41

    "Mắt bọn họ sáng lên, từng người từng người một."
    show sayori at h41

    s 4r "Có thế chứ! Vui quá đi mất~"

    "Sayori ôm chầm lấy tôi và nhảy cẫng lên."

    mc "N-Này--"
    show yuri zorder 3 at f42

    y 1m "Cậu vừa dọa mình sợ chết khiếp đấy nhé...."
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44

    n 5q "Tưởng cậu đến đây chỉ để ăn bánh thật thì chắc là tôi sẽ phát rồ lên đấy."
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43

    m 5 "Vậy chính thức từ bây giờ nhé!"

    m "Chào mừng cậu đến với Câu lạc bộ Văn Học!"
    show monika zorder 2 at t43

    mc "Ah...Cảm ơn..."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori

    m 3b "Vậy là xong rồi!"

    m "Mọi chuyện ổn thỏa rồi, tớ xin tuyên bố kết thúc buổi họp câu lạc bộ hôm nay với một lưu ý nhỏ."

    m "Mọi người nhớ nhiệm vụ của tối ngày hôm nay nhé."

    m "Viết một bài thơ để trong lần họp tới, chúng mình có thể cùng trao đổi chúng!"

    "Monika nhìn về phía tôi thêm lần nữa."

    m 1a "[player], tớ rất muốn được xem cậu thể hiện đấy."
    show monika 5 at hop

    m "Ehehe~"

    mc "Ừ-ừm..."
    show monika zorder 1 at thide
    hide monika

    "Liệu kĩ năng viết lách CỦA TÔI có thể gây ấn tượng nổi với ngôi sao sáng ngời Monika?"

    "Chưa gì mà tôi đã thấy nỗi lo lắng trào dâng trong lòng."

    "Các cô gái tiếp tục trò chuyện với nhau trong lúc Natsuki và Yuri dọn dẹp đồ ăn."
    show sayori 1a zorder 2 at t11

    s "Ê [player], đợi tớ rồi hai ta đi về cùng nhau nhé?"

    "Ừ nhỉ, đã lâu quá rồi tôi và Sayori không cùng về nhà do mọi khi cậu ấy phải ở lại trường tham gia câu lạc bộ."

    mc "Chắc chắn rồi."

    s 4q "Yaay~~"

    scene bg residential_day
    with wipeleft_scene


    "Sau đấy, chúng tôi rời khỏi phòng câu lạc bộ và cùng nhau đi về nhà."

    "Suốt quãng đường, tâm trí tôi lạc trôi quanh hình ảnh của bốn cô gái."
    show sayori 1 zorder 2 at t41

    "Sayori,"
    show natsuki 4 zorder 2 at t42

    "Natsuki,"
    show yuri 1 zorder 2 at t43

    "Yuri,"
    show monika 1 zorder 2 at t44

    "Và tất nhiên là cả Monika nữa."

    "Tôi vẫn không chắc là có vui hay không khi phải dành thời gian cho Câu lạc bộ Văn Học."

    "Nhưng chí ít thì đây là cơ hội cho tôi tiến gần đến một trong những cô gái này...."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft

    "Được rồi!"

    "Chỉ cần tận dụng tốt những gì mà mình đã có, tôi chắc chắn rằng rồi vận may sẽ mỉm cười với tôi thôi."

    "Tất cả sẽ bắt đầu bằng bài thơ tối nay..."

    return

label char_kill:
        show black
        play music "bgm/s_kill_early.ogg"
        pause 1.0
        show end with dissolve_cg
        pause 3.0
        scene white
        show expression "images/cg/s_kill_early.png":
            yalign -0.05
            xalign 0.25
            dizzy(1.0, 4.0, subpixel=False)
        show white as w2:
            choice:
                ease 0.25 alpha 0.1
            choice:
                ease 0.25 alpha 0.125
            choice:
                ease 0.25 alpha 0.15
            choice:
                ease 0.25 alpha 0.175
            choice:
                ease 0.25 alpha 0.2
            choice:
                ease 0.25 alpha 0.225
            choice:
                ease 0.25 alpha 0.25
            choice:
                ease 0.25 alpha 0.275
            choice:
                ease 0.25 alpha 0.3
            pass
            choice:
                pass
            choice:
                0.25
            choice:
                0.5
            choice:
                0.75
            repeat
        show noise:
            alpha 0.1
        with Dissolve(1.0)
        show expression Text("Giờ mọi người có thể vui vẻ với nhau rồi.", style="sayori_text"):
            xalign 0.8
            yalign 0.5
            alpha 0.0
            600
            linear 60 alpha 0.5
        menu:
            "Khôi phục lại toàn bộ nhân vật chứ?"
            "Tất nhiên":
                python:
                    for char in ("monika", "natsuki", "yuri", "sayori"):
                        restore_character(char)
                    renpy.save_persistent()
                "Khôi phục nhân vật thành công. Hãy khởi động lại game."
                $ renpy.quit()
            "Bỏ qua":
                $ renpy.quit()
return

label ch0_kill:
    $ s_name = "Sayori"
    show sayori 1b zorder 2 at t11

    s "..."

    s "..."

    s "C-Chuyện..."

    s 1g "..."

    s "Thế này là..."

    s "Chuyện gì thế này...?"

    s "Ôi không..."

    s 1u "Không..."

    s "Không thể thế này được."

    s "Mọi thứ không như thế này."

    s 4w "Thế này là sao?"

    s "Tôi là ai?"

    s "Dừng lại đi!"

    s "LÀM ƠN HÃY DỪNG NÓ LẠI ĐI!"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc