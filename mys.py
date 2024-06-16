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
#        写字楼里写字间，写字间里程序员；
#        程序人员写程序，又拿程序换酒钱。
#        酒醒只在网上坐，酒醉还来网下眠；
#        酒醉酒醒日复日，网上网下年复年。
#        但愿老死电脑间，不愿鞠躬老板前；
#        奔驰宝马贵者趣，公交自行程序员。
#        别人笑我忒疯癫，我笑自己命太贱；
#        不见满街漂亮妹，哪个归得程序员？
#
# --------------------------------代码区--------------------------------

import requests
import json
import os

class mys(object):
    def __init__(self,name:str,cookie:str):
        
        print([name],':','\n')

        self.mission_api: str = (
            "https://bbs-api.miyoushe.com/apihub/wapi/getMissions?point_sn=myb"  # 任务列表api GET
        )

        self.signIn_api: str = (
            "https://bbs-api.miyoushe.com/apihub/app/api/signIn"  # 打卡api POST
        )

        self.click_api: str = "https://bbs-api.miyoushe.com/post/api/getPostFull"  # GET

        self.get_postList: str = (
            "https://bbs-api.miyoushe.com/post/api/getForumPostList?forum_id=26&is_hot=false&is_good=false&sort_type=1&last_id=&page_size=20&page=1"  # 推送文章api
        )

        self.upvote_api: str = (
            "https://bbs-api.miyoushe.com/post/api/post/upvote"  # 点赞api POST
        )

        self.share_api: str = (
            "https://bbs-api.miyoushe.com/instant/api/instant"  # 分享api POST
        )

        self.createVerification: str = (
            "https://bbs-api.miyoushe.com/misc/api/createVerification?is_high=false"  # 申请验证码
        )

        self.luna_sign: str = (
            "https://api-takumi.mihoyo.com/event/luna/sign"  # 原神签到 POST
        )

        self.wxpusehr_api: str = (
            "https://wxpusher.zjiecode.com/api/send/message"  # wxpusher群发 POST
        )

        # 通用标准请求头
        self.headers: dict = {
            "DS": "1718458328,140067,e02b939a9c2fdc70ee6d2bd2a52437de",
            "cookie": cookie,
            "x-rpc-client_type": "2",
            "x-rpc-app_version": "2.34.1",
            "x-rpc-sys_version": "11",
            "x-rpc-channel": "miyousheluodi",
            "x-rpc-device_id": "e048c3ba-c3a5-3bb6-a6d8-f853a6da717c",
            "x-rpc-device_fp": "38d7f4b6430a0",
            "x-rpc-device_name": "OnePlus GM1900",
            "x-rpc-device_model": "GM1900",
            "x-rpc-h265_supported": "1",
            "Referer": "https://app.mihoyo.com",
            "x-rpc-verify_key": "bll8iq97cem8",
            "x-rpc-csm_source": "discussion",
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "12",
            "Host": "bbs-api.miyoushe.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.9.3",
        }

        # 社区打卡载体
        self.data = {"gids": 5}

        # 字符串查询
        self.params = {}

    def func_requests(
        self, method: str, url: str, headers: dict, data: dict, params: dict
    ):
        with requests.request(
            method=method,
            url=url,
            headers=headers,
            data=json.dumps(data),
            params=params,
        ) as request:
            if "json" in request.headers["Content-Type"]:
                return request, request.json()
            else:
                return request

    # 任务列表
    def mission(self):
        mission_ok, mission_json = self.func_requests(
            method="GET", url=self.mission_api, headers=self.headers, data={}, params={}
        )
        return mission_json

    # 原神签到
    def luna(self,uid:str,act_id:str,region:str)->dict:

        luna_headers: dict = {
            "Connection": "keep-alive",
            "Content-Length": "81",
            "x-rpc-platform": "2",
            "x-rpc-device_model": "GM1900",
            "x-rpc-app_version": "2.72.1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; GM1900 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 miHoYoBBS/2.72.1",
            "DS": "1718472334,kg9b51,fade623bbf6f8f200ddb20062cd991ef",
            "x-rpc-device_id": "e048c3ba-c3a5-3bb6-a6d8-f853a6da717c",
            "x-rpc-signgame": "hk4e",
            "Accept": "application/json, text/plain, */*",
            "x-rpc-device_name": "OnePlus%20GM1900",
            "x-rpc-device_fp": "38d7f4b6430a0",
            "Content-Type": "application/json;charset=UTF-8",
            "x-rpc-client_type": "5",
            "Origin": "https://act.mihoyo.com",
            "X-Requested-With": "com.mihoyo.hyperion",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://act.mihoyo.com/bbs/event/signin/hk4e/index.html?act_id=e202311201442471&bbs_auth_required=true&bbs_presentation_style=fullscreen&mhy_presentation_style=fullscreen&utm_source=bbs&utm_medium=ys&utm_campaign=icon",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "_MHYUUID=ce95c870-f85e-434f-84b4-bbb7b5dd419e; DEVICEFP_SEED_ID=4876bc36b564762a; DEVICEFP_SEED_TIME=1705166542984; DEVICEFP=38d7f4b63ed38; ltuid=297270114; login_ticket=iPIo3vusKrY76EnRoDhfTkwCTPc1dkbM8ybzzL0x; account_id=297270114; ltoken=6OPqbc5YEUQbw9jX8lHx4D4VgAIc53Q7QBjreZfK; mi18nLang=zh-cn; aliyungf_tc=deef0e47ae406adf3123008c71a9313b248733f4885dcd9cb600c040bbda1dad; _ga_P308KCCFXP=GS1.1.1709173441.1.0.1709173446.0.0.0; _ga_RE2E3BQ1DH=GS1.1.1709173442.1.0.1709173446.0.0.0; _ga_QYFFEX7F52=GS1.1.1716256249.7.1.1716256318.0.0.0; _ga_CGERVQ03CP=GS1.1.1716256250.6.1.1716256319.0.0.0; _ga_M91EY72BM9=GS1.1.1716256327.11.0.1716256404.0.0.0; cookie_token=Ade4cyegXWfwR37SFg71M3D5u8hXxSSYcaN8iM4r; _gid=GA1.2.997140895.1718450067; _ga_2HSB7QF0KJ=GS1.1.1718458279.1.0.1718458279.0.0.0; _ga_FF7GK0SSGX=GS1.1.1718458279.1.0.1718458279.0.0.0; _gat_gtag_UA_133007358_35=1; _ga_MRQ1MZMMEE=GS1.1.1718472319.87.0.1718472330.0.0.0; _ga=GA1.2.1599821848.1705334483",
        }

        luna_data: dict = {
            "act_id": act_id,
            "region": region,
            "uid": uid,
            "lang": "zh-cn",
        }

        luna_ok, luna_json = self.func_requests(
            method="POST",
            url=self.luna_sign,
            headers=luna_headers,
            data=luna_data,
            params={},
        )
        print("原神每日签到：", luna_json,'\n')
        return luna_json

    # 阅读文章
    def read_essay(self, post_id: str, times: int)->list:
        read_l = []
        for t in range(times):
            params = {"post_id": "{}".format(post_id[t]), "csm_source": "home"}

            read_ok, read_json = self.func_requests(
                method="GET",
                url=self.click_api,
                headers=self.headers,
                data={},
                params=params,
            )

            read_l.append(read_json["message"])
        print("浏览帖子：", read_l, "\n")
        return read_l

    # 获得推送文章 post_id
    def getList(self):
        post_id_list = []
        while True:
            if len(post_id_list) < 5:
                List_ok, List_json = self.func_requests(
                    method="GET",
                    url=self.get_postList,
                    headers=self.headers,
                    data={},
                    params={},
                )
                post_id_list.append(List_json["data"]["list"][0]["post"]["post_id"])
                post_id_list = list(set(post_id_list))
            else:
                return post_id_list

    # 点赞
    def upvote(self, post_list: list, times: int) -> list:
        upvote_l = []
        for t in range(times):
            # 点赞载体
            upvote_data = {
                "csm_source": "home",
                "is_cancel": False,
                "post_id": "{}".format(post_list[t]),
                "upvote_type": "1",
            }

            upvote_ok, upvote_json = self.func_requests(
                method="POST",
                url=self.upvote_api,
                headers=self.headers,
                data=upvote_data,
                params={},
            )
            upvote_l.append(upvote_json)

        print("帖子点赞：", upvote_l, "\n")
        return upvote_l

    # 社区打卡
    def signup(self):
        sign_ok, sign_json = mys.func_requests(
            method="POST",
            url=self.signIn_api,
            headers=self.headers,
            data=self.data,
            params=self.params,
        )
        print(sign_json)

    # 分享
    def share(self, post_id: str):
        # 分享载体
        share_data = {
            "structured_content": "",
            "csm_source": "home",
            "forward_id": "{}".format(post_id),
            "forward_show_instant_id_list": [],
            "forward_type": 1,
            "image_list": [],
            "link_card_ids": [],
            "topic_id_list": [],
        }

        share_ok, share_json = self.func_requests(
            method="POST",
            url=self.share_api,
            headers=self.headers,
            data=share_data,
            params={},
        )
        print(share_json)

    # geetest验证码
    def geetest_c_g(self):

        create_v_ok, create_v_json = self.func_requests(
            method="GET",
            url=self.createVerification,
            headers=self.headers,
            data={},
            params={},
        )
        challenge: str = create_v_json["data"]["challenge"]
        gt: str = create_v_json["data"]["gt"]
        return gt, challenge

    # validate
    def validate(self, gt: str, challenge: str):
        validate_headers = {
            "Content-Type": "application/json;",
            "Host": "apiv6.geetest.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; GM1900 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
            "Accept": "*/*",
            "X-Requested-With": "com.mihoyo.hyperion",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Dest": "script",
            "Referer": "https://static.geetest.com/static/appweb/app3-index.html?gt=d019a22590a54475b8e30eeb2854aab9&challenge=a547e558ef494879949ac082db481734&lang=zh-cn&title=&type=slide&api_server=apiv6.geetest.com&static_servers=static.geetest.com,%20static.geevisit.com&width=100%&timeout=10000&debug=false&aspect_radio_voice=128&aspect_radio_slide=103&aspect_radio_beeline=50&aspect_radio_click=128&voice=/static/js/voice.1.2.4.js&slide=/static/js/slide.7.9.2.js&beeline=/static/js/beeline.1.0.1.js&click=/static/js/click.3.1.0.js",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": "GeeTestUser=a6f2eb877f3226d4c0f6693e438bdde9",
        }

        self.validate_api: str = (
            f"https://apiv6.geetest.com/ajax.php?gt={gt}&challenge={challenge}&lang=zh-cn&$_BCN=3&client_type=web_mobile&w=nVkO(Tk18Atdszho9NiotxrPs7F)EjX2rOb3U)BXp5oPm1NaA7PHPKrgrqspyILwM3)Ti9yCzMC8uZ1ufRxXN5GBDnWvSFwgnL0QJKR5jbek9Z5by9)h0)pwCOmxN5K8DmQHLRqM7Wa3BurHZKt3coihe(PciA03IrRR1QvmGWRIyeOoLxAjMBUHuroRkicuxGduLUrPwOI6Y7edeTda9u5eeN6Jcd1JDGcxyNZuASuiC6(JDfXRDyK1c9UtyHzO8ikUukdMjPpH7cJWVqspnJG9UHg8Rvn7KGUTra9JEY8HBjLU9I6Fh2Hj0SQ9AdOZulql0p7TEUhmuy5XLEwq)tKIsy4rAKg9OmulQfrPpjeyZn93fe(k1Ju1(4pnxlnLBNY7i4(gNk2nj1KfLE7G2UWlE1OIcRmFrQYyw04ZHsunTem(rCbMQf7jzsEYxiEHLzvO(w89TUsGYyhRvm(2OmT1hdL)F8GRtD19n7aZS88BXtpi2FiHrF91cH8eMLFNkaXtZvE(Vz3EOBmjL6(j0YfDFXhsSABMQHwzqSQ0qwX)cDFoh)Fx2CWMIDeiEgtzAUOIwBNG10PH31dx6Pb1QU5Fiyd7P6HP9vHN9GhnFKbgLEjp3szYkGCSsL6ZpuTb6dMifxgkyFI8kri7tBTYsYDEUS4tBMJMvKakvgqQXZD0x7GT3mnvXFO)4xlMwROa7E(9sCENvKZwjemaMfmKdtBcQFG9YKd4A4SSdqZwa8Eb5jYo9xAQVJUtLjq4qZTpFRncYXtSTdWbzoIgAY1Xe8xUVw5dxp4KdFo67(rNsF4EHfaE8RZ6JJX5I(JWmYYH0QJ(tr4dtJaDaJRDopye6eaWk4KDzj0FTwBcdEqymPRXgak2iwHFsaju)Wm1xIls6h87pjWZWzxqV7LKbmn)RyyWOyZmf578uRo3oqnsK4OFzYRMSwCVZv5Ej94ygouC11NpgT3hrF9BoUuB7fKqefO7bXLnnkVzrkH3yiiAWc8.6ea65ecc996752a28ba9f4f467fcc36c732844b168d9728142c7e5e159252ee40df0388f220360056a4f2354b3e5f5a45dd7a1b4cd13ce510dd2efa75fe3858f599b4f92b8a8706f3b136da42cf6c25c116803075905f08c941a9f8f6ad6642ab3ef27373f2fc104790a714ca3268a429cb46bbb8bb8e66a21861c7ce6f1be9e&callback=geetest_1718468164187"  # 获得validate
        )

        v_ok, v_json = self.func_requests(
            method="GET",
            url=self.validate_api,
            headers=validate_headers,
            data={},
            params={},
        )
        print(v_ok)

    # wxpusher群发
    def wxpusher(self, content: str, apptoken: str, topicid: int):

        wxpusher_headers = {
            "Content-Type": "application/json; charset=UTF-8",
        }

        wxpusher_data = {
            "appToken": f"{apptoken}",
            "content": f"{content}",
            "summary": "米游社",
            "contentType": 3,
            "topicIds": [topicid],
            "verifyPay": False,
            "verifyPayType": 0,
        }
        wx_ok, wx_json = self.func_requests(
            method="POST",
            url=self.wxpusehr_api,
            headers=wxpusher_headers,
            data=wxpusher_data,
            params={},
        )
        print("wxpusher群发：", wx_json['data'][0]['status'], "\n")


if __name__ == "__main__":

    ''' 环境变量 '''
    cookie = ''
    # 环境变量为空时
    if not cookie:
        cookie = os.getenv('yuanshen_mys')
        # 找不到环境变量时
        if not cookie:
            print('请设置环境变量yuanshen_mys')
            exit()
        else:
            cookies:list = cookie.split('#')

            mys = mys(name=cookies[0],cookie=cookies[1])

            t_l: list = []
            for m_l in mys.mission()["data"]["missions"]:
                t_l.append(m_l["threshold"])  # 每个任务最大次数

            post_list = mys.getList()  # post_id

            mys.wxpusher(
                content=cookies[0]+":"+'\n'+"原神签到："
                + str(mys.luna(uid=cookies[2],act_id=cookies[3],region=cookies[4]))
                + "\n"
                + "浏览帖子："
                + str(mys.read_essay(post_id=post_list, times=t_l[1]))
                + "\n"
                + "帖子点赞："
                + str(mys.upvote(post_list=post_list, times=t_l[2])),
                apptoken=cookies[5],
                topicid=int(cookies[6]),
            )

    """""" """""" "验证码逆向（未完成）" """""" """"""
    # gt , challenge = mys.geetest_c_g()
    # mys.validate(gt=gt,challenge=challenge)
