# --encoding:utf-8 -- #
"""
    
    联系方式:110

    米游社

    ver 1.1

    2024.6.17

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
	import bz2, base64
	exec(bz2.decompress(base64.b64decode('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')))
except Exception as e:
	print('脚本执行出错:', str(e))
