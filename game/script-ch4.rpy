label ch4_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    play music t6


    "Hôm nay đã là chủ nhật rồi."
    if ch4_scene == "natsuki":

        "Cứ nghĩ tới việc Natsuki tới nhà khiến tôi càng cảm thấy lo lắng hơn."

        "Tôi tự nhủ với mình rằng không có gì phải lo lắng cả, nhưng mà chả hiệu quả tí nào."

        "Tôi không biết cậu ta sẽ cư xử ra sao khi chỉ có hai người với nhau?"

        "Tới hôm đó tới giờ, cậu ấy nhắn tôi không biết bao nhiêu tin."

        "Ngay sau khi trao đổi số, bọn tôi gửi cho nhau một tin để kiểm tra. Không ngờ là việc đó lại khơi mào cuộc trò chuyện."

        "Cậu ta cứ như là một người khác khi nhắn tin vậy, sử dụng rất nhiều emoji và từ ngữ rất dễ thương."

        "Nhưng mà lại rất hay phàn nàn, điều này là hiển nhiên với Natsuki rồi."

        "Cơ mà tạm để chuyện về Natsuki sang một bên đã..."
    else:

        "Cứ nghĩ tới việc Yuri tới nhà khiến tôi càng cảm thấy lo lắng hơn."

        "Tôi vẫn tự nhủ với mình là không có gì phải lo lắng cả, nhưng mà chả hiệu quả tí nào."

        "Yuri là một người sống nội tâm và cũng rất dễ gần."

        "Tôi cá rằng khi chỉ có hai người thì cậu ấy sẽ thoải mái giao tiếp với tôi hơn."

        "Chúng tôi vẫn thỉnh thoảng nhắn tin cho nhau."

        "Ban đầu cậu ấy rất ngại ngùng, nhưng rồi cũng quen dần và để cho tôi có thể hiểu hơn về cậu ấy."

        "Cơ mà tạm để chuyện về Yuri sang một bên đã..."

    "Tôi vẫn chưa nghe tin gì từ Sayori kể từ lúc cậu ấy rời câu lạc bộ vào hôm đó."

    "Không có tin nhắn nào như mọi ngày..."

    "Tất nhiên tôi không ép buộc cậu ấy ngày nào cũng nhắn tin với tôi nhưng tôi thực sự lo lắng."

    "Về những điều mà Sayori và Monika đã nói..."

    "Liệu rằng tôi có sai lầm không khi cứ để Sayori như vậy, có thể cậu ấy đang thực sự cần tôi cho dù cố tỏ ra trưởng thành?"

    stop music fadeout 2.0
    scene bg house
    with wipeleft_scene

    "Tôi quyết định sẽ đi thăm Sayori trước khi [ch4_name] đến."

    "Không cần Sayori trả lời, tôi chỉ nhắn \"Tớ sắp sang đây.\" và qua nhà cậu ấy luôn, như tôi vẫn hay làm."

    "Đến nhà Sayori, tôi gõ cửa báo hiệu rồi tự mình mở cửa bước vào."

    "Từ xưa đã vậy rồi, chúng tôi có thói quen vào nhà nhau mà không cần xin phép, coi nhau như thành viên trong một gia đình vậy."
    scene black with wipeleft

    "Căn nhà thật yên tĩnh."

    "Tầng một không có ai, tôi đoán cậu ấy đang ở trong phòng của mình."

    "Thật là lạ khi cậu ấy không chạy xuống và chào đón tôi như mọi khi."

    "Tôi lên phòng ngủ của Sayori và cuối cùng cũng được gặp cậu ấy."
    scene bg sayori_bedroom with wipeleft
    mc "Sayori?"

    play music t10
    show sayori 1ba zorder 2 at t11

    s "Chào, [player]~"
    show sayori 1by

    "Tôi ngồi xuống."

    "Sayori gượng cười, khác hẳn cậu ấy mọi khi."

    "Cả hai đều ngập ngừng, không nói nên lời."

    s "Lần cuối cậu vào phòng tớ... Đã lâu lắm rồi nhỉ?"

    mc "Ah... Cậu nói phải."

    mc "Từ khá lâu rồi đó."

    mc "Mọi thứ vẫn như hồi xưa nhỉ?"

    "Phòng của Sayori lúc nào cũng bừa bộn cả."

    "Tôi nhận ra vẫn những con thú bông ấy và mấy đồ trang trí treo tường ở vị trí của nó suốt bao năm rồi."
    s 2bl "Ehehe~"

    s "Nếu cậu mà đến đây thường xuyên hơn, thì căn phòng đã không bừa bộn như này."

    mc "Tớ toàn phải dọn cho cậu mỗi khi đến đây..."

    s 1bb "Sao hôm nay đột nhiên cậu lại muốn đến đây vậy?"

    s "Chẳng phải cậu đã hẹn gặp [ch4_name] vào hôm nay sao?"

    mc "Ừm, nhưng..."

    mc "...Khoan đã, sao cậu biết được chuyện đó?"

    "Sayori đã bỏ đi trước khi khi các thành viên trong câu lạc bộ bàn về lễ hội."

    s 1ba "Monika đã nói với tớ."

    s "Chả phải cậu ấy là người sắp xếp mọi thứ liên quan đến việc chuẩn bị cho lễ hội à?"

    mc "À, phải rồi..."

    mc "Nhưng còn cậu thì sao?"

    mc "Chẳng phải hôm nay cậu sẽ giúp Monika à?"

    s 4bb "Tất nhiên rồi!"

    s "Nhưng tớ chỉ giúp cậu ấy qua mạng thôi."

    s "Bọn tớ không cần phải gặp mặt nhau."

    mc "Ah, vậy chỉ có tớ và [ch4_name] thôi sao..."
    s 1ba "Yep~"

    "Cuộc đối thoại lại một lần nữa chìm vào im lặng."
    show sayori 1bk

    "Sayori nhìn vào khoảng không vô định."

    "Hành động và biểu cảm không hề giống cậu ấy chút nào."

    "Tôi phải nói ra vấn đề chính thôi."

    mc "Chỉ là...tớ muốn tới hỏi thăm cậu."

    mc "Sau khi cậu bỏ về vào hôm thứ sáu."

    mc "Chắc chắn là có chuyện gì không ổn, cậu đừng có mà giấu tớ!"

    mc "Tớ rất hiểu cậu mà."

    mc "Vậy nên..."

    "Sayori mỉm cười và lắc đầu."

    s 1bd "Thế là không tốt đâu, [player]."


    s "Tại sao mọi chuyện không như mọi khi được vậy?"

    s 1by "Tất cả là lỗi tại tớ."

    s "Nếu tớ không yếu đuối đến vậy và để cảm xúc tiêu cực của mình bộc lộ ra ngoài..."

    s 1bk "Thật là một sai lầm ngu xuẩn..."

    s "Tớ đã khiến cho cậu phải lo lắng đến mức này."

    s "Cậu lẽ ra không phải đến cái chỗ này."

    s 1bd "Cậu lẽ ra không phải vướng bận về tớ trong đầu khi còn đang phải chuẩn bị làm việc cùng người khác."

    s "Đây...chắc là hình phạt của tớ?"

    s "Sự trừng phạt đích đáng dành cho kẻ ích kỉ."

    s "Việc cậu đến đây hôm nay nhất định là như vậy."

    s "Là để tớ phải hứng chịu hậu quả."
    s 4bq "Ehehe~"
    mc "Sayori!"
    show sayori 4bb

    "Tôi đặt hai tay lên vai Sayori."

    mc "Cậu đang lảm nhảm cái quái gì thế?!"

    mc "Cậu có nghĩ gì trước khi thốt ra những lời đấy không?"

    mc "Tớ biết là có chuyện gì không ổn đã xảy ra."

    mc "Nhưng chẳng có lí do gì khiến cho cậu phải như thế cả."

    mc "Vậy nên hãy kể cho tớ biết đó là chuyện gì mau lên...!"

    mc "Tớ sẽ không thôi chừng nào còn chưa biết!"
    s 4bl "Ah..."
    s "Ahaha..."

    "Sayori nở một nụ cười trống rỗng."

    s 4by "Cậu thực sự đẩy tớ vào đường cùng rồi đó, [player]."

    s "Nhưng mà này..."

    s 1ba "Cậu sai rồi."

    s "Chẳng có chuyện gì xảy ra với tớ cả."

    s "Tớ vẫn luôn như thế."

    s "Chỉ là với cậu thì mới lần đầu được thấy."

    mc "Thấy cái gì?"

    mc "Cậu đang nói cái gì vậy hả, Sayori?"
    s 1bq "Ehehe~"

    s 1ba "Cuối cùng cậu đã khiến tớ phải nói ra điều này, [player] à."

    s "Chắc là tớ không còn lựa chọn nào khác nữa rồi."

    s 1bc "Chuyện là..."

    s "Thực sự là cả cái cuộc đời này của tớ tràn ngập sự thất vọng."

    s 1bb "Cậu có biết không?"

    s "Thử nghĩ xem tại sao ngày nào tớ cũng đi học muộn?"

    s "Bởi vì tớ chả tìm được một lí do gì để ra khỏi giường cả."

    s 1by "Cố gắng cũng làm sao mà thay đổi nổi cái thứ thất bại vô dụng này, mọi thứ đều vô ích?"

    s "Tới trường để làm gì?"

    s "Ăn uống để làm gì?"

    s "Có bạn bè cũng để làm gì?"

    s "Mọi người đừng có mà tốn năng lượng để quan tâm tới cái thứ như tớ chứ?"

    s "Đó là cảm nhận của tớ đấy."

    s "Và đó là lý do tại sao tớ chỉ muốn mọi người vui vẻ..."

    s "Để không ai phải lo lắng về tớ."
    mc "..."

    "Tôi bị sốc bởi những lời của cậu ấy."

    "Tôi thậm chí còn không biết phải làm sao để đáp lại."

    "Làm sao mà lại có chuyện như thế được cơ chứ, tôi chơi thân với Sayori từ lâu rồi kia mà?"

    "Cậu ấy thực sự không muốn mình quan tâm tới cậu ấy ư?"

    mc "...Tại sao vậy hả, Sayori?"

    s 1bg "Hử...?"

    mc "Tại sao cậu không bao giờ nói với tớ về điều đó?"

    mc "Cảm giác giống như tớ bị một người bạn thân phản bội vậy."

    mc "Bởi vì nếu tớ biết, tớ sẽ làm mọi thứ để giúp đỡ cậu!"

    mc "Dù cho có thế nào đi chăng nữa...."

    mc "Tớ có thể cố gắng để làm cho ngày nào của cậu cũng là một ngày vui."

    mc "Chúng ta là bạn thân cơ mà!"

    mc "Tất cả những gì cậu cần làm chỉ đơn giản là nói với tớ!"

    s 1bk "Cậu chẳng hiểu gì cả, [player]."

    s "Cậu nghĩ tại sao tớ lại không bảo cậu?"

    s 1bd "Bởi vì sự nỗ lực của cậu với tớ sẽ chỉ là vô ích thôi, thay vì thế cậu có thể làm những thứ quan trọng hơn."

    s "Tớ không muốn được ai chăm sóc hết."

    s "Bản thân không ra gì, còn muốn kéo theo người khác khiến họ vất vả."

    s 1ba "Cảm xúc những lúc như vậy lẫn lộn lắm, tuy là có chút hạnh phúc."

    s "Nhưng cũng khiến đầu tớ đau như búa bổ."
    s 4bq "Ahaha~"

    s 4ba "Vì thế tớ thật lòng luôn muốn cậu kết bạn với những người khác..."

    s "Tớ chỉ muốn giúp mọi người vui vẻ bên nhau mà thôi."

    s 1bb "Nhưng mà, về sau tớ cũng khám phá ra nhiều điều khác."

    s "Nhìn thấy cậu kết bạn và ngày càng thân thiết với mọi người trong câu lạc bộ..."

    s 1bk "Cảm giác đau đớn như bị giáo đâm qua tim tớ."

    s "Đó là lí do tại sao."

    s "Lí do tại sao tớ nghĩ ông trời chỉ muốn tra tấn tớ thôi."

    s "Con đường nào tớ chọn cũng đầy đau đớn cả."
    s "Ahaha~"

    mc "Cậu đã đúng khi bảo là tớ chả hiểu cái gì cả..."

    mc "Tớ không hiểu được cảm xúc của cậu, Sayori."

    mc "Nhưng tớ cũng không cần phải hiểu."

    mc "Cho dù có phải trả bất cứ giá nào, tớ muốn giúp cậu không bị tổn thương..."

    mc "Đó là những gì tớ sẽ làm."

    s 1bd "Không, [player]."

    s "Sẽ chẳng có gì."

    s "Chẳng có gì cả."

    s "Điều duy nhất giúp được tớ là cứ để mọi chuyện diễn ra bình thường như bao ngày."

    s 1bk "Nhưng tớ lại quá ích kỉ."

    s "Tớ đã khiến cho cậu phát hiện ra con người thật tệ hại của tớ."

    "Dòng nước mắt chảy dài trên khuôn mặt Sayori."

    s 1bv "Tớ bắt cậu tham gia câu lạc bộ văn học cũng là vì bản tính ích kỉ."

    s "Và con tim đau đớn này đã bị trừng trị theo cách mà tớ không thể hiểu được."

    s "Và giờ thì tới cậu, tớ cũng làm cậu tổn thương theo."

    s 1bt "Tớ thật yếu đuối và ích kỉ."

    s "Đó là con người thật sự của tớ đấy."

    s "Và đó là lý do tại sao tớ chấp nhận hình phạt này."

    s 1bv "Bởi vì tớ xứng đáng nhận nó...!"

    "Không suy nghĩ gì thêm, tôi vòng tay qua vai Sayori."

    "Tôi ôm chặt cậu ấy vào lòng."
    scene black with dissolve_cg
    s "A-Ah--"
    s "[player]..."
    mc "Sayori."

    mc "Tớ không quan tâm cậu cảm thấy tồi tệ như nào."

    mc "Việc cậu thuyết phục tớ gia nhập câu lạc bộ cũng giúp tớ hạnh phúc mà."

    mc "Được bên cạnh cậu nhiều hơn và nhìn cậu vui vẻ mỗi ngày."

    mc "Việc kết bạn với những người khác chỉ là phụ."

    mc "Làm ơn đừng bao giờ quên rằng tớ quan tâm tới cậu đến nhường nào."

    "Tớ cũng không bao giờ thay đổi suy nghĩ đó đâu."
    s "[player]..."

    "Sayori không ôm lại tôi."

    "Mặc dù tôi đang ôm cậu ấy, nhưng đôi tay của Sayori vẫn không nhúc nhích."

    "Tiếng nấc của cậu ấy thổn thức bên tai tôi."

    s "Không..."

    s "Đừng làm vậy...với tớ..."

    s "Xin cậu đó..."
    s "[player]..."

    s "Tớ..."

    "Sayori nghẹn ngào nói trong tiếng khóc nức nở."

    "Tôi không biết những việc tôi làm như này có đúng không."

    "Nhưng tôi muốn cậu ấy hiểu được sự quan tâm của tôi."

    mc "Nếu cậu cứ một mực cho rằng mình ích kỉ, vậy thì tớ cũng ích kỉ luôn đấy."

    mc "Tớ sẽ tìm cách thay đổi chuyện này, bằng bất cứ giá nào đi chăng nữa."

    mc "Tớ sẽ giúp cậu xua tan đi cảm giác đó."

    mc "Bất cứ việc gì cậu cần tớ làm..."

    mc "Đừng ngại ngần nói ra."

    mc "Nếu cậu không làm vậy, tớ sẽ bực lắm đấy."
    s "..."

    s "Tớ...không biết nữa..."

    s "Tớ không biết..."

    s "Tớ không biết..."

    "Cuối cùng Sayori cũng ôm lại tôi, hai tay vòng qua người tôi, nhẹ nhàng."

    s "Tớ không biết gì cả."

    s "Tất cả mọi thứ đều thật đáng sợ..."

    s "Tớ không thể hiểu nổi cảm xúc của chính mình nữa, [player]..."

    s "Chỉ có những lúc tớ đau khổ thì tớ mới không thấy cảm xúc gì."

    s "Nhưng..."

    s "Cái ôm của cậu ấm áp quá..."

    s "...Và nó cũng thật đáng sợ nữa."
    scene bg sayori_bedroom
    show sayori 1bv zorder 2 at i11
    with dissolve_cg

    "Sayori buông tôi ra."

    "Tôi cũng bỏ tay khỏi người của cậu ấy."

    mc "Ngày mai là lễ hội rồi."

    s 1bk "Ừm..."

    mc "Sẽ vui lắm đấy, nhỉ?"

    s "Ừm."

    mc "Hãy để tớ dành cả ngày hôm đó bên cạnh cậu nhé?"
    s 1bh "U-Um..."
    s "Ah--"

    mc "Vậy quyết định thế nhé."

    mc "Tớ hứa đấy."

    s 1bk "Tớ..."

    s "Mong rằng mọi chuyện sẽ tốt đẹp..."

    mc "Ừm."

    "Sayori lấy tay lau nước mắt."

    "Nếu được thì tôi định ở lại đây cả ngày luôn."

    "Khỉ thật, tại sao mình lại có kế hoạch vào hôm nay cơ chứ..."

    mc "Có lẽ tớ nên hủy--"

    s 1bh "Không, đừng--!"

    s 1bg "Đừng làm vậy..."

    s "Nếu cậu làm như thế...tớ sẽ không tha thứ cho cậu đâu."

    mc "Nhưng..."

    mc "Dù sao [ch4_name] cũng sắp sửa đến nhà tớ mất rồi..."

    mc "Cậu đến nhà tớ làm cùng luôn nhé?"

    mc "Tớ nghĩ là sẽ vui lắm."

    "Thật bất ngờ, Sayori lắc đầu."

    s 1bd "Tớ xin lỗi."

    s "Tớ không muốn làm gì hôm nay nữa."

    s "Cậu hiểu điều đó mà?"
    mc "Ah..."

    mc "Thực sự...tớ không hiểu câu nói của cậu lắm."

    mc "Nhưng dù sao thì tớ sẽ cố gắng làm việc để buổi lễ ngày mai sẽ thật tuyệt vời với cậu."

    s "Vậy là ổn rồi."

    s "Cậu không cần phải lo lắng quá nhiều đâu."

    s 4ba "Tớ sẽ gặp lại cậu vào ngày mai."

    mc "...Được thôi."

    mc "Tớ rất mong đợi đến lúc đó."
    scene bg residential_day with wipeleft_scene

    "Tôi nói lời tạm biệt với Sayori và rời khỏi nhà cậu ấy."

    "Trên đường về nhà, tôi vẫn cảm thấy có chút không thoải mái."

    "Nhưng tôi không thể bận tâm về nó mãi khi mà [ch4_name] sắp sửa đến rồi..."

    "Chắc là Sayori nói đúng."

    "Tôi không nên suy nghĩ quá nhiều mà nên tập trung để ngày mai sẽ là một ngày tuyệt vời."

    "Hãy làm tốt những việc cần làm trước mắt đã!"
    call expression "ch4_exclusive_" + ch4_scene
    call ch4_end

    return


label ch4_exclusive_natsuki:
    play music t6 fadeout 2.0
    scene bg house with wipeleft_scene

    "Tôi chỉ phải đợi Natsuki có vài phút thôi."

    "Khi tôi còn đang mải suy nghĩ lơ mơ thì đã nhận được tin nhắn của cậu ấy bảo rằng đang ở ngoài cửa rồi."

    "Không chần chừ, tôi mở của cho cậu ấy vào."
    show natsuki 2bj zorder 2 at t11
    mc "..."

    n "Chào."

    mc "...Chào cậu."

    "Tôi không biết tôi đang mong chờ điều gì, nhưng lần đầu nhìn thấy Natsuki trong thường phục khiến tôi khá ngạc nhiên."

    "Thật là một bộ trang phục dễ thương, trái ngược hoàn toàn với bộ đồng phục thường ngày."

    n 4bc "Xì, chưa gì cậu đã làm tôi thấy ngại rồi!"

    n "Chúng ta phải làm việc lâu đấy, đây là lần đầu cậu nhìn thấy tôi ngoài trường nhưng hãy cứ như thường ngày đi xem nào."

    n "Mà kệ cậu, tôi vào đây."
    scene bg kitchen
    show natsuki 1bj zorder 2 at t11
    with wipeleft

    mc "Cậu mang nhiều thứ thế..."

    "Natsuki vác theo một cái túi lớn chứa đủ loại dụng cụ làm bánh."

    n 2bj "Ừ thì tại tôi nghĩ chắc chắn là bếp nhà cậu không hề có tí dụng cụ làm bánh nào cả mà."

    n "Cậu đã mua đủ những thứ tôi bảo chưa?"

    mc "Ừm, xong cả rồi."

    "Hôm qua, Natsuki đã yêu cầu tôi những nguyên liệu cần thiết nếu bếp nhà tôi không có."

    n 2bl "Tốt!"

    n "Thật mừng là cậu hoàn thành xuất sắc công việc được giao."

    mc "Ừm...Không vấn đề gì."

    "Tôi rất bất ngờ, Natsuki khen ngợi tôi thay vì nói những lời châm chọc thường ngày."

    "Chắc là khi ra ngoài cậu ấy cư xử khác với lúc ở trong trường?"

    mc "Nhà bếp thẳng tiến nào..."

    n 2by "Khoan đã, cậu định cứ để tôi phải vác cái bọc nặng trĩu này á?"

    n "Tính ga-lăng của cậu vứt đâu mất rồi hả, [player]?"

    mc "Gì cơ..."

    mc "Tớ đâu phải là một quý ông mà cần cái đó?"

    "Natsuki đưa cái túi sang cho tôi đỡ lấy."
    mc "Ghk--"

    mc "Nặng vãi chưởng--!"
    n 4bz "Ahaha!"

    n "Tôi đã mang nó từ tận nhà đến đây đấy."

    n 4bl "Cậu thấy tôi có giỏi không?"

    mc "Ừ giỏi..."

    mc "Rất là ấn tượng đấy, Natsuki à."

    mc "Có vẻ đúng là tớ đã luôn đánh giá thấp cậu rồi."
    n 4by "Ehehe~"

    n "Là do cậu nghĩ tôi lùn có phải không?"

    n 4ba "Đồ khốn."

    "Natsuki đấm vào ngực tôi một cái."

    mc "Này, này."

    mc "Chiều cao của cậu thì có liên quan quái gì đến việc đó."

    mc "Cậu thực sự ghét cái chiều cao khiêm tốn của mình thế à?"
    n 1bk "Hả?"
    n "Ừ thì..."

    n 1bc "Tôi không có ghét nó..."

    n "Chỉ là, tôi muốn mọi người đừng có nghĩ rằng nhỏ con thì không làm được việc gì."

    n 1ba "Nhỏ bé mà vẫn làm được hơn người khác cảm giác tuyệt lắm."

    n "Nhưng mà chỗ đó..."

    n 5bw "...Mà thôi, không có gì đâu!"

    n "Tại sao cậu lại bắt tôi nói ra những điều ấy hả?"

    n 5bq "Đừng có tưởng cậu có thể làm cho tôi nói mấy điều kì quặc chỉ vì chúng ta đang không ở trường nhé!"

    n "Bắt đầu làm việc được chưa đây? Có nhiều thứ tôi cần phải dạy cho cậu lắm đấy."
    mc "Ahaha."

    n 5bn "Cậu cười cái gì chứ??"

    mc "Thế mới giống cậu thường ngày chứ."

    mc "Trông cậu rất vui vẻ những lúc nói thẳng thắn suy nghĩ trong đầu như vậy."

    n 1bm "N-Này!"

    n "Cậu {i}đang{/i} đối xử với tôi như là một đứa trẻ con đấy à!"

    n "Tôi đã cố gắng tử tế với cậu một chút rồi đấy có biết không."

    n 1br "Chỉ vì tôi không có cơ thể trưởng thành và quyến rũ như Yuri mà cậu tự cho mình cái quyền coi tôi như trẻ c--"
    n 1bo "A-Ah--"

    "Natsuki nói lắp bắp, mặt cậu ấy đỏ ửng lên."
    mc "Natsuki à..."

    n 1bp "Quên chuyện vừa rồi đi!"

    n "Tôi không có nói gì hết nữa."

    mc "Tớ xin lỗi."

    n 1bh "Hả?"

    mc "Tớ rất cảm kích việc cậu đã cố cư xử một cách tử tế."

    mc "Đáng lẽ ra tớ cũng nên tỏ ra tử tế một chút."

    mc "Nhưng về vấn đề kia..."

    mc "Về vấn đề cậu đang lo lắng, hãy nhớ rằng rằng ngoài kia có hàng triệu người cũng có thân hình như cậu."
    n 1bq "Ah..."

    n "Làm sao mà cậu...dám khẳng định chắc nịch như thế được?"

    mc "Cứ tin tớ lần này đi."

    n "..."

    n 5bx "...Kinh tởm."

    mc "Này!"

    mc "Vừa rồi là nói tớ đấy hả?"

    n 5bw "Thì còn có ai ở đây nữa à?"

    mc "Trời ạ..."

    mc "Chúng ta nên bắt đầu vào việc đi thì hơn."
    n 2bl "Ahaha!"

    n "Cậu có vẻ khó chịu khi một đứa con gái bảo cậu là đồ kinh tởm nhỉ."

    n 2bd "Cuối cùng cũng tìm ra được điểm yếu của cậu rồi, [player]."

    "Natsuki cười khúc khích."

    mc "Tha cho tớ đi..."

    "Tôi cứ kệ cho Natsuki thích châm chọc tôi thế nào cũng được, sao mà cản nổi cậu ta."

    "Ít nhất thì việc đó cũng khiến cho cậu ta vui vẻ hơn, những thứ trong túi được lấy ra và chúng tôi bắt đầu công việc."

    scene bg kitchen
    with wipeleft_scene

    "Trong chớp mắt, cả cái phòng bếp trở thành một mớ hỗn độn."

    "Thìa, đĩa bát bẩn, bột mì, nước tràn và túi ni lông rải rác khắp mọi ngóc ngách căn phòng."

    "Cái máy trộn không đủ lớn để làm một lúc hết chỗ bột trong một lần được, vì vậy chúng tôi phải chia nhỏ ra trộn nhiều lần."

    "Natsuki luôn quan sát tỉ mỉ những gì tôi làm để chắc chắn rằng tôi không phá hỏng món bánh nướng của cậu ấy."
    show natsuki 2bk zorder 2 at t11

    n "[player], cậu để lọ phẩm màu ở đâu vậy?"

    n "Bột sắp được rồi, đưa tôi cái khay để bỏ nó vào."

    mc "Hình như phẩm màu ở trong cái túi để cạnh bàn ấy."

    mc "Nó dùng để làm gì thế?"

    n 4bl "Để tạo màu cho bánh chứ còn gì nữa!"

    n 4bj "Tôi sẽ làm mỗi khay một màu bánh khác nhau."

    n "Bằng cách này thì mặc dù hương vị không khác nhau là mấy, nhưng vẫn tạo cảm giác mọi người đang tự chọn bánh họ thích."

    mc "Ah, ý tưởng dễ thương đấy."

    mc "Vậy chúng ta có làm tương tự với kem không?"

    n 4bk "Cậu thích thế à?"
    mc "Ah..."

    mc "Cậu đang hỏi tớ đấy à?"

    mc "Tớ thực sự không biết nữa, vậy nên..."

    n 1bm "Thôi nào..."

    n "Cậu vẫn chưa đặt cả tấm lòng của mình vào việc này!"

    n "Cứ coi như việc này rất vui vẻ đi, đừng căng thẳng."

    mc "Tớ đang vui đây mà..."

    "Tôi không biết rằng Natsuki đang muốn gì ở tôi nữa."

    "Trong khi nói chuyện, tôi xem cậu ấy đặt bột vào những chiếc bát nhỏ và nhỏ vài giọt màu thực phẩm vào từng bát."

    mc "Ah, trông thật tuyệt."

    n 2bj "Thấy chưa?"

    n "Nướng bánh không chỉ là cứ làm theo sách hướng dẫn đâu."

    n "Công đoạn trình bày là phần để cậu tha hồ sáng tạo và cũng là phần vui nhất."

    n "Được nhìn thấy ánh mắt thèm thuồng của những người sẽ ăn chúng là một phần thưởng cực kì giá trị đối với tôi."

    mc "Giống như mấy chiếc cậu làm vào ngày tớ vào hội đó hả?"

    "Tôi nhớ lại cái cách cậu ấy tự hào giới thiệu những chiếc bánh nướng hình mèo, cùng với nét mặt hân hoan của Sayori và Monika."

    "Tôi tự hỏi liệu tôi cũng có thể làm Natsuki tự hào như thế không?"

    mc "Ừm..."

    mc "Vậy thì tớ cũng sẽ lên màu cho kem."

    n "Cuối cùng cậu cũng hoàn toàn nhập cuộc."

    n "Nhưng nhớ là phải làm kĩ càng phần trộn kem trước khi dùng phẩm màu nhé."

    mc "Ừm, tớ hiểu rồi."

    "Cái máy trộn đang bị dùng để trộn bột, vì vậy tôi phải trộn cái bát kem to đùng bằng cây đánh trứng cầm tay."

    n 4bc "Hử?"

    n "Phần kem vẫn chưa được đều!"

    n "Cậu phải ráng sức lên đi chứ?"

    mc "À, ừm..."

    mc "Tớ sẽ làm thêm một lúc nữa."

    n 4bg "Xì, tôi sẽ phải ở đây cả đêm mất thôi nếu cậu chỉ làm được có vậy."

    n "Nhìn đây này."

    "Natsuki giật lấy cây đánh trứng và dùng tay còn lại của cậu ấy hơi nghiêng bát kem."

    n 4be "Cậu cần...phải đánh...thật lực vào!"

    "Chỉ mất có vài giây thôi, phần kem đã được đánh đều và quyện vào nhau."

    n 4ba "Đấy thấy không?"

    "Natsuki dùng một ngón tay quệt nhẹ ít kem trong bát và nếm thử như để kiểm tra."

    "Thấy thế, tôi cũng làm theo."

    n 1bh "Này!"

    "Natsuki ngay tức khắc nắm lấy cổ tay tôi."

    n 4bh "Tôi không muốn có ngón tay ghê tởm của {i}cậu{/i} ở trong bát kem của tôi đâu."

    mc "Kem của cậu á?"

    mc "Ai mới là người làm kem từ đầu tới giờ?"

    "Tôi đáp trả lại và cố gắng đưa ngón tay vào trong bát."

    n 4by "Đừng có để tôi phải đánh cậu như đánh kem đấy!"

    mc "Có giỏi thì cậu thử làm thế đi!"

    "Tôi đẩy mạnh hơn đủ để ngón tay có thể chạm tới phần kem trong bát."

    "Ngay đúng lúc tôi đang đắc thắng vì đã lấy được chút kem và định bỏ trốn thì Natsuki kéo giật tôi lại."
    mc "Ah--!"

    "Lực kéo của Natsuki làm tôi mất thăng bằng và ngã nhưng vô tình cũng khiến cậu ấy ngã theo tôi."

    n 1bx "Đồ kinh tởm!"

    n "Câụ làm kem dính trên mặt tôi rồi này!"

    mc "Cậu nghĩ đó lỗi của ai hả?!"

    "Một cục kem dính trên má của Natsuki."
    n 1bw "Nnn--"

    "Cậu ta cố gắng liếm chỗ kem nó bằng lưỡi của mình, nhưng chúng lại quá xa."

    n 1br "Mồ..."

    n "Cho cậu biết mặt."

    n 4bd "Nhận lấy này!"

    "Natsuki đành dùng tay quệt chỗ kem trên má nhưng sau đó cậu ta đưa tay hướng về phía mặt tôi."

    mc "Còn lâu--!"

    "Tôi nhanh hơn rồi."

    "Tôi nắm lấy cổ tay cậu ấy trước khi bị bôi kem lên mặt."

    "Natsuki cố cả tay còn lại để chống trả, nhưng tôi cũng bắt được nó."
    $ persistent.clear[4] = True
    scene n_cg3_base
    show n_cg3_exp1
    show n_cg3_cake
    with dissolve_cg

    n "Ahahaha! Dừng lại đi!"

    mc "Chỉ khi nào cậu xin lỗi vì đã gọi tớ là đồ kinh tởm!"

    n "Được rồi, được rồi!"

    n "Tôi xin lỗi vì đã gọi cậu là đồ kinh tởm."

    n "Cậu biết là tôi không có ý đó thật mà."

    n "Chỉ là do phản ứng của cậu trông rất thú vị."

    n "...Cậu cũng làm thế với tôi suốt rồi còn gì!"

    n "Lúc nào cũng khiến tôi nói ra những thứ kì quặc."

    n "Cậu không nên trêu chọc con gái như thế đâu."

    mc "Thật vậy hả?"

    mc "Vậy thì, có lẽ tớ cũng không nên làm thế này..."
    show n_cg3_cake at cgfade
    hide n_cg3_cake

    "Tôi đưa tay Natsuki lại gần và liếm chỗ kem dính trên ngón tay cậu ta."
    show n_cg3_exp1 at cgfade
    show n_cg3_exp2 at cgfade
    hide n_cg3_exp1

    n "C-C-Cái gì--?"

    n "C-Cậu vừa--"
    n "A-Ah--"

    "Natsuki trông rất ngạc nhiên, cậu ấy có vẻ bối rối thay vì nổi cáu trước hành động của tôi."

    "Mặt cậu ấy đỏ ửng lên."
    hide n_cg3_exp2
    n "[player]..."

    n "Cậu đúng là không nên làm điều đó với con gái...trừ khi cậu thực sự thích họ..."

    n "Cậu biết điều đó mà...phải không?"
    mc "..."

    "Cậu ấy đang hỏi cái gì vậy?"

    "Sao tự nhiên bầu không khí thay đổi nhanh thế?"

    mc "Tớ..."

    "Natsuki im lặng nhìn tôi."

    "Tôi có thể nghe thấy cả tiếng thở hổn hển của cậu ấy."

    "Sao tự nhiên tôi lại cảm thấy hơi chóng mặt thế nhỉ...?"
    n "Á?!"
    scene bg kitchen with dissolve_cg

    "Bất ngờ, chuông báo cháy kêu lên."

    "Natsuki chạy vội đến chỗ lò nướng."

    mc "Có gì bị cháy à?"

    mc "Tớ tưởng cậu còn chưa cho bánh nướng vào lò."


    n "{i}*Ho*{/i}"

    n "Hèn gì..."

    n 1bb "Sao cậu lại bỏ khay không có gì vào đây, đồ ngốc này!"

    n "Sai lầm ngớ ngẩn như thế mà cũng mắc thì tài thật. Ai mà chả biết phải xếp bánh lên khay rồi mới cho vào lò."

    mc "Là tại cậu không kiểm tra trước khi bật lò lên đấy chứ!"

    n 1bs "Đừng đổ lỗi của cậu lên đầu tôi!"
    n "Trời..."

    "Natsuki sử dụng đôi găng tay lót để lấy cái khay ra khỏi lò."

    "Cậu ấy đặt nó lên trên bếp."

    "Đồng hồ báo cháy cũng ngừng kêu."

    n 1bq "Bây giờ..."

    n "Tôi...sẽ đặt bánh vào lò nướng."

    mc "Ừm..."

    "Sự căng thẳng của khoảnh khắc trước đấy vẫn còn đọng lại trong đầu chúng tôi."

    "Nhưng khoảnh khắc đó đã tan biến mất rồi."

    "Tôi nhìn Natsuki đưa khay bánh nướng vào lò."

    "Sau đó, tôi nhặt cây đánh trứng lên và tiếp tục trộn kem như chưa hề có chuyện gì xảy ra."

    scene bg kitchen
    show natsuki 4bz zorder 2 at t11
    with wipeleft_scene

    n "Ahh, mùi thơm quá!"

    "Những chiếc bánh nướng đã sẵn sàng để ra lò."

    "Ngay khi Natsuki vừa mở lò lấy bánh, một hương thơm ngọt ngào, ấm áp tràn ngập căn phòng."

    n 4bl "Trông chúng dễ thương quá đi mất thôi!"

    "Cậu ấy tự hào khoe với tôi những chiếc bánh đủ màu trên từng khay."

    mc "Trông chúng sẽ ngon lành hơn nữa khi chúng ta thêm kem vào."

    n 2ba "Không cần cậu phải chuyện đó nói thì {i}tôi{/i} cũng biết!"

    n "Tôi đã mang theo cả đồ để trang trí rồi đây, cố gắng làm cho sáng tạo nhé."

    n "Đây, hãy múc một ít kem vào mấy cái túi này."

    "Natsuki đưa cho tôi vài chiếc túi bơm kem."

    n 2bj "Những chiếc túi bơm kem này sẽ làm cho lớp kem phủ trên bánh trở nên đẹp và mềm mại hơn là quệt thẳng vào."

    n "Có thể gắn vòi hình bông hoa nữa này!"

    n "Nhưng lúc này chúng ta chưa cần phải sử dụng cái đó."

    mc "Vậy còn cái này để làm gì?"

    "Tôi cầm lấy một cái túi bơm kem có vòi nhỏ hơn."

    n 4bk "Cái vòi nhỏ để có thể vẽ những họa tiết trang trí."

    n "Cậu cũng thể sử dụng nó để viết chữ lên bánh."

    n "Như là 'Chúc mừng sinh nhật!' hoặc gì đó."

    mc "Huh, tớ hiểu rồi..."

    mc "Tớ vừa nảy ra một ý tưởng với cái này."
    n "Hử?"

    mc "Sự kiện của chúng ta làm về văn học, đúng không?"

    mc "Chúng ta có thể làm bánh có chút không khí 'văn chương' bằng cách viết những từ khác nhau trên mỗi chiếc bánh."

    mc "Sẽ rất thú vị khi mọi người chọn bánh nướng dựa trên những từ mà họ thích."
    n 1bq "Uu..."
    mc "Hm?"

    n "Tôi cứ nghĩ cậu sắp sửa thốt ra những ý tưởng ngu ngốc..."

    n 1bs "Nhưng nó lại...thực sự rất là dễ thương đấy, vậy nên..."
    mc "Ahaha."

    mc "Chắc tại tớ bị ảnh hưởng từ cậu."

    n 5bh "C-Cậu nói thế là ý gì hả?"

    n "Tôi không có dễ thương!"

    mc "Thôi nào..."

    mc "Chúng ta đâu có ở trường, sẽ không có ai đánh giá gì đâu."

    mc "Với cái cách cậu cư xử và mặc bộ quần áo như này mà cậu muốn tớ không nghĩ cậu dễ thương được à."

    n 5bs "Ừ-ừ thì..."

    "Giọng của Natsuki nhỏ dần."

    n "Tôi cũng nghĩ cậu như thế..."
    mc "Hả?"

    mc "Cậu vừa nói?"

    n 1bw "K-Không, không có gì đâu!"

    n "Mau trang trí cho bánh thôi!"

    "Natsuki nhanh chóng thắt những vòi bơm vào mỗi túi."

    n 1bh "Sẽ có nhiều việc để làm đấy, chúng ta không được lãng phí thời gian đâu!"

    n "Đây, tôi sẽ chỉ cho cậu cách."

    "Không cho tôi có cơ hội để nói về chuyện vừa rồi, Natsuki nhanh chóng chuyển về công việc ngay."

    "Cậu ấy chỉ cho tôi cách phủ kem và sau đó cả hai đều chăm chú làm việc."

    scene bg kitchen with wipeleft_scene

    "Sau khi hoàn thành, Natsuki đặt tất cả bánh cạnh nhau để chúng tôi có thể chiêm ngưỡng thành quả của mình."
    show natsuki 4bl zorder 2 at t11

    n "Chúng thật dễ thương quá đi mất thôi!"

    mc "Ừm, chúng thật là dễ thương."

    n 1bm "Uu...Tôi thèm ăn luôn một cái quá!"

    mc "Ừm, thì cậu cứ ăn đi."

    mc "Có một cái chẳng sao đâu mà."

    n 1bc "Ừm, nhưng mà..."

    n "Tôi còn phải để bụng để ăn cơm bố tôi nấu tối nay nữa."
    mc "Ahaha."

    mc "Sayori thì lại hoàn toàn trái ngược."

    mc "Nếu cậu ấy mà ở đây, thì phải hơn chục cái sẽ bị thủ tiêu trong chớp mắt."

    mc "Và cậu ấy sẽ bỏ luôn bữa tối."

    n 4bg "Nhưng mà, như thế không tốt cho sức khỏe đâu!"

    n 4bs "Với cả, tôi phải ăn nhiều nhất mình có thể để không phụ công sức bố tôi nấu..."

    n 4bq "...Dù sao thì."

    n 4bc "Tôi đã mong là chúng ta vẫn còn thời gian để cùng đọc manga, nhưng đến giờ tôi phải về rồi..."

    mc "Ồ, cậu về sớm vậy?"

    mc "Chán nhỉ."

    n 1bg "Tại cậu làm việc quá lề mề đấy!"

    n "Cậu nên xem xét lại bản thân đi."

    n "Không phải lúc nào cũng có được cơ hội như này đâu."

    mc "Trời ạ..."

    "Như thường lệ, Natsuki lại đổ lỗi cho tôi."

    n 2bk "Ngày mai cậu đem theo bánh nướng đến trường luôn nhé?"

    n "Nếu cậu và Sayori chia nhau mang đi thì chỉ cần một chuyến là mang được cả thảy rồi."

    mc "Ừm, cứ như vậy đi."

    mc "Và đừng lo, tớ sẽ không để cậu ấy ăn vụng đâu."
    n 2ba "Ahaha."

    n "Ước gì cậu ấy cũng nghe lời tôi như nghe lời cậu nhỉ."

    mc "À..."

    mc "Ừm."
    show natsuki zorder 1 at thide
    hide natsuki

    "Tôi nghĩ lại cuộc trò chuyện của tôi và Sayori trước đó."

    "Tôi cảm thấy thật vô vọng."

    "Sayori bình thường luôn nghe lời tôi, nhưng vào lúc đó cậu ấy chẳng chịu nghe gì cả, cứ như là một người nào khác."
    show natsuki 4bl zorder 2 at t11

    n "Okay, tôi đã thu dọn xong rồi đây."

    n "Hôm nay cậu làm việc tốt lắm!"

    mc "Cậu cũng vậy."

    mc "Để tôi tiễn cậu một đoạn..."

    scene bg house with wipeleft_scene

    "Vậy là Natsuki đã sẵn sàng chuẩn bị ra về."

    "Cảm giác buổi chiều hôm nay trôi đi thật nhanh chóng."

    "Hơn nữa..."

    "Có phải tôi đã có được cơ hội để có thể gần gũi hơn với cậu ấy như tôi muốn không nhỉ?"
    show natsuki 1bh zorder 2 at t11

    n "À, ừm..."

    n "Tôi nghĩ tôi sẽ về, và..."

    n 1bq "Cảm ơn cậu vì đã giúp đỡ và mọi thứ..."

    n "Hẹn gặp lại cậu vào ngày mai."

    mc "Đợi đã, Natsuki."


    mc "Những lời mà cậu nói vào lúc trước...về việc không có nhiều cơ hội như thế này ấy."

    mc "Sẽ không chỉ có vậy thôi chứ?"

    mc "Hôm nay vui lắm."

    mc "Cậu đã chỉ cho tớ thấy làm bánh vui đến thế nào!"

    "Vậy nên là..."

    mc "Cậu có thể đến đây vào bất cứ khi nào cậu muốn."

    mc "Chúng ta sẽ có thêm nhiều cơ hội vui vẻ với nhau giống như chiều hôm nay."

    mc "Có thể là cả đọc manga nữa, hay đi đâu đó--"
    n 1bm "Um--"

    n "Cậu...thực sự có ý đó hả?"

    "Ánh mắt Natsuki tràn đầy căng thẳng, cứ như cậu ấy đang cố gắng giấu đi biểu cảm của mình."

    mc "Ừm."

    mc "Tớ muốn dành nhiều thời gian bên cậu hơn."
    n 1bq "[player]..."

    n "Tôi cứ nghĩ cậu chỉ quan tâm đến hoàn thành công việc thôi..."
    n 1br "Uu..."

    n 1bn "Tôi xin lỗi, tôi phải về sớm hôm nay."

    n "Tôi thực sự không muốn như thế!"

    n "Thật sự tôi cũng muốn...ở lại đây lâu nhất có thể."

    n "Tôi cũng cảm thấy như cậu vậy, vì thế nên..."
    stop music fadeout 2.0
    show natsuki 1bi at face with dissolve

    "Natsuki bất chợt lại gần tôi."

    mc "Khoan đã, Natsuki--"

    "Chỉ đứng cách nhau có một bước chân, Natsuki ngước lên nhìn tôi."

    "Tôi có thể cảm thấy những ngón tay của cậu ấy nhẹ nhàng nắm lấy vạt áo tôi, cứ như đang giữ tôi lại vậy."

    "Tôi không thể rời mắt khỏi khuôn mặt dễ thương kia, hai má hồng rực, ánh mắt lấp lánh, cặp môi hơi khẽ mở."

    "Chuyện gì đang diễn ra thế này...?"

    "Cảm nhận được hơi thở nhẹ nhàng ấy, đầu óc tôi bắt đầu trở nên choáng váng."

    n 1bh "Tôi cũng cảm thấy..."

    n "Từ lâu rồi..."

    show natsuki zorder 2 at t11

    "Natsuki đột nhiên lùi lại."
    n "S-Sayori?!"
    mc "Hể?!"
    show natsuki zorder 2 at t22
    show sayori 1bl zorder 3 at f21
    s "Ah..."

    s "C-Chào cậu, [player]..."
    mc "Sayori--!"

    mc "Vừa nãy, chúng tớ chỉ--"
    s 1bq "Ehehe~"

    s "Không sao đâu, [player]."

    s 1ba "Tớ chỉ định ghé qua chào cậu thôi~"
    show sayori zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5bq "A-Ah..."

    n "Thì..."

    n 5bw "L-Lẽ ra cậu nên tới đây sớm hơn một chút!"

    n "Tại tớ đang chuẩn bị về nhà mất rồi, và..."
    show natsuki zorder 2 at t22
    show sayori zorder 3 at f21

    s 1bh "Aw, vậy sao?"

    s "Thế thì buồn nhỉ..."
    show sayori zorder 2 at t21
    show natsuki zorder 3 at f22

    n 2bq "À, ừm..."

    n "Tớ sẽ lại gặp cậu vào lễ hội ngày mai mà, không sao đâu."

    n 2bb "Đừng có mà ăn vụng bánh nướng đấy nhé!"

    n "Hẹn gặp lại cậu sau!"
    show natsuki at lhide
    hide natsuki

    "Natsuki bối rối chạy thật nhanh đi trong khi Sayori đứng sau vẫy tay chào tạm biệt."
    return

label ch4_exclusive_yuri:
    play music t6 fadeout 2.0
    scene bg house with wipeleft_scene

    "Ngay khi vừa bước đến cửa nhà thì tôi đã phải giật mình vì một chuyện không lường trước."
    mc "Yuri--?"
    show yuri 2bq zorder 2 at t11
    y "Ah..."

    y "Ơn trời..."

    mc "Cậu đến....hơi sớm quá nhỉ..."

    mc "Mình xin lỗi, mình có việc phải ra ngoài!"

    mc "Bắt cậu đợi ở ngoài thế này. Cậu đến đã lâu chưa?"

    y 1bf "Không sao đâu, mình chỉ vừa mới đến thôi."

    y 1bh "Chỉ là có hơi lo lăng một chút khi bấm chuông mà không thấy ai mở cửa..."

    mc "Cậu có thể nhắn tin cho tớ mà."

    mc "Nếu biết vậy thì tớ đã chạy về nhà thật nhanh rồi."

    y 2bv "Ah...ừ nhỉ..."

    y "Mình lỡ quên mất nó...vì một vài lí do."

    "Sao cậu ấy lại quên cái điều hiển nhiên vậy chứ, nhưng mà kệ đi, tôi quyết định không hỏi."

    mc "Chúng ta mau...vào trong đi."

    mc "Cậu mang nhiều đồ thế?"

    y 1ba "Ừm, cần nhiều mà."

    y "Cậu có tìm mua đủ những thứ những mình bảo không?"

    mc "Hy vọng là đủ rồi."

    mc "Có nhiều đồ cần mua quá nên tớ cũng không chắc lắm."

    y "Mình nghĩ là sẽ ổn thôi, nếu thiếu thì chúng ta tìm cách xoay sở."
    scene bg bedroom with wipeleft

    "Tôi dẫn Yuri lên phòng mình."

    "Ánh mắt tò mò của cậu ấy nhìn ngắm khắp căn phòng khiến tôi thấy hơi căng thẳng."
    show yuri 2bm zorder 2 at t11

    y "Phòng cậu sạch sẽ quá..."
    mc "Ahaha..."

    mc "Tớ đã dọn dẹp trước khi cậu đến đây mà..."

    y 2ba "Cậu chu đáo thật đấy."

    mc "Ah, không có gì..."

    mc "Sẽ rất là đáng xấu hổ nếu cậu đến đây mà thấy phòng của tớ như bãi chiến trường."
    y 1ba "Hmm..."

    y "Ừm, mình rất thích dọn dẹp mà..."

    y "Mình sẽ sẵn lòng giúp cậu dọn nếu trường hợp kia xảy ra."
    mc "Ah--"

    mc "Như vậy tớ còn thấy xấu hổ hơn!"
    show yuri 1be

    mc "Khoan đã, đừng mở nó--!"

    "Tôi nhanh chóng giữ được cổ tay của Yuri trước khi cậu ấy kịp mở ngăn kéo bàn học của tôi."


    y "Mình xin lỗi...!"

    y 4bb "Mình không nghĩ trước khi làm..."

    y "Mình hay lơ đãng như vậy!"

    mc "Không, không sao đâu..."

    "Tôi buông tay Yuri ra."
    show yuri 1bl

    "Cậu ấy đặt hai tay lên đùi, như thể đang cố kiềm chế bản thân để tránh làm tôi phật lòng."

    mc "Vậy, ừm..."

    mc "Chúng ta...vào việc thôi nhỉ?"
    y 2bu "Ah..."

    y "Phải rồi..."

    y 2bf "Um, mình đã chuẩn bị vài thứ để cậu có thể làm..."

    y "Đồ trang trí và mấy thứ khác để tạo không khí."

    mc "Tạo không khí...?"

    y 1ba "Cậu biết đấy..."

    y "Đèn mờ, nến thơm..."

    mc "À, là mấy cái đó."

    mc "Tớ không ngờ cậu chuẩn bị kĩ càng đến vậy."

    y 1bc "Tất nhiên rồi."

    y "Mình muốn những vị khách đặt chân vào cậu lạc bộ chúng ta sẽ có cảm giác như sang thế giới khác luôn."

    y 1ba "Chắc là nhiều người sẽ vào chỉ vì tò mò..."

    y 1bj "Và vì cả...bánh nướng nữa, mình nghĩ vậy..."

    y 1ba "Nhưng mình vẫn muốn cho họ những trải nghiệm tuyệt vời khiến họ muốn ở lại lâu hơn."

    mc "Nghe thật tuyệt vời."

    mc "Thi thoảng tớ quên mất rằng cậu là người rất mãnh liệt."
    y 1bt "Ah--"

    y 2bt "Mãnh liệt...?"

    mc "Tớ nghĩ rằng từ đấy rất hợp miêu tả cậu."

    y "Nghe có vẻ...xấu?"

    mc "Không, không phải thế."

    mc "Đó thực sự là điều mà tớ thích ở cậu."

    y 3bu "C-Có thật thế không..."

    y "Nghe cậu nói vậy làm mình thấy nhẹ nhõm lắm..."

    y "Và có chút hạnh phúc nữa..."

    mc "Ừm, cậu không cần phải quá lo lắng đâu."

    mc "Cứ thư giãn như đang ở chính nhà mình thôi."

    y 3bl "Thư giãn..."

    y 1bf "Mình có mua một vài thứ để giúp mọi người thư giãn đấy."

    y "Mình định dùng chúng để hỗ trợ giúp cho việc ngâm thơ đỡ căng thẳng..."

    mc "Vậy sao? Nó là gì vậy?"

    y "Để mình xem nào..."

    "Yuri lục trong túi của cậu ấy."

    "Cậu ấy lấy ra một vài cây nến và một vật gì đó hình trụ được làm bằng gỗ."

    y "Tiện đường mình đến đây mình có ghé qua cửa hàng để mua mấy thứ này."

    y "Mình dự định bọc cửa sổ lại bằng giấy đen để chỉ có ánh sáng của nến có thể thắp sáng căn phòng."

    y 1ba "Cậu thấy thế có hay không?"

    mc "Ừm, tớ cũng nghĩ nó khá tuyệt đó."

    mc "Vậy còn vật làm bằng gỗ kia để làm gì?"

    y 1bf "Ồ, cái này hả?"

    y "Nó là máy dùng để khuếch tán mùi hương của tinh dầu."

    y "Cậu có biết nhiều về xông hương liệu không?"

    mc "Tớ không rõ lắm..."

    y 1ba "À, vậy sao?"

    y "Đó là một trong những sở thích của mình để góp phần tạo nên bầu không khí."

    y "Tùy theo loại dầu hoặc thảo dược mà cậu chọn, cậu có thể thay đổi không khí căn phòng."

    y "Cậu còn có thể cảm thấy như nó thấm qua cơ thể của mình vậy."

    y 3bm "Thư giãn, năng lượng tích cực, lãng mạn, sự phản chiếu..."

    y "Tất cả cứ như ma thuật vậy."
    show yuri 3ba

    "Yuri bấm nút phía bên dưới cái máy hình trụ kia."

    "Trong chớp mắt, một luồng hơi phun qua cái lỗ nhỏ ở phía trên."

    mc "Wow, mùi thơm quá."

    mc "Loại này dùng để tạo không khí gì vậy?"

    y 1ba "Đây là tinh dầu hoa nhài."

    y "Hương thơm thật ngọt ngào và tự nhiên phải không?"

    mc "Ừm, cậu miêu tả mùi hương của nó rất đúng."

    y 1bb "Mình chọn hoa nhài cho sự kiện lần này bởi nó có thể khiến cho ta có cảm giác thật dễ chịu."

    y "Hương hoa nhài sẽ giúp cậu thăng hoa cảm xúc."

    y 1bu "Cơ thể ta sẽ thấy ấm áp hơn, tim đập nhanh hơn."

    y 1ba "Thật là phù hợp cho việc ngâm thơ."

    mc "Nghe cũng có vẻ hợp lý..."

    mc "Có vẻ cậu là chuyên gia trong vụ này rồi vì vậy tớ sẽ tin tưởng giao toàn bộ cho cậu quyết định."
    show yuri 1bc

    "Yuri mỉm cười dịu dàng, trông như đang hoàn toàn tận hưởng mùi hương."

    "Cậu ấy lại tiếp tục lấy ra trong cặp một vài tập giấy mỏng."
    show yuri 1ba

    mc "Chúng để làm gì vậy?"

    y 1bf "À ừm..."

    y "Cậu đã mua loại giấy gấp origami mà mình bảo chưa?"

    mc "Ừ, tớ đã mua nó rồi đây..."

    y "Chúng ta sẽ không dùng chúng để gấp origami."

    y "Mình muốn viết những từ ngữ khác nhau lên trên những mẩu giấy đó."

    y "Chúng ta sẽ cần đến khoảng một trăm mẩu giấy."

    mc "Vậy sao?"

    mc "Thế chúng dùng để làm gì?"

    y 2bf "Mình sẽ cắt và nối chúng thành một dải ruy băng và sau đó treo trên cửa lớp."

    y "Sau đó chúng ta có thể dùng giấy buộc vào dải ruy băng để tạo thành một cái rèm cửa."

    y 2bm "Vậy chẳng phải thật đẹp sao?"

    y "Nó sẽ thu hút được những ánh mắt của những người đi ngang qua..."

    y 2ba "Để họ có hứng thú ghé vào một chút."

    mc "Ý tưởng đó thực sự rất sáng tạo!"

    mc "Cậu thật là tuyệt vời đó Yuri."

    y 4ba "Thật...vậy sao?"

    y "Ừm, mình cứ lo là...mình lại làm mọi thứ hơi bị quá đáng."
    y 3bu "Fufufu."

    "Yuri cười khúc khích với gò má đỏ ửng."

    "Trông có vẻ cậu ấy thoải mái hơn khi chỉ có hai đứa bọn tôi?"

    "Hay cũng có thể do sự phấn khích khi làm việc mà cậu ấy thích."

    y 1ba "Cậu cầm lấy bút dạ này, [player]."

    y "Hãy cứ viết những gì mà cậu thích."

    y "Mình sẽ giúp cậu ngay sau khi mình cắt xong chỗ ruy băng này."

    mc "Ah, được thôi."

    "Ngồi trên sàn cùng nhau, cả hai đều cố gắng làm việc chăm chỉ."

    "Tôi cẩn thận viết các kí tự lên giấy, tôi phải tỉ mỉ hết sức vì chữ viết của tôi không đẹp cho lắm."

    "Yuri thì đang chia cuộn ruy băng ra từng đoạn nhỏ hơn."

    "Sau đó, cậu ấy lấy từ trong cặp ra một con dao bỏ túi."

    mc "Ồ...?"

    "Con dao đó có một vẻ đẹp thật lạ."

    "Tay cầm bằng bạc với họa tiết lượn sóng được khắc trên đó."

    "Lưỡi dao có màu xanh nhạt."

    mc "Chắc hẳn đó không phải con dao bình thường..."

    mc "Nó trông thật đặc biệt."
    y 4bb "A-Ah..."

    y "Ừm..."

    "Cảm thấy xấu hổ, Yuri liền nhìn đi chỗ khác."

    mc "Sao vậy?"

    y "Cậu nghĩ nó kì dị à..."

    mc "Yuri, mình đâu có đánh giá gì."

    mc "Mỗi người có một suy nghĩ khác nhau cơ mà?"

    y "Vậy hãy hứa với mình rằng cậu vẫn đối xử với mình như bình thường..."

    mc "Ừm, tớ hứa."

    y 2bi "Vậy thì..."

    y "Chả là, mình khá thích dao..."

    y "Mình bị...thu hút bởi vẻ đẹp của chúng..."

    y 2bv "M-Mình không thể kiềm chế được!"

    y "Mình cũng không rõ nó là tại sao nữa..."

    y "Kết hợp giữa sự nguy hiểm và khéo léo, như vậy đấy..."

    y 4bb "Uu, mình đang nói cái gì thế này...?"

    y "Đừng nghĩ mình là đứa lập dị nhé..."
    mc "Ahaha."

    y "Cậu đang cười mình đấy kìa..."

    mc "Không, tớ đâu có cười cậu."

    mc "Chỉ là trông cậu khá ngộ khi vừa nói vừa lo lắng như vậy."

    mc "Tớ nghĩ, ừ thì...đó cũng là một sở thích thú vị đấy."

    mc "Và có vẻ nó phù hợp với cậu."

    y 2bt "Phù hợp với mình...?"

    mc "Ừm...trông rất mạnh mẽ đấy. Ahaha."

    mc "Không thể phủ nhận rằng hình dáng con dao này rất là ngầu."

    y 2bu "Thật không...?"

    "Yuri cuối cùng cũng bớt căng thẳng hơn."

    y 1ba "Cậu có muốn cầm thử không?"

    mc "Tất nhiên rồi, đưa tớ xem thử."

    "Yuri cẩn thận đưa cho tôi con dao, chuôi cầm chĩa về hướng tôi."

    "Tôi cầm lấy và ngắm nhìn con dao trên tay mình."

    "Con dao có vẻ nặng và cực kỳ chắc chắn."

    "Cậu mua ở đâu được con dao như này vậy...?"

    "Tò mò muốn biết độ sắc của nó như nào, tôi đã thử đưa ngón tay lên mũi dao."
    mc "Ow--!"
    y 3bn "[player]--!!"

    y "Sao cậu lại làm thế?!"

    mc "Tớ không ngờ nó lại sắc như vậy...!"

    mc "Tớ còn gần như là chưa chạm tới nó."

    y "L-Là lỗi của mình!"

    y 3bo "Mình nên cảnh báo với cậu trước..."

    y "Rằng con dao này cực kỳ sắc..."

    y "Nó có thể cắt da thịt như cắt giấy vậy."

    y 2bv "Ôi trời ạ..."

    "Một giọt máu chảy ra từ đầu ngón tay tôi."

    "Yuri cầm lấy tay tôi và nhìn kĩ vết thương."
    y 2bt "Ah..."

    "Cậu ấy nhìn nó chằm chằm, vẻ mặt hơi khó chịu."

    mc "Không có gì nghiêm trọng đâu mà, tớ sẽ đi rửa ngay bây giờ--"
    mc "A-Ah!"

    "Yuri bất ngờ đưa ngon tay tôi vào miệng cậu ấy và liếm vết thương."

    "Tôi có thể cảm thấy lưỡi của cậu ấy cuộn quanh ngón tay tôi."

    "Giật mình, tôi rút lại ngón tay của mình."
    y "O-Oh..."

    y 3bo "X-Xin lỗi!"

    y "Mình lại làm mà không suy nghĩ!"

    y 4bc "Mình..."

    "Yuri cúi mặt xuống, mặt cậu ấy đỏ bừng lên."
    mc "Yuri..."

    y "Đó là việc đáng xấu hổ nhất mà mình từng làm..."

    y "Sao mình có thể làm việc như vậy chứ??"

    y "Mình xin lỗi, mình xin lỗi..."
    mc "Ah..."

    "Hành động đó có chút kì lạ và làm tôi khá bất ngờ..."

    "Nhưng chắc rằng cậu ấy chỉ đang muốn cố gắng giúp đỡ tôi thôi nhỉ...?"

    mc "Yuri, tớ nghĩ cậu không cần phản ứng thái quá thế đâu..."
    y "Uuuh..."

    "Cậu ấy vẫn không chịu ngẩng đầu lên."

    "Nếu cậu ấy mà cứ thế này mãi thì sao xong việc trong chiều nay được?"

    mc "Thôi nào ổn rồi mà..."

    "Chắc đây là việc cực kì ngu ngốc nhưng dù sao tôi cũng phải làm thôi."

    "Tôi cầm tay Yuri lên và liếm ngón trỏ của cậu ấy."
    show yuri 3bn at h11
    y "[player]--!!"

    y "C-Cậu vừa....?"

    mc "G-Giờ thì hòa rồi nhé..."
    y 3bv "..."

    "Yuri nhìn tôi với vẻ mặt hơi nghiêm trọng."
    mc "Ahaha..."

    mc "Đó đúng là ý tưởng tồi tệ mà..."

    "Nếu không có hương thơm ngọt ngào từ tinh dầu hoa nhài thì chắc hẳn bầu không khí hiện giờ sẽ căng lắm."

    y 1bu "Cậu kì quặc thật đấy, [player]."

    "Yuri cười tủm tỉm."

    mc "Hử...?"

    "Yuri bảo {i}mình{/i} kì lạ sao?"

    "Tôi không thể đưa ra lời biện hộ nào cho bản thân sau hành động vừa rồi..."

    y 1bf "Cậu để băng gạc ở đâu nhỉ?"

    mc "À..."

    mc "Tớ nghĩ là không cần dùng tới nó đâu."

    mc "Chỉ là một vết cắt nhỏ thôi mà."

    mc "Nhìn này, máu cũng đông lại rồi mà."

    y 1ba "Ừm..."

    y "Thật là nhẹ nhõm."

    "Có vẻ sự căng thẳng đang dần tan biến."

    "Chúng tôi lại tiếp tục quay trở lại công việc."

    "Tôi xem Yuri dùng con dao cắt những dải ruy băng như cắt không khí vậy."

    "Tôi lại tiếp tục loay hoay với đống giấy."

    scene bg bedroom with wipeleft_scene

    "Sau khi gắn giấy với ruy băng xong xuôi, hai đứa đặt tất cả ở cạnh nhau."

    "Nó đẹp hơn cả tôi mong đợi, dùng làm rèm cửa đúng là rất được."

    mc "Trông thật tuyệt."

    mc "Cậu quả là sáng suốt khi nghĩ ra ý tưởng tuyệt vời này, Yuri."
    show yuri 1bq zorder 2 at t11

    y "Ah, cảm ơn cậu..."

    y "Chỉ là mấy thứ mình học trên mạng thôi, không phải gì to tát đâu mà."

    y 1ba "Chúng ta bắt tay vào việc tiếp nhé?"

    mc "Ừm, cùng làm thôi nào."

    mc "Cậu đã nghĩ được gì chưa?"

    y "Mình định sẽ làm một biểu ngữ."

    y "Vì thế nên mình mới bảo cậu mua bảng màu vẽ."

    mc "À, đúng rồi."

    "Một trong những món đồ mà Yuri đã yêu cầu tôi mua đó là bộ vẽ màu nước."

    y 1bf "Chúng ta sẽ cần sáu ly nước để chuẩn bị màu vẽ."

    y "Cậu chuẩn bị giúp mình nhé?"

    mc "Có ngay đây."

    mc "Sáu ly nước..."

    mc "Tớ sẽ quay lại ngay, chỉ mất 1 phút thôi."

    y 1ba "Cảm ơn cậu."

    y 2bf "À mà chỉ cần một chút nước là được rồi nhé."

    y "Nếu cậu đổ nhiều quá, màu sẽ bị loãng đấy."

    scene bg bedroom with wipeleft_scene

    "Nghe lời Yuri, tôi sử dụng loại cốc nhỏ bằng nhựa thay vì dùng hẳn cốc to."

    "Tôi để chúng lên đĩa để tránh làm rớt màu ra ngoài, rồi mang chúng quay trở lại phòng."
    mc "Yuri?"
    show yuri 1bd zorder 2 at t11

    y "Ơi?"

    "Tôi vào trong phòng đúng lúc nhìn thấy Yuri đang sắn tay áo lên."

    mc "À, không có gì đâu..."

    mc "Mặt cậu có vẻ hơi đỏ nhỉ?"

    mc "Chắc tại trong phòng nóng quá hả?"
    y 3bq "Ah--"

    y "Không, không phải thế!"

    y "Không sao cả đâu, nên..."

    y "Chúng ta cùng trộn màu đi."

    "Yuri cắt đứt cuộc hội thoại để đi bóc vỏ những viên màu, rồi thả chúng vào trong mấy cái ly."

    y 1ba "Vậy..."

    y "Mình nghĩ chúng ta lên làm gì đó trông đơn giản nhưng đẹp."

    y "Mình muốn tô nền cả tấm biểu ngữ này..."

    y "Đoạn đầu sẽ dùng màu bình minh, kế đó là ban ngày, tiếp đến là hoàng hôn và cuối cùng là đêm."

    y "Sau khi màu khô, mình sẽ viết một vài lời trích dẫn giúp tạo cảm hứng lên biểu ngữ."

    y "Chúng ta có thể treo nó trên bức tường phía sau bục giảng của phòng học."

    mc "Ah, nghe ổn đấy."

    mc "Cậu định sẽ viết gì?"

    y 2bm "Ừm..."

    y "...Mình sẽ không nói trước để giữ sự bất ngờ."

    "Yuri mỉm cười với tôi."

    mc "Nếu cậu đã nói vậy..."
    show yuri zorder 1 at thide
    hide yuri

    "Sau khi trải tấm biểu ngữ ra, Yuri và tôi quỳ xuống ở hướng đối diện nhau để không làm cản trở công việc của người kia."

    "Yuri sử dụng một cây cọ và chấm một vài chấm màu khác nhau trên tấm biểu ngữ để đánh dấu chỗ cần tô màu trước khi bắt đầu tô."

    mc "Làm tớ nhớ lại hồi tiểu học quá đi..."

    "Vẽ biểu ngữ với màu nước làm tôi cảm thấy rất giống mấy bài tập mĩ thuật hồi xưa."

    "Quả thật là thoải mái."
    show yuri 2bt zorder 2 at t11
    y "A..."

    y "Mình xin lỗi nếu cậu cảm thấy việc này quá trẻ con nhé...!"

    mc "Không, ý tớ không phải vậy."

    mc "Tớ thấy nó vui mà, kiểu vậy."

    y 1bs "...Ừm."

    y "Đúng là vui thật."

    y "Mình rất vui khi cậu cũng cảm thấy thế."

    "Yuri dừng vẽ lại một lúc, như đang suy ngẫm về chuyện nào đó."

    y 2bl "Đối với mình..."

    y "Mình không thích ra ngoài và làm những điều điên khùng để có thể vui vẻ."

    y "Không thích một tí nào cả."

    y 2bf "Mình chỉ thích những lúc mà mình có thể dành thời gian bên ai đó..."

    y "Mặc dù chúng chỉ là việc gì đó nhỏ nhặt, như đọc sách vậy - không cần phải nói chuyện nhiều."

    y 2ba "Chỉ cần có một người bạn luôn bên mình là đủ khiến cho mọi thứ trở nên tốt đẹp hơn."

    y "Mình nghĩ chỉ cần thế là đủ để mình hạnh phúc rồi."

    mc "Thật vậy sao...?"

    "Mặc dù Yuri và tôi khá là khác nhau, nhưng tôi có thể hiểu được cậu ấy đang nghĩ những gì."

    "Tôi cũng chung suy nghĩ như vậy khi nói về anime và game, đơn giản là có người để xem hay chơi cùng là hạnh phúc rồi."

    mc "Cậu giống tớ thật đấy."

    "Yuri cười nhẹ nhàng."

    y 1bm "Mình biết là cậu sẽ hiểu mà..."

    "Yuri nghiêng mình qua tấm biểu ngữ để lấy một cây cọ chưa được sử dụng."

    "Nhưng đúng lúc tôi cũng định làm thế, vậy là đầu chúng tôi vô tình va vào nhau."
    y 3bn "Kya--!"

    mc "T-Tớ xin lỗi!"

    "Yuri co người lại, tôi thì nhanh chóng đưa tay lên."

    mc "Cậu có đau không?"

    y 2bv "K-Không, mình không sao."

    y "Chỉ hơi giật mình một chút thôi... Không có gì đâu."

    y "Xin lỗi, đáng lẽ ra mình nên nhờ cậu lấy nó hộ mình..."

    mc "Không phải lỗi của cậu mà."

    mc "A... Mặt cậu..."

    "Có vài giọt màu trên mặt và cổ của Yuri."

    y 2bt "Có gì đó trên mặt mình sao?"

    mc "Ừm, lỡ để màu bắn lên cậu rồi..."

    mc "Xin lỗi, là tại của tớ!"

    mc "Mình sẽ đi lấy khăn ngay."
    show yuri zorder 1 at thide
    hide yuri

    "Tôi vội vã lấy ra một chiếc khăn nhỏ, sau đó làm ẩm nó với nước nóng."

    "Tôi trở lại phòng và quỳ xuống trước mặt cậu ấy."
    $ persistent.clear[5] = True
    scene y_cg3_base with dissolve_cg

    mc "Đây..."

    "Tôi dùng khăn lau nhẹ mặt và cổ của Yuri."
    show y_cg3_exp1 at cgfade
    y "Ah--"

    mc "Có chuyện gì vậy?"

    y "Hơi nóng quá ấy mà."

    mc "Xin lỗi..."

    mc "Tớ không muốn dùng nước lạnh."

    "Sau khi lau xong, tôi rút tay mình lại."

    "Nhưng Yuri đột nhiên giữ cỗ tay tôi lại."
    hide y_cg3_exp1

    y "Chờ đã--"

    mc "Ế?"
    show y_cg3_exp1 at cgfade

    y "Chỉ...một chút nữa được không."

    y "Cảm giác đó thật tuyệt..."
    mc "A..."

    "Tay tôi vẫn đang ở cạnh cổ Yuri."
    hide y_cg3_exp1

    "Cậu ấy nhìn thẳng vào mắt tôi."

    "Biểu cảm mạnh mẽ giống y như lúc tôi chứng kiến Yuri đọc sách."

    "Gần như thể cậu ấy thoát ly khỏi thực tại, đắm chìm trong cảm xúc."

    "Đôi môi kia hơi khẽ mở, tôi cảm nhận được hơi thở nhẹ nhàng."

    "Chuyện gì đang diễn ra vậy...?"

    "Có phải cảm giác chóng mặt này là tại hương thơm của dầu hoa Nhài không nhỉ?"

    "Những ngón tay của Yuri nhẹ nhàng cuộn quanh cổ tay tôi, cảm giác rạo rực truyền thẳng lên cả cánh tay."

    "Và đột ngột, mặt của cả hai hình như đang tiến sát lại gần nhau..."
    y "Ah..."

    "Yuri từ từ lùi xa dần ra."

    y "Xin lỗi..."

    y "Chắc là hôm nay mình hơi mệt."

    y "Mình không cố ý tỏ ra lơ đễnh đâu..."

    mc "K-Không sao đâu mà..."
    scene bedroom with dissolve_cg

    "Khoảnh khắc đó kết thúc nhanh như khi nó bắt đầu vậy."

    "Yuri lại nhặt chiếc cọ vẽ lên."

    "Nhưng cử động của cậu ấy có phần hơi vụng về, như thể đang không tập trung vậy."

    "Tôi vẫn im lặng, buộc phải hành xử như chưa có chuyện gì xảy ra."

    "Tôi nhặt lấy cây cọ của mình và tiếp tục làm theo Yuri."

    scene bedroom with wipeleft_scene

    mc "Vậy là xong rồi..."

    "Tôi đã hoàn thành bầu trời đêm với những đốm trắng là những ngôi sao sáng."

    "Nhìn tổng thể tấm biểu ngữ, trông nó thật đẹp và toát lên vẻ tự nhiên."
    show yuri 1ba zorder 2 at t11

    y "Mình nghĩ là tốt hơn những gì mình mong đợi đấy."

    y "Mình thực sự rất hài lòng với kết quả này."

    mc "Ừm, tớ cũng vậy."

    mc "Bây giờ cậu sẽ viết chữ lên đó à?"

    y 1bf "Ah, chưa đâu..."

    y "Phải đợi màu khô trước đã chứ."

    mc "Ừ nhỉ, có lẽ phải mất một lúc đấy nhỉ."

    y 2bh "Ừm..."

    y "Có lẽ tốt hơn hết là để nó ở đây, sáng mai cậu sẽ đem nó theo."

    y 2bf "Mình có thể hoàn thành việc viết chữ trước khi sự kiện bắt đầu."

    y "Thế có được không?"

    mc "Ổn mà."

    y 1ba "Vậy thì tuyệt vời."

    y "Còn bây giờ thì..."

    y "Mình nghĩ chắc là không còn gì để chúng ta làm nữa rồi."

    mc "Phù."
    y 1bc "Ahaha."

    y "Nghe như thể cậu mong nó kết thúc ấy."

    y 1ba "Không biết là cậu có thấy thoải mái khi làm việc không?"

    mc "À, không, không phải vậy."

    mc "Tớ vui vì công việc hoàn thành ổn thoả mà."

    y 2ba "À ra vậy."

    y "Mình cũng thế."

    y "Tại mình có hơi lo lắng về thời gian..."

    y "Mình cần về sớm để chuẩn bị cho bữa tối."
    mc "À..."

    mc "Vậy cậu phải về bây giờ à?"

    "Tôi đã hy vọng rằng hai đứa có chút thời gian rảnh sau khi xong việc..."

    y 2bl "Ừm..."
    y "..."

    "Yuri lại ngẫm nghĩ một lúc."

    y 3bv "M-Mình không thể để mặc công việc ở nhà được..."

    y "Mình xin lỗi!"

    y "Mình ước gì chúng ta có thêm chút thời gian..."

    mc "Đó không phải lỗi của cậu."

    mc "Là do tớ làm chậm quá."

    y 1bt "Không, cậu không phải nhận lỗi đâu."

    y "Quan trọng nhất là...mọi việc đã hoàn thành, phải vậy không?"

    mc "Ừm..."

    y 1bu "Vậy nên..."

    y "Mình không cảm thấy thất vọng...hay gì đâu nhé."

    "Trong khi gói ghém đồ đạc của mình, trông Yuri có vẻ hơi chán nản."

    "Tôi hiểu lí do vì sao."

    "Có vẻ như rất hiếm khi cậu ấy có thời gian thoải mái bên bạn bè."

    "Nhưng đây có phải là lần cuối đâu nào..."

    scene bg house with wipeleft_scene

    "Thu dọn đồ đạc xong, tôi tiễn cậu ấy ra cửa trước."
    show yuri 1ba zorder 2 at t11

    y "Cảm ơn cậu vì đã chấp nhận giúp mình."

    mc "Không có gì, giúp được cậu mình cũng thấy rất vui mà."

    mc "Nếu ngày mai cậu cần tớ mang đến trường cái gì nữa thì cứ bảo nhé."

    y "Mình sẽ nhớ bảo cậu."

    y 1bu "Ừm, vậy..."

    "Yuri trông có vẻ bồn chồn."

    y 2bu "Mình nghĩ là...mình sẽ gặp lại cậu vào ngày mai."

    mc "Khoan đã--"
    show yuri 2bt

    "Tôi nói mà không suy nghĩ."

    mc "Về chuyện ngày hôm nay..."

    mc "Cậu đừng bận tâm về chuyện chúng ta không có nhiều thời gian."

    mc "Sẽ còn những dịp khác nữa cơ mà."

    mc "Cậu có thể đến đây bất cứ khi nào cậu muốn, thậm chí chúng ta có thể đi đâu đó--"

    mc "À, mình quên mất là cậu không thích ra ngoài cho lắm--"
    show yuri 2bs

    "Khi tôi vẫn còn đang ấp úng, Yuri chỉ mỉm cười bẽn lẽn."

    mc "Cơ mà..."

    mc "Chắc cậu hiểu ý tớ mà, cho nên..."

    y 1bs "Cậu chu đáo thật đấy, [player]."

    "Yuri tiến lại gần và nắm chặt lấy tay tôi."
    show yuri 2bs at face(y=600) with dissolve
    stop music fadeout 2.0

    y "Mình rất thích điều đó ở cậu..."

    mc "Ừm..."

    "Tôi phải trả lời thế nào đây?"

    "Khi tôi còn đang bận suy nghĩ thì Yuri đột ngột lùi lại."
    show yuri 3bn zorder 2 at t11
    y "S-Sayori--?"
    mc "Ế?!"
    show sayori 1bl zorder 3 at f21
    show yuri zorder 2 at t22
    s "Ah..."

    s "C-Chào cậu, [player]..."
    mc "Sayori--!"

    mc "Vừa nãy, chúng tớ chỉ--"
    s 1bq "Ehehe~"

    s "Không sao đâu, [player]."

    s 1ba "Tớ chỉ định ghé qua chào cậu thôi~"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y 3bq "U-Um..."

    y "Ừm, rất vui được gặp cậu..."

    y 3bv "Nhưng tớ xin lỗi, tới lúc tớ phải về mất rồi!"
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21

    s 1bh "Aw, thật vậy sao?"

    s "Thế thì buồn nhỉ..."
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22

    y 2bt "Tớ xin lỗi..."

    y "Nhưng chúng ta sẽ gặp nhau tại lễ hội ngày mai, vậy nên..."

    y "Mọi chuyện vẫn ổn thôi, phải không?"
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21

    s 4bq "Tất nhiên rồi!"

    "Sayori tươi cười."
    show sayori 4ba
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22

    y 4bc "Ư-Ừm, vậy..."

    y "Hẹn gặp lại cậu vào ngày mai!"
    show yuri at lhide
    hide yuri

    "Yuri vội vàng rời đi với vẻ mặt xấu hổ."

    "Sayori vẫy tay chào tạm biệt cậu ấy."
    return



label ch4_end:
    play music t10 fadeout 2.0
    show sayori 1ba zorder 2 at t11


    mc "Tớ tưởng cậu bảo là không muốn sang nhà tớ!"

    s 2bl "Ahaha, ừm..."

    s "Tớ đã cố ngồi yên trong phòng mình..."

    s "Nhưng trí tưởng tượng bắt đầu hành hạ tớ..."

    s 1by "Vì vậy nên tớ đã đến đây để tự mình chứng kiến nó."

    mc "Chứng kiến cái gì cơ?"

    mc "Cậu đang nói về cái gì vậy?"

    s "Cậu biết mà..."

    s "Việc cậu đã vui vẻ như nào ở bên cạnh [ch4_name]."

    s "Và ngày càng thân thiết với cậu ta."

    s 1bt "Nó thực sự làm tớ...rất hạnh phúc..."

    s "Cậu đã có được những người bạn tốt."

    s "Đó là tất cả những gì tớ muốn."

    "Những giọt nước mắt bắt đầu lăn trên má Sayori."

    s 4bv "Đó là tất cả những gì tớ muốn--!"

    s "Tại sao tớ lại có cảm giác này chứ, [player]?"

    s "Lẽ ra tớ nên cảm thấy vui cho cậu."

    s 4bw "Tại sao tớ lại cảm thấy như con tim mình bị xé làm đôi vậy?"

    s "Nó đau lắm..."

    s "Đau lắm..."

    s "Tớ biến mất thì có phải hay hơn không!"

    mc "Sayori, đừng nói vậy!"

    s 1bw "Đó là sự thật, [player] à!"

    s "Nếu tớ không ở đây, cậu đã không phải phung phí lòng thương hại của mình với tớ!"

    s "Cậu sẽ không phải chịu đựng với sự ích kỷ của tớ!"

    s 1bv "Monika nói đúng..."

    s "Tớ chỉ nên..."
    mc "Monika...?"

    mc "Monika đã nói đúng về cái gì cơ?"
    s "..."
    mc "Sayori..."

    mc "Những gì tớ nói lúc trước đều là thật lòng."

    mc "Tớ sẽ không để chuyện này tiếp diễn."

    mc "Quan tâm tới cậu không phải là gánh nặng."

    mc "Ngược lại, tớ còn thấy rất vui vì được làm điều đó."

    mc "Tớ sẽ không bao giờ đánh đổi nó với bất kì thứ gì khác."

    mc "Kể cả có phải dành trọn cuộc đời mình..."

    mc "Tớ cũng sẽ ở bên cậu cho đến khi cậu không còn cảm thấy đau đớn nữa."

    s 1bk "N-Nhưng..."

    "Sayori nhìn đi chỗ khác."

    "Tôi đặt tay lên vai của Sayori để trấn an cậu ấy."

    s "Tớ sợ lắm, [player]..."

    s "Tớ thực sự đã rất sợ..."

    mc "Cậu sợ vì chuyện gì, Sayori?"

    s "Tớ sợ rằng..."

    s "Rằng tớ thích cậu nhiều hơn cả cậu thích tớ..."
    mc "Sayori...?"

    s 1bu "Điều đó đúng mà, phải vậy không?"

    s "Tớ đã quá yếu đuối và bắt đầu thích cậu quá nhiều..."

    s "Tớ đã tự ép mình làm vậy."
    s "[player]..."

    s 4bw "Tớ thích cậu nhiều đến nỗi như muốn chết đi!"

    s "Đó là những gì tớ cảm thấy!"

    s 2bv "Và...và..."

    mc "Vậy là đủ rồi, Sayori..."

    mc "Tớ không muốn cậu phải đau khổ thêm một chút nào nữa."

    "Tôi nắm lấy tay Sayori."

    mc "Cậu có nhớ tớ đã từng bảo rằng tớ sẽ luôn dành những điều tốt nhất cho cậu không?"

    mc "Cậu vẫn sẽ tin tớ chứ?"

    "Sayori không nói gì, chỉ khẽ gật đầu."

    mc "Cho dù tớ không hiểu hết mọi cảm xúc của cậu..."

    mc "Nhưng tớ biết thứ mà cậu đang cần nhất."

    mc "Và tớ sẽ dành nó cho cậu ngay bây giờ."
    show black zorder 4 with dissolve_cg

    menu:
        mc "Sayori..."
        "Tớ yêu cậu.":


            $ sayori_confess = True
            hide black with dissolve_cg
            call ch4_end_yes
        "Cậu sẽ luôn là người bạn thân nhất của tớ.":

            $ sayori_confess = False
            hide black with dissolve_cg
            call ch4_end_no

    return

label ch4_end_yes:

    mc "Tớ yêu cậu."

    s 1bv "Ế--?"

    mc "Vừa rồi là cảm xúc từ tận đáy lòng tớ."

    mc "Vì vậy...không có chuyện cậu thích tớ hơn tớ thích cậu được đâu."

    mc "Tớ nên nhận ra điều này sớm hơn."

    mc "Nhưng việc dành thời gian với mọi người trong câu lạc bộ..."

    mc "Có những người bạn mới..."

    mc "Và vui vẻ với cậu mọi ngày..."

    mc "Những điều đó càng giúp tớ nhận ra cậu quan trọng tới nhường nào."

    mc "Đó là lý do vì sao tớ sẵn sàng chấp nhận những gánh nặng của cậu."

    mc "Miễn là chúng ta cứ tiếp tục như thế này mỗi ngày..."

    mc "Cùng với cậu luôn bên cạnh tớ..."

    mc "Tớ tin rằng chúng ta sẽ hạnh phúc."
    s "[player]..."
    $ persistent.clear[8] = True
    scene s_cg3 with dissolve_cg

    "Đột nhiên Sayori ôm chặt lấy tôi."
    s "[player]..."

    s "Như vậy...có thực sự ổn không?"

    mc "Không sao đâu."

    "Tôi cũng ôm lại cậu ấy chặt hơn."

    mc "Cậu sẽ không bao giờ phải rời xa tớ nữa đâu."

    s "Tớ yêu cậu, [player]..."

    s "Tớ muốn ở bên cậu mãi mãi."

    mc "Tớ cũng vậy."
    s "..."

    "Tôi cảm thấy có vẻ như Sayori thả lỏng tay hơn một chút."

    s "Chuyện gì thế này...?"
    mc "Sayori...?"

    s "Lẽ ra tớ phải cảm thấy hạnh phúc chứ nhỉ..."

    s "Tớ luôn nghĩ đây sẽ là khoảnh khắc hạnh phúc nhất đời mình."

    s "Nhưng tại sao..."

    s "Kể cả bây giờ..."

    s "Tại sao những đám mây đen vẫn chưa tan biến?"

    s "Chúng vẫn còn hiện hữu trong tớ, [player]..."

    mc "Sẽ ổn thôi, Sayori..."

    mc "Có thể sẽ mất chút thời gian để mọi thứ tươi đẹp trở lại."

    mc "Nhưng cho dù có mất bao nhiêu thời gian đi chăng nữa, tớ vẫn sẽ ở đây."

    mc "Cậu chỉ cần quan tâm đến điều đó thôi."

    s "Ừ-Ừm..."

    s "Tớ...tin cậu..."
    scene bg house
    show sayori 1bv zorder 2 at i11
    with dissolve_cg

    "Sayori và tôi từ từ buông tay ra."

    mc "Vậy..."

    mc "Vậy lễ hội ngày mai...sẽ là buổi hẹn hò đầu tiên của chúng ta nhỉ?"
    s 1by "Ehehe..."

    s "Cậu đang nói gì vậy?"

    s "Tớ không muốn nghĩ về mấy chuyện đó đâu."

    s "Tớ muốn mọi thứ cứ như bình thường thế này là được rồi."

    s "Kể cả khi chúng ta...là một cặp."

    s 1bk "Tớ cũng chẳng biết phải cư xử làm sao cho đúng nữa..."

    s "Chuyện này thật mới mẻ và có phần hơi đáng sợ."

    mc "Tớ hiểu rồi."

    mc "Chúng ta sẽ tiến triển từ từ để cậu cảm thấy thoải mái nhất."

    s 1bd "Nè, [player]..."

    "Sayori ngước mắt lên nhìn tôi một lần nữa và nở một nụ cười đượm buồn."

    s 4bd "Kể cả nếu như tớ thực sự, thực sự buồn..."

    s "Thì đây là điều tốt nhất cho tớ...đúng không?"
    mc "Ế...?"

    "Tôi thực sự không hiểu được hết ý của Sayori trong câu nói đó."

    mc "Cậu đang nói điều đó làm cậu buồn sao, Sayori?"

    s 4bk "T-Tớ không biết nữa..."

    s "Tớ không thể hiểu nổi cảm xúc của mình nữa."

    s "Lời thổ lộ của cậu như chùm gai quấn quanh trái tim tớ vậy..."

    s 4bd "Nhưng đó cũng là lí do vì sao tớ muốn tin tưởng cậu..."

    s "Cậu biết điều gì tốt nhất cho tớ mà..."

    mc "...Ừm."

    mc "Đúng vậy."

    mc "Tớ hứa đấy."
    show sayori zorder 1 at thide
    hide sayori

    "Nói như vậy nhưng thật ra tôi chưa bao giờ cảm thấy chắc chắn khi nhắc đến Sayori cả."

    "Tôi biết tôi yêu cậu ấy, và cậu ấy cũng yêu tôi."

    "Nhưng đôi lúc tôi cũng không thể hiểu nổi cảm xúc của Sayori như chính cậu ấy vậy."

    "Mặc dù vậy tôi vẫn phải làm thế chỉ để có thể an ủi cậu ấy..."

    "Tôi vẫn luôn tự hỏi rằng liệu mình có nên làm gì đó nhiều hơn thế nữa không."

    "Tôi biết những ý nghĩ ấy sẽ tiếp tục đeo bám tôi cho đến khi mọi chuyện trở lại bình thường."

    "Liệu đó có phải ý Sayori muốn nói khi bảo rằng muốn mọi việc vẫn như cũ?"

    "Tôi cũng không biết nữa."

    "Nhưng tôi biết rằng tôi nhất định sẽ cố gắng hết sức mình."

    "Sayori rất quan trọng đối với tôi."

    "Và tôi sẽ trả bất cứ giá nào để có được một tương lai hạnh phúc bên cậu ấy."
    return


label ch4_end_no:

    mc "Cậu sẽ luôn là người bạn thân nhất của tớ."

    mc "Điều cậu cần là mọi thứ diễn ra bình thường như mọi khi."

    mc "Monika đã kể cho tớ rằng..."

    mc "Rằng cậu đã rất hạnh phúc khi tớ gia nhập câu lạc bộ."

    mc "Tớ biết hiện giờ cậu đang rất chật vật với mớ cảm xúc hỗn độn."

    mc "Nhưng..."

    mc "Hãy tin tớ rằng tớ biết điều gì là tốt nhất dành cho cậu...và tớ muốn cậu luôn vui vẻ."

    mc "Tớ hứa tớ sẽ đưa mọi thứ trở lại như bình thường."

    s 1bt "Tớ..."

    s "Tớ...hiểu rồi..."

    "Sayori cố gắng để gượng cười với những biểu cảm đau khổ trên khuôn mặt."
    s "Ahaha..."

    s "Cảm giác này có phải giống như...bị ai đó đâm vào ngực không nhỉ?"

    s "Tớ phải viết một bài thơ về nó mới được..."
    mc "Sayori--"

    s "Tớ ổn mà."

    s "Đây chỉ là hình phạt dành cho tớ...cậu nhớ chứ?"

    s "Vì tớ quá ích kỉ..."

    s "Vì vậy, hãy làm ơn..."

    s "Làm ơn đừng quan tâm đến mớ cảm xúc ngu ngốc này."

    s "Tớ biết là cậu đúng."

    s "Tớ đã biết từ lâu rằng con đường này chỉ dẫn đến đau khổ."

    s "Đó là lý do vì sao tớ lại đến đây..."

    s "Chỉ để nghe được câu trả lời mà tớ cần nghe."

    s "Và một điều nữa..."

    s "Cậu cũng đúng khi nói tớ chỉ muốn mọi thứ trở lại như nó đã từng."

    s "Giờ thì tớ hiểu rồi."

    s "Cậu thực sự hiểu tớ hơn ai hết, [player]..."

    s 4bv "Tớ sẽ luôn tin tưởng cậu vô điều kiện..."

    s "Tất cả mọi thứ..."

    s "Vậy nên..."
    show sayori zorder 1 at thide
    hide sayori

    "Nụ cười trên môi Sayori cuối cùng cũng đã tắt."

    "Đột nhiên cậu ấy quay lại rồi ngã khuỵu xuống."
    s "{i}AAAAAaaaaAAAAAAAAHH!!!!{/i}"

    "Hai tay ôm chặt lấy đầu, cậu ấy gào to hết mức có thể."

    "Tôi cảm thấy rất sốc, không biết phải phản ứng ra sao nữa."
    show sayori 4bt zorder 2 at t11

    show sayori at lhide
    hide sayori

    "Sayori quay đầu lại nhìn liếc qua tôi với nụ cười yếu ớt trước khi cậu ấy chạy biến đi mất."
    mc "Sayori!"
    "..."

    "Tôi đứng bất lực trước nhà của mình."

    "Tại sao điều đó làm tôi cảm thấy thật tồi tệ?"

    "Tôi không thể làm gì hơn được nữa."

    "Điều tốt nhất tôi có thể làm là giúp Sayori vượt qua những cảm xúc của mình và đưa cậu ấy trở lại con đường đúng đắn."

    "Nhưng đôi lúc tôi cũng không thể hiểu nổi cảm xúc của Sayori như chính cậu ấy vậy."

    "Mặc dù vậy tôi vẫn phải làm thế chỉ để có thể an ủi cậu ấy..."

    "Tôi vẫn luôn tự hỏi mình rằng có nên làm gì đó nhiều hơn thế nữa không."

    "Tôi biết ý nghĩ này sẽ tiếp tục đeo bám tôi cho đến khi mọi chuyện trở lại bình thường."

    "Tôi sẽ cố gắng hết sức mình."

    "Sayori sẽ luôn là người bạn thân nhất của tôi."

    "Và tôi sẽ trả bất cứ giá nào để có thể đem về nụ cười cho cậu ấy."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
