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
except Ex
