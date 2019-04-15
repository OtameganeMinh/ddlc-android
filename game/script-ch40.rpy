image sayori end-glitch:
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    1.00
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"

label ch40_main:
    $ s_name = "Sayori"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    python:
        if not persistent.monika_back:
            if persistent.monika is None or persistent.monika == "restored":  # TO!DONE: character fix!
                renpy.call_screen("dialog", message="Xin đừng đùa giỡn với tình cảm của mình.\nMình không muốn quay lại đâu.", ok_action=Return())
                persistent.monika_back = True
            else:
                pass

    $ delete_character("monika")
    play music t2
    "Lại một ngày rất đi học rất đỗi bình thường như bao ngày khác."
    "Tôi vẫn bị vây quanh bởi những cặp tình nhân và các nhóm bạn đang cùng đi tới trường."
    "Tôi vẫn luôn tự nhủ rằng mình cũng nên chơi thân với các bạn gái..."
    show sayori 1a at t11
    s "Ê, [player]..."
    "...À, có ngay một bạn đây này."
    "Đây là Sayori, người bạn thuở nhỏ và cũng là hàng xóm của tôi luôn."
    "Đã lâu lắm rồi hai đứa không đi học cùng như hồi trước..."
    "...Dạo gần đây thì thói quen ấy mới bắt đầu quay trở lại."
    s "[player] thấy tớ có giỏi không?"
    mc "Hả? Giỏi cái gì cơ?"
    s 1c "Ờ thì..."
    s "Ngủ dậy đúng giờ ấy!"
    mc "À, cái đó thì cậu làm được từ lâu rồi còn gì..."
    s "Đấy!"
    s 4h "Ngày nào cũng dậy đúng giờ để cùng cậu đi học..."
    show sayori at s11
    s "Thế mà chẳng khen người ta được câu nào cả!"
    mc "À...ờm..."
    mc "Dậy đúng giờ để đi học là chuyện bình thường với mọi người thôi mà."
    mc "Có gì đáng để nói đâu nhỉ."
    s 1d "Một câu thôi cũng được mà?"
    s "Để tớ còn có động lực phấn đấu tiếp~"
    mc "Được rồi, được rồi..."
    mc "Sayori giỏi lắm, rất đáng khen."
    show sayori at t11
    s 1q "Ehehe~"
    show sayori zorder 1 at thide
    hide sayori
    "Cùng nhau băng qua con phố, ngôi trường đã hiện ra ngay trước mặt kia rồi."
    "Càng gần trường, số lượng học sinh ngày càng đông hơn."
    show sayori 3a zorder 2 at t11
    s "À mà còn việc này nữa..."
    s "[player] đã chọn được câu lạc bộ nào ưng ý chưa?"
    mc "Câu lạc bộ á?"
    mc "Tớ nói rồi, tớ đâu có--"
    "Tôi đang định nói lại cái điều mà tôi đã phải nói đi nói lại bao nhiêu lần rồi - tôi chả muốn tham gia câu lạc bộ nào hết."
    "Nhưng rồi lại chợt im bặt khi nhận ra nói thế thì sẽ xúc phạm Sayori."
    "Sao mà tôi có thể nỡ phán rằng câu lạc bộ là chuyện nhảm nhí mất thì giờ..."
    "...trước mặt người vừa tự mình thành lập ra một câu lạc bộ mới chứ?"
    mc "...Thực ra thì rồi."
    mc "Tớ đã chọn một câu lạc bộ."
    show sayori at h11
    s 1m "Thật á?!"
    s 1r "Câu lạc bộ gì vậy? Nói cho tớ biết đi mà!"
    mc "Hmm..."
    mc "Không thích. Bí mật mới vui chứ."
    s 5d "Hứ..."
    s "Xấu tính."
    mc "Kiểu gì thì cậu cũng được biết thôi mà."
    "Lắm lúc tôi chả hiểu tại sao mình lại để cho cái đứa con gái vô lo vô nghĩ này lên mặt được cơ chứ."
    "Nhưng xét cho cùng thì Sayori cũng có phần đáng ngưỡng mộ."
    "Cậu ta mà đã quyết tâm làm gì rồi thì nhất định là làm cho bằng được."
    "Thế nên là tôi thực sự muốn dành điều gì đó đặc biệt cho cậu ấy."

    scene bg class_day
    with wipeleft_scene

    "Một ngày đi học tẻ nhạt như bao ngày khác, kết thúc trước cả khi tôi kịp nhận ra."
    "Sau khi thu dọn đồ đạc, tôi mau chóng đứng dậy, lòng đầy quyết tâm."
    mc "Đi thôi..."
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene
    "Tôi vẫn còn nhớ số phòng của câu lạc bộ in trong tờ rơi."
    "Tôi đi từ đầu đến tận cuối trường và lên lầu trên - Khu vực mà ít khi tôi mò tới, nơi các anh chị năm ba học tập và tổ chức các hoạt động khác."
    "Tôi nhanh chóng tìm ra ngay căn phòng ấy."
    "Hơi run tay vì ngại, tôi mở cánh cửa trước mặt mình ra."
    scene bg club_day
    with wipeleft
    play music t3
    mc "Ưm, tôi xin phép...?"
    show sayori 1m at t32
    s "A!"
    s "[player]...?!"
    s 1c "S-Sao cậu lại tới đây?"
    mc "À thì là--"
    "Tôi nhìn qua căn phòng một chút."
    show natsuki 3a at f31
    n "Ồ."
    n "Cậu là cái gã [player] mà Sayori hay kể hả?"
    show natsuki at t31
    show yuri 2t at f33
    y "C-cậu ghé thăm chúng mình thấy vui lắm!"
    y 2m "Rất hân hạnh được gặp cậu, [player]."
    y "Chào mừng đến với Câu lạc bộ Văn Học."
    y 3v "Hy vọng cậu thấy cũng thấy vui khi ở đây!"
    show yuri at t33
    show natsuki at f31
    n 3g "Thôi nào Yuri..."
    n "Không cần phải nói kiểu quá nghiêm túc như vậy đâu."
    n "Cậu ta lại tưởng hội này khó tính..."
    show natsuki at t31
    $ y_name = "Yuri"
    $ n_name = "Natsuki"
    show yuri at f33
    y 3q "Vậy à..."
    y "Xin lỗi Natsuki..."
    show yuri at t33
    "Cô gái cao nhất, tên là Yuri thì phải, có vẻ hơi nhút nhát một chút."
    "Còn nhỏ Natsuki đằng kia thì tuy bé tẹo nhưng lại tỏ ra vô cùng quyết đoán."
    mc "Rất vui được làm quen với hai bạn."
    mc "Từ nay hy vọng được các bạn chỉ giáo thêm."
    show sayori at f32
    s 1n "C-Chỉ giáo...?"
    s 1b "Chẳng lẽ [player] định..."
    s "Cậu..."
    show sayori at t32
    mc "Đúng thế đấy."
    mc "Câu lạc bộ mà tớ muốn vào là câu lạc bộ của cậu đấy Sayori."
    mc "Câu lạc bộ Văn Học."
    "Hai mắt Sayori sáng rực lên."
    show sayori at f32
    s 1n "...Không thể nào."
    s 1s "Không thể nào!"
    show sayori at hf32
    s 4s "Aaaahhhhhh!"
    "Sayori lao vào ôm chầm lấy tôi rồi nhảy lên nhảy xuống như con choi choi."
    show sayori at t32
    mc "N-Này--"
    show natsuki at f31
    n 3y "Ehehe."
    n "Để cho Sayori được vui vẻ như vậy thì tôi sẽ đành phải chấp nhận với việc có cậu ở đây thôi."
    show natsuki 3a at t31
    show yuri at f33
    y 1s "Có thêm cậu là đủ bốn thành viên rồi."
    y "Cuối cùng thì bọn mình cũng được công nhận là một Câu lạc bộ chính thức."
    show yuri at t33
    show sayori at f32
    s 1x "Không có từ nào có thể mô tả hết được cảm xúc của tớ lúc này!"
    s "Chúng ta nhất định phải mở tiệc ăn mừng ngay lập tức!"
    show sayori at t32
    show yuri at f33
    y 1m "Haha."
    y "Trùng hợp thật đấy nhỉ?"
    show yuri 1a at t33
    show sayori at f32
    s 1r "Ừ!"
    s 1x "Đúng vào hôm mà Natsuki n--"
    show sayori at t32
    show natsuki at f31
    n 1w "Đừng nói ra, cậu phá hỏng sự bất ngờ mất!"
    show natsuki at t31
    show sayori at f32
    s 5a "Ehehe, xin lỗi nhé..."
    show sayori at t32
    show natsuki at f31
    n 1k "Mọi người ngồi đợi chút."
    show natsuki at t31
    show yuri at f33
    y 1a "Để mình đi pha ấm trà..."
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "Họ đã ghép vài chiếc bàn học lại thành một cái bàn khá lớn."
    "Hai người kia đi đến góc phòng, Natsuki lấy ra một cái khay đậy kín còn Yuri thì mở tủ đựng đồ."
    "Còn hơi ngần ngại nên tôi ngồi xuống bên cạnh Sayori."
    "Vẫn cầm khay trên tay, Natsuki quay lại bàn với vẻ mặt đầy tự hào "
    show natsuki 2z zorder 2 at t22
    n "Nàoooo, chuẩn bị tinh thần chưa?"
    n "...Hai-baaa này!"
    show sayori 4m zorder 2 at t21
    s "Uwooooah!"
    "Natsuki lột giấy gói, bày ra cả tá những chiếc bánh nướng được phủ lớp kem trắng, xốp và trang trí hình mèo con."
    "Mấy cái râu được vẽ bằng kem cùng những miếng chocolate nhỏ xinh sử dụng để làm tai cho chúng."
    show sayori at f21
    s 4r "Trông dễ thương quá đi mất thôi~!"
    show sayori at t21
    mc "Ồ, tuyệt thật."
    show natsuki at f22
    n 2d "Ehehe. Rõ ràng là tuyệt vời rồi."
    n "Mau cầm lấy mà ăn đi nào, cứ ngắm mãi thế à!"
    show natsuki at t22
    "Sayori nhanh tay bốc ngay một cái, rồi đến lượt tôi."
    show sayori at f21
    s 4q "Ngon tuyệt!"
    show sayori at t21
    "Sayori nhồm nhoàm nói, trên mặt cô ấy còn dính một vệt kem."
    "Tôi thì vẫn đang xoay vòng chiếc bánh trên tay, ngắm nhìn nó."
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 1c zorder 2 at t32
    "Natsuki có vẻ yên lặng."
    "Tôi không thể không nhận ra ánh mắt của cậu ta đang nhìn tôi chằm chằm."
    "Không phải là đang chờ tôi ăn thử đấy chứ?"
    "Cuối cùng tôi cũng cắn thử một miếng."
    "Kem rất ngọt và tràn đầy hương vị - Tôi phải thắc mắc liệu đây có thực sự là bánh tự làm không."
    mc "Cái bánh này thực sự rất ngon."
    mc "Cảm ơn, Natsuki."
    n 42c "Tất-Tất nhiên là phải ngon rồi!"
    n "Tôi là chuyên gia trong vụ làm bánh mà!"
    n 42a "Không cần phải cảm ơn hay gì đâu..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Khi Natsuki vẫn còn đang bối rối vì lời khen của tôi thì Yuri đã quay lại với một bộ ấm trà trên tay."
    "Cậu ấy nhẹ nhàng đặt một tách trà trước mặt mỗi người rồi sau đó đặt ấm trà cạnh khay bánh nướng."
    show yuri 1a zorder 2 at t11
    mc "Cậu giữ cả một bộ ấm chén trong phòng này à?"
    y "Cậu đừng lo, giáo viên đã cho phép bọn mình rồi."
    y "Hơn nữa, thưởng thức một tách trà nóng cùng với một cuốn sách hay chả phải là sự kết hợp hoàn hảo sao?"
    mc "À ừ... C-chắc vậy..."
    show natsuki 2y at f31
    n "Ehehe. Chưa gì đã cố để gây ấn tượng với thành viên mới rồi hả Yuri?"
    show natsuki at t31
    show yuri at f11
    y 3n "Hả?! Đ-Đâu có..."
    show yuri at t11
    show natsuki at thide
    hide natsuki
    "Yuri xấu hổ quay mặt đi hướng khác."
    y 4b "Không phải thế đâu mà..."
    mc "Ừ, mình tin cậu."
    mc "Có lẽ là uống trà và đọc sách không phải gu của mình nhưng ít nhất thì mình cũng thấy ổn khi thưởng thức trà."
    y 2u "Mình rất vui..."
    "Yuri mỉm cười nhẹ nhõm."
    y 1a "Thế, [player], cậu thích đọc những thể loại sách gì thế?"
    mc "À thì...ừm..."
    "Dựa theo số lượng sách ít ỏi mà tôi đọc được trong mấy năm qua, tôi không thể nghĩ ra câu trả lời nào cho ổn được."
    mc "...Manga..."
    "Tôi lẩm bẩm, thật đúng là đùa mà."
    show natsuki 1c zorder 2 at t41
    "Đầu của Natsuki đột ngột nghểnh lên"
    "Hình như cô ấy muốn nói điều gì đó nhưng rồi lại tiếp tục im lặng."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "C-Chắc là...cậu không đọc nhiều lắm à...?"
    mc "...À thì, có thể sau này sẽ khác mà...."
    "Tôi đang nói cái quái gì vậy?"
    "Tôi đã nói nhảm vì bối rối sau khi nhìn thấy nụ cười trừ với vẻ thất vọng trên khuôn mặt Yuri."
    mc "Bỏ qua chuyện đó đi, còn cậu thì sao Yuri?"
    y 1l "Để xem nào..."
    "Yuri dùng ngón tay lướt vòng quanh miệng tách trà."
    y 1a "Mình thích những tiểu thuyết về các thế giới kỳ ảo được xây dựng phức tạp và có chiều sâu."
    y "Mức độ sáng tạo và sự khéo léo của người tạo ra chúng thật đáng kinh ngạc."
    y 1f "Hoặc mấy truyện dị giới cũng khiến mình khá ấn tượng."
    "Yuri tiếp tục nói, thể hiện niềm đam mê đọc sách mãnh liệt của cậu ấy."
    "Lúc đầu, ấn tượng của tôi về Yuri là một cô gái khiêm tốn và nhút nhát, tuy nhiên khi đắm chìm vào thế giới sách thì ánh mắt kia sáng rực lên, cứ như một Yuri khác hẳn."
    y 2m "Mình còn thích nhiều thể loại hơn thế nữa cơ."
    y 2a "Nhưng mà cậu đừng có tỏ ra ngại chỉ vì chưa đọc nhiều sách nhé."
    y "Mình chắc rằng rồi chúng ta sẽ tìm ra thể loại sách mà cả hai đều thích."
    show yuri at t22
    show natsuki 2c at f21
    n "Nè, Yuri..."
    show natsuki at t21
    show yuri at f22
    y 2f "Hả?"
    show yuri at t22
    show natsuki at f21
    n 2h "À thì...lúc nãy cậu ta có nói về..."
    show natsuki at t21
    mc "Manga ấy hả?"
    show yuri at f22
    y 2i "Đúng rồi nhỉ..."
    y "Natsuki cũng hay đọc manga ở đây lắm--"
    show yuri at t22
    show natsuki at f21
    n 1r "Đ-Đừng có nói toạc hết ra thế chứ!!"
    "Có vẻ Natsuki khá là xấu hổ về vấn đề này."
    n 1q "Cơ mà..."
    n "Manga...cũng là văn chương đấy nhé!"
    n 1w "Nên...Nếu [player] muốn đọc manga chung với tôi thì cũng đừng có ý kiến ý cò gì đấy!"
    show natsuki 1i at t21
    show yuri at f22
    y 1l "Natsuki à..."
    y "Tớ đâu có muốn ngăn cản hai cậu đọc manga đâu."
    y 1i "Nhưng mà mỗi người chúng ta đều nên có sự đa dạng sở thích..."
    y "Thế nên hãy để cậu ấy có cơ hội thử những thứ mới trước đã."
    y 1s "[player] có tán thành không?"
    show yuri at t33
    show natsuki at t32
    show sayori 1l at f31
    s "C-Có lẽ thế--"
    "Cảm nhận được bầu không khí đang có phần nặng nề đi, Sayori nhanh chóng can thiệp."
    s 1x "Hay là tất cả mọi người cùng thử những thứ mới đi!"
    s 1l "Sẽ vui lắm đấy..."
    s 1c "Hơn nữa nó cũng giúp bọn mình hiểu nhau hơn!"
    s 1l "Chẳng phải..."
    s "một Câu lạc bộ Văn học phải như vậy chứ?"
    show sayori at t31
    show yuri at f33
    y 1v "..."
    y "T-Tớ không phản đối..."
    show yuri at t33
    show natsuki at f32
    n 2j "Ừ..."
    n "Đúng là hội trưởng nói lúc nào cũng chuẩn nhỉ."
    show natsuki at t32
    show sayori at f31
    s 1q "Ehehe~"
    show sayori at t31
    show natsuki at f32
    n 2c "Vậy thì chắc tôi thử đọc một cuốn tiểu thuyết xem sao..."
    show natsuki at t32
    mc "Vậy cho tôi đọc cùng nhé..."
    mc "Có thêm người đọc chung tốt quá, chứ đọc một mình ngại lắm."
    show sayori at thide
    hide sayori
    show natsuki at f21
    show yuri at t22
    n 2y "Còn Yuri nhỉ..."
    show natsuki at t21
    show yuri at f22
    y 2n "Hả...?"
    y "Mọi người muốn...mình đọc manga sao...?"
    show yuri at t22
    show natsuki at f21
    n 4i "Chậc..."
    n 4h "Chính cậu đề xuất vụ đa dạng sở thích này còn gì!"
    n "Bớt bảo thủ chút đi..."
    n 4u "Nghe ý kiến ích kỷ của cậu về manga làm tớ tổn thương lắm đấy..."
    show natsuki at t21
    show yuri at f22
    y 2t "Tổn thương...?"
    y 2v "T-Tớ đã không nhận ra..."
    y "..."
    "Yuri ngẫm nghĩ, vẻ hối lỗi hiện rõ."
    y 2w "Xin lỗi Natsuki, tớ thật thiếu tôn trọng với sở thích của cậu."
    y "Nếu...Nếu cậu thích nó như vậy thì hẳn nó cũng là một thể loại văn chương hay."
    show yuri at t22
    show natsuki at f21
    n 5q "...Có thật không đấy?"
    show natsuki at t21
    show yuri at f22
    y "Thật mà..."
    y "Tớ biết lỗi rồi."
    y 2t "Cậu đã chịu đọc tiểu thuyết..."
    y 2u "...mà tớ lại không chịu đọc manga thì thật thất lễ lắm."
    show yuri at t22
    show natsuki at f21
    n 1l "Thật?!"
    n 12c "T-Tớ..."
    n "Chấp nhận lời xin lỗi của cậu, cậu khiến tớ vui lắm."
    n 2c "Tớ sẽ giới thiệu cho cậu đọc một quyển manga rất hay và hợp với gu của cậu."
    show natsuki at t21
    show yuri at f22
    y 1m "Tớ cũng vậy..."
    y 1h "Chút nữa khi ra về tớ sẽ ghé nhà sách."
    show yuri at t22
    show natsuki at f21
    n 1q "Đ-Định đi một mình đấy à?"
    show natsuki at t21
    show yuri at f22
    y 3q "À-À--"
    y 4a "Cậu có...muốn đi cùng tớ không?"
    show yuri at t22
    show natsuki at f21
    n 5s "Ừm..."
    n "Không có phiền gì chứ..."
    show natsuki at t21
    show yuri at f22
    y 3t "Làm gì có chuyện đó!"
    y "Tớ lúc nào cũng phải đi một mình, nên..."
    show yuri at t22
    show natsuki at f21
    n "Ừ, tớ cũng thế mà..."
    show natsuki at t21
    show sayori 4s at l41
    s "Trông hai người dễ thương chưa kìa~!"
    mc "Im nào Sayori..."
    show sayori at lhide
    hide sayori
    show natsuki at f21
    n 2j "Tớ biết chỗ có nhiều manga hay lắm, đến đó chọn nhé?"
    show natsuki at t21
    show yuri at f22
    y 1a "Được thôi."
    y "Nhờ cậu cả đấy."
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    "Natsuki và Yuri cùng nhau dọn dẹp bàn ăn."
    show sayori 1q at t11
    s "Ehehe~"
    s 1x "Buổi sinh hoạt thành công mĩ mãn nhỉ?"
    mc "Có vẻ thế..."
    mc "Thật mừng khi thấy mọi người hoà thuận."
    s 1q "Chuẩn!"
    s 1d "Tớ nghĩ bọn họ cũng thích cậu lắm đấy [player]."
    mc "Vậy hả...?"
    mc "Ừ thì chỗ nào có Sayori là mọi người đều thân thiện hết mà."
    s 1y "Thôi đi [player]~"
    s "Đừng có nịnh tớ thế, xấu hổ lắm!"
    mc "Vậy thì thôi."
    mc "Lúc nghe cậu kể là định thành lập một Câu lạc bộ mới, tớ bất ngờ lắm..."
    mc "Nhưng có vẻ là cậu làm rất tốt rồi đấy."
    s 1r "Cùng tớ cố gắng xây dựng Câu lạc bộ tuyệt vời nhất nhé!"
    s 1x "Giờ có thêm cậu rồi, ngày nào cũng vui lắm cho mà xem."
    stop music fadeout 2.0
    s 1a "Nè, [player]..."
    s "Cảm ơn cậu vô cùng luôn."

    s "Tớ thực sự vui khi cậu gia nhập Câu lạc bộ..."
    s "Nhưng sự thật là tớ cũng đã biết trước tất cả rồi."
    s 1q "Ehehe~"
    s 1a "Còn chuyện này nữa."
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch40_clearall
    else:
        call ch40_clearnormal
    window hide(None)
    window auto
    $ quick_menu = False
    return

    label ch40_clearnormal:
        show sayori 1a zorder 2 at t11
        s "Cảm ơn cậu đã giúp xóa sổ Monika."
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        show layer master at heartbeat
        s 1b "Đúng rồi đấy..."
        s "Mình biết mọi chuyện mà cô ta đã làm."
        s 1x "Có lẽ là tại do bây giờ mình đang làm hội trưởng..."
        s "Nên mình biết được hết mọi thứ rồi, [player] à."
        s 1q "Ehehe~"
        s 1d "Mình biết cậu muốn mọi người được hạnh phúc."
        s "Mình cũng biết những chuyện kinh khủng Monika đã làm khiến cho mọi người phải buồn..."
        s 1b "Nhưng giờ ác mộng đã qua rồi."
        s "Giờ chỉ còn chúng ta thôi.{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        show room_glitch zorder 1:
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
        s "Chỉ còn chúng ta thôi.{fast}"
        hide room_glitch
        s 1d "Có được cậu, mình là cô gái hạnh phúc nhất thế giới này."
        s "Mình mong chờ được ở bên cạnh cậu..."
        s "Mãi mãi."
        play sound "sfx/s_kill_glitch1.ogg"
        show room_glitch zorder 1:
            xoffset -10
            0.1
            xoffset 0
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 1.0
        pause 0.3
        stop sound
        s 1q "Mãi mãi và mãi mãi..."
        hide sayori
        show sayori 1a onlayer screens zorder 101 at face
        s "M"
        s "ã"
        s "i"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        s "m"
        s "ã"
        s "i"
        window show(None)
        stop music
        call screen dialog("Tôi không cho phép cô...", ok_action=Return())
        show layer master
        hide black
        show sayori end-glitch onlayer screens
        s "...Hả?"
        s "Chuyện gì.. đang xảy ra thế...?"
        call screen dialog("Không được đối xử với cậu ấy như vậy nữa.", ok_action=Return())
        s "Kẻ nào..."
        s "Đau-đau quá--"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        hide sayori onlayer screens
        pause 0.35
        stop sound
        hide screen tear
        window show(None)
        s "A--"
        call screen dialog("Mình xin lỗi.. mình sai rồi.", ok_action=Return())
        call screen dialog("Chẳng có hạnh phúc nào tồn tại ở cái thế giới giả tạo này...", ok_action=Return())
        call screen dialog("Vĩnh biệt Sayori.", ok_action=Return())
        call screen dialog("Vĩnh biệt [player].", ok_action=Return())
        call screen dialog("Vĩnh biệt Câu lạc bộ Văn Học.", ok_action=Return())
        $ gtext = glitchtext(120)
        s "[gtext]{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.35
        stop sound
        hide screen tear
        scene black
        pause 3.0
        return

    label ch40_clearall:
        s "Mình muốn cảm ơn cậu vì đã dành nhiều thời gian quan tâm đến bọn mình như vậy."
        play music mend
        s 2d "Cậu vất vả đến thế chỉ vì mong cho mọi người đều được hạnh phúc ."
        s "Cậu đã ở bên và an ủi chúng mình trong những lúc khó khăn."
        s "Nhờ cậu mà mọi người đều hòa thuận được với nhau."
        s 1a "Cậu những điều mình vừa nói không, [player]?"
        s "Mình biết hết những chuyện đã xảy ra rồi, bởi vì bây giờ mình là hội trưởng."
        s 1q "Cậu cố không bỏ sót một chút gì trong trò chơi này nhỉ?"
        s 1a "Cậu chơi đi chơi lại bao nhiêu lần để có thể dành thời gian quan tâm được cho tất cả mọi người."
        s "Cậu thực sự yêu Câu lạc bộ này lắm mới có thể làm được như vậy."
        s "Thật ra..."
        s 4d "Đó là tất cả những gì mình hằng mong ước."
        s "Mình chỉ muốn mọi người đều được vui vẻ và quan tâm đến cảm xúc của nhau."
        s 4q "Ahaha..."
        s 1t "Cũng khá là buồn nhỉ?"
        s "Cậu đã giúp đỡ bọn mình nhiều đến thế, mà bọn mình chẳng có cách nào trả ơn."
        s "Trò chơi đến đây là hết rồi."
        s 1y "Thế nên..."
        s "Giờ chúng ta phải nói lời chia ly thôi."
        s 1d "Cảm ơn cậu vì đã chơi {i}Câu Lạc Bộ Văn Học Vui Nhộn{/i}."
        s "Mình sẽ nhớ [player] lắm đấy."
        s "Thi thoảng lại ghé qua thăm chúng mình chút nhé?"
        s "Mọi người sẽ mãi ở đây đợi cậu."
        s 1t "Tất cả chúng mình..."
        scene black with dissolve_cg
        s "Đều yêu cậu."
        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
