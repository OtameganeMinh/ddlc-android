init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
        
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natsuki_exclusive2_1:
    scene bg club_day
    with wipeleft_scene


    "Tôi nghe như có tiếng thở dài hậm hực của Natsuki ở phía tủ để đồ."

    "Không biết cậu ấy đang khó chịu vì chuyện gì nhỉ?"

    "Tôi lại đó để xem liệu Natsuki có cần giúp gì không."
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r zorder 2 at t11
    with wipeleft_scene
    $ style.say_dialogue = style.normal

    mc "Cậu đang tìm gì à?"
    $ style.say_dialogue = style.edited

    n 4x "con đĩ monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Monika khốn thật..."

    n "Suốt ngày lấy đồ của tôi ra xong không để lại được đúng vị trí ban đầu!"

    n "Sắp xếp ngăn nắp bộ sưu tập của mình còn có nghĩa lý gì nữa khi mà người khác cứ liên tục lục tung nó lên chứ?"

    "Natsuki lôi mấy cái hộp và vài chồng sách trên giá ra."
    mc "Sưu tập truyện tranh à..."

    n 2c "Cậu cũng đọc truyện tranh đúng không?"
    mc "Ah--"

    mc "...Thi thoảng thôi..."

    "Có những thứ mà ta không nên nhận là mình thích nếu như chưa biết ý kiến đối phương ra sao. Truyện tranh là ví dụ tiêu biểu."

    mc "...Làm sao mà cậu biết được?"

    n 2k "Tôi vô tình nghe thấy cậu nhắc đến vài lần."

    n "Với cả nhìn mặt cậu thôi cũng đủ đoán ra rồi."

    "Rốt cuộc thế là sao. Có gì trên mặt tôi ư...?"

    mc "R-Ra là vậy à..."

    "Có một cuốn truyện tranh nằm lẻ loi giữa những chồng sách đủ thể loại ở góc tủ."

    "Thấy tò mò nên tôi rút nó ra khỏi chồng sách."

    n 1b "A, ra là ở {i}đây{i}!"

    "Natsuki giật cuốn truyện khỏi tay tôi."

    "Rồi quay sang cất nó vào cái hộp chứa đầy truyện cạnh đó."

    n 4d "Aah, ngon rồi đấy!"

    n "Đúng là chả có gì ức chế bằng nhìn bộ sưu tập truyện của mình thiếu mất một quyển nhỉ?"

    mc "Chuẩn không cần chỉnh..."

    "Tôi lại gần để nhìn rõ hơn bộ sưu tập mà cậu ấy ngưỡng mộ."
    mc "Parfait Girls à...?"

    "Tôi chưa nghe tên bộ truyện này bao giờ."

    "Chắc hẳn là do nó không thuộc thể loại tôi thích đọc, hoặc đơn giản là do nó dở tệ."

    n 5g "Nếu định đánh giá gì tôi thì cậu đi ra ngoài kia mà phán."

    "Cậu ấy chỉ tay ra phía cửa phòng."

    mc "N-Này, mình đâu có ý phán xét gì cậu...!"

    mc "Tôi còn chưa hề hé răng cơ."

    n 5c "Vấn đề ở cái giọng điệu của cậu đấy."
    $ style.say_dialogue = style.normal

    n "Nghe đây này, [player]."

    n 4l "Coi như đây là bài học đầu tiên mà Câu lạc bộ dạy cho cậu:{nw}"
    $ _history_list[-1].what = "Coi như đây là bài học đầu tiên mà Câu lạc bộ dạy cho cậu: Đừng có đánh giá một cuốn sách qua bìa!"
    $ style.say_dialogue = style.edited

    n "Đừng có đánh giá một cuốn sáchsssssssssss sssss ss{space=20}h{space=40}h{space=120}h{space=160}h{space=200}h"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()

    n "À mà--"

    "Natsuki lấy ra từ trong hộp tập đầu tiên của bộ Parfait Girls."

    n "Cậu cứ xem thử nội dung của nó đi là hiểu điều tôi vừa nói ngay!"

    "Cậu ta dúi nó vào tay tôi."
    mc "Ah..."

    "Tôi nhìn chằm chằm vào bìa cuốn truyện."

    "Trên đó là hình bốn cô gái mặc đồ sặc sỡ và tạo dáng kiểu nữ tính quá trớn."

    "Nồng nặc mùi \"moe\"."

    n 4b "Còn đứng trơ ra đấy nữa à!"
    mc "Uwa--"
    show natsuki zorder 1 at thide
    hide natsuki

    "Tôi bị Natsuki chộp lấy tay và kéo ra khỏi tủ để đồ."

    "Rồi cậu ấy ngồi xuống và tựa lưng vào tường, chỗ ngay bên dưới cửa sổ."

    "Sau đó vỗ vỗ xuống khoảng trống bên cạnh mình, ra hiệu cho tôi ngồi đó."
    show bg club_day
    show natsuki 2a zorder 2 at t11
    with wipeleft

    mc "Sao không lấy ghế mà ngồi cho thoải mái...?"

    "Hỏi vậy chứ tôi vẫn ngồi xuống cùng Natsuki."

    n 2k "Không được."

    n "Ngồi ghế thì sao mà đọc chung được."

    mc "Eh? Tại sao lại thế?"

    mc "À...Đúng là ngồi như này thì được gần nhau hơn nhỉ..."
    n 2o "--!"

    n 5r "Đ-Đừng có nói ra!"

    "Cậu làm cho tôi thấy ngại rồi đấy!"

    "Natsuki khoanh tay lại và ngồi lùi ra xa tôi một chút."

    mc "Xin lỗi..."
    show natsuki 5g

    "Việc cậu ta để cho tôi ngồi cạnh đúng là chuyện không thể ngờ tới được..."

    "Mà dù sao thì cũng chả gây hại gì cho tôi cả."

    "Tôi mở trang đầu tiên."

    "Ngay vài giây sau, Natsuki đã bắt đầu sáp lại gần hơn, cố trở lại khoảng cách sát sàn sạt khi nãy vì tưởng tôi đang không để ý."

    "Còn có thể cảm nhận được cả ánh mắt cậu ấy đang nhìn qua vai mình, hẳn là còn háo hức muốn đọc còn hơn tôi nữa."

    n 1k "Wow, chả thể nhớ nổi mình đọc tập một từ bao giờ...?"


    mc "Cậu không có thói quen đọc lại sách cũ lúc rảnh hả?"

    n 2k "Không."

    n "Chắc phải đọc hết cả bộ xong tôi mới nghĩ tới chuyện đọc lại."

    n 2c "Mà này, cậu có chú ý đọc không đấy hả?"
    mc "Uh..."

    "Tôi vẫn đang đọc nhưng diễn biến truyện vẫn chưa có gì đặc sắc cả nên có thể nói chuyện cùng lúc cũng chả sao."

    "Có vẻ là truyện về cuộc sống của một đám học sinh cao trung."

    "Thể loại đời thường đây mà."

    "Thể loại này thì tôi thấy nhàm chán quá rồi, chỉ có thêm hài hước vào để bù cho cốt truyện tẻ nhạt giống y xì nhau."
    $ persistent.clear[0] = True
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg

    mc "...Cậu không thấy chán hả?"

    n "Không hề!"

    mc "Chỉ ngồi xem mình đọc truyện vậy thôi á?"

    n "À thì...!"

    n "Như vậy...cũng được rồi."

    mc "Tùy cậu thôi..."

    mc "...Chắc là được chia sẻ sở thích của mình với người khác cũng vui rồi nhỉ."

    mc "Rủ được bạn bè đọc cùng những bộ mà mình đang đọc là mình cũng thấy mãn nguyện lắm."

    mc "Ai cũng như vậy hết."
    n "...?"
    mc "Hm?"

    mc "Không đúng thế à?"
    show n_cg1_exp2 at cgfade
    n "Um..."

    m "Không phải..."

    n "Tại, tôi cũng chẳng rõ cho lắm."

    mc "...Ý cậu là sao?"

    mc "Cậu chưa bao giờ đọc truyện tranh cùng bạn bè à?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade

    n "Đừng có nhắc tới chuyện đó?"

    n "Mồ..."

    mc "Ah...Xin lỗi..."
    n "Hmph."

    n "Sao mà tôi bảo bọn bạn đọc được..."

    n "Chúng nó cho rằng chỉ trẻ con mới đọc truyện tranh thôi."

    n "Tôi mà nhắc đến là bọn nó lại cứ kiểu..."

    n "'Eh? Đúng là nhóc Natsuki vẫn còn chưa lớn.'"

    n "Thật khiến cho tôi muốn đấm vào mặt mỗi đứa một cái cho bõ tức..."

    mc "Urgh, xung quanh toàn loại người như vậy đấy..."

    mc "Thành thật mà nói thì, phải mất rất nhiều công sức mới có thể tìm được những người bạn không cười chê phán xét chứ chưa nói gì đến có thích hay không..."

    mc "Từ lâu mình cũng đã phải chấp nhận sống chung với chuyện đó, coi như bình thường rồi."

    mc "Nhưng với tính cách như cậu thì chắc là khó hơn..."
    hide n_cg1_exp3
    n "Hm."

    n "Ừm, khá là chính xác đó."

    "{i}...Hử, cậu ta bảo cái gì chính xác cơ??{/i}"
    $ style.say_dialogue = style.normal

    n "Xung quanh toàn loại người kiểu ấy nên cất truyện trong phòng riêng còn chả được..."

    $ style.say_dialogue = style.edited

    n "Bố tôi mà biết thì chết mất."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Ông già tao mà biết chắc lão nện tao tơi bời mất."

    n "Cũng may mà cất ở Câu lạc bộ thì sẽ được an toàn."
    show n_cg1_exp3 at cgfade

    n "Mỗi một điểm trừ là phải nghe Monika phàn nàn..."

    n "Ugh! Sao mọi người cứ như muốn dồn tôi vào đường cùng thế nhỉ?"

    mc "Nhưng sau cùng thì vẫn ổn mà, phải không?"

    mc "Mình đang ngồi ngay đây, đọc cuốn truyện cậu giới thiệu."

    n "Thế thì có giải quyết được những vấn đề vừa nói đâu."

    mc "Thì đúng là vậy..."

    mc "Nhưng ít ra lúc này cậu đang vui vẻ là tốt rồi mà, không phải vậy sao?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."

    n "...Vậy ư?"
    mc "Ahaha."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade

    n "Jeez, tán chuyện đủ rồi đấy!"

    n "Cậu có định đọc tiếp không hả?"

    mc "Rồi, rồi..."

    "Tôi lật sang trang tiếp theo."
    show black with dissolve_cg






    "Tôi đọc được một lúc rồi."
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade

    "Natsuki im lặng một cách lạ thường."

    "Tôi liếc sang bên cậu ấy."
    hide black with dissolve_cg

    "Hình như ngủ gật mất rồi thì phải."

    mc "Ê, Natsuki..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade

    n "H-Hả...?"

    "Đột nhiên Natsuki ngã thẳng vào người tôi."
    play sound fall
    $ style.say_dialogue = style.normal

    mc "N-Này--"
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base

    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r zorder 2 at t11
    m "Ôi trời ạ..."

    m 1d "Natsuki, cậu có sao không vậy?"
    show monika zorder 2 at t21
    show natsuki 12b zorder 3 at f22

    show natsuki zorder 2 at t22
    show monika zorder 3 at f21

    m 1a "Nè..."
    show monika zorder 2 at t21

    "Monika lục cặp, lấy ra thứ trông có vẻ như là một thanh lương khô."

    "Rồi ném nó về phía Natsuki."

    "Đột nhiên, mắt Natsuki như sáng lên."

    "Nhanh như chớp, cậu ấy nhặt thanh lương khô dưới sàn rồi vội vàng xé lớp vỏ bọc bên ngoài."
    show natsuki zorder 3 at f22

    n 1s "Tôi đã bảo cậu là đừng có đưa mmph..."
    show natsuki zorder 2 at t22

    "Chưa nói hết câu, cậu ta đã nhồi luôn cả thanh vào miệng."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11

    m "Đừng lo, [player]."

    m "Natsuki không sao đâu mà."

    m "Thi thoảng chuyện này lại xảy ra."

    m 1a "Thế nên trong cặp mình luôn có chút đồ ăn dành riêng cho cậu ấy."

    m 5a "À mà...!"

    m "Đến lúc chia sẻ thơ rồi nhỉ?"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
