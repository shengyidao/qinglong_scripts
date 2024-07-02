# --encoding:utf-8 -- #
"""
    
    联系方式:110

    易班

    ver 1.0

    2024.6.17

    实现 每日签到 点赞

    环境变量名:yuanshen_yb

    参数:
    Authorization loginToken orgId 其中 orgId位于 含getRecommend的url中
    
    群发wxpusher 提取 appToken topicid 

    格式:export yuanshen_yb = 备注#Authorization#loginToken#appToken#topicid#orgId

    定时 每天9点一次
    cron: 0 0 9 * * ? 

"""

#   --------------------------------一般不动区--------------------------------
#
#                                               #v;;@
#                                           .8@;;;3;;;;&@@u
#                                     ##%$$$$;;;*n8;;$;;;~&$$$$$@&          3@
#                                +@$%$$$$$$$%!;;;%;a$%*;;#$$$$%$$$$%$@!    *n *@n
#                              &$$$$$$$$$$$$$@*;;;$;;;;;@$$%$$$$$$$$$$%$$@%
#                             $$$$$$$$$$$$$$$$;;;;8;;;;$$$$$$$$i#$$%3i!@i@$$@
#                             #$$$$$$$$$$$$$$%$&&&#@@@@$$$$$$$#!!i#%#i!i3#$$$%&.&$
#                             @$$$$$$$$$$$$&@@@@@@@@&$$$$$$$$$%$!6@@iii6!!@@$@$$&.
#                          +&$%$@@@6iiiiizzzzuzzzzzazzzazzui!@@&%$$$$&i%$#@!i@%$$@
#                        #@@&&iiizzuazzaazzz@zzaazaaazazzzzaazzzzii#@$$$$$ii!i!$$%+
#                      @&&&@@uzzzzaazzzzzzi8zzzzazzazazaaizzzzazazzzaiii@$#!#i###
#                      @&&i#zzzazazzizi#@@6^izzzzzaazazu$izazzazzzzzaaz1iii8#$#@%%
#                      +i@zzzaazz11zzi!@+-%3zaaza1zzzi!#iaazz68zzzzzzzzz1iii&&#i$@
#                       i#1zazzza@azi38++. ;iuzzziazz8++*6azzzzzzzzzzzazazzii6&$&$.
#        .3       @    #i@zzzzaa3i@@3     .@&izzziu1#-- -@&###azuuzzaazzzzazzi&&# %^
#       z-i!*       a  ii@azzzzz@-6  @@@@   &@izz%#8- +8   $@3  &!azzzzzaaazzz@   -$#
#      o   !!1  -o  @+!8 @izaazz@ @  *&1    % %iaa#8  #   @@@@~  @izazzzaazzzzi    &$~
#     6    iii      3    .i1auaa! %        +o  -@i%.  @          @;$zazzzzzzaza    @%$.
#     n            !      #!iziiz@  %#;..8$        .  .@        @.a#zzaazzizzz%     $$@
#   * ^            #      va@ii3!ia$  ..                 ;&@@@1   %zzaaaaiizaz@
# ~;% ;           ~ #     @aaaz@#  ......     3           ....   $zzzza1i86azz#    za.@ 6
#     #          a .@@@   &aaaa@               -&@!       .... -6uiiizi#ai@izau    3z @;
#      ~         #        +uuuu!@                             ^++oiii%3-&1i&azz@   61~  &
#      -~        @         @uuu!-i63..                         $#@i+--%3iia!#izzu      * .
#        n       o          &311#iiiii@!                    .---o@#iii%aaaz-   i@&&^
#         @~      @          !31u@ii#i$&@@8!3#;-------++-1##3@ 8@.!iii1aaa&
#           #~;    !      #$#@%336$%#8@%%$$#&63i3n  @!!6668#&$$$$#!ii#aauu#
#        ..   +8~~~;;@@@&.@3#&$&%%#$&8888%&$$%$$%@&$$$$$$$$$$$@88888#uuuu$$-
#             .   .-%   6~@%$$8#$#$$88888888&#$#&a6%$%$#@8888888888@113u@$$$$
#                   1    -z$$$$6366%$%$&%88888&#&u;~;86686686%v%@611!3&$$$$#z  ;u
#                    1--+#^@$$$6$8#%aaai$668688;$&66668686688% a!338&$$$$$v.  .^@
#                      @@@@@$&#@ ^u%!uu%%88866$@#&8666686668%&   -a$&$$$@.  8@#
#                        $&##     @##816666666868#8666666366&$.   3u%$%@&8;*@ %@
#            @   @                 %#@366368$$@66866666666636&;&  @u%3$@#u$u-  o&
#       @ @. @ -v8i%               !6336666663&6666636!66336!66z~  @~#!11uuui1   #
#       @ @  @  @ @               #&&@663666$va$6666!33666666#&$%@  # @!1u33$6!!$  @
#       @ @ @.  @ @   @@@@- @&   @&$@1&6!636a$@1%6663!3333&$z1$$$$@@    +#838#!&v3   v
#       @@@ @ 8 -a@              @%$;&i$&666#n6%;3#3336@&&**#;#$$$#6za    .3$3131 -
#       n -@ @@ i@@.             #$@~%8$$$&@on@@@@$v&$%$$$$$$3n$$&iz%%a&     o33#
#              @   +            +&&@a&$$$%$$ou$$$$$&&~~$$$$1$@;$$&#%%z868$@@!;#3-
#                                v   .@&&$$$&$#%%%&@#&$&$$$$$&;#@@@&%$#%&@   %8u!
#                             !%&       #$&#ou6%!%#  .#&$$$$@       1 @$^
#                            a@ .i-i+ . ^&%%33!8%%%     #&&+       !1@#8@
#                            @$6-@  i#&    -8@@@@#@#^     @&^     %n*!@.
#                           &$$++i$
#                             .@$$%$
#
# ...................................................................
#           堂主保佑             永无BUG
#           堂主镇楼             BUG辟邪
#
#   堂主曰:
#
#        一日复一日，代码何其多！
#        只愿无bug，每日醉成仙！
#
# --------------------------------代码区--------------------------------
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))
