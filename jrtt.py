# --encoding:utf-8 -- #

"""

    联系方式:110

    今日头条

    VERSION 1.0

    实现了 每日签到获取金币 种树浇水得金币 获得浇树的水滴 但未实现除虫

    参赛：cookie

    环境变量 export yuanshen_jrtt = 备份#cookie

    多号 @ 分割

    cron 建议设置到 晚上9点之后

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
  print(str(e))
