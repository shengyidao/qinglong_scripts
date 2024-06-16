# --encoding:utf-8 -- #
"""
    
    联系方式:110

    米游社

    ver 1.0

    2024.6.15

    实现 原神每日签到 米游币获取: 浏览帖子(3 20) 每日点赞(5 30) 分享贴子(1 10)

    环境变量名:yuanshen_mys

    参数:任意含mhy的url 中的 cookie , uid , act_id , region

    群发wxpusher 提取 appToken topicid

    格式:export yuanshen_mys = 备注#cookie#uid#act_id#region#appToken#topicid

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
    import lzma, base64
    exec(lzma.decompress(base64.b64decode('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')))
except Exception as e:
    print('脚本执行出错:', str(e))
