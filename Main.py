# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class resume:
    def __init__(self,school,resumes):
        self.resumes=resumes
        self.school=school
    def broswer(self):
        chrome_options = Options()
        google = webdriver.Chrome(chrome_options=chrome_options)
        for one in self.school:
            one_school=self.school.get(one)
            print(one)
            if one=='清华':
                self.qinghua(one_school,google)
            elif one =='北航':
                self.beihang(one_school,google)
            elif one=='北科大':
                self.beikeda(one_school,google)
            elif one=='北邮':
                self.beiyou(one_school,google)
            elif one=='北交大':
                self.beijiaoda(one_school,google)
            elif one=='牛客网':
                self.niukewang(one_school,google)
            elif one=='北师范':
                self.beishifang(one_school,google)

    def qinghua(self,one_school,google):
        #login
        website = one_school.get('website')
        username = one_school.get('username')
        password = one_school.get('password')
        google.get(website)
        time.sleep(2)
        login_username=google.find_element_by_css_selector("input[id='u_login_id']")
        login_username.clear()
        login_username.send_keys(username)
        login_pass = google.find_element_by_css_selector("input[id='u_login_passwd']")
        login_pass.clear()
        login_pass.send_keys(password)
        google.find_element_by_css_selector("input[id='u_login_submit']").click()
        time.sleep(2)
        # 是否回复招聘帖子
        print("回复上一次的信息")
        #reply=1为回复上一次的帖子
        reply=1
        reply_sites = ["http://www.newsmth.net/nForum/#!article/Career_Upgrade/600265",
                       "http://www.newsmth.net/nForum/#!article/Career_Upgrade/586519",
                       "http://www.newsmth.net/nForum/#!article/Career_Upgrade/520796"]
        reply_sites_num = len(reply_sites)
        if reply:
            if reply_sites_num:
                for x in reply_sites:
                    google.get(x)
                    time.sleep(5)
                    replay = google.find_element_by_css_selector("textarea[id='quick_text']")
                    #回复信息
                    replay.send_keys("up")
                    google.find_element_by_css_selector("td[id='quick_submit'] input").click()
                    time.sleep(10)
        #新发帖为1
        new_post=0
        if new_post:
            for h in self.resumes:
                google.get("http://www.newsmth.net/nForum/#!article/Career_Upgrade/post")
                time.sleep(2)
                title=google.find_element_by_css_selector("input[id='post_subject']")
                print(h)
                title.send_keys(h)
                resume_content=google.find_element_by_css_selector("textarea[id='post_content']")
                resume_content.send_keys(self.resumes.get(h))
                google.find_element_by_css_selector("input[value='发表帖子']").click()
                time.sleep(5)
        time.sleep(10)
    def beihang(self,one_school,google):
        # login
        website = one_school.get('website')
        username = one_school.get('username')
        password = one_school.get('password')
        google.get(website)
        print(website)
        time.sleep(2)
        login_username = google.find_element_by_css_selector("input[name='username']")
        login_username.clear()
        login_username.send_keys(username)
        login_pass = google.find_element_by_css_selector("input[name='password']")
        login_pass.clear()
        login_pass.send_keys(password)
        google.find_element_by_css_selector("input[name='loginsubmit']").click()
        time.sleep(2)
        # 新发帖为1
        new_post = 1
        if new_post:
            for h in self.resumes:
                google.get("http://www.buaaer.com/bbs/forumdisplay.php?fid=36")
                time.sleep(2)
                title = google.find_element_by_css_selector("input[name='subject']")
                print(h)
                title.send_keys(h)
                resume_content = google.find_element_by_css_selector("textarea[class='autosave']")
                resume_content.send_keys(self.resumes.get(h))
                #google.find_element_by_css_selector("input[name='topicsubmit']").click()
                time.sleep(5)

    def beijiaoda(self,one_school,google):
        # login
        website = one_school.get('website')
        username = one_school.get('username')
        password = one_school.get('password')
        google.get(website)
        time.sleep(2)
        login_username = google.find_element_by_css_selector("input[name='username']")
        login_username.clear()
        login_username.send_keys(username)
        login_pass = google.find_element_by_css_selector("input[name='password']")
        login_pass.clear()
        login_pass.send_keys(password)
        google.find_element_by_css_selector("button[class='pn vm']").click()
        time.sleep(5)
        # 新发帖为1
        new_post = 1
        if new_post:
            for h in self.resumes:
                google.get("http://zhixing.bjtu.edu.cn/forum.php?mod=post&action=newthread&fid=623&special=0")
                time.sleep(2)
                title = google.find_element_by_css_selector("input[name='subject']")
                print(h)
                title.send_keys(h)
                google.switch_to.frame("e_iframe")
                resume_content = google.find_element_by_css_selector("body[contenteditable='true']")
                resume_content.send_keys(self.resumes.get(h))
                google.switch_to.default_content()
                google.find_element_by_css_selector("button[name='topicsubmit']").click()
                time.sleep(2)
    def beikeda(self,one_school,google):
        # login
        website = one_school.get('website')
        username = one_school.get('username')
        password = one_school.get('password')
        google.get(website)
        time.sleep(5)
        login_username = google.find_element_by_css_selector("input[id='ls_username']")
        login_username.clear()
        login_username.send_keys(username)
        login_pass = google.find_element_by_css_selector("input[id='ls_password']")
        login_pass.clear()
        login_pass.send_keys(password)
        google.find_element_by_css_selector("button[class='pn vm']").click()
        time.sleep(10)
        # 新发帖为1
        new_post = 1
        if new_post:
            for h in self.resumes:
                #北科的bug
                google.get(website)
                time.sleep(10)
                forword=1
                while forword:
                    google.find_element_by_css_selector("a[id='typeid_fast_ctrl'").click()
                    google.find_element_by_css_selector("div[class='sltm'] ul li:nth-child(2)").click()
                    title = google.find_element_by_css_selector("input[id='subject']")
                    title.clear()
                    print(h)
                    title.send_keys(h)
                    resume_content = google.find_element_by_css_selector("textarea[id='fastpostmessage']")
                    resume_content.clear()
                    resume_content.send_keys(self.resumes.get(h))
                    #anser = google.find_element_by_css_selector("input[name='secanswer']")
                    #anser.send_keys('city.ibeike.com')
                    google.find_element_by_css_selector("button[name='topicsubmit']").click()
                    #北科大服务器太烂，多给点时间
                    time.sleep(30)
                    cur_url = google.current_url
                    if "forum" in cur_url:
                        forword=1
                        print("没有跳转，继续发帖")
                    else:
                        forword=0
                        print("发帖成功，跳转到首页")


    def niukewang(self,one_school,google):
        website = one_school.get('website')
        username = one_school.get('username')
        password = one_school.get('password')
        google.get(website)
        time.sleep(2)
        login_username = google.find_element_by_css_selector("input[id='emailIpt']")
        login_username.clear()
        login_username.send_keys(username)
        login_pass = google.find_element_by_css_selector("input[id='passwordIpt']")
        login_pass.clear()
        login_pass.send_keys(password)
        google.find_element_by_css_selector("a[id='loginBtn']").click()
        time.sleep(5)
        new_post = 1
        if new_post:
            for h in self.resumes:
                google.get("https://www.nowcoder.com/discuss/v2/post?type=0")
                time.sleep(2)
                title = google.find_element_by_css_selector("div[class='topic-publish'] input")
                title.clear()
                title.send_keys(h)
                google.find_element_by_css_selector("button[class='btn btn-default dropdown-toggle']").click()
                time.sleep(2)
                google.find_element_by_css_selector("div[id='jsCpn_6_component_0'] ul li:nth-child(7) a").click()
                google.switch_to.frame(0)
                resume_content = google.find_element_by_css_selector("body[class='ke-content']")
                resume_content.clear()
                resume_content.send_keys(self.resumes.get(h))
                google.switch_to.default_content()
                #判断要发送的简历，牛客每次只能发送一篇JD
                if h=="基础平台部-测试开发工程师":
                    google.find_element_by_css_selector("a[data-type='submit']").click()
                time.sleep(5)

    def beiyou(self,one_school,google):
        # login
        website = one_school.get('website')
        username = one_school.get('username')
        password = one_school.get('password')
        google.get(website)
        time.sleep(2)
        login_username = google.find_element_by_css_selector("input[id='u_login_id']")
        login_username.clear()
        login_username.send_keys(username)
        login_pass = google.find_element_by_css_selector("input[id='u_login_passwd']")
        login_pass.clear()
        login_pass.send_keys(password)
        google.find_element_by_css_selector("input[id='u_login_submit']").click()
        time.sleep(2)
        # 新发帖为1
        new_post = 1
        if new_post:
            for h in self.resumes:
                google.get("https://bbs.byr.cn/#!article/Job/post")
                time.sleep(2)
                title = google.find_element_by_css_selector("input[id='post_subject']")
                print(h)
                title.send_keys(h)
                resume_content = google.find_element_by_css_selector("textarea[id='post_content']")
                resume_content.send_keys(self.resumes.get(h))
                google.find_element_by_css_selector("input[value='发表帖子']").click()
                time.sleep(5)
    def beishifang(self,one_school,google):
        #没有权限
        pass

if __name__ == "__main__":
    school = {'清华': {'website': 'http://www.newsmth.net/nForum/#!section/Career', 'username': 'sincloudwind','password': 'asdf123'},
              '北邮': {'website':'https://bbs.byr.cn/#!default','username':'wyn','password':'880106'},
              '北航': {'website': 'http://www.buaaer.com/bbs/logging.php?action=login',
                       'username': 'hr_desktopqa','password': 'Desktopqa123'},
              '北师范': {'website': 'https://www.oiegg.com/logging.php?action=login',
                      'username': 'hr_desktopqa','password': 'Desktopqa123'},
              '北科大': {'website': 'http://city.ibeike.com/forum-180-1.html',
                      'username': 'hr_desktopqa','password': 'Desktopqa123'},
              '北交大1': {'website': 'http://zhixing.bjtu.edu.cn/topic-findyourjob.html',
                      'username': 'hrdesktopqa','password': 'Desktopqa123'},
               '牛客网':{'website':'https://www.nowcoder.com/login',
                      'username':'hr_desktopqa@126.com','password':'Desktopqa123'}
              }
    resumes={
             "【校招】【社招】搜狗手机助手-测试开发工程师":"\r\n岗位职责：\r\n1、参与搜狗手机助手客户端及服务端的全流程测试工作，包括需求分析、设计评审、测试方案制定、测试用例设计和执行，缺陷跟踪与质量分析。\r\n2、负责产品的功能、性能、稳定性、自动化等测试工作。\r\n3、负责与产品、开发等配合方的沟通配合推进项目进度。\r\n4、负责团队的技术创新，解决复杂的各类问题。\r\n \r\n任职要求：\r\n1、本科及以上学历，计算机相关专业毕业；\r\n2、熟悉Android系统，对手机相关的新鲜事物非常感兴趣，有持续学习能力；\r\n3、头脑灵活，勇于创新，具有较强的发散思维；\r\n4、工作积极主动，细致、有耐心，不浮躁，有强烈的责任感，对结果负责；\r\n5、能适应互联网公司的工作节奏，有一定的抗压能力；\r\n6、性格开朗，善于沟通，有团队意识，富有正能量；\r\n \r\n【特别提示】：搜狗欢迎专情的你，所以提醒你只能选择两个项目，请慎重投递\r\n投递简历时请注明应聘的职位，联系邮箱：hr_desktopqa@126.com ",
             "【校招】【社招】搜狗浏览器-测试开发工程师":"岗位职责： \r\n1、负责基础平台部各业务线产品服务端测试工作，包括服务端功能测试、性能及稳定性测试、自动化测试、安全测试等。 \r\n2、参与需求设计分析，制定测试方案，设计测试用例，测试执行，问题跟进，测试报告等； \r\n3、提交、分析、跟踪软件设计缺陷，评估项目风险，保障产品质量； \r\n4、与开发团队进行有效沟通，推动解决测试中发现的问题。 \r\n5、具备创新思维，积极思考和发掘工作中的问题，通过开发工具或其它手段提升测试质量及效率。 \r\n\r\n任职要求： \r\n1、计算机相关专业毕业； \r\n2、具备一定测试开发经验，熟练掌握一门语言； \r\n3、熟练使用各种测试工具； \r\n4、熟练使用Linux操作系统； \r\n5、对技术有强烈的兴趣和爱好，具有较强的学习能力，有想法； \r\n6、能够熟练的使用各种测试设计方法，具有较强的测试发散度； \r\n7、能适应互联网公司的工作节奏，有一定的抗压能力； \r\n8、性格开朗，善于沟通，有团队意识，富有正能量； \r\n9、能够独立思考和解决问题； \r\n10、工作积极主动，细致、有耐心，不浮躁，有强烈的责任感，对结果负责；\r\n\r\n【特别提示】：搜狗欢迎专情的你，所以提醒你只能选择两个项目，请慎重投递\r\n投递简历时请注明应聘的职位，联系邮箱：hr_desktopqa@126.com ",
             "【校招】【社招】基础平台部-测试开发工程师":"职位描述：\r\n搜狗浏览器即搜狗高速浏览器，是国内最早发布的双核浏览器，完美融合了全球最快的Webkit内核和兼容性最佳的IE内核，保证良好兼容性的同时极大提升了网页浏览速度。该浏览器具有9级加速体系、自动网络收藏夹、独立播放网页视频、flash游戏提取操作等多项特色功能，并且兼容大部分用户使用习惯，支持多标签浏览、鼠标手势、隐私保护、广告过滤等主流功能。独创预提取功能\r\n \r\n【特别提示】：搜狗欢迎专情的你，所以提醒你只能选择两个项目，请慎重投递\r\n \r\n岗位职责：\r\n1、负责搜狗浏览器复杂功能的黑灰盒测试工作\r\n2、参与需求设计分析，制定测试方案，设计测试用例，测试执行，问题跟进，测试报告\r\n3、处理用户反馈的各种问题\r\n4、不断进行总结，能够发现并解决工作中遇到的问题，经常产出有价值的总结和分享\r\n5、负责团队测试流程及方法的改进\r\n6、负责团队自动化测试方案的实施及改进\r\n \r\n任职要求：\r\n1、计算机相关专业毕业；\r\n2、具备丰富的程序设计经验，能够熟练使用C++和Python；\r\n3、对技术有强烈的兴趣和爱好，具有较强的学习能力；\r\n4、头脑灵活，具有较强的测试发散度；\r\n5、能适应互联网公司的工作节奏，有一定的抗压能力；\r\n6、性格开朗，善于沟通，有团队意识，富有正能量；\r\n7、能够独立思考和解决问题；\r\n8、工作积极主动，细致、有耐心，不浮躁，有强烈的责任感，对结果负责；\r\n投递简历时请注明应聘的职位，联系邮箱：hr_desktopqa@126.com ",
			 "【校招】【社招】【搜狗】iOS开发工程师":"/r/n职位职责：/r/n1.负责iOS手机软件的相关开发工作；/rn2.能够深入了解产品需求，并根据需求对独立的模块进行设计、编码、调试、配置等工作；/r/n3.对iOS平台开发技术进行研究，不断优化产品的质量、性能、用户体验；/r/n/r/n任职资格：/r/n1.扎实的计算机基础，较强的算法能力，精通Objective-C；/r/n2.熟悉iOS常用的framework，对内存管理、对象生命周期有清晰的认识；/r/n3.对UIKit有清晰的理解，能够熟练编写自定义控件和常用动画效果；/r/n4.对iOS中的内存管理、多线程、设计模式、消息通讯机制，安全机制有深入了解；/r/n5.具备主流开源组件使用经验，熟练使用Instruments等调测工具；/r/n6.思路清晰，善于思考，责任心强；/r/n7.善于沟通，具备较强的团队协作意识和能力；/r/n8.有AppStore上线优秀作品者优先；/r/n9.有图像处理开发经验者优先；/r/n/r/n招聘单位：北京搜狗科技发展有限公司/r/n/r/n投递简历时请注明应聘的职位，联系邮箱：hr_desktopqa@126.com"

            }
    element=resume(school,resumes)
    element.broswer()
